#!/usr/bin/python3

p = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - p)), end="")
    p = 32 if p == 0 else 0

