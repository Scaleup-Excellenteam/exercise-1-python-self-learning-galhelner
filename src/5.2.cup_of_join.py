def cup_of_join(*lists, sep='-'):
    # handle edge case - lists argument is empty
    if not lists:
        return None

    result_list = []
    for lst in lists:
        for item in lst:
            # append each argument list's items to the final list
            result_list.append(item)
        # append the seperator char after each argument list
        result_list.append(sep)

    # remove the last seperator char inserted at the end of lists concat
    result_list.pop()
    return result_list


if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
