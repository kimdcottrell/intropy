import inspect


def print_args(*args):
    """test how *args works"""
    for k, v in enumerate(args):
        print(f"arg array index: {k} contained {v}")


def print_kwargs(**kwargs):
    """test how **kwargs works"""
    for k, v in kwargs.items():
        print(f"kwargs dictionary index {k} contained {v}")


def _internal_func(arg1):
    """
    intended to be an internal, procedural function.
    it is ran within public_func.

    accessible in the help via:
    help(intro_to_functions._internal_func)
    """
    print(f"{inspect.currentframe().f_code.co_name} says: {arg1}!\n"
          f"and it was called by {inspect.currentframe().f_back.f_code.co_name}")


def public_func():
    """so I heard you liked functions, so I put a function inside your function"""
    _internal_func('hi!')


def add(a, b):
    print(f"ADDING: {a} + {b}")
    return a + b
