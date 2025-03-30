"""
Week 7 Ex 2 - sent_turtle
"""
class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.

    Changes I did:
        1. added title (str) to the message_details dictionary - for search_inbox implementation
        2. added read (bool) to the message_details dictionary - for read_inbox implementation
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_title (str): The message title
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """ Read a given amount of messages from the user inbox.

        Args:
            username (str): The username to read from its inbox.
            num_messages (int, optional): The amount of messages to read. Defaults to None.

        Returns:
            list: If num_messages is specified, it will return the first num_messages unread messages,
            otherwise it will return all unread messages.

        Raises:
            KeyError: If the username does not exist.
        """
        if num_messages is None:
            user_box = self.boxes[username]
        else:
            user_box = self.boxes[username][:num_messages]

        # only messages that isn't read need to be returned
        user_box = [message_details for message_details in user_box if not message_details['read']]

        messages = []
        for message_details in user_box:
            message_details['read'] = True
            messages.append(message_details)
        return messages

    def search_inbox(self, username, search_string):
        """ Search for messages containing search_string.

        Args:
            username (str): The username to search for his inbox.
            search_string (str): The string to search in the inbox messages.

        Returns:
            list: A list of messages containing search_string.

        Raises:
            KeyError: If username is not exist
        """

        user_box = self.boxes[username]
        result_box = []
        for message_details in user_box:
            if search_string in message_details['title'] or search_string in message_details['body']:
                result_box.append(message_details)
        return result_box


if __name__ == '__main__':
    # test class methods
    users = ['user1', 'user2']
    post_office = PostOffice(users)
    for i in range(10):
        post_office.send_message(users[0], users[1], 'title' + str(i), 'body' + str(i))
    print(post_office.read_inbox(users[1], 2))
    print(post_office.read_inbox(users[1]))
    print(post_office.search_inbox(users[1], '2'))
