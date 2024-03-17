#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join(my_string.split('c'))
    my_string = ''.join(my_string.split('C'))
    return mystring
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
