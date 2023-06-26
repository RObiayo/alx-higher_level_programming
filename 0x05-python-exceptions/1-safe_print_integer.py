#!/usr/bin/python3


def safe_print_integer(value):
    """Display an integer with "{:d}".format().

    Args:
        value (int): Printed integer

    Returns:
        If a TypeError or ValueError appears - False.
        If doesnt - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
