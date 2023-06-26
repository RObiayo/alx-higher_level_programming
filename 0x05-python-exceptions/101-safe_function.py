#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Funstions executor

    Args:
        fct: Executor function
        args: Arguments for fct.

    Returns:
        If an error appears - None.
        If not - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
