import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {(end - start) * 1000:.2f} мс")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)

slow_function()