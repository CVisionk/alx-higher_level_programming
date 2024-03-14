#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)-1
    if len(sys.argv) == 1:
        print("{} arguments.".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{} : {}".format(i, arg))
