from lark import Lark

grammar = r'''start: constant_declaration* (constant_declaration | assign_value)*

value: NUMBER
    | array
    | computation

declaration: NAME value

NAME: /[a-z][a-z0-9_]*/

array: "(" [value ("," value)*] ")"

constant_declaration: "general " NAME " = " value ";"

assign_value: NAME " = " value ";"

computation: "$" (arg arg OPERATION | min | max) "$"

arg: computation | NAME | NUMBER | min | max

args: arg ("," arg)+

min: "min(" args ")"

max: "max(" args ")"

OPERATION : "+" | "-" | "*" 

%import common.SIGNED_NUMBER -> NUMBER
%import common.WS
%ignore WS
'''

lang_parser = Lark(grammar)

text = r'''general sus = $7 $7 8 +$ +$;
mda = $7 $min(1, 5)$ +$;
'''
res = lang_parser.parse(text)
print(res.pretty())