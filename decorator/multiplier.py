from functools import wraps


def multiplier(wrapped_function):

    @wraps(wrapped_function)
    def wrapper(*args, **kwds):
        return wrapped_function(*args, **kwds) * 2

    return wrapper
