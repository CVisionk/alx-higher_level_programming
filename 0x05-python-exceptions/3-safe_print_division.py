#!/usr/bin/python3
def safe_print_division(a, b):
    result = "None"
    try:
        result = a / b
    except Exception:
        pass
    finally:
        result = str(result)
    print("Inside result: {}".format(result))
    return result
