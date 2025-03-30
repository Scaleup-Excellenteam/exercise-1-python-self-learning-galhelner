"""
Week 5 Ex 2 - cup_of_join
"""
def cup_of_join(*lists, sep=None):
    """Create a list with all the items of each argument list seperated by a given seperator string.

    Args:
        lists (tuple): zero or more lists.
        sep (str): seperator string.

    Returns:
        list: A list with all the items from all argument lists seperatad by the seperator string.
    """
    # handle edge case - lists argument is empty
    if not lists:
        return None

    result_list = []
    for lst in lists:
        for item in lst:
            result_list.append(item)
        if sep is not None:
            result_list.append(sep)

    return result_list


if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
