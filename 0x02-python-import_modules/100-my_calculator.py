#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        op = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] in list(op.keys()):
            A = int(sys.argv[1])
            B = int(sys.argv[3])
            print("{} {} {} = {}".format(A, sys.argv[2], B, op[sys.argv[2]](A, B)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
