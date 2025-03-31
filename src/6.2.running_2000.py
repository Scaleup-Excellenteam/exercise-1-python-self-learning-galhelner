"""
Week 6 Ex 2 - running_2000
"""
import time


def running_2000(f, *args, **kwargs):
    """Measure the running time of a function with its arguments Using pref_counter for higher precision.

    Args:
        f (function): function to measure.
        args (tuple): arguments to pass to the function.
        kwargs (dictionary): key-value pairs arguments to pass to the function.

    Returns:
        float: the running time of the function execution.
    """
    start_time = time.perf_counter()  # store starting time
    f(*args, **kwargs)  # call the function with given arguments
    end_time = time.perf_counter()  # store ending time
    return end_time - start_time  # return the diff time period


if __name__ == '__main__':
    # test cases
    print(running_2000(print, 'hello'))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
