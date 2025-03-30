from PIL import Image


def remember_remember(filepath, black_threshold=50):
    """
    Extract encrypted message from an image
    :param filepath: encrypted file path
    :param black_threshold: the minimum number represent black pixel
    :return: the encrypted message
    """
    try:
        image = Image.open(filepath).convert('L')  # read the image using pillow package and convert it to grayscale
        pixels = image.load()  # load the pixels from the image
        width, height = image.size  # get the image dimension

        message = ''

        for x in range(width):
            for y in range(height):
                # check if the pixel in the current row is black
                if pixels[x, y] < black_threshold:
                    # encrypted character found, it's a part of the message
                    message += chr(y)

        return message
    except FileNotFoundError:
        print('File not found!')
        return None


if __name__ == '__main__':
    print('Encrypted message: ', remember_remember('resources/code.png'))
