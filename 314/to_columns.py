from typing import List  # not needed when we upgrade to 3.9

names = "Bob Julian Tim Sara Eva Ana Jake Maria".split()
def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    columns = []
    for indx, name in enumerate(names,1):
        padding = -(len(name)) % 10
        col = f'| {name}{" " * padding}'
        columns.append(col)
        if indx % cols == 0:
            columns.append('\n')
    print(''.join(columns))












print_names_to_columns(names)