da: bool = True
net: bool = False
x: int = 1
string: str = 'blabla'
floated: float = 123.456

numbers: list[int] = [1, 2, 3, 4]

list_of_string_numbers = list(map(str, numbers))

string_of_numbers = '|'.join(list_of_string_numbers)

list_name: list[str] = [
    'vlad zverev',
    'sergei zverev',
    'sergei turbozverev',
    'masha fedina',
]


def is_zverev(name: str) -> bool:
    return name.split(' ')[-1] == 'zverev'


for name in list_name:
    words = name.split(' ')

    first_name, last_name = words

    if last_name == 'zverev':
        print(name)
