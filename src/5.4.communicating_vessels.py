"""
Week 5 Ex 4 - communicating_vessels
"""
import itertools


def interleaves(*iterables):
    """Create an interleaved list of all iterables items.

    Args:
        iterables (tuple): zero or more iterable of items.

    Returns:
        list: A list of interleaved items from all the iterables.
    """
    # zip function will provide the interleaving process
    # module function chain.from_iterable will flatten the tuples returned from zip
    return list(itertools.chain.from_iterable(zip(*iterables)))


def generator_interleaves(*iterables):
    """Yields interleaved items from given iterables.

    Args:
        iterables (tuple): zero or more iterable of items.

    Yields:
         T: Elements from the provided iterables in an interleaved order. 
           The type of yielded elements depends on the input iterables.
    """
    # get all the iterators from the argument iterables
    iterators = [iter(it) for it in iterables]
    # use module function zip_longest that preforms the interleaving
    for values in itertools.zip_longest(*iterators, fillvalue=None):
        for value in values:
            # zip_longest puts None where the length isn't equal
            # so, None values should be ignored
            if value is not None:
                # yield each non-None value
                yield value


if __name__ == '__main__':
    print(interleaves('abc', [1, 2, 3], ('!', '@', '#')))
    for interleaved_value in generator_interleaves('abc', [1, 2, 3], ('!', '@', '#')):
        print(interleaved_value)
