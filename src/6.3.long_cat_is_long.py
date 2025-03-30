def long_cat_is_long(text):
    # split the text into words and remove any symbol that is not an alpha
    words = [''.join(filter(str.isalpha, word.lower())) for word in text.split()]
    # build a dictionary where keys are the words and values are the word's length
    return {word: len(word) for word in words}


if __name__ == '__main__':
    # test case
    text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
    """
    print(long_cat_is_long(text))
