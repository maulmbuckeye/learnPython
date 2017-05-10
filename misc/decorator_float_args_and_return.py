# From Python in Practice, Mark Summerfield, pp. 48-50
import functools


def mean_unwrapped(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


def float_args_and_return(wrapped_function):
    """
    A decorator
    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function
        :param args: 
        :param kwargs: 
        :return: the result of the wrapped function as a float
        """
        args = [float(arg) for arg in args]
        return float(wrapped_function(*args, **kwargs))
    return wrapper


@float_args_and_return
def mean(first, second, *rest):
    return mean_unwrapped( first, second, *rest)


def float_args_and_return2(wrapped_function):
    """
    A decorator
    """
    @functools.wraps(wrapped_function)
    def wrapper(*args, **kwargs):
        """
        The wrapper function
        :param args: 
        :param kwargs: 
        :return: the result of the wrapped function as a float
        """
        args = [float(arg) for arg in args]
        return float(wrapped_function(*args, **kwargs))
    return wrapper


@float_args_and_return2
def mean2(first, second, *rest):
    return mean_unwrapped( first, second, *rest)


print(mean_unwrapped(1,5))
print(mean_unwrapped(1, 5, 9))
try:
    print(mean_unwrapped("1", 5, 9))
except TypeError as t:
    print(t)

print("\n\n_______Now the first attempt of decorating_____")
print(mean("1", 5, 9))
print(mean.__name__)
print(help(mean))

print("\n\n_______Now the second attempt of decorating_____")
print(mean2("1", 5, 9))
print(mean2.__name__)
print(help(mean2))
