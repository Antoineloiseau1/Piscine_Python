import sys
import string


if __name__ == "__main__":
    # this program counts the number of characters in his argument or input
    try:
        assert len(sys.argv) <= 2, "AssertionError: more than one \
argument are provided"
    except AssertionError as msg:
        sys.exit(msg)
    if (len(sys.argv) == 1):
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]
    punct = string.punctuation
    print("The text contains", len(text), "characters:")
    print(len([i for i in text if i.isupper()]), "upper letters")
    print(len([i for i in text if i.islower()]), "lower letters")
    print(len([i for i in text if i in punct]), "punctuation marks")
    if (len(sys.argv) == 1):
        print(len([i for i in text if i.isspace()]), "spaces")
    else:
        print(len([i for i in text if i.isspace()]), "spaces")
    print(len([i for i in text if i.isdigit()]), "digits")
