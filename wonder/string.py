import re


def to_snake_case(string):
    string = string.lower()

    string = re.sub('[^a-z0-9]+', '_', string)

    words = string.split('_')

    for i, word in enumerate(words):
        if ' ' in word:
            words[i] = re.sub(' +', '_', word)

    string = '_'.join(words)

    return string
