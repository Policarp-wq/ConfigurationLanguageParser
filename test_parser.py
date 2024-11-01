import pytest

from parser import *


@pytest.mark.parametrize("input, expected", [
    (r'general test = 1;', {"test": 1}),
    (r'general test = $1 2 +$;', {'test': 3}),
    (r'general test = $1 2 -$;', {'test': -1}),
    (r'general test = $1 $-5 0 min$ +$;', {'test': -4}),
    (r'general test = $1 $-5 0 max$ +$;', {'test': 1}),
    (r'general ls = (1, 2, 3);', {"ls": [1, 2, 3]}),
    (r'general ls = (1, $1 $52 0 max$ +$, 3);', {"ls": [1, 53, 3]}),
    (r'''general sus = $7 $7 8 *$ +$;
general mda = $7 $1 5 max$ +$;
general lol = (1, $-100 -200 max$, 3);
general mx = $-5 10 max$;
mx = $10 5 -$;
''', {"lol": [1, -100, 3], "mx" : 5, "mda" : 12, "sus" : 63 }),

])
def test_parser(input, expected):
    assert parse_text(input) == expected


@pytest.mark.parametrize("input, expected", [
    (r'general test = 1;', 'test: 1'),
    (r'general test = $1 2 +$;', 'test: 3'),
    (r'general test = $1 2 -$;', 'test: -1'),
    (r'general kek = $1 $-5 0 min$ +$;', 'kek: -4'),
    (r'general kek = $1 $-5 0 max$ +$;', 'kek: 1'),
])
def test_convert(input, expected):
    assert convert_to_yaml(parse_text(input)).strip() == expected
