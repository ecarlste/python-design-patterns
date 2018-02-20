from functools import wraps


def adder(wrapped_function):

    @wraps(wrapped_function)
    def wrapper(*args, **kwds):
        return wrapped_function(*args, **kwds) + 10

    return wrapper
