def cache(func):
    notebook = {}

    def wrapper(*args):
        if args in notebook:
            return notebook[args]

        result = func(*args)
        notebook[args] = result
        return result

    return wrapper


@cache
def slow_function(x):
    print("Считаю...")
    return x * 2


print(slow_function(5))
print(slow_function(5))
print(slow_function(10))