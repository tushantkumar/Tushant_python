
from MyPackage.my_function_file import Stack_calls


def start_fun(service_info, stock_info):
    print("start_fun started".center(40, '_'))
    print(f"Wait while we are contacting {service_info}")
    print(f"Trying to yield stock details of {stock_info} ")
    print("start_fun completed".center(40, '_'))


def log_fun(logger1, logger2):
    print("log_fun started".center(40, '_'))
    print(f"Logging Info to {logger1} ")
    print(f"Logging Info to {logger2} ")
    print("log_fun completed".center(40, '_'))


@Stack_calls(start_fun, log_fun, ["BSE", "Infy"], ["ETW", "Console"])
def actual_fun(x, y, z):
    print("actual_fun Recieving", x, y, z)


actual_fun(10, 20, 30)
