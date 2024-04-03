#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numInt = 0
    try:
        for i,item in enumerate(my_list):
            if i < x:
                print("{:d}".format(item))
                numInt += 1
    except Exception:
        pass
    return numInt

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
