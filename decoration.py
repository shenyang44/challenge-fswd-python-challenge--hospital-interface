def decorator(my_func):
    def wrapped_func(*args):

        print('\n -------------------------------------')

        my_func(args[0])

        print('\n -------------------------------------')

    return wrapped_func


# @some_decorator  # adds functionality to `my_function`
# def my_function():
#     print("Hello World")
