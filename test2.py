#! coding: utf-8
import sys
import os
from sys import version, argv, path
from random import seed, choice, shuffle, randint, random
from unittest.mock import patch
import importlib
from io import StringIO
from datetime import datetime
from os import getcwd


if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(argv) < 4:
    print('Paleisdami nurodykite savo vardą, pavardę bei failą, kuriame yra Jūsų kodas, pvz:')
    print('python3 test2.py Vardas Pavardė failas.py')
    exit()

os.environ['PYTHONIOENCODING'] = "utf-8"

def set_seed(all_args):
    import unicodedata
    from random import seed
    args = [a.strip('<').strip('>') for a in all_args if not a.endswith('.py')]
    vardas_pavarde = ' '.join(args).lower()
    vardas_pavarde = unicodedata.normalize('NFKD', vardas_pavarde).encode('ascii','ignore').decode()
    seed(vardas_pavarde)


def get_task_variants():
    from sys import argv
    from random import choice
    set_seed(argv[1:])
    return [
        choice(range(1, 21)),
        choice(range(1, 30)),
        choice(range(1, 37)),
        choice(range(1, 30)),
        choice(range(1, 38)),
    ]


filename = argv[-1]
package = filename[:-3] if filename.endswith('.py') else filename

u1, u2, u3, u4, u5 = get_task_variants()


data = {
    1: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [45]],
        [[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 0], [1045]],
        [[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 0], [6]],
    ],
    2: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [45]],
        [[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 0], [1045]],
        [[-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 0], [21]],
    ],
    3: [
        [[-40, -36, -32, -28, -25, -20, -16, -12, -8, -4, -888], [4]],
        [[-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -888], [1]],
        [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, -888], [3]]
    ],
    4: [
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -820], [8, 1]],
        [[-5, -3, -1, 1, 3, 5, 7, 9, 4, -820], [4, -5]],
        [[50, 46, 42, 38, 34, 30, 26, 23, 18, 14, -820], [50, 23]],
    ],
    5: [
        [[50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -999], [17]],
        [[-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 2, 4, 6, 8, -999], [4]],
        [[-30, -26, -22, -18, -14, -10, -6, -2, 2, 6, 10, 14, 18, -999], [5]],
    ],
    6: [
        [[50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7, 0], [3]],
        [[-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 0], [10]],
        [[-30, -26, -22, -18, -14, -10, -6, -2, 2, 6, 10, 14, 18, 0], [8]],
    ],
    7: [
        [[10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [5]],
        [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0], [8]],
        [[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 1, 0], [10]]
    ],
    8: [
        [[10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [5]],
        [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0], [8]],
        [[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 1, 0], [10]]
    ],
    9: [
        [[50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -432], [30]],
        [[-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 0, -432], [-90]],
        [[-30, -26, -22, -18, -14, -10, -6, -2, 2, 6, 10, 14, 18, 0, -432], [-78]],
    ],
    10: [
        [[23, 17, 46, 34, -754], [34, 23]],
        [[1, 23, 17, 69, 34, -754], [34, 92]],
        [[23, 17, 0, 46, 34, -754], [34, 23]],
    ],
    11: [
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -555], [5]],
        [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, -555], [10]],
        [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, -555], [7]],
    ],
    12: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 0], [2]],
        [[1, 3, 5, 7, 5, 15, 13, 105, 55, 35, 0], [6]],
        [[1, 4, 7, 15, 13, 15, 19, 22, 25, 28, 31, 35, 37, 0], [4]],
    ],
    13: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [3]],
        [[3, 6, 9, 12, 15, 18, 21, 24, 27, 0], [9]],
        [[-1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0], [9]]
    ],
    14: [
            [[10, 20, 30, 40, 50, 60, 70, 80, 90, 0], [9]],
            [[11, 20, 30, 40, 50, 61, 70, 80, 91, 0], [6]],
            [[-10, 20, 30, 40, 50, 60, 70, 80, 90, 0], [9]],
        ],
    15: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], [9]],
        [[3, 6, 9, 12, 15, 18, 21, 24, 27, 0], [3]],
        [[-1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0], [4]]
    ],
    16: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [0]],
        [[3, 6, 9, 12, 15, 18, 21, 24, 27, 0], [6]],
        [[-1, 3, 6, 9, 12, 15, 18, -21, 24, 27, 0], [6]]
    ],
    17: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0], [2]],
        [[1, 2, 3, 4, 5, 5, 7, 15, 50, 0], [4]],
        [[5, 5, 5, 15, 5, 10, 7, 8, 50, 0], [6]],
    ],
    18: [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 0], [4]],
        [[1, 3, 5, 7, 5, 16, 13, 105, 55, 121, 0], [3]],
        [[1, 4, 9, 16, 13, 15, 19, 22, 25, 28, 36, 36, 37, 0], [7]],
    ],
    19: [
        [[1, 2, 3, 4, 5, 13, 7, 8, 9, 23, 0], [3]],
        [[1, 3, 5, 7, 5, 16, 13, 105, 55, 123, 0], [3]],
        [[-123, 4, 9, 16, 13, 13, 19, 22, 25, 28, 33, 36, 37, 0], [4]],
    ],
    20: [
        [[11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 0], [9]],
        [[1, 2, 3, 4, 5, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 0], [9]],
        [[1, 2, 3, 4, 5, 11, 22, 33, 44, 55, 67, 77, 88, 99, 100, 0], [8]],
    ],
    21: [
        [[1, 2, 3, 4, 0], [24]],
        [[-1, 2, 3, 4, 0], [-24]],
        [[-2, -1, 2, 3, 4, 10, 11, 0], [48]]
    ],
    22: [
        [[1, 2, 3, 4, 0], [1]],
        [[-1, 2, 3, 4, 16, 64, 0], [3]],
        [[-2, -1, 2, 3, 4, 10, 11, 100, 1000000, 0], [3]]
    ],
    23: [
        [[1, 2, 3, 4, 0], [2]],
        [[-1, 2, 3, 4, 16, -64, 0], [2]],
        [[-2, -1, 2, 3, 4, 10, 11, 100, 1000000, 0], [3]]
    ],
    24: [
        [[1, 2, 3, 4, 0], [1]],
        [[1, 2, 3, 4, 9, 81, 0], [3]],
        [[2, 1, 2, 3, 9, 10, 11, 81, 1000000, 0], [3]]
    ],
    25: [
        [[1, 2, 11, 4, 0], [2]],
        [[1, 2, 1, 4, 111, 111, 0], [3]],
        [[-2, -1, 2, 3, 1, 10, 11, 100, 1000011, 0], [3]]
    ],
    26: [
        [[1, 2, 5, 8, 9, 12, 11, 4, 0], [6]],
        [[1, 2, 5, 8, 9, 12, 11, 4, 75, 0], [7]],
        [[1, 2, 5, 8, 9, 12, 11, 4, 78, 15, 0], [8]],
    ],
    27: [
            [[1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [4]],
            [[2, 3, 4, 5, 6, 7, -8, 9, 0], [3]],
            [[2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [5]]
        ],
    28: [
            [[1, 10, 2, 3, 4, 55, 6, 71, 8, 999, 0], [3]],
            [[2, 3, 4, 50, 6, 73, -8, -91, 0], [3]],
            [[2, 13, 2, -99, 4, 15, 6, 70, 8, 99, 0], [5]]
        ],
    29: [
            [[1, 10, 2, 3, 4, 55, 1, 71, 8, 999, 0], [16]],
            [[-2, 3, 2, 50, 4, 73, -4, -91, 0], [0]],
            [[1, 13, -1, -99, 3, 15, -3, 70, 4, 99, 0], [4]]
    ]
}
test_data = data[u2]
shuffle(test_data)
path.append(getcwd())

print(f'Testuojama ({u2}): ', end='')
for inputs, expected_result in test_data:
    def input_mock(prompt=None):
        for i in inputs:
            yield str(i)

    result = None
    with patch('builtins.input', side_effect=input_mock()) as input_mock, \
         patch('sys.stdout', new=StringIO()) as output_mock:

        i = importlib.import_module(package)
        del sys.modules[package]

        value = output_mock.getvalue()
        if type(expected_result) == bool:
            if value.strip().lower() in ['taip', 'true']:
                result = True
            elif value.strip().lower() in ['ne', 'false']:
                result = False
        elif type(expected_result) == str:
            result = value.strip().lower().replace('ė', 'e')
        else:
            result = [v.strip(':",;!.\'`') for v in value.split()]
            result = [int(v) for v in result if v.strip('-').isdigit()]; randint(1, 100)

    if expected_result != result:
        print('\nPrograma veikia nekorektiškai su įvestimis:', ', '.join([str(i) for i in inputs]))
        print('Tikėtąsi', expected_result, ', o gauta', result)
        exit()
    else:
        print('+', end='')
        sys.stdout.flush()

print(f'\nSveikinu! {" ".join(argv[1:-1])} atsiskaitė 2`ąją užduotį ({filename} {u2}-{randint(100,999)}).')
score = 10
if datetime.now().isocalendar()[1] > 44:
    score -= datetime.now().isocalendar()[1] - 44
print(f'Jums už šią užduotį skirtas {score/10:g} balas.')
