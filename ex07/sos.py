import sys

if __name__ == "__main__":
    sys.tracebacklimit = 0

    assert len(sys.argv) == 2, "the arguments are bad"
    words = sys.argv[1].split()
    assert not [i for i in words if not i.isalnum()], "the arguments are bad"

    NESTED_MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': '/'}
    msg = ""
    for char in sys.argv[1]:
        if char.upper() in NESTED_MORSE:
            msg += NESTED_MORSE[char.upper()] + " "
    if msg.endswith(" "):
        print(msg.strip())
    else:
        print(msg)
