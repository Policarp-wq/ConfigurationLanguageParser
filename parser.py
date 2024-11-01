import lark.exceptions
from lark import Lark, Transformer, v_args
from yaml import load, dump

grammar = r'''start: constant_declaration* (constant_declaration | assign_value)*

value: NUMBER
    | array
    | computation


NAME: /[a-z][a-z0-9_]*/

array: "(" [value ("," value)*] ")"

constant_declaration: "general " NAME " = " value ";"

assign_value: NAME " = " value ";"

computation: "$" (arg arg OPERATION) "$"

arg: computation | NAME | NUMBER

OPERATION : "+" | "-" | "*" | "min" | "max"

%import common.SIGNED_NUMBER -> NUMBER
%import common.WS
%ignore WS   
'''


@v_args(inline=True)
class ConfigTransformer(Transformer):
    def __init__(self):
        super().__init__()
        self.constants = {}

    # array = list
    NUMBER = int
    NAME = str
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'min': lambda x, y: min(x, y),
        'max': lambda x, y: max(x, y)
    }

    banned_names = ['min', 'max', 'general']

    @v_args(inline=False)
    def array(self, arr):
        return arr

    def OPERATION(self, op):
        return op.value

    @v_args(inline=False)
    def computation(self, args):
        if len(args) == 0:
            return args
        if len(args) == 3:
            return self.operations[args[-1]](args[0], args[1])

    def constant_declaration(self, name, value):
        if name in self.banned_names:
            raise Exception(f'Variable {name} could not be named like key words! {self.banned_names}')
        self.constants[name] = value

    def assign_value(self, name, value):
        if name in self.banned_names:
            raise Exception(f'Variable {name} could not be named like key words! {self.banned_names}')
        self.constants[name] = value
        return name

    def value(self, val):
        return val

    def arg(self, v):
        if isinstance(v, int):
            return v
        if isinstance(v, str):
            if v not in self.constants:
                raise Exception(f'{v} not in constants!')
            return self.constants[v]
        return v



def parse_text(text):
    lang_parser = Lark(grammar)
    try:
        tree = lang_parser.parse(text)
        transformer = ConfigTransformer()
        res = transformer.transform(tree)
        return transformer.constants
    except lark.exceptions.LarkError as ex:
        print(ex)
        raise ex


def convert_to_yaml(constants):
    return (dump(constants)).strip()



text = r'''general sus = $7 $7 8 +$ +$;
general mda = $7 $1 5 max$ +$;
general lol = (1, $-100 -200 max$, 3);
general mx = $-5 10 max$;
mx = $10 5 -$;
'''

text = r'general test = (1, 2,3);'
print(convert_to_yaml(parse_text(text)))



