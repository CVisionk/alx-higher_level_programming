#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    for i, item in enumerate(my_list):
        try:
            if i < x:
                print(item, end="")
                num_printed += 1
        except Exception:
            break
    print()
    return num_printed
