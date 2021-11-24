from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    """Combine lists with 'sep': separator in between the lists"""
    combined = []
    if len(lst_of_lst) == 0:
        return None
    for ind, _list in enumerate(lst_of_lst):
        combined.extend(_list)
        if ind == len(lst_of_lst) -1:
            return combined
        combined.append(sep)
    return combined