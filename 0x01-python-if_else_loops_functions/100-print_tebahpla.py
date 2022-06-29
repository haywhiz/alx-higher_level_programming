#!/usr/bin/python3
for r in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(r - 32) if r % 2 != 0 else chr(r)), end="")
