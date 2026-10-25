def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if i < len(expected_types):
                    if not isinstance(args[i], expected_types[i]):
                        raise TypeError(f"Аргумент {i+1} должен быть {expected_types[i]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))

try:
    print(add(2, "3"))
except TypeError as e:
    print(f"Ошибка: {e}")