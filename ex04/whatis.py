import sys

if (len(sys.argv) == 1):
	exit()

try:
	assert len(sys.argv) == 2, "AssertionError: more than one argument are provided"
except AssertionError as msg:
	sys.exit(msg)

try:
	assert len(sys.argv[1]) > 0, "AssertionError: argument is not an integer"
except AssertionError as msg:
	sys.exit(msg) 

try:
	assert ((sys.argv[1][0].startswith(("+", "-")) and sys.argv[1][1:].isdigit()) or sys.argv[1].isdigit()), "AssertionError: argmument is not an integer"
except AssertionError as msg:
	sys.exit(msg)

if (sys.argv[1][-1] in ["0", "2", "4", "6", "8"]):
	print("I'm Even.")
else:
	print("I'm Odd.")
