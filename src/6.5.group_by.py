import itertools


def group_by(func, iterable):
    try:
        # using dictionary comprehension to create the final dictionary
        # and a list comprehension inside of it to create for each key the values list
        return {
            func(key_item): [
                val_item for val_item in iterable if func(val_item) == func(key_item)
            ]
            for key_item in iterable
        }
    except TypeError:
        # some item of the iterable is an invalid type to execute func(item)
        print('Not all the iterable items types are valid for the grouping function!')
        return None


if __name__ == '__main__':
    # test cases
    print(group_by(len, ['hi', 'bye', 'yo', 'try']))
    group_by(sum, [[1, 2, 3], 4, 'you cant sum me'])
