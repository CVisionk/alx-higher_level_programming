#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments.".format(len(sys.argv)-1))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{} : {}".format(i, arg))
