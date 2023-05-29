#!/usr/bin/python3

def safe_print_division(a, b):
    if isinstance(a, int) and isinstance(b, int):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            result = None
        finally:
            print("Inside result: {}".format(result))
