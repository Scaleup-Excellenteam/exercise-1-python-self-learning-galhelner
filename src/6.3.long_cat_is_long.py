"""
Week 6 Ex 3 - long_cat_is_long
"""


def long_cat_is_long(text):
    """Create a dictionary where the keys are length of valid alpha words and values are the words.

    Args:
        text (str): String of the whole text to read and create the dict.

    Returns:
        dict: A dictionary where the keys are length of valid alpha words and values are the words.
    """
    # split the text into words and remove any symbol that is not an alpha
    split_words = [''.join(filter(str.isalpha, word.lower())) for word in text.split()]
    # remove empty words added because join
    words = [word for word in split_words if word]
    # build a dictionary where keys are the words and values are the word's length
    return {word: len(word) for word in words}


if __name__ == '__main__':
    # test case
    result = long_cat_is_long("Bla bla bla tralala 123")
    print(result)
