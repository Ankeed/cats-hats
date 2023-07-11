# 1. Write a decorator that ensures a function is only
# called by users with a specific role. Each function
# should have an user_type with a string type in kwargs.


def is_admin(func):
    def role_check(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return role_check


@is_admin
def show_customer_receipt(user_type: str):
    print('Hello Admin')


show_customer_receipt(user_type='user')  # ValueError: Permission denied
show_customer_receipt(user_type='admin')  # code pass


# 2. Write a decorator that wraps a function in a
# try-except block and prints an error if any
# type of error has happened. Example:


def catch_errors(func):
    def try_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e, "- Error")
    return try_error


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})  # KeyError
some_function_with_risky_operation({'key': 'bar'})  # pass
