#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{}" .format(int(0)))
    elif len(sys.argv) == 2:
        print("{}" .format(int(sys.argv[1])))
    else:
        a = int(sys.argv[1])
        for i in range(2, len(sys.argv)):
            a += int(sys.argv[i])
        print("{}" .format(a))
