"""
Week 5 Ex 1 - thats_the_way
"""
import os


def thats_the_way(directory_path, prefix="deep"):
    """Find all filenames inside a directory that are starts with a given prefix.

    Args:
        directory_path (str): path of the directory to check the filenames in it.
        prefix (str, optional): the prefix string that the filenames should start with.

    Returns:
        list: A list of all filenames in the directory that starts with the prefix string.
    """
    files_in_directory = os.listdir(directory_path)
    start_with_prefix = [filename for filename in files_in_directory if filename.startswith(prefix)]
    return start_with_prefix


if __name__ == "__main__":
    filenames = thats_the_way(directory_path="images")
    # check if thats_the_way return only 2 filenames
    assert len(filenames) == 2
    # print the filenames returned
    print(filenames)
