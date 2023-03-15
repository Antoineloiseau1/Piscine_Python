import sys


def count_punct(text:  str) -> int:
    count = 0
    for i in range(0, len(text)):
        if text[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            count = count + 1
    return count


if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "AssertionError: more than \
        one argument are provided"
    except AssertionError as msg:
        sys.exit(msg)

    if (len(sys.argv) == 1):
        text = input("What is the text to count?\n")
    else:
        text = sys.argv[1]
    print("The text contains", len(text), "characters:")
    print(len([i for i in text if i.isupper()]), "upper letters")
    print(len([i for i in text if i.islower()]), "lower letters")
    print(count_punct(text), "punctuation marks")
    if (len(sys.argv) == 1):
        print(len([i for i in text if i.isspace()]) + 1, "spaces")
    else:
        print(len([i for i in text if i.isspace()]), "spaces")
    print(len([i for i in text if i.isdigit()]), "digits")
