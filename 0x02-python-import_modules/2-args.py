#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    total = len(sys.argv) - 1  # not including script name

    if total == 1:
        print("1 arguement:")
    elif total == 0:
        print("0 arguments.")
    else:
        print("{} arguements:".format(total))
    for x in range(total):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
