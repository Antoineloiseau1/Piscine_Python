import sys

sys.tracebacklimit = 0

if (len(sys.argv) == 1):
	exit()

assert len(sys.argv) == 2, "more than one argument are provided"
assert len(sys.argv[1]) > 0, "argument is not an integer" 
assert ((sys.argv[1][0].startswith(("+", "-")) and sys.argv[1][1:].isdigit()) or sys.argv[1].isdigit()), "argmument is not an integer"

if (sys.argv[1][-1] in ["0", "2", "4", "6", "8"]):
	print("I'm Even.")
else:
	print("I'm Odd.")
