def is_lower_alpha(byte):
    """
    Helper function to check if a binary byte is an ascii code of a lower case english letter.
    :param byte: binary byte to check
    :return: True if byte is a lower case ascii, otherwise False
    """
    return 97 <= byte <= 122


def parsle_tongue(filepath='resources/logo.jpg', chunk_size=1024):
    partial_message = b""
    try:
        with open(filepath, 'rb') as file:
            # read the binary file in smaller chunks
            while chunk := file.read(chunk_size):
                # add the potential partial message from previous chunk to the current one
                data = partial_message + chunk

                message = b""  # store the potential message

                for byte in data:
                    if is_lower_alpha(byte):
                        # current byte is an ascii of english lower case letter - might be a message
                        message += bytes([byte])
                    elif byte == b"!"[0]:
                        if len(message) >= 5:
                            # current byte is an ascii of the char '!'
                            # and the potential message length is 5 or more
                            # congratulations we found the message! let's yield it as an ascii word
                            yield message.decode("ascii")
                    else:
                        # the current byte can't be a part of valid message
                        message = b""

                # so far we got a part of a potential valid message
                # we pass it to the next chunk of data
                partial_message = message
    except FileNotFoundError:
        print("File not found!")


if __name__ == '__main__':
    # iterating our generator to print all founded messages
    for message in parsle_tongue():
        print(message)
