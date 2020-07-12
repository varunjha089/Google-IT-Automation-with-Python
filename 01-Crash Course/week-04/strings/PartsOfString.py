def first_and_last(message):
    """
    It will return True if message is empty string or it's First and Last character are same.
    False only when First and Last character are not equal.
    :param message:
    :return: Boolean Value only
    """

    return True if not message.strip() else True if message[0] == message[-1] else False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
