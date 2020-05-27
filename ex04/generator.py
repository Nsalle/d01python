import string
import random


def error_check(text, sep, option=None):
    if not isinstance(text, str):
        print("First argument (text) must be a string")
        quit()
    if not isinstance(sep, str):
        print("Second argument (separator) must be a string")
        quit()
    if option:
        if option not in ['shuffle', 'ordered', 'unique']:
            print("Invalid option")
            quit()


def shuffle(text, sep):
    txt = text.split(sep)
    random.shuffle(txt)
    i = 0
    while i < len(txt):
        yield txt[i]
        i += 1


def ordered(text, sep):
    txt = text.split(sep)
    txt.sort()
    i = 0
    while i < len(txt):
        yield txt[i]
        i += 1


def unique(text, sep):
    txt = text.split(sep)
    txt = list(dict.fromkeys(txt))
    i = 0
    while i < len(txt):
        yield txt[i]
        i += 1


def noopt(text, sep):
    txt = text.split(sep)
    i = 0
    while i < len(txt):
        yield txt[i]
        i += 1


def generator(text, sep=" ", option=None):
    error_check(text, sep, option)
    if option == "shuffle":
        return shuffle(text, sep)
    elif option == "ordered":
        return ordered(text, sep)
    elif option == "unique":
        return unique(text, sep)
    else:
        return noopt(text, sep)


# test = "ctest ben dquatre amots ben ben"
# for word in generator(test):
#    print(word)
