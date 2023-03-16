import sys
from ft_filter import ft_filter

if __name__ == "__main__":
    sys.tracebacklimit = 0

    assert len(sys.argv) == 3, "the arguments are bad"
    assert sys.argv[2].isnumeric(), "the arguments are bad"

    S = sys.argv[1]
    N = (int)(sys.argv[2])
    lst = S.split()
    filtered_string = ft_filter(lambda string: len(string) > N, lst)
    print(list(filtered_string))
