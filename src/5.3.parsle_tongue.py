"""
Week 5 Ex 3 - parsle_tongue
"""
def is_lower_alpha(byte):
    """Check if a binary byte is an ascii code of a lower case english letter.

    Args:
        byte (byte): binary byte to check

    Returns:
        bool: True if byte is a lower case ascii, otherwise False
    """
    return 97 <= byte <= 122


def parsle_tongue(filepath='resources/logo.jpg', chunk_size=1024):
    """Yields an encrypted messages from a binary image file.

    Args:
        filepath (str, optional): The binary image file path.
        chunk_size (int, optional): The size of each bytes chunk read from the file.

    Yields:
        str: Encrypted message (5 or more english letters and after it '!') from the binary image file.
    """
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
    for message_found in parsle_tongue():
        print(message_found)
