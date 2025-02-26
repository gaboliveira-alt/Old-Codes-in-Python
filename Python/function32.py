def light_decorator(func):
    def wrapper():
        result = func()
        print("Off the lights")
        return result
    return wrapper

@light_decorator
def watch_movie():
    return "Aproveite o filme"

print(watch_movie())
