
"""
Module text_indentation
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    '''
    This function prints a text with 2 new lines\
        after each of these characters: ., ? and :
    '''
    new_text = ''
    if type(text) != str:
        raise TypeError("text must be a string")

    for symbol in ".:?":
        text = (symbol + "\n\n").join(
            [line.strip(" ") for line in text.split(symbol)])

    print("{}".format(text), end="")
