""" Convert emoticon to emoji """

def main():
    """ Convert emoticon to emoji """

    # Request user input as plain text (emoticons)
    plain = input("Enter some text: ")

    # Call convert function on plain text and convert (emojis)
    converted = convert(plain)

    # Print converted text
    print(converted)

def convert(emoticon):
    """ Convert emoticons to emojis """
    emoji = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
