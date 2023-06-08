#!/usr/bin/python3

if __name__ == "__main__":  # to execute directly
    """displaying result of addition of all arguements"""
    import sys

    result = 0
    for x in range(len(sys.argv) - 1):  # excluding script name
        result = result + int(sys.argv[x + 1])  # cast arg to intergers
    print("{:d}".format(result))
