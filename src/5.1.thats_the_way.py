import os


def thats_the_way(directory_path, prefix="deep"):
    files_in_directory = os.listdir(directory_path)
    start_with_prefix = [filename for filename in files_in_directory if filename.startswith(prefix)]
    return start_with_prefix


if __name__ == "__main__":
    directory_path = "images"
    filenames = thats_the_way(directory_path)
    # check if thats_the_way return only 2 filenames
    assert len(filenames) == 2
    # print the filenames returned
    print(filenames)
