'============Модули и пакеты=========='
# любой файл с расширением '.py' - модуль
 
# пакет - набор модулей (обязательно должен быть фвйл __init__.py)

'=================Работа с файлами==============='
# open - это функция, которая открывает файл в определенном режиме 
'режимы'
# r - read(только для чтения)
# w - write(только для записи, каждый раз когда вы открываете файл в режиме записи то что было внутри очищается)
# a - append(только для дозаписи, добавляет в конец)
# x - создает файл но если такой есть то 
# b - binary (в бинарном виде)

# file = open('test.txt', 'r')
# print(file.read()) 

def execution_logger(func):
    """Decorator that logs the execution of the function."""
    def wrapper(*args, **kwargs):
        print("Executing function...")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

def double_result(func):
    """Decorator that doubles the result of a numeric function."""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return result * 2
            else:
                raise ValueError("Function must return a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

def add_exclamation(func):
    """Decorator that adds an exclamation mark to string results."""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result + "!"
            else:
                raise ValueError("Function must return a string value.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

def limit_calls(max_calls):
    """Decorator that limits the number of times a function can be called."""
    def decorator(func):
        call_count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal call_count
            if call_count < max_calls:
                call_count += 1
                return func(*args, **kwargs)
            else:
                print("Function is no longer available.")
                return None
        return wrapper
    return decorator

def log_arguments(func):
    """Decorator that logs the arguments passed to the function."""
    def wrapper(*args, **kwargs):
        print(f"Arguments received: {args}, {kwargs}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper


@execution_logger
@double_result
def add(a, b):
    return a + b

@execution_logger
@add_exclamation
def greet(name):
    return f"Hello, {name}"

@limit_calls(3)
@log_arguments
def process_data(data):
    return f"Processing {data}"


print(add(2, 3))  
print(greet("Alice"))  
print(process_data("Sample Data")) 
print(process_data("Sample Data"))  
print(process_data("Sample Data")) 
print(process_data("Sample Data"))  
