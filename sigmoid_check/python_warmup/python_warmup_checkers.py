import inspect
import math
import sys
from io import StringIO
from functools import wraps

def compare_nested(a, b):
    """
    Recursively compares types and values of two elements, including nested structures.
    """
    if type(a) != type(b):
        return False

    # If it's a dictionary, compare keys and values recursively
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return False
        return all(compare_nested(a[key], b[key]) for key in a)

    # If it's a list, tuple, or set, compare elements recursively
    elif isinstance(a, (list, tuple, set)):
        if len(a) != len(b):
            return False
        return all(compare_nested(x, y) for x, y in zip(a, b))

    # If it's any other type, directly compare values
    else:
        return a == b

def output_checker(expected_output):
    """
    Decorator for checking if the function output matches the expected output.

    Args:
        expected_output (str): The expected output of the function.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            old_stdout = sys.stdout
            sys.stdout = captured_output = StringIO()

            try:
                func(*args, **kwargs)
                output = captured_output.getvalue().strip()
                sys.stdout = old_stdout

                if str(output) == str(expected_output):
                    print("✅ Great job! Exercise completed successfully.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
            except Exception:
                sys.stdout = old_stdout
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def variable_checker(expected_variables):
    """
    Decorator for checking if the function returns the expected variables.

    Args:
        expected_variables (dict): A dictionary of expected variable names and their values.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if not isinstance(result, dict):
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
                    return
                if all(result.get(var_name) == expected_value for var_name, expected_value in expected_variables.items()):
                    print("✅ Great job! Exercise completed successfully.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
            except Exception:
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def test_case_checker(test_cases):
    """
    Decorator for checking multiple test cases.

    Args:
        test_cases (list): A list of tuples, each containing input arguments and expected output.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_passed = True
            for inputs, expected in test_cases:
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()

                try:
                    func(*inputs)
                    output = captured_output.getvalue().strip()
                    sys.stdout = old_stdout

                    if str(output) != str(expected):
                        all_passed = False
                        break
                except Exception:
                    sys.stdout = old_stdout
                    all_passed = False
                    break

            if all_passed:
                print("✅ Great job! Exercise completed successfully.")
            else:
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def conditional_test_case_checker(conditional_test_cases):
    """
    Decorator for checking conditional test cases.

    Args:
        conditional_test_cases (list): A list of tuples, each containing input arguments, a condition function, and expected output.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_passed = True
            for inputs, condition, expected in conditional_test_cases:
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()

                try:
                    func(*inputs)
                    output = captured_output.getvalue().strip()
                    sys.stdout = old_stdout

                    if condition(*inputs):
                        if str(output) != str(expected):
                            all_passed = False
                            break
                    elif output:
                        all_passed = False
                        break
                except Exception:
                    sys.stdout = old_stdout
                    all_passed = False
                    break

            if all_passed:
                print("✅ Great job! Exercise completed successfully.")
            else:
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def input_output_checker(test_cases):
    """
    Decorator for checking if a function produces the expected output for given inputs.

    Args:
        test_cases (list): A list of dictionaries, each containing 'input' and 'expected' dictionaries.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_passed = True

            for case in test_cases:
                try:
                    result = func(**case['input'])
                    if result != case['expected']:
                        all_passed = False
                        break
                except Exception:
                    all_passed = False
                    break

            if all_passed:
                print("✅ Great job! Exercise completed successfully.")
            else:
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def input_output_checker_type(test_cases):
    """
    Decorator for checking if a function produces the expected output for given inputs,
    while ensuring that all types and values in both the input and output are identical, 
    even in nested structures.
    
    Args:
        test_cases (list): A list of dictionaries, each containing 'input' and 'expected'.
    
    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_passed = True

            for case in test_cases:
                try:
                    # Call the function with the input arguments
                    result = func(**case['input'])

                    # Check if types and values of result match the expected output, recursively
                    if not compare_nested(result, case['expected']):
                        all_passed = False
                        break

                except Exception as e:
                    print(f"❗ An error occurred: {e}")
                    all_passed = False
                    break

            if all_passed:
                print("✅ Great job! Exercise completed successfully.")
            else:
                print("❗ The implementation is incorrect or the exercise was not implemented.")

        return wrapper
    return decorator

def functions_input_output_checker(test_cases):
    """
    Decorator for checking if the returned function of the function produces the expected output for given inputs.

    Args:
        test_cases (dict): A dictionary where keys are function names and values are lists of test cases.
                           Each test case is a dictionary containing 'input' and 'expected' keys.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                returned_funcs = func(*args, **kwargs)
                all_passed = True
                for func_name, cases in test_cases.items():
                    if func_name not in returned_funcs:
                        all_passed = False
                        break
                    test_func = returned_funcs[func_name]
                    for case in cases:
                        try:
                            args = case['input'].get('*args', [])
                            if args:
                                result = test_func(*args)
                            else:
                                result = test_func(**case['input'])
                            if result != case['expected']:
                                all_passed = False
                                break
                        except Exception:
                            all_passed = False
                            break

                if all_passed:
                    print("✅ Great job! Exercise completed successfully.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
            except Exception:
                print("❗ The implementation is incorrect or the exercise was not implemented.")
        
        return wrapper
    return decorator

def nested_functions_input_output_checker(test_cases):
    """
    Decorator for checking if the returned function (including nested functions) of the function
    produces the expected output for given inputs.

    Args:
        test_cases (dict): A dictionary where keys are function names and values are lists of test cases.
                           Each test case is a dictionary containing 'input' and 'expected' keys.
                           For nested functions, 'input' should be a list of dictionaries, one for each nested call.

    Returns:
        function: Decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                returned_funcs = func(*args, **kwargs)
                all_passed = True
                for func_name, cases in test_cases.items():
                    if func_name not in returned_funcs:
                        all_passed = False
                        break
                    test_func = returned_funcs[func_name]
                    for case in cases:
                        try:
                            if isinstance(case['input'], list):  # Nested function calls
                                result = test_func
                                for input_dict in case['input']:
                                    result = result(**input_dict)
                            else:  # Single function call
                                result = test_func(**case['input'])
                            
                            if result != case['expected']:
                                all_passed = False
                                break
                        except Exception as e:
                            print(f"Error in test case: {e}")
                            all_passed = False
                            break

                if all_passed:
                    print("✅ Great job! Exercise completed successfully.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
            except Exception as e:
                print(f"❗ An error occurred: {e}")
        
        return wrapper
    return decorator

def test_decorator(test_cases, decorated_key):
    """
    A decorator for testing decorator functions.
    
    Args:
        test_cases (list): A list of dictionaries, each containing:
            - 'input': A dictionary with 'func' (the function to be decorated) and its arguments
            - 'expected': The expected output after applying the decorator
    
    Returns:
        function: A decorated function that tests the decorator implementation
    """
    def outer_wrapper(decorator_func):
        @wraps(decorator_func)
        def wrapper(*args, **kwargs):
            try:
                result = decorator_func(*args, **kwargs)
                decorator = result[decorated_key]
                all_passed = True
                
                for case in test_cases:
                    input_func = case['input']['func']
                    input_args = case['input'].get('args', ())
                    input_kwargs = case['input'].get('kwargs', {})
                    expected = case['expected']
                    
                    # Apply the decorator to the input function
                    decorated_func = decorator(input_func)
                    
                    # Call the decorated function and compare the result
                    result = decorated_func(*input_args, **input_kwargs)
                    if result != expected:
                        all_passed = False
                        break
                
                if all_passed:
                    print("✅ All test cases passed. The decorator works as expected.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")
                
                return decorator_func
            except Exception as e:
                print("❗ The implementation is incorrect or the exercise was not implemented.")    
        
        return wrapper
    return outer_wrapper

def test_classes_and_methods(test_cases):
    def outer_wrapper(exercise_func):
        @wraps(exercise_func)
        def wrapper(*args, **kwargs):
            try:
                result = exercise_func(*args, **kwargs)
                
                if not isinstance(result, dict):
                    print("❗ The implementation is incorrect or the exercise was not implemented.")   
                    return result

                all_passed = True
                
                for class_name, class_tests in test_cases.items():
                    if class_name not in result:
                        all_passed = False
                        continue
                    
                    cls = result[class_name]
                    
                    if not isinstance(cls, type):
                        all_passed = False
                        continue

                    # Check parameters
                    if 'parameters' in class_tests:
                        expected_params = set(class_tests['parameters'])
                        try:
                            instance = cls(**{param: None for param in expected_params})
                            actual_params = set(vars(instance).keys()) - {'__dict__', '__weakref__'}
                            if expected_params != actual_params:
                                all_passed = False
                        except Exception as e:
                            all_passed = False
                    
                    # Check subclass
                    if 'subclass_of' in class_tests:
                        parent_class = class_tests['subclass_of']
                        if isinstance(parent_class, str):
                            if parent_class not in result:
                                all_passed = False
                                continue
                            parent_class = result[parent_class]
                        if not issubclass(cls, parent_class):
                            all_passed = False
                    
                    # Check methods
                    if 'methods' in class_tests:
                        for method_name, method_tests in class_tests['methods'].items():
                            if not hasattr(cls, method_name):
                                all_passed = False
                                continue
                            
                            method = getattr(cls, method_name)
                            for test in method_tests:
                                try:
                                    instance = cls(**test.get('init_args', {}))
                                    
                                    # Create instances for method arguments if needed
                                    method_args = {}
                                    for arg_name, arg_value in test.get('args', {}).items():
                                        if isinstance(arg_value, dict) and all(k in arg_value for k in test.get('init_args', {})):
                                            method_args[arg_name] = cls(**arg_value)
                                        else:
                                            method_args[arg_name] = arg_value
                                    
                                    result_test = method(instance, **method_args)
                                    expected = test['expected']
                                    
                                    if isinstance(expected, dict) and 'type' in expected:
                                        # Check if the result is an instance of the expected type
                                        if not isinstance(result_test, cls):
                                            all_passed = False
                                            continue
                                        
                                        # Check attributes of the resulting object
                                        for attr, value in expected.get('attributes', {}).items():
                                            if getattr(result_test, attr) != value:
                                                all_passed = False
                                    elif result_test != expected:
                                        all_passed = False
                                except Exception as e:
                                    all_passed = False
                                    print(f"Error in method {method_name}: {str(e)}")
                    
                    # Check instances
                    if 'instances' in class_tests:
                        for instance_test in class_tests['instances']:
                            try:
                                instance = cls(**instance_test['args'])
                                for attr, value in instance_test.get('attributes', {}).items():
                                    if getattr(instance, attr) != value:
                                        all_passed = False
                            except Exception as e:
                                all_passed = False
                
                if all_passed:
                    print("✅ All tests passed. The classes and methods work as expected.")
                else:
                    print("❗ The implementation is incorrect or the exercise was not implemented.")    
                
                return result
            except Exception as e:
                print(f"❗ The implementation is incorrect or the exercise was not implemented. Error: {str(e)}")    
        
        return wrapper
    return outer_wrapper

# create a decorator that will check if the function has a docstring;
def docstring_checker(configuration):
    def outer_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                the_function = func(*args, **kwargs)
                if not the_function[configuration.get('function', False)]:
                    print("❗ The function does not have a docstring.")
                else:
                    print("✅ The function has a docstring.")
            except Exception:
                print("❗ The implementation is incorrect or the exercise was not implemented.")
        
        return wrapper
    return outer_wrapper

# print the text "Hello, World!" to the console;
check_exercise_1 = output_checker("Hello, World!")
# print the result of 3 + 5;
check_exercise_2 = output_checker("8")
# create a variable called "name" and assign it the value "John";
check_exercise_3 = variable_checker({"name": "John"})
# print the text "Hello, John!" to the console using the variable `name`;
check_exercise_4 = test_case_checker([
    (("John",), "Hello, John!"),
    (("Alice",), "Hello, Alice!"),
    (("Bob",), "Hello, Bob!"),
])
# create a variable called "age" and assign it the value 25;
check_exercise_5 = variable_checker({"age": 25})
# print the text "John is 25 years old" to the console using the variables `name` and `age`
check_exercise_6 = test_case_checker([
    (("John", 25), "John is 25 years old"),
    (("Alice", 30), "Alice is 30 years old"),
    (("Bob", 40), "Bob is 40 years old"),
])
# create a variable called "is_old" and assign it the value True;
check_exercise_7 = variable_checker({"is_old": True})
# print the text "John is old" to the console if `is_old` is True;
check_exercise_8 = conditional_test_case_checker([
    ((True,), lambda x: x, "John is old"),
    ((False,), lambda x: not x, ""),
])
# swap the values of the variables `name` and `age` using a third variable;
check_exercise_9 = input_output_checker([
    {'input': {'name': 'John', 'age': 25}, 'expected': {'name': 25, 'age': 'John'}},
    {'input': {'name': 'Alice', 'age': 30}, 'expected': {'name': 30, 'age': 'Alice'}},
])
# swap the values of the variables `name` and `age` using only two variables;
check_exercise_10 = input_output_checker([
    {'input': {'name': 'John', 'age': 25}, 'expected': {'name': 25, 'age': 'John'}},
    {'input': {'name': 'Alice', 'age': 30}, 'expected': {'name': 30, 'age': 'Alice'}},
])
# create a variable called "height" and assign it the value 1.75;
check_exercise_11 = variable_checker({"height": 1.75})
# print the text "John is 25 years old and is 1.75m tall" to the console using the variables `name`, `age` and `height`;
check_exercise_12 = test_case_checker([
    (("John", 25, 1.75), "John is 25 years old and is 1.75m tall"),
    (("Alice", 30, 1.80), "Alice is 30 years old and is 1.8m tall"),
    (("Bob", 40, 1.70), "Bob is 40 years old and is 1.7m tall"),
])
# create a variable called "is_tall" and a variable called "is_old" and assign them the values True and False, respectively;
check_exercise_13 = variable_checker({"is_tall": True, "is_old": False})
# print the text "John is tall and old" to the console if `is_tall` and `is_old` are True;
check_exercise_14 = conditional_test_case_checker([
    ((True, True), lambda x, y: x and y, "John is tall and old"),
    ((True, False), lambda x, y: x and y, ""),
    ((False, True), lambda x, y: x and y, ""),
    ((False, False), lambda x, y: x and y, ""),
])
# print the text "John is tall or old" to the console if `is_tall` or `is_old` are True;
check_exercise_15 = conditional_test_case_checker([
    ((True, True), lambda x, y: x or y, "John is tall or old"),
    ((True, False), lambda x, y: x or y, "John is tall or old"),
    ((False, True), lambda x, y: x or y, "John is tall or old"),
    ((False, False), lambda x, y: x or y, ""),
])
# print the text "John is not tall" to the console if `is_tall` is False;
check_exercise_16 = conditional_test_case_checker([
    ((True,), lambda x: not x, ""),
    ((False,), lambda x: not x, "John is not tall"),
])
# print the text "John is not old" to the console if `is_old` is False;
check_exercise_17 = conditional_test_case_checker([
    ((True,), lambda x: not x, ""),
    ((False,), lambda x: not x, "John is not old"),
])
# print the text "John is tall and not old" to the console if `is_tall` is True and `is_old` is False;
check_exercise_18 = conditional_test_case_checker([
    ((True, True), lambda x, y: x and not y, ""),
    ((True, False), lambda x, y: x and not y, "John is tall and not old"),
    ((False, True), lambda x, y: x and not y, ""),
    ((False, False), lambda x, y: x and not y, ""),
])
# print the text "John is not tall and old" to the console if `is_tall` is False and `is_old` is True;
check_exercise_19 = conditional_test_case_checker([
    ((True, True), lambda x, y: not x and y, ""),
    ((True, False), lambda x, y: not x and y, ""),
    ((False, True), lambda x, y: not x and y, "John is not tall and old"),
    ((False, False), lambda x, y: not x and y, ""),
])
# print the text "John is older than 30" to the console if `age` is greater than 30;
check_exercise_20 = conditional_test_case_checker([
    ((25,), lambda x: x > 30, ""),
    ((30,), lambda x: x > 30, ""),
    ((35,), lambda x: x > 30, "John is older than 30"),
])
# print the text "John is younger than 30" to the console if `age` is less than 30;
check_exercise_21 = conditional_test_case_checker([
    ((25,), lambda x: x < 30, "John is younger than 30"),
    ((30,), lambda x: x < 30, ""),
    ((35,), lambda x: x < 30, ""),
])
# create a variable `x` and assign it the value 42; create a variable `y` and assign it the value 9; create a variable `z` and assign it the value 7;
check_exercise_22 = variable_checker({"x": 42, "y": 9, "z": 7})
# create a dictionary called `computations` with the keys "add_x_y", "add_x_z", "add_y_z", "sub_x_y", "sub_x_z", "sub_y_z", "mul_x_y", "mul_x_z", "mul_y_z", "div_x_y", "div_x_z", "div_y_z", "mod_x_y", "mod_x_z", "mod_y_z", "pow_x_y", "pow_x_z", "pow_y_z" and the values the results of the respective operations;
check_exercise_23 = input_output_checker([
    {
        'input': {'x': 1, 'y': 1, 'z': 1},
        'expected': {
            'computations': {
                "add_x_y": 2,
                "add_x_z": 2,
                "add_y_z": 2,
                "sub_x_y": 0,
                "sub_x_z": 0,
                "sub_y_z": 0,
                "mul_x_y": 1,
                "mul_x_z": 1,
                "mul_y_z": 1,
                "div_x_y": 1.0,
                "div_x_z": 1.0,
                "div_y_z": 1.0,
                "mod_x_y": 0,
                "mod_x_z": 0,
                "mod_y_z": 0,
                "pow_x_y": 1,
                "pow_x_z": 1,
                "pow_y_z": 1
            }
        }
    },
    {
        'input': {'x': 2, 'y': 3, 'z': 4},
        'expected': {
            'computations': {
                "add_x_y": 5,
                "add_x_z": 6,
                "add_y_z": 7,
                "sub_x_y": -1,
                "sub_x_z": -2,
                "sub_y_z": -1,
                "mul_x_y": 6,
                "mul_x_z": 8,
                "mul_y_z": 12,
                "div_x_y": 0.6666666666666666,
                "div_x_z": 0.5,
                "div_y_z": 0.75,
                "mod_x_y": 2,
                "mod_x_z": 2,
                "mod_y_z": 3,
                "pow_x_y": 8,
                "pow_x_z": 16,
                "pow_y_z": 81
            }
        }
    },
])
# given a tuple `coordinates` with the values (1, 2, 3), unpack the values into the variables `x`, `y` and `z`;
check_exercise_24 = input_output_checker([
    {'input': {'coordinates': (1, 2, 3)}, 'expected': {'x': 1, 'y': 2, 'z': 3}},
    {'input': {'coordinates': (4, 5, 6)}, 'expected': {'x': 4, 'y': 5, 'z': 6}},
])
# create a tuple called `coordinates` with the values of the variables `x`, `y` and `z`;
check_exercise_25 = input_output_checker([
    {'input': {'x': 1, 'y': 2, 'z': 3}, 'expected': {'coordinates': (1, 2, 3)}},
    {'input': {'x': 4, 'y': 5, 'z': 6}, 'expected': {'coordinates': (4, 5, 6)}},
])
# convert the variable `number1` from float to integer and `number2` from integer to float;
check_exercise_26 = input_output_checker_type([
    {'input': {'number1': 1.0, 'number2': 2}, 'expected': {'number1': 1, 'number2': 2.0}},
    {'input': {'number1': 3.0, 'number2': 4}, 'expected': {'number1': 3, 'number2': 4.0}},
])
# convert the variable `elements1` from a list to a tuple and `elements2` from a tuple to a list;
check_exercise_27 = input_output_checker_type([
    {'input': {'elements1': [1, 2, 3], 'elements2': (4, 5, 6)}, 'expected': {'elements1': (1, 2, 3), 'elements2': [4, 5, 6]}},
    {'input': {'elements1': [7, 8, 9], 'elements2': (10, 11, 12)}, 'expected': {'elements1': (7, 8, 9), 'elements2': [10, 11, 12]}},
])
# given the list `elements`, set the value true to the variable `present` if the element "Python" is in the list, otherwise return false;
check_exercise_28 = input_output_checker([
    {'input': {'elements': ["Java", "C++", "Python", "JavaScript"]}, 'expected': {'present': True}},
    {'input': {'elements': ["Java", "C++", "JavaScript"]}, 'expected': {'present': False}},
])
# given the list `elements` and the list `to_check`, create the dictionary `presence` with the keys being the elements of `to_check` and the values being True if the element is in `elements`, otherwise False;
check_exercise_29 = input_output_checker([
    {
        'input': {'elements': ["Java", "C++", "Python", "JavaScript"], 'to_check': ["Python", "JavaScript", "Ruby"]},
        'expected': {'presence': {"Python": True, "JavaScript": True, "Ruby": False}}
    },
    {
        'input': {'elements': ["Java", "C++", "JavaScript"], 'to_check': ["Python", "JavaScript", "Ruby"]},
        'expected': {'presence': {"Python": False, "JavaScript": True, "Ruby": False}}
    },
])
# given the variable `text_to_repeat`, repeat it 5 times and assign it to the variable `text`;
check_exercise_30 = input_output_checker([
    {'input': {'text_to_repeat': "Hello"}, 'expected': {'text': "HelloHelloHelloHelloHello"}},
    {'input': {'text_to_repeat': "World"}, 'expected': {'text': "WorldWorldWorldWorldWorld"}},
])
 # given the variable `text`, assign to the variable `text` the first 5 characters of the string;
check_exercise_31 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'text': "Hello"}},
    {'input': {'text': "Python Programming"}, 'expected': {'text': "Pytho"}},
])
# given the variable `text`, assign the last 5 characters to the variable `last_five`;
check_exercise_32 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'last_five': "orld!"}},
    {'input': {'text': "Python Programming"}, 'expected': {'last_five': "mming"}},
])
# given the variable `text`, change the text in uppercase;
check_exercise_33 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'text': "HELLO, WORLD!"}},
    {'input': {'text': "Python Programming"}, 'expected': {'text': "PYTHON PROGRAMMING"}},
])
# given the variable `text`, change the the text in lowercase;
check_exercise_34 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'text': "hello, world!"}},
    {'input': {'text': "Python Programming"}, 'expected': {'text': "python programming"}},
])
# given the variable `text`, change the text with the first letter in uppercase;
check_exercise_35 = input_output_checker([
    {'input': {'text': "hello, world!"}, 'expected': {'text': "Hello, world!"}},
    {'input': {'text': "python programming"}, 'expected': {'text': "Python programming"}},
])
# given the variable `text`, assignt the 18th character to the variable `char`;
check_exercise_36 = input_output_checker([
    {'input': {'text': "123456789123456789"}, 'expected': {'char': "9"}},
    {'input': {'text': "Python Programming"}, 'expected': {'char': "g"}},
])
# given the variable `text`, assign the last character to the variable `last_char`;
check_exercise_37 = input_output_checker([
    {'input': {'text': "123456789123456789"}, 'expected': {'last_char': "9"}},
    {'input': {'text': "Python Programming"}, 'expected': {'last_char': "g"}},
])
# given the variable `text`, extract every third character starting the first one and assign it to the variable `every_third`;
check_exercise_38 = input_output_checker([
    {'input': {'text': "123456789123456789"}, 'expected': {'every_third': "147147"}},
    {'input': {'text': "Python Programming"}, 'expected': {'every_third': "Ph oai"}},
])
# given the variable `text`, extract every third character starting the second one and assign it to the variable `every_third`;
check_exercise_39 = input_output_checker([
    {'input': {'text': "123456789123456789"}, 'expected': {'every_third': "258258"}},
    {'input': {'text': "Python Programming"}, 'expected': {'every_third': "yoPgmn"}},
])
# given the variable `text` assign to the variable `length` the length of the string;
check_exercise_40 = input_output_checker([
    {'input': {'text': "123456789123456789"}, 'expected': {'length': 18}},
    {'input': {'text': "Python Programming"}, 'expected': {'length': 18}},
])
# given the variable `text`, assign to the variable `words` the number of words in the string;
check_exercise_41 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'words': 2}},
    {'input': {'text': "Python Programming"}, 'expected': {'words': 2}},
])
# given the variable `text`, assign to the variable `words` a list with all the words in the string;
check_exercise_42 = input_output_checker([
    {'input': {'text': "Hello, World!"}, 'expected': {'words': ["Hello,", "World!"]}},
    {'input': {'text': "Python Programming"}, 'expected': {'words': ["Python", "Programming"]}},
])
# given the list `elements`, assign to the variable `last_element` the last element of the list;
check_exercise_43 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'last_element': 5}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'last_element': "Programming"}},
])
# given the list `elements`, assign to the variable `first_half` the first half of the list;
check_exercise_44 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'first_half': [1, 2]}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'first_half': ["Python"]}},
])
# given the list `elements`, assign to the variable `second_half` the second half of the list;
check_exercise_45 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'second_half': [3, 4, 5]}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'second_half': ["Programming"]}},
])
# given the list `elements`, assign to the variable `middle` the middle element of the list given that the list has an odd number of elements;
check_exercise_46 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'middle': 3}},
    {'input': {'elements': ["Yolo", "Python", "Programming"]}, 'expected': {'middle': "Python"}},
])
# given the list `elements`, assign to the variable `sorted_elements` the list sorted in ascending order;
check_exercise_47 = input_output_checker([
    {'input': {'elements': [5, 3, 1, 4, 2]}, 'expected': {'sorted_elements': [1, 2, 3, 4, 5]}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'sorted_elements': ["Programming", "Python"]}},
])
# given the list `elements`, assign to the variable `reversed_elements` the list in reverse order;
check_exercise_48 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'reversed_elements': [5, 4, 3, 2, 1]}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'reversed_elements': ["Programming", "Python"]}},
])
# given the list `elements`, assign to the variable `unique_elements` the list with unique elements;
check_exercise_49 = input_output_checker([
    {'input': {'elements': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]}, 'expected': {'unique_elements': [1, 2, 3, 4]}},
    {'input': {'elements': ["Python", "Python", "Programming"]}, 'expected': {'unique_elements': ["Programming", "Python"]}},
])
# given the list `elements`, insert the element "Python" in the second position of the list, append the element "is" in the last position and remove the element "Java", and add the elements of the list `elements_to_add` to the list;
check_exercise_50 = input_output_checker([
    {'input': {'elements': ["Java", "Programming"], 'elements_to_add': ["Python", "is"]}, 'expected': {'elements': ["Python", "Programming", "is", "Python", "is"]}},
    {'input': {'elements': ["Java", 2], 'elements_to_add': [4, 5]}, 'expected': {'elements': ["Python", 2, "is", 4, 5]}},
])
# given the list `elements`, assign to the variable `sum_elements` the sum of the elements;
check_exercise_51 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'sum_elements': 15}},
    {'input': {'elements': [10, 20, 30, 40, 50]}, 'expected': {'sum_elements': 150}},
])
# given the list `elements`, assign to the variable `max_element` the maximum element of the list;
check_exercise_52 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'max_element': 5}},
    {'input': {'elements': [10, 20, 30, 40, 50]}, 'expected': {'max_element': 50}},
])
# given the list `elements`, assign to the variable `min_element` the minimum element of the list;
check_exercise_53 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'min_element': 1}},
    {'input': {'elements': [10, 20, 30, 40, 50]}, 'expected': {'min_element': 10}},
])
# given the list `elements`, assign to the variable `average` the average of the elements;
check_exercise_54 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'average': 3.0}},
    {'input': {'elements': [10, 20, 30, 40, 50]}, 'expected': {'average': 30.0}},
])
# given the list `elements`, pop the last element of the list and assign it to the variable `last_element`;
check_exercise_55 = input_output_checker([
    {'input': {'elements': [1, 2, 3, 4, 5]}, 'expected': {'last_element': 5, 'elements': [1, 2, 3, 4]}},
    {'input': {'elements': ["Python", "Programming"]}, 'expected': {'last_element': "Programming", 'elements': ["Python"]}},
])
# given the tuples `coordinates1` and `coordinates2`, assign to the variable `distance` the distance between the two points;
check_exercise_56 = input_output_checker([
    {'input': {'coordinates1': (0, 0), 'coordinates2': (3, 4)}, 'expected': {'distance': 5.0}},
    {'input': {'coordinates1': (1, 1), 'coordinates2': (4, 5)}, 'expected': {'distance': 5.0}},
])
# given the tuples `first_tuple` and `second_tuple`, assign to the variable `concatenated_tuple` the concatenation of the two tuples;
check_exercise_57 = input_output_checker([
    {'input': {'first_tuple': (1, 2, 3), 'second_tuple': (4, 5, 6)}, 'expected': {'concatenated_tuple': (1, 2, 3, 4, 5, 6)}},
    {'input': {'first_tuple': ("Python", "Programming"), 'second_tuple': ("is", "fun")}, 'expected': {'concatenated_tuple': ("Python", "Programming", "is", "fun")}},
])
# given the tuple `tuple_to_multiply`, assign to the variable `multiplied_tuple` the tuple multiplied by 3;
check_exercise_58 = input_output_checker([
    {'input': {'tuple_to_multiply': (1, 2, 3)}, 'expected': {'multiplied_tuple': (1, 2, 3, 1, 2, 3, 1, 2, 3)}},
    {'input': {'tuple_to_multiply': ("Python", "Programming")}, 'expected': {'multiplied_tuple': ("Python", "Programming", "Python", "Programming", "Python", "Programming")}},
])
# given the dictionary `student_dictionary`, assign to the variable `students` a list with all the keys of the dictionary;
check_exercise_59 = input_output_checker([
    {'input': {'student_dictionary': {"Alice": 25, "Bob": 30, "Charlie": 35}}, 'expected': {'students': ["Alice", "Bob", "Charlie"]}},
    {'input': {'student_dictionary': {"John": 20, "Jane": 22, "Jack": 24}}, 'expected': {'students': ["John", "Jane", "Jack"]}},
])
# given the dictionary `student_dictionary`, assign to the variable `grades`a list with all the values of the dictionary;
check_exercise_60 = input_output_checker([
    {'input': {'student_dictionary': {"Alice": 25, "Bob": 30, "Charlie": 35}}, 'expected': {'grades': [25, 30, 35]}},
    {'input': {'student_dictionary': {"John": 20, "Jane": 22, "Jack": 24}}, 'expected': {'grades': [20, 22, 24]}},
])
# given the dictionary `student_dictionary`, assign to the variable `students` a list of all the items of the dictionary;
check_exercise_61 = input_output_checker([
    {'input': {'student_dictionary': {"Alice": 25, "Bob": 30, "Charlie": 35}}, 'expected': {'students': [("Alice", 25), ("Bob", 30), ("Charlie", 35)]}},
    {'input': {'student_dictionary': {"John": 20, "Jane": 22, "Jack": 24}}, 'expected': {'students': [("John", 20), ("Jane", 22), ("Jack", 24)]}},
])
# given the dictionaries `class_dictionary` and `students_dictionary`, add to the `class_dictionary` the items of the `students_dictionary`;
check_exercise_62 = input_output_checker([
    {'input': {'class_dictionary': {"Alice": 25, "Bob": 30}, 'students_dictionary': {"Charlie": 35, "David": 40}}, 'expected': {'class_dictionary': {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}}},
    {'input': {'class_dictionary': {"John": 20, "Jane": 22}, 'students_dictionary': {"Jack": 24, "Jill": 26}}, 'expected': {'class_dictionary': {"John": 20, "Jane": 22, "Jack": 24, "Jill": 26}}},
])
# given the dictionary `class_dictionary`, remove the item with the key "John";
check_exercise_63 = input_output_checker([
    {'input': {'class_dictionary': {"Alice": 25, "John": 30, "Charlie": 35}}, 'expected': {'class_dictionary': {"Alice": 25, "Charlie": 35}}},
    {'input': {'class_dictionary': {"John": 20, "Jane": 22, "Jack": 24}}, 'expected': {'class_dictionary': {"Jane": 22, "Jack": 24}}},
])
# given the dictionary `class_dictionary`, assign to the variable `alex_grade` the grade of Alex, if it exists;
check_exercise_64 = input_output_checker([
    {'input': {'class_dictionary': {"Alice": 25, "Bob": 30, "Charlie": 35}}, 'expected': {'alex_grade': None}},
    {'input': {'class_dictionary': {"Alex": 40, "Jane": 22, "Jack": 24}}, 'expected': {'alex_grade': 40}},
])
# given the set `first_set`, assign to the variable `second_set` the `first_set` with the elements "Python" and "is" added;
check_exercise_65 = input_output_checker([
    {'input': {'first_set': {1, 2, 3}}, 'expected': {'second_set': {1, 2, 3, "Python", "is"}}},
    {'input': {'first_set': {"Python", "Programming"}}, 'expected': {'second_set': {"Python", "Programming", "Python", "is"}}},
])
# given the set `first_set`, assign to the variable `second_set` the `first_set` with the elements "Python" and "is" removed;
check_exercise_66 = input_output_checker([
    {'input': {'first_set': {1, "Python", "is"}}, 'expected': {'second_set': {1, }}},
    {'input': {'first_set': {"Python", "Programming", "is"}}, 'expected': {'second_set': {"Programming"}}},
])
# given the set `first_set`, assign to the variable `second_set` the union of `first_set` with the set {"Python"};
check_exercise_67 = input_output_checker_type([
    {'input': {'first_set': {"Python", "Python"}}, 'expected': {'second_set': {"Python"}}},
])
# given the sets `first_set` and `second_set`, assign to the variable `third_set` the intersection of the two sets;
check_exercise_68 = input_output_checker([
    {'input': {'first_set': {1, 2, 3}, 'second_set': {3, 4}}, 'expected': {'third_set': {3}}},
    {'input': {'first_set': {"Python", "Programming"}, 'second_set': {"Programming", "is"}}, 'expected': {'third_set': {"Programming"}}},
])
# given the sets `first_set` and `second_set`, assign to the variable `third_set` the difference of the two sets;
check_exercise_69 = input_output_checker([
    {'input': {'first_set': {1, 2, 3}, 'second_set': {2, 3, 4}}, 'expected': {'third_set': {1}}},
    {'input': {'first_set': {"Python", "Programming"}, 'second_set': {"Programming", "is"}}, 'expected': {'third_set': {"Python"}}},
])
# given the sets `first_set` and `second_set`, assign to the variable `third_set` the symmetric difference of the two sets and remove the element "Python" from it, if present;
check_exercise_70 = input_output_checker([
    {'input': {'first_set': {2, 3}, 'second_set': {2, 3, 4}}, 'expected': {'third_set': {4}}},
    {'input': {'first_set': {"Programming"}, 'second_set': {"Programming", "is"}}, 'expected': {'third_set': {"is"}}},
])
# convert all values of the dictionary `computations` to floats;
check_exercise_71 = input_output_checker_type([
    {'input': {'computations': {"add_x_y": 2, "add_x_z": 2, "add_y_z": 2, "sub_x_y": 0, "sub_x_z": 0, "sub_y_z": 0, "mul_x_y": 1, "mul_x_z": 1, "mul_y_z": 1, "div_x_y": 1.0, "div_x_z": 1.0, "div_y_z": 1.0, "mod_x_y": 0, "mod_x_z": 0, "mod_y_z": 0, "pow_x_y": 1, "pow_x_z": 1, "pow_y_z": 1}},
     'expected': {'computations': {"add_x_y": 2.0, "add_x_z": 2.0, "add_y_z": 2.0, "sub_x_y": 0.0, "sub_x_z": 0.0, "sub_y_z": 0.0, "mul_x_y": 1.0, "mul_x_z": 1.0, "mul_y_z": 1.0, "div_x_y": 1.0, "div_x_z": 1.0, "div_y_z": 1.0, "mod_x_y": 0.0, "mod_x_z": 0.0, "mod_y_z": 0.0, "pow_x_y": 1.0, "pow_x_z": 1.0, "pow_y_z": 1.0}},
    },
    {'input': {'computations': {"add_x_y": 5, "add_x_z": 6, "add_y_z": 7, "sub_x_y": -1, "sub_x_z": -2, "sub_y_z": -1, "mul_x_y": 6, "mul_x_z": 8, "mul_y_z": 12, "div_x_y": 0.6666666666666666, "div_x_z": 0.5, "div_y_z": 0.75, "mod_x_y": 2, "mod_x_z": 2, "mod_y_z": 3, "pow_x_y": 8, "pow_x_z":16, "pow_y_z": 81}},
     'expected': {'computations': {"add_x_y": 5.0, "add_x_z": 6.0, "add_y_z": 7.0, "sub_x_y": -1.0, "sub_x_z": -2.0, "sub_y_z": -1.0, "mul_x_y": 6.0, "mul_x_z": 8.0, "mul_y_z": 12.0, "div_x_y": 0.6666666666666666, "div_x_z": 0.5, "div_y_z": 0.75, "mod_x_y": 2.0, "mod_x_z": 2.0, "mod_y_z": 3.0, "pow_x_y": 8.0, "pow_x_z": 16.0, "pow_y_z": 81.0}},
    },
])
# convert all values of the dictionary `computations` to integers;
check_exercise_72 = input_output_checker_type([
    {'input': {'computations': {"add_x_y": 2.0, "add_x_z": 2.0, "add_y_z": 2.0, "sub_x_y": 0.0, "sub_x_z": 0.0, "sub_y_z": 0.0, "mul_x_y": 1.0, "mul_x_z": 1.0, "mul_y_z": 1.0, "div_x_y": 1.0, "div_x_z": 1.0, "div_y_z": 1.0, "mod_x_y": 0.0, "mod_x_z": 0.0, "mod_y_z": 0.0, "pow_x_y": 1.0, "pow_x_z": 1.0, "pow_y_z": 1.0}},
     'expected': {'computations': {"add_x_y": 2, "add_x_z": 2, "add_y_z": 2, "sub_x_y": 0, "sub_x_z": 0, "sub_y_z": 0, "mul_x_y": 1, "mul_x_z": 1, "mul_y_z": 1, "div_x_y": 1, "div_x_z": 1, "div_y_z": 1, "mod_x_y": 0, "mod_x_z": 0, "mod_y_z": 0, "pow_x_y": 1, "pow_x_z": 1, "pow_y_z": 1}},
    },
    {'input': {'computations': {"add_x_y": 5.0, "add_x_z": 6.0, "add_y_z": 7.0, "sub_x_y": -1.0, "sub_x_z": -2.0, "sub_y_z": -1.0, "mul_x_y": 6.0, "mul_x_z": 8.0, "mul_y_z": 12.0, "div_x_y": 0.6666666666666666, "div_x_z": 0.5, "div_y_z": 0.75, "mod_x_y": 2.0, "mod_x_z": 2.0, "mod_y_z":3.0, "pow_x_y": 8.0, "pow_x_z": 16.0, "pow_y_z": 81.0}},
     'expected': {'computations': {"add_x_y": 5, "add_x_z": 6, "add_y_z": 7, "sub_x_y": -1, "sub_x_z": -2, "sub_y_z": -1, "mul_x_y": 6, "mul_x_z": 8, "mul_y_z": 12, "div_x_y": 0, "div_x_z": 0, "div_y_z": 0, "mod_x_y": 2, "mod_x_z": 2, "mod_y_z": 3, "pow_x_y": 8, "pow_x_z": 16, "pow_y_z": 81}},
    },
])
# create a dictionary called `comparisons` with the keys "eq_x_y", "eq_x_z", "eq_y_z", "ne_x_y", "ne_x_z", "ne_y_z", "gt_x_y", "gt_x_z", "gt_y_z", "ge_x_y", "ge_x_z", "ge_y_z", "lt_x_y", "lt_x_z", "lt_y_z", "le_x_y", "le_x_z", "le_y_z" and the values the results of the respective operations given the variables x, y, z;
check_exercise_73 = input_output_checker([
    {
        'input': {'x': 1, 'y': 1, 'z': 1},
        'expected': {
            'comparisons': {
                "eq_x_y": True,
                "eq_x_z": True,
                "eq_y_z": True,
                "ne_x_y": False,
                "ne_x_z": False,
                "ne_y_z": False,
                "gt_x_y": False,
                "gt_x_z": False,
                "gt_y_z": False,
                "ge_x_y": True,
                "ge_x_z": True,
                "ge_y_z": True,
                "lt_x_y": False,
                "lt_x_z": False,
                "lt_y_z": False,
                "le_x_y": True,
                "le_x_z": True,
                "le_y_z": True
            }
        }
    },
    {
        'input': {'x': 2, 'y': 3, 'z': 4},
        'expected': {
            'comparisons': {
                "eq_x_y": False,
                "eq_x_z": False,
                "eq_y_z": False,
                "ne_x_y": True,
                "ne_x_z": True,
                "ne_y_z": True,
                "gt_x_y": False,
                "gt_x_z": False,
                "gt_y_z": False,
                "ge_x_y": False,
                "ge_x_z": False,
                "ge_y_z": False,
                "lt_x_y": True,
                "lt_x_z": True,
                "lt_y_z": True,
                "le_x_y": True,
                "le_x_z": True,
                "le_y_z": True
            }
        }
    },
])
# create a dictionary called `logicals` with the keys "and_x_y", "and_x_z", "and_y_z", "or_x_y", "or_x_z", "or_y_z", "not_x", "not_y", "not_z" and the values the results of the respective operations given the variables x, y, z;
check_exercise_74 = input_output_checker([
    {
        'input': {'x': True, 'y': True, 'z': True},
        'expected': {
            'logicals': {
                "and_x_y": True,
                "and_x_z": True,
                "and_y_z": True,
                "or_x_y": True,
                "or_x_z": True,
                "or_y_z": True,
                "not_x": False,
                "not_y": False,
                "not_z": False
            }
        }
    },
    {
        'input': {'x': True, 'y': False, 'z': True},
        'expected': {
            'logicals': {
                "and_x_y": False,
                "and_x_z": True,
                "and_y_z": False,
                "or_x_y": True,
                "or_x_z": True,
                "or_y_z": True,
                "not_x": False,
                "not_y": True,
                "not_z": False
            }
        }
    },
])
# replace the word "amazing!" with "amazing! Especially when is taught at Sigmoid" in the variable `amazing_string`;
check_exercise_75 = test_case_checker([
    (("Python is amazing!",), "Python is amazing! Especially when is taught at Sigmoid"),
])
# Given the variable `numero`, assign to the variable `resultado` the string `positive` if `numero` is positive, `negative` if `numero` is negative, and `zero` if `numero` is zero
check_exercise_76 = input_output_checker([
    {'input': {'numero': 1}, 'expected': {'resultado': "positive"}},
    {'input': {'numero': -1}, 'expected': {'resultado': "negative"}},
    {'input': {'numero': 0}, 'expected': {'resultado': "zero"}},
])
# Given the variable `age`, assign to the variable `can_vote` "permis" if `age` is 18 or older, "nepermis" otherwise
check_exercise_77 = input_output_checker([
    {'input': {'age': 18}, 'expected': {'can_vote': "permis"}},
    {'input': {'age': 17}, 'expected': {'can_vote': "nepermis"}},
])
# Given the variable `temperature`, assign to the variable `state` the string `solid` if `temperature` is less than 0, `liquid` if `temperature` is between 0 and 100, and `gas` if `temperature` is greater than 100
check_exercise_78 = input_output_checker([
    {'input': {'temperature': -1}, 'expected': {'state': "solid"}},
    {'input': {'temperature': 0}, 'expected': {'state': "liquid"}},
    {'input': {'temperature': 101}, 'expected': {'state': "gas"}},
])
# Given the variable `score`, assign to the variable `grade` the string "A" if `score` is 90 or above, "B" if it's 80 or above, "C" otherwise
check_exercise_79 = input_output_checker([
    {'input': {'score': 90}, 'expected': {'grade': "A"}},
    {'input': {'score': 80}, 'expected': {'grade': "B"}},
    {'input': {'score': 70}, 'expected': {'grade': "C"}},
])
# Given the variable `day`, assign to the variable `day_type` the string "weekend" if `day` is "Saturday" or "Sunday", "weekday" if it's "Monday" through "Friday", "invalid" otherwise
check_exercise_80 = input_output_checker([
    {'input': {'day': "Saturday"}, 'expected': {'day_type': "weekend"}},
    {'input': {'day': "Monday"}, 'expected': {'day_type': "weekday"}},
    {'input': {'day': "Invalid"}, 'expected': {'day_type': "invalid"}},
    {'input': {'day': "Sunday"}, 'expected': {'day_type': "weekend"}},
    {'input': {'day': "Friday"}, 'expected': {'day_type': "weekday"}},
    {'input': {'day': "Tuesday"}, 'expected': {'day_type': "weekday"}},
    {'input': {'day': "Wednesday"}, 'expected': {'day_type': "weekday"}},
    {'input': {'day': "Thursday"}, 'expected': {'day_type': "weekday"}},
])
# Given the variables `income` and `dependents`, assign to the variable `tax_rate` 0.1 if `income` < 50000 or `dependents` > 3, 0.2 if `income` < 100000, 0.3 otherwise
check_exercise_81 = input_output_checker([
    {'input': {'income': 40000, 'dependents': 4}, 'expected': {'tax_rate': 0.1}},
    {'input': {'income': 60000, 'dependents': 2}, 'expected': {'tax_rate': 0.2}},
    {'input': {'income': 120000, 'dependents': 2}, 'expected': {'tax_rate': 0.3}},
])
# Given the variables `is_raining` and `has_umbrella`, assign to the variable `action` the string "Stay home" if `is_raining` is True and `has_umbrella` is False, "Take umbrella" if `is_raining` is True and `has_umbrella` is True, "Go out" otherwise
check_exercise_82 = input_output_checker([
    {'input': {'is_raining': True, 'has_umbrella': False}, 'expected': {'action': "Stay home"}},
    {'input': {'is_raining': True, 'has_umbrella': True}, 'expected': {'action': "Take umbrella"}},
    {'input': {'is_raining': False, 'has_umbrella': False}, 'expected': {'action': "Go out"}},
])
# Given the variables `is_weekend` and `is_holiday`, assign to the variable `is_day_off` True if either `is_weekend` or `is_holiday` is True, False otherwise
check_exercise_83 = input_output_checker([
    {'input': {'is_weekend': True, 'is_holiday': False}, 'expected': {'is_day_off': True}},
    {'input': {'is_weekend': False, 'is_holiday': True}, 'expected': {'is_day_off': True}},
    {'input': {'is_weekend': False, 'is_holiday': False}, 'expected': {'is_day_off': False}},
])
# Given the variables `is_sunny`, `is_warm`, and `has_sunscreen`, assign to the variable `beach_day` "Yes" if it's sunny and warm and you have sunscreen, or if it's sunny and not too warm (regardless of sunscreen), "No" otherwise
check_exercise_84 = input_output_checker([
    {'input': {'is_sunny': True, 'is_warm': True, 'has_sunscreen': True}, 'expected': {'beach_day': "Yes"}},
    {'input': {'is_sunny': True, 'is_warm': False, 'has_sunscreen': True}, 'expected': {'beach_day': "Yes"}},
    {'input': {'is_sunny': True, 'is_warm': True, 'has_sunscreen': False}, 'expected': {'beach_day': "No"}},
    {'input': {'is_sunny': False, 'is_warm': True, 'has_sunscreen': True}, 'expected': {'beach_day': "No"}},
])
# Given the variable `number`, assign to the variable `parity` the string "even" if `number` is even, "odd" otherwise, using a ternary operator
check_exercise_85 = input_output_checker([
    {'input': {'number': 2}, 'expected': {'parity': "even"}},
    {'input': {'number': 3}, 'expected': {'parity': "odd"}},
])
# Given the variable `fruit`, assign to the variable `is_citrus` True if `fruit` is in the list ["orange", "lemon", "lime", "grapefruit"], False otherwise
check_exercise_86 = input_output_checker([
    {'input': {'fruit': "orange"}, 'expected': {'is_citrus': True}},
    {'input': {'fruit': "apple"}, 'expected': {'is_citrus': False}},
    {'input': {'fruit': "lemon"}, 'expected': {'is_citrus': True}},
    {'input': {'fruit': "grapefruit"}, 'expected': {'is_citrus': True}},
    {'input': {'fruit': "lime"}, 'expected': {'is_citrus': True}},
    {'input': {'fruit': "banana"}, 'expected': {'is_citrus': False}},
])
# Given a list of numbers called `numbers`, assign to the variable `has_negative` True if any number in the list is negative, False otherwise
check_exercise_87 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4, 5]}, 'expected': {'has_negative': False}},
    {'input': {'numbers': [1, 2, 3, -4, 5]}, 'expected': {'has_negative': True}},
    {'input': {'numbers': [1, 2, 3, 4, 5, -1]}, 'expected': {'has_negative': True}},
])
# Given a list of booleans called `test_results`, assign to the variable `all_passed` True if all values in the list are True, False otherwise
check_exercise_88 = input_output_checker([
    {'input': {'test_results': [True, True, True]}, 'expected': {'all_passed': True}},
    {'input': {'test_results': [True, False, True]}, 'expected': {'all_passed': False}},
    {'input': {'test_results': [False, False, False]}, 'expected': {'all_passed': False}},
])
# Given the variable `password`, assign to the variable `is_correct` True if `password` is "secret123", False otherwise
check_exercise_89 = input_output_checker([
    {'input': {'password': "secret123"}, 'expected': {'is_correct': True}},
    {'input': {'password': "password"}, 'expected': {'is_correct': False}},
])
# Given the variable `username`, assign to the variable `is_valid` True if the length of `username` is between 3 and 20 characters (inclusive), False otherwise
check_exercise_90 = input_output_checker([
    {'input': {'username': "abc"}, 'expected': {'is_valid': True}},
    {'input': {'username': "a"}, 'expected': {'is_valid': False}},
    {'input': {'username': "a" * 21}, 'expected': {'is_valid': False}},
])
# Given the variable `num`, assign to the variable `category` the string "low" if `num` is less than 50, "medium" if it's between 50 and 100, "high" if it's greater than 100
check_exercise_91 = input_output_checker([
    {'input': {'num': 49}, 'expected': {'category': "low"}},
    {'input': {'num': 50}, 'expected': {'category': "medium"}},
    {'input': {'num': 101}, 'expected': {'category': "high"}},
])
# Given the variable `email`, assign to the variable `domain` the string "personal" if `email` ends with "@gmail.com", "work" if it ends with "@company.com", "education" if it ends with ".edu", "unknown" otherwise
check_exercise_92 = input_output_checker([
    {'input': {'email': "example@gmail.com"}, 'expected': {'domain': "personal"}},
    {'input': {'email': "example@company.com"}, 'expected': {'domain': "work"}},
    {'input': {'email': "example@school.edu"}, 'expected': {'domain': "education"}},
    {'input': {'email': "wrong"}, 'expected': {'domain': "unknown"}},
])
# Given the variable `data`, assign to the variable `data_type` the string "numeric" if `data` is of type int or float, "text" if it's of type str, "boolean" if it's of type bool, "other" otherwise
check_exercise_93 = input_output_checker([
    {'input': {'data': 1}, 'expected': {'data_type': "numeric"}},
    {'input': {'data': "text"}, 'expected': {'data_type': "text"}},
    {'input': {'data': True}, 'expected': {'data_type': "boolean"}},
    {'input': {'data': [1, 2, 3]}, 'expected': {'data_type': "other"}},
])
# Given a list `numbers` and a variable `target`, assign to the variable `position` the index of `target` in the list if it exists, -1 if it doesn't exist, and -2 if the list is empty
check_exercise_94 = input_output_checker([
    {'input': {'numbers': [1, 2, 3], 'target': 2}, 'expected': {'position': 1}},
    {'input': {'numbers': [1, 2, 3], 'target': 4}, 'expected': {'position': -1}},
    {'input': {'numbers': [], 'target': 4}, 'expected': {'position': -2}},
])
# Given the variable `password`, assign to the variable `is_strong` True if `password` is at least 8 characters long and contains both uppercase and lowercase letters, False otherwise
check_exercise_95 = input_output_checker([
    {'input': {'password': "Password"}, 'expected': {'is_strong': True}},
    {'input': {'password': "password"}, 'expected': {'is_strong': False}},
    {'input': {'password': "pass"}, 'expected': {'is_strong': False}},
    {'input': {'password': "PASSWORD"}, 'expected': {'is_strong': False}},
])
# Given the variables `x`, `y`, and `z`, assign to the variable `is_triangle` True if the sum of any two sides is greater than the third side for all three combinations, False otherwise
check_exercise_96 = input_output_checker([
    {'input': {'x': 3, 'y': 4, 'z': 5}, 'expected': {'is_triangle': True}},
    {'input': {'x': 1, 'y': 1, 'z': 3}, 'expected': {'is_triangle': False}},
    {'input': {'x': 1, 'y': 3, 'z': 3}, 'expected': {'is_triangle': True}},
])
# Given the variable `name`, assign to the variable `greeting` the string "Hello, {name}!" if `name` is not empty, "Hello, Guest!" otherwise, using a ternary operator
check_exercise_97 = input_output_checker([
    {'input': {'name': "Alice"}, 'expected': {'greeting': "Hello, Alice!"}},
    {'input': {'name': ""}, 'expected': {'greeting': "Hello, Guest!"}},
])
# Given a set `valid_colors` and a variable `chosen_color`, assign to the variable `is_valid_choice` True if `chosen_color` is in `valid_colors`, False otherwise
check_exercise_98 = input_output_checker([
    {'input': {'valid_colors': {"red", "green", "blue"}, 'chosen_color': "red"}, 'expected': {'is_valid_choice': True}},
    {'input': {'valid_colors': {"red", "green", "blue"}, 'chosen_color': "yellow"}, 'expected': {'is_valid_choice': False}},
])
# Given a list of strings called `words`, assign to the variable `has_long_word` True if any word in the list has more than 10 characters, False otherwise
check_exercise_99 = input_output_checker([
    {'input': {'words': ["short", "longlonglong"]}, 'expected': {'has_long_word': True}},
    {'input': {'words': ["short", "long"]}, 'expected': {'has_long_word': False}},
])
# Given a list of numbers called `measurements`, assign to the variable `within_tolerance` True if all numbers in the list are between 0 and 100 (inclusive), False otherwise
check_exercise_100 = input_output_checker([
    {'input': {'measurements': [1, 2, 3, 4, 5]}, 'expected': {'within_tolerance': True}},
    {'input': {'measurements': [1, 2, 3, 4, 101]}, 'expected': {'within_tolerance': False}},
    {'input': {'measurements': [1, 2, 3, 4, -1]}, 'expected': {'within_tolerance': False}},
    {'input': {'measurements': [1, 2, 3, 4, 100]}, 'expected': {'within_tolerance': True}},
])
# Given two time strings `time1` and `time2` in "HH:MM" format, assign to the variable `is_later` True if `time2` is later than `time1`, False otherwise
check_exercise_101 = input_output_checker([
    {'input': {'time1': "12:00", 'time2': "13:00"}, 'expected': {'is_later': True}},
    {'input': {'time1': "12:00", 'time2': "11:00"}, 'expected': {'is_later': False}},
    {'input': {'time1': "12:00", 'time2': "12:00"}, 'expected': {'is_later': False}},
])
# Given a dictionary `stock` and a variable `item`, assign to the variable `availability` "In stock" if `item` is a key in `stock` and its value is greater than 0, "Out of stock" otherwise
check_exercise_102 = input_output_checker([
    {'input': {'stock': {"apple": 5, "banana": 0}, 'item': "apple"}, 'expected': {'availability': "In stock"}},
    {'input': {'stock': {"apple": 5, "banana": 0}, 'item': "banana"}, 'expected': {'availability': "Out of stock"}},
    {'input': {'stock': {"apple": 5, "banana": 0}, 'item': "orange"}, 'expected': {'availability': "Out of stock"}},
])
# Given variables `hours`, `minutes`, and `seconds`, assign to the variable `time_format` the string in "HH:MM:SS" format if all are provided, "HH:MM" format if only hours and minutes are provided, "HH" format if only hours are provided
check_exercise_103 = input_output_checker([
    {'input': {'hours': 12, 'minutes': 30, 'seconds': 45}, 'expected': {'time_format': "12:30:45"}},
    {'input': {'hours': 12, 'minutes': 30, 'seconds': None}, 'expected': {'time_format': "12:30"}},
    {'input': {'hours': 12, 'minutes': None, 'seconds': None}, 'expected': {'time_format': "12"}},
])
# Given a variable `operation` and two variables `a` and `b`, assign to the variable `result` the sum if `operation` is "+", difference if "-", product if "*", quotient if "/", "Error" if "/" and `b` is 0, "Invalid operation" for any other operation
check_exercise_104 = input_output_checker([
    {'input': {'operation': "+", 'a': 2, 'b': 3}, 'expected': {'result': 5}},
    {'input': {'operation': "-", 'a': 5, 'b': 3}, 'expected': {'result': 2}},
    {'input': {'operation': "*", 'a': 2, 'b': 3}, 'expected': {'result': 6}},
    {'input': {'operation': "/", 'a': 6, 'b': 3}, 'expected': {'result': 2}},
    {'input': {'operation': "/", 'a': 6, 'b': 0}, 'expected': {'result': "Error"}},
    {'input': {'operation': "%", 'a': 6, 'b': 3}, 'expected': {'result': "Invalid operation"}},
])
# Given a filename `file`, assign to the variable `file_type` "Image" if the file ends with .jpg, .png, or .gif, "Document" if it ends with .doc, .docx, or .pdf, "Spreadsheet" if it ends with .xls or .xlsx, "Other" for any other extension
check_exercise_105 = input_output_checker([
    {'input': {'file': "image.jpg"}, 'expected': {'file_type': "Image"}},
    {'input': {'file': "document.doc"}, 'expected': {'file_type': "Document"}},
    {'input': {'file': "spreadsheet.xls"}, 'expected': {'file_type': "Spreadsheet"}},
    {'input': {'file': "file.txt"}, 'expected': {'file_type': "Other"}},
])
# Given variables `start_date`, `end_date`, and `check_date` all being a string in "HH:MM:SS" format, assign to the variable `is_within_range` True if `check_date` is between `start_date` and `end_date` (inclusive), False otherwise
check_exercise_106 = input_output_checker([
    {'input': {'start_date': "12:00:00", 'end_date': "13:00:00", 'check_date': "12:30:00"}, 'expected': {'is_within_range': True}},
    {'input': {'start_date': "12:00:00", 'end_date': "13:00:00", 'check_date': "13:30:00"}, 'expected': {'is_within_range': False}},
    {'input': {'start_date': "12:00:00", 'end_date': "13:00:00", 'check_date': "11:30:00"}, 'expected': {'is_within_range': False}},
])
# Given a variable `version` in the format "X.Y.Z", assign to the variable `is_compatible` True if X is 2, Y is greater than 5, and Z is any number, or if X is 3 and Y is less than 2, False otherwise
check_exercise_107 = input_output_checker([
    {'input': {'version': "2.6.1"}, 'expected': {'is_compatible': True}},
    {'input': {'version': "2.5.0"}, 'expected': {'is_compatible': False}},
    {'input': {'version': "3.9.0"}, 'expected': {'is_compatible': False}},
    {'input': {'version': "3.0.0"}, 'expected': {'is_compatible': True}},
])
# Given a list of numbers `values`, assign to the variable `processed` a new list where each number is doubled if it's even, or tripled if it's odd, using a ternary operator in a list comprehension
check_exercise_108 = input_output_checker([
    {'input': {'values': [1, 2, 3, 4]}, 'expected': {'processed': [3, 4, 9, 8]}},
    {'input': {'values': [1, 3, 5, 7]}, 'expected': {'processed': [3, 9, 15, 21]}},
])
# Given a variable `text` and a list of `keywords`, assign to the variable `is_relevant` True if any of the keywords are found in the text (case-insensitive), False otherwise
check_exercise_109 = input_output_checker([
    {'input': {'text': "Python is amazing!", 'keywords': ["python", "java", "c++"]}, 'expected': {'is_relevant': True}},
    {'input': {'text': "Python is amazing!", 'keywords': ["java", "c++"]}, 'expected': {'is_relevant': False}},
    {'input': {'text': "Python is amazing!", 'keywords': ["amazing", "great"]}, 'expected': {'is_relevant': True}},
])
# Given a list of `Employee` objects called `staff`, assign to the variable `has_manager` True if any employee has the title "Manager", False otherwise (assume each Employee object has a `title` attribute)
class Employee:
    def __init__(self, title):
        self.title = title
check_exercise_110 = input_output_checker([
    {'input': {'staff': [Employee("Developer"), Employee("Manager"), Employee("Designer")]}, 'expected': {'has_manager': True}},
    {'input': {'staff': [Employee("Developer"), Employee("Designer")]}, 'expected': {'has_manager': False}},
])
# Given a list of strings called `inputs`, assign to the variable `all_valid` True if all strings in the list are valid email addresses (use a simple check like contains "@" and "."), False otherwise
check_exercise_111 = input_output_checker([
    {'input': {'inputs': ["yolo@gmail.com", "check.com", "hey@com"]}, 'expected': {'all_valid': False}},
    {'input': {'inputs': ["check@gmail.com", "hey@com"]}, 'expected': {'all_valid': False}},
    {'input': {'inputs': ["ciao@gmail.com", "bella@gmail.com"]}, 'expected': {'all_valid': True}},
])
# Given two integers `a` and `b`, assign to the variable `has_common_bit` True if `a` and `b` have at least one common bit set to 1 in their binary representation, False otherwise
check_exercise_112 = input_output_checker([
    {'input': {'a': 5, 'b': 3}, 'expected': {'has_common_bit': True}},
    {'input': {'a': 3, 'b': 4}, 'expected': {'has_common_bit': False}},
    {'input': {'a': 5, 'b': 6}, 'expected': {'has_common_bit': True}},
])
# Given a variable `password`, assign to the variable `meets_policy` True if `password` contains at least one uppercase letter, one lowercase letter, one digit, and is at least 8 characters long, False otherwise
check_exercise_113 = input_output_checker([
    {'input': {'password': "Password123"}, 'expected': {'meets_policy': True}},
    {'input': {'password': "password"}, 'expected': {'meets_policy': False}},
    {'input': {'password': "PASSWORD"}, 'expected': {'meets_policy': False}},
    {'input': {'password': "Pass123"}, 'expected': {'meets_policy': False}},
])
# Given a variable `length` and a variable `unit` (either "m", "ft", or "yd"), assign to the variable `meters` the length converted to meters
check_exercise_114 = input_output_checker([
    {'input': {'length': 1, 'unit': "m"}, 'expected': {'meters': 1}},
    {'input': {'length': 1, 'unit': "ft"}, 'expected': {'meters': 0.3048}},
    {'input': {'length': 1, 'unit': "yd"}, 'expected': {'meters': 0.9144}},
])
# Given a variable `status_code`, assign to the variable `message` a descriptive string based on common HTTP status codes (200: "OK", 404: "Not Found", 500: "Server Error", etc.)
check_exercise_115 = input_output_checker([
    {'input': {'status_code': 200}, 'expected': {'message': "OK"}},
    {'input': {'status_code': 404}, 'expected': {'message': "Not Found"}},
    {'input': {'status_code': 500}, 'expected': {'message': "Server Error"}},
])
# Given variables `width` and `height`, assign to the variable `shape` the string "square" if width equals height, "landscape" if width is greater, "portrait" if height is greater
check_exercise_116 = input_output_checker([
    {'input': {'width': 1, 'height': 1}, 'expected': {'shape': "square"}},
    {'input': {'width': 1, 'height': 2}, 'expected': {'shape': "portrait"}},
    {'input': {'width': 2, 'height': 1}, 'expected': {'shape': "landscape"}},
])
# Given variables `username`, `email`, and `age`, assign to the variable `registration_status` "Accepted" if all are valid (non-empty username, valid email format (the mail contains the character `@` and `.`), age between 18 and 99), otherwise assign the string "Username is empty", "Invalid email format", or "Age is not between 18 and 99" as appropriate
check_exercise_117 = input_output_checker([
    {'input': {'username': "Alice", 'email': "alice@gmail.com", 'age': 25}, 'expected': {'registration_status': "Accepted"}},
    {'input': {'username': "", 'email': "alice@gmail.com", "age": 25}, 'expected': {'registration_status': "Username is empty"}},
    {'input': {'username': "Alice", 'email': "alicegmail.com", "age": 25}, 'expected': {'registration_status': "Invalid email format"}},
    {'input': {'username': "Alice", 'email': "alice@gmail.com", "age": 17}, 'expected': {'registration_status': "Age is not between 18 and 99"}},
])
# Given boolean variables `is_admin`, `is_staff`, and `is_active`, assign to the variable `can_access_dashboard` True if the user is an active admin or an active staff member, False otherwise
check_exercise_118 = input_output_checker([
    {'input': {'is_admin': True, 'is_staff': True, 'is_active': True}, 'expected': {'can_access_dashboard': True}},
    {'input': {'is_admin': False, 'is_staff': True, 'is_active': True}, 'expected': {'can_access_dashboard': True}},
    {'input': {'is_admin': True, 'is_staff': False, 'is_active': False}, 'expected': {'can_access_dashboard': False}},
])
# Given variables `is_weekday`, `is_business_hours`, and `is_holiday`, assign to the variable `is_open` True if it's a weekday during business hours and not a holiday, False otherwise
check_exercise_119 = input_output_checker([
    {'input': {'is_weekday': True, 'is_business_hours': True, 'is_holiday': False}, 'expected': {'is_open': True}},
    {'input': {'is_weekday': False, 'is_business_hours': True, 'is_holiday': False}, 'expected': {'is_open': False}},
    {'input': {'is_weekday': True, 'is_business_hours': False, 'is_holiday': False}, 'expected': {'is_open': False}},
    {'input': {'is_weekday': True, 'is_business_hours': True, 'is_holiday': True}, 'expected': {'is_open': False}},
])
# Given a variable `full_name`, assign to the variable `display_name` the first name if `full_name` contains a space, otherwise assign the full name, using a ternary operator
check_exercise_120 = input_output_checker([
    {'input': {'full_name': "Alice Smith"}, 'expected': {'display_name': "Alice"}},
    {'input': {'full_name': "Alice"}, 'expected': {'display_name': "Alice"}},
])
# # Given a variable `grade` (0-100), assign to the variable `letter_grade` "A" for 90-100, "B" for 80-89, "C" for 70-79, "D" for 60-69, "F" for 0-59
check_exercise_121 = input_output_checker([
    {'input': {'grade': 95}, 'expected': {'letter_grade': "A"}},
    {'input': {'grade': 85}, 'expected': {'letter_grade': "B"}},
    {'input': {'grade': 75}, 'expected': {'letter_grade': "C"}},
    {'input': {'grade': 65}, 'expected': {'letter_grade': "D"}},
    {'input': {'grade': 55}, 'expected': {'letter_grade': "F"}},
])
# Given a list of strings `phrases`, assign to the variable `contains_python` True if any phrase contains the word "python" (case-insensitive), False otherwise, using a generator expression
check_exercise_122 = input_output_checker([
    {'input': {'phrases': ["Python is amazing!", "Java is cool"]}, 'expected': {'contains_python': True}},
    {'input': {'phrases': ["Java is cool", "C++ is great"]}, 'expected': {'contains_python': False}},
])
# Given two sets `required_skills` and `candidate_skills`, assign to the variable `is_qualified` True if the candidate has all the required skills, False otherwise
check_exercise_123 = input_output_checker([
    {'input': {'required_skills': {"Python", "Java", "SQL"}, 'candidate_skills': {"Python", "Java", "SQL"}}, 'expected': {'is_qualified': True}},
    {'input': {'required_skills': {"Python", "Java", "SQL"}, 'candidate_skills': {"Python", "Java"}}, 'expected': {'is_qualified': False}},
])
# Given a variable `product_code`, assign to the variable `is_electronics` True if the product code starts with "EL", False otherwise
check_exercise_124 = input_output_checker([
    {'input': {'product_code': "EL123"}, 'expected': {'is_electronics': True}},
    {'input': {'product_code': "AB123"}, 'expected': {'is_electronics': False}},
])
# Given a dictionary `scores` with names as keys and numeric scores as values, assign to the variable `grades` a new dictionary where scores are replaced with letter grades (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59)
check_exercise_125 = input_output_checker([
    {'input': {'scores': {"Alice": 95, "Bob": 85, "Charlie": 75}}, 'expected': {'grades': {"Alice": "A", "Bob": "B", "Charlie": "C"}}},
    {'input': {'scores': {"Alice": 55, "Bob": 65, "Charlie": 75}}, 'expected': {'grades': {"Alice": "F", "Bob": "D", "Charlie": "C"}}},
])
# Given variables `hours`, `minutes`, and `seconds`, assign to the variable `time_of_day` "Morning" for 5:00-11:59, "Afternoon" for 12:00-16:59, "Evening" for 17:00-20:59, "Night" for 21:00-4:59
check_exercise_126 = input_output_checker([
    {'input': {'hours': 10, 'minutes': 30, 'seconds': 0}, 'expected': {'time_of_day': "Morning"}},
    {'input': {'hours': 15, 'minutes': 30, 'seconds': 0}, 'expected': {'time_of_day': "Afternoon"}},
    {'input': {'hours': 18, 'minutes': 30, 'seconds': 0}, 'expected': {'time_of_day': "Evening"}},
    {'input': {'hours': 23, 'minutes': 30, 'seconds': 0}, 'expected': {'time_of_day': "Night"}},
])
# Given a list `numbers`, assign to the variable `description` "Ascending" if the list is in ascending order, "Descending" if in descending order, "Unsorted" otherwise
check_exercise_127 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4, 5]}, 'expected': {'description': "Ascending"}},
    {'input': {'numbers': [5, 4, 3, 2, 1]}, 'expected': {'description': "Descending"}},
    {'input': {'numbers': [1, 3, 2, 5, 4]}, 'expected': {'description': "Unsorted"}},
])
# Given variables `username` and `domain`, assign to the variable `valid_email` True if `username` contains only letters, numbers, dots, or underscores and `domain` ends with ".com", ".org", or ".edu", False otherwise
check_exercise_128 = input_output_checker([
    {'input': {'username': "alice_123", 'domain': "gmail.com"}, 'expected': {'valid_email': True}},
    {'input': {'username': "alice-123", 'domain': "gmail.com"}, 'expected': {'valid_email': False}},
    {'input': {'username': "alice_123", 'domain': "gmail.org"}, 'expected': {'valid_email': True}},
    {'input': {'username': "alice_123", 'domain': "gmail"}, 'expected': {'valid_email': False}},
    {'input': {'username': "alice_123", 'domain': "gmail.edu"}, 'expected': {'valid_email': True}},
    {'input': {'username': "alice_123", 'domain': "gmail.net"}, 'expected': {'valid_email': False}},
])
# Given variables `sales_target`, `actual_sales`, `customer_satisfaction`, assign to the variable `bonus_percentage` 20% if sales target was met and satisfaction is above 4.5, 10% if either condition is true, 0% otherwise
check_exercise_129 = input_output_checker([
    {'input': {'sales_target': 1000, 'actual_sales': 1000, 'customer_satisfaction': 5}, 'expected': {'bonus_percentage': 20}},
    {'input': {'sales_target': 1000, 'actual_sales': 1000, 'customer_satisfaction': 4}, 'expected': {'bonus_percentage': 10}},
    {'input': {'sales_target': 1000, 'actual_sales': 900, 'customer_satisfaction': 5}, 'expected': {'bonus_percentage': 10}},
    {'input': {'sales_target': 1000, 'actual_sales': 900, 'customer_satisfaction': 4}, 'expected': {'bonus_percentage': 0}},
])
# Given a dictionary `stock` and a variable `item`, assign to the variable `item_price` the price of the item if it exists in the stock, "Not available" otherwise, using a ternary operator and the dictionary's get method
check_exercise_130 = input_output_checker([
    {'input': {'stock': {"apple": 1, "banana": 2}, 'item': "apple"}, 'expected': {'item_price': 1}},
    {'input': {'stock': {"apple": 1, "banana": 2}, 'item': "orange"}, 'expected': {'item_price': "Not available"}},
])
# Given a list of version strings `versions` in "X.Y.Z" format, assign to the variable `all_stable` True if all versions have X greater than or equal to 1, False otherwise
check_exercise_131 = input_output_checker([
    {'input': {'versions': ["1.0.0", "1.2.3", "2.0.0"]}, 'expected': {'all_stable': True}},
    {'input': {'versions': ["0.1.0", "1.2.3", "2.0.0"]}, 'expected': {'all_stable': False}},
])
# Given a list of numbers `values`, assign to the variable `signs` a new list where each number is replaced with "positive", "negative", or "zero"
check_exercise_132 = input_output_checker([
    {'input': {'values': [1, -2, 0]}, 'expected': {'signs': ["positive", "negative", "zero"]}},
    {'input': {'values': [-1, 2, -3]}, 'expected': {'signs': ["negative", "positive", "negative"]}},
])
# Given a variable `sentence`, assign to the variable `sentence_type` "Question" if it ends with "?", "Exclamation" if it ends with "!", "Statement" otherwise
check_exercise_133 = input_output_checker([
    {'input': {'sentence': "How are you?"}, 'expected': {'sentence_type': "Question"}},
    {'input': {'sentence': "I'm great!"}, 'expected': {'sentence_type': "Exclamation"}},
    {'input': {'sentence': "Hello"}, 'expected': {'sentence_type': "Statement"}},
])
# Given a date string `date_str` in "YYYY-MM-DD" format, assign to the variable `season` "Winter", "Spring", "Summer", or "Fall" based on the month
check_exercise_134 = input_output_checker([
    {'input': {'date_str': "2022-01-01"}, 'expected': {'season': "Winter"}},
    {'input': {'date_str': "2022-04-01"}, 'expected': {'season': "Spring"}},
    {'input': {'date_str': "2022-07-01"}, 'expected': {'season': "Summer"}},
    {'input': {'date_str': "2022-10-01"}, 'expected': {'season': "Fall"}},
])
# Given three sets `A`, `B`, and `C`, assign to the variable `set_relation` "Subset" if A is a subset of B else "Superset" if C is a superset of B else "Equal" if A equals C else "Disjoint" if A and C are disjoint
check_exercise_135 = input_output_checker([
    {'input': {'A': {1, 2}, 'B': {1, 2, 3}, 'C': {2, 3}}, 'expected': {'set_relation': "Subset"}},
    {'input': {'A': {1, 2}, 'B': {1, 2, 3}, 'C': {1, 2, 3}}, 'expected': {'set_relation': "Subset"}},
    {'input': {'A': {1, 2}, 'B': {1, 2, 3}, 'C': {4, 5}}, 'expected': {'set_relation': "Subset"}},
    {'input': {'A': {1, 2}, 'B': {1, 2, 3}, 'C': {2, 3, 4}}, 'expected': {'set_relation': "Subset"}},
    {'input': {'A': {1, 12}, 'B': {1, 2, 3}, 'C': {1, 2, 3, 4, 5}}, 'expected': {'set_relation': "Superset"}},
    {'input': {'A': {1, 12}, 'B': {1, 123}, 'C': {1, 12}}, 'expected': {'set_relation': "Equal"}},
    {'input': {'A': {1, 12}, 'B': {5, 6}, 'C': {3, 4}}, 'expected': {'set_relation': "Disjoint"}},
])
# Given a list of numbers `numbers`, create a new list `squared` containing the square of each number
check_exercise_136 = input_output_checker([
    {'input': {'numbers': [1, 2, 3]}, 'expected': {'squared': [1, 4, 9]}},
    {'input': {'numbers': [2, 3, 4]}, 'expected': {'squared': [4, 9, 16]}},
])
# Given a number `n`, calculate its factorial using a while loop
check_exercise_137 = input_output_checker([
    {'input': {'n': 5}, 'expected': {'factorial': 120}},
    {'input': {'n': 0}, 'expected': {'factorial': 1}},
])
# Given a number `n`, assign to the variable `output` a string with `n` lines, each containing `i` asterisks, where `i` ranges from 1 to `n` in the format "*\n**\n***\n"
check_exercise_138 = input_output_checker([
    {'input': {'n': 3}, 'expected': {'output': "*\n**\n***\n"}},
    {'input': {'n': 5}, 'expected': {'output': "*\n**\n***\n****\n*****\n"}},
])
# Given a list of strings `words`, create a new list `indexed_words` where each element is a tuple of (index, word)
check_exercise_139 = input_output_checker([
    {'input': {'words': ["apple", "banana", "cherry"]}, 'expected': {'indexed_words': [(0, "apple"), (1, "banana"), (2, "cherry")]}},
    {'input': {'words': ["one", "two", "three"]}, 'expected': {'indexed_words': [(0, "one"), (1, "two"), (2, "three")]}},
])
# Given two lists `names` and `ages`, create a dictionary `person_info` where names are keys and ages are values
check_exercise_140 = input_output_checker([
    {'input': {'names': ["Alice", "Bob"], 'ages': [25, 30]}, 'expected': {'person_info': {"Alice": 25, "Bob": 30}}},
    {'input': {'names': ["Charlie", "David"], 'ages': [35, 40]}, 'expected': {'person_info': {"Charlie": 35, "David": 40}}},
])
# Given a list of numbers `numbers`, create a new list `doubled` containing only the even numbers multiplied by 2
check_exercise_141 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'doubled': [4, 8]}},
    {'input': {'numbers': [2, 3, 4, 5]}, 'expected': {'doubled': [4, 8]}},
])
# Given a list of strings `words`, create a new list `long_words` containing all the words with more than 5 characters from the original list except for "python"
check_exercise_142 = input_output_checker([
    {'input': {'words': ["python", "java", "c++", "javascript"]}, 'expected': {'long_words': ["javascript"]}},
    {'input': {'words': ["python", "java", "c++", "ruby"]}, 'expected': {'long_words': []}},
])
# Given a list of numbers `numbers`, assign to the variable `string_of_numbers` a string containing all the numbers greater than 100, separated by commas, or "Not found" if none are found
check_exercise_143 = input_output_checker([
    {'input': {'numbers': [50, 150, 200, 250]}, 'expected': {'string_of_numbers': "150,200,250"}},
    {'input': {'numbers': [50, 60, 70, 80]}, 'expected': {'string_of_numbers': "Not found"}},
])
# Given a list of numbers `numbers`, create a new list `positive_numbers` containing only the positive numbers
check_exercise_144 = input_output_checker([
    {'input': {'numbers': [-1, 2, -3, 4]}, 'expected': {'positive_numbers': [2, 4]}},
    {'input': {'numbers': [-1, -2, -3, -4]}, 'expected': {'positive_numbers': []}},
])
# Assign all multiples of 5 from 5 to 50 (inclusive) using a for loop and range() to the variable `multiples_of_five`
check_exercise_145 = input_output_checker([
    {'input': {}, 'expected': {'multiples_of_five': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]}},
])
# Given a list of numbers `numbers`, assign to the variable `sum_of_even` the sum of all even numbers in the list found till the first negative number
check_exercise_146 = input_output_checker([
    {'input': {'numbers': [2, 4, 6, -3, 8, 10]}, 'expected': {'sum_of_even': 12}},
    {'input': {'numbers': [2, 4, 6, 8, 10]}, 'expected': {'sum_of_even': 30}},
])
# Given a 2D list `matrix`, calculate and assign the sum of each row to a new list `row_sums`
check_exercise_147 = input_output_checker([
    {'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, 'expected': {'row_sums': [6, 15, 24]}},
    {'input': {'matrix': [[1, 2], [3, 4], [5, 6]]}, 'expected': {'row_sums': [3, 7, 11]}},
])
# Given three lists `names`, `ages`, and `cities`, create a list of dictionaries `people` where each dictionary contains the name, age, and city of a person
check_exercise_148 = input_output_checker([
    {'input': {'names': ["Alice", "Bob"], 'ages': [25, 30], 'cities': ["New York", "Los Angeles"]}, 'expected': {'people': [{"name": "Alice", "age": 25, "city": "New York"}, {"name": "Bob", "age": 30, "city": "Los Angeles"}]}},
    {'input': {'names': ["Charlie", "David"], 'ages': [35, 40], 'cities': ["Chicago", "Houston"]}, 'expected': {'people': [{"name": "Charlie", "age": 35, "city": "Chicago"}, {"name": "David", "age": 40, "city": "Houston"}]}},
])
# Create 2D list of a 5x5 multiplication table named `multiplication_table`, but skip the multiplication step when either number is 3 and assign 0 instead
check_exercise_149 = input_output_checker([
    {'input': {}, 'expected': {'multiplication_table': [[1, 2, 0, 4, 5], [2, 4, 0, 8, 10], [0, 0, 0, 0, 0], [4, 8, 0, 16, 20], [5, 10, 0, 20, 25]]}},
])
# Given a 2D list `matrix`, find and assign the first negative number to the variable `value`, or 0 if no negative number is found
check_exercise_150 = input_output_checker([
    {'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, -9]]}, 'expected': {'value': -9}},
    {'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, 'expected': {'value': 0}},
])
# Given a dictionary `inventory` with item names as keys and quantities as values, create a new dictionary `low_stock` containing only items with quantities less than 10
check_exercise_151 = input_output_checker([
    {'input': {'inventory': {"apple": 5, "banana": 15, "cherry": 3}}, 'expected': {'low_stock': {"apple": 5, "cherry": 3}}},
    {'input': {'inventory': {"apple": 10, "banana": 15, "cherry": 20}}, 'expected': {'low_stock': {}}},
])
# Given a list of numbers `numbers`, replace each number with the sum of itself and the next number (the last number should remain unchanged)
check_exercise_152 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'numbers': [3, 5, 7, 4]}},
    {'input': {'numbers': [2, 4, 6, 8]}, 'expected': {'numbers': [6, 10, 14, 8]}},
])
# Given a number `n`, assign all prime numbers less than n to the list `primes`
check_exercise_153 = input_output_checker([
    {'input': {'n': 10}, 'expected': {'primes': [2, 3, 5, 7]}},
    {'input': {'n': 20}, 'expected': {'primes': [2, 3, 5, 7, 11, 13, 17, 19]}},
])
# Given a positive integer `n`, assign its binary representation as a string to the variable `binary`
check_exercise_154 = input_output_checker([
    {'input': {'n': 5}, 'expected': {'binary': "101"}},
    {'input': {'n': 10}, 'expected': {'binary': "1010"}},
])
# Given a string `text`, create a new string named `processed` where every second character is replaced with '_'
check_exercise_155 = input_output_checker([
    {'input': {'text': "hello"}, 'expected': {'processed': "h_l_o"}},
    {'input': {'text': "world"}, 'expected': {'processed': "w_r_d"}},
])
# Given two lists of numbers `list1` and `list2`, create a new list containing the larger number for each index between the two lists
check_exercise_156 = input_output_checker([
    {'input': {'list1': [1, 2, 3], 'list2': [4, 5, 6]}, 'expected': {'larger_numbers': [4, 5, 6]}},
    {'input': {'list1': [1, 2, 3], 'list2': [4, 3, 2]}, 'expected': {'larger_numbers': [4, 3, 3]}},
])
# Given a 3D list `matrix`, assign to the variable `flattened` a new list containing all the elements of the matrix in a single dimension
check_exercise_157 = input_output_checker([
    {'input': {'matrix': [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]}, 'expected': {'flattened': [1, 2, 3, 4, 5, 6, 7, 8]}},
    {'input': {'matrix': [[[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]]}, 'expected': {'flattened': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}},
])
# Given a 3D list `matrix` and `target`, assign to the tuple `indexes` the indices of the target element in the matrix, or (-1, -1, -1) if not found
check_exercise_158 = input_output_checker([
    {'input': {'matrix': [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 'target': 6}, 'expected': {'indexes': (1, 0, 1)}},
    {'input': {'matrix': [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 'target': 9}, 'expected': {'indexes': (-1, -1, -1)}},
])
# Given a dictionary `school` where keys are subject names and values are dictionaries with keys are student names and values are grades, assign to the variable `average_grades` a new dictionary with subject names as keys and average grades on the subject as values
check_exercise_159 = input_output_checker([
    {'input': {'school': {"Math": {"Alice": 90, "Bob": 80}, "Science": {"Alice": 85, "Bob": 95}}}, 'expected': {'average_grades': {"Math": 85, "Science": 90}}},
    {'input': {'school': {"Math": {"Alice": 90, "Bob": 80}, "Science": {"Alice": 85, "Bob": 75}}}, 'expected': {'average_grades': {"Math": 85, "Science": 80}}},
])
# Given a list of numbers `numbers`, create a new list where each element is the sum of the current and the next two elements in the original list (the last two elements should use 0 for missing values)
check_exercise_160 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4, 5]}, 'expected': {'sums': [6, 9, 12, 9, 5]}},
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'sums': [6, 9, 7, 4]}},
])
# Given two lists `x_coords` and `y_coords` and `accepted_coordinates`, assign all possible coordinate pairs (x, y) to the list `coordinates` where x is from `x_coords`, y is from `y_coords`, and the pair is in `accepted_coordinates`
check_exercise_161 = input_output_checker([
    {'input': {'x_coords': [1, 2, 3], 'y_coords': [4, 5, 6], 'accepted_coordinates': [(1, 4), (2, 5), (3, 6)]}, 'expected': {'coordinates': [(1, 4), (2, 5), (3, 6)]}},
    {'input': {'x_coords': [1, 2, 3], 'y_coords': [4, 5, 6], 'accepted_coordinates': [(1, 4), (3, 6)]}, 'expected': {'coordinates': [(1, 4), (3, 6)]}},
])
# Given a list `items` and a number `k`, create a new list named `rotated` where the elements are rotated k positions to the right
check_exercise_162 = input_output_checker([
    {'input': {'items': [1, 2, 3, 4, 5], 'k': 2}, 'expected': {'rotated': [4, 5, 1, 2, 3]}},
    {'input': {'items': [1, 2, 3, 4, 5], 'k': 3}, 'expected': {'rotated': [3, 4, 5, 1, 2]}},
])
# Given three lists `keys`, `values`, and `defaults`, create a dictionary where keys are from `keys`, values are from `values` if available, otherwise from `defaults`
check_exercise_163 = input_output_checker([
    {'input': {'keys': ["a", "b", "c"], 'values': [1, 2], 'defaults': [0]}, 'expected': {'merged': {"a": 1, "b": 2, "c": 0}}},
    {'input': {'keys': ["a", "b", "c"], 'values': [1], 'defaults': [0, 2]}, 'expected': {'merged': {"a": 1, "b": 0, "c": 2}}},
])
# Given a list of strings `data`, create a new list named `lowercase` with all strings converted to lowercase, skipping any string that's shorter than 3 characters
check_exercise_164 = input_output_checker([
    {'input': {'data': ["Python", "Java", "C++", "JS"]}, 'expected': {'lowercase': ["python", "java"]}},
    {'input': {'data': ["Python", "Java", "C++", "JS", "Go"]}, 'expected': {'lowercase': ["python", "java"]}},
])
# Given a list of numbers `numbers`, find and assign the first pair of numbers that sum to 100 to the variables `num1` and `num2`, or 0 if no such pair exists
check_exercise_165 = input_output_checker([
    {'input': {'numbers': [10, 20, 30, 40, 50, 60, 70, 80, 90]}, 'expected': {'num1': 40, 'num2': 60}},
    {'input': {'numbers': [1, 2, 3, 4, 5, 6, 7]}, 'expected': {'num1': 0, 'num2': 0}},
])
# Given the value `n`, assign all numbers that are not multiples of 3 or 17 to the list `others` until the list reaches `n` elements
check_exercise_166 = input_output_checker([
    {'input': {'n': 5}, 'expected': {'others': [1, 2, 4, 5, 7]}},
    {'input': {'n': 10}, 'expected': {'others': [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]}},
])
# Given a number `n`, assign its prime factors in ascending order to the list `factors` if any, or assign an empty list if it's a prime number
check_exercise_167 = input_output_checker([
    {'input': {'n': 12}, 'expected': {'factors': [2, 3]}},
    {'input': {'n': 13}, 'expected': {'factors': []}},
])
# Given a list of numbers `numbers`, calculate the sum of all positive numbers and the product of all negative numbers and assign them to the variables `sum_pos` and `prod_neg`
check_exercise_168 = input_output_checker([
    {'input': {'numbers': [1, -2, 3, -4, 5]}, 'expected': {'sum_pos': 9, 'prod_neg': 8}},
    {'input': {'numbers': [-1, -2, -3, -4, -5]}, 'expected': {'sum_pos': 0, 'prod_neg': -120}},
])
# Given a string `binary_number`, convert it to a deciaml integer and assign it to the variable `decimal_number`
check_exercise_169 = input_output_checker([
    {'input': {'binary_number': "1010"}, 'expected': {'decimal_number': 10}},
    {'input': {'binary_number': "1111"}, 'expected': {'decimal_number': 15}},
])
# Given a 2D list `matrix`, assign to the variable `diagonal` a new list containing the diagonal elements of the matrix
check_exercise_170 = input_output_checker([
    {'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, 'expected': {'diagonal': [1, 5, 9]}},
    {'input': {'matrix': [[1, 2], [3, 4]]}, 'expected': {'diagonal': [1, 4]}},
])
# Given a 2D list `matrix`, assign to the variable `transpose` a new list containing the transpose of the matrix
check_exercise_171 = input_output_checker([
    {'input': {'matrix': [[1, 2, 3], [4, 5, 6]]}, 'expected': {'transpose': [[1, 4], [2, 5], [3, 6]]}},
    {'input': {'matrix': [[1, 2], [3, 4], [5, 6]]}, 'expected': {'transpose': [[1, 3, 5], [2, 4, 6]]}},
])
# Given a string `text`, count the number of words (assuming words are separated by spaces), ignoring any "stop words" ("the", "a", "an") and assign the count to the variable `word_count`
check_exercise_172 = input_output_checker([
    {'input': {'text': "the quick brown fox"}, 'expected': {'word_count': 3}},
    {'input': {'text': "the quick brown fox jumps over the lazy dog"}, 'expected': {'word_count': 7}},
])
# Given a list of strings `words` and a target string `target`, assign the index of the first occurrence of the target in the list, or -1 if it's not found
check_exercise_173 = input_output_checker([
    {'input': {'words': ["apple", "banana", "cherry"], 'target': "banana"}, 'expected': {'index': 1}},
    {'input': {'words': ["apple", "banana", "cherry"], 'target': "orange"}, 'expected': {'index': -1}},
])
# Given a dictionary `prices` with item names as keys and prices as values, increase all prices by 10% and round to 2 decimal places
check_exercise_174 = input_output_checker([
    {'input': {'prices': {"apple": 1.99, "banana": 0.99, "cherry": 2.99}}, 'expected': {'updated_prices': {"apple": 2.19, "banana": 1.09, "cherry": 3.29}}},
    {'input': {'prices': {"apple": 1.00, "banana": 2.00, "cherry": 3.00}}, 'expected': {'updated_prices': {"apple": 1.10, "banana": 2.20, "cherry": 3.30}}},
])
# Given a list of numbers `numbers`, create a new list `numeros` where each element is the absolute difference between the current and the next number in the list
check_exercise_175 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'numeros': [1, 1, 1]}},
    {'input': {'numbers': [2, 4, 6, 8]}, 'expected': {'numeros': [2, 2, 2]}},
])
# Given the variable `n`, assign to the list `triangle` the first n triangular numbers (1, 3, 6, 10, 15, ...)
check_exercise_176 = input_output_checker([
    {'input': {'n': 5}, 'expected': {'triangle': [1, 3, 6, 10, 15]}},
    {'input': {'n': 3}, 'expected': {'triangle': [1, 3, 6]}},
])
# Given a list of numbers `numbers`, create a new list where each element is the running average of all previous elements (including itself)
check_exercise_177 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'averages': [1, 1.5, 2, 2.5]}},
    {'input': {'numbers': [2, 4, 6, 8]}, 'expected': {'averages': [2, 3, 4, 5]}},
])
# Given a list of passwords `passwords`, assign only the "strong" passwords (at least 8 characters, containing uppercase, lowercase, digit, and special character) to the list `strong_passwords`
check_exercise_178 = input_output_checker([
    {'input': {'passwords': ["Password1!", "password1!", "password1", "Password1"]}, 'expected': {'strong_passwords': ["Password1!"]}},
    {'input': {'passwords': ["Password1!", "password1!", "password1", "Password1#", "Password1"]}, 'expected': {'strong_passwords': ["Password1!", "Password1#"]}},
])
# Given a dictionary `switcher`, create a new dictionary `inverted` where keys and values are swapped
check_exercise_179 = input_output_checker([
    {'input': {'switcher': {"on": "off", "off": "on"}}, 'expected': {'inverted': {"off": "on", "on": "off"}}},
    {'input': {'switcher': {"yes": "no", "no": "yes"}}, 'expected': {'inverted': {"no": "yes", "yes": "no"}}},
])
# Given a list of numbers `numbers` and a window size `k`, compute and assign the moving averages of the numbers in the list with the given window size to the list `averages`
check_exercise_180 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4, 5], 'k': 3}, 'expected': {'averages': [2, 3, 4]}},
    {'input': {'numbers': [2, 4, 6, 8, 10], 'k': 2}, 'expected': {'averages': [3, 5, 7, 9]}},
    {'input': {'numbers': [1, 2, 3, 4, 5], 'k': 1}, 'expected': {'averages': [1, 2, 3, 4, 5]}},
])
# Given the variable `n` generate the first n terms of the sequence defined by a(n) = a(n-1) + a(n-2) + a(n-3), with a(0) = a(1) = a(2) = 1
check_exercise_181 = input_output_checker([
    {'input': {'n': 5}, 'expected': {'sequence': [1, 1, 1, 3, 5]}},
    {'input': {'n': 7}, 'expected': {'sequence': [1, 1, 1, 3, 5, 9, 17]}},
])
# Given a list of numbers `numbers`, find and assign the indices of the peak elements (elements greater than both neighbors) to the list `peak_elements`
check_exercise_182 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 2, 1]}, 'expected': {'peak_elements': [2]}},
    {'input': {'numbers': [1, 2, 3, 2, 4, 2]}, 'expected': {'peak_elements': [2, 4]}},
])
# Given a dictionary `sales` where keys are product names and values are lists of daily sales, create a new dictionary with total sales for each product
check_exercise_183 = input_output_checker([
    {'input': {'sales': {"apple": [1, 2, 3], "banana": [4, 5, 6]}}, 'expected': {'total_sales': {"apple": 6, "banana": 15}}},
    {'input': {'sales': {"apple": [1, 2, 3], "banana": [4, 5, 6], "cherry": [7, 8, 9]}}, 'expected': {'total_sales': {"apple": 6, "banana": 15, "cherry": 24}}},
])
# Given a list of strings `words`, sort the list based on the number of distinct characters in each word (in descending order)
check_exercise_184 = input_output_checker([
    {'input': {'words': ["apple", "banana", "cherry"]}, 'expected': {'words': ["cherry", "apple", "banana"]}},
    {'input': {'words': ["apple", "banana", "cherry", "date"]}, 'expected': {'words': ["cherry", "apple", "date", "banana"]}},
])
# Given a list of numbers `numbers`, assign to the variable `max_diff` the maximum difference between any two elements in the list
check_exercise_185 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4]}, 'expected': {'max_diff': 3}},
    {'input': {'numbers': [2, 4, 6, 8]}, 'expected': {'max_diff': 6}},
])
# Given the string variables `number`, try to convert it to an integer and assign it to the variable `integer`, or assign -1 if it's not possible
check_exercise_186 = input_output_checker([
    {'input': {'number': "123"}, 'expected': {'integer': 123}},
    {'input': {'number': "abc"}, 'expected': {'integer': -1}},
])
# Given the variables `n` and `m`, assign to the variable `division_value` the result of dividing n by m, or -1 if the variables are not numeric or the division is not possible
check_exercise_187 = input_output_checker([
    {'input': {'n': 10, 'm': 2}, 'expected': {'division_value': 5}},
    {'input': {'n': "abc", 'm': 2}, 'expected': {'division_value': -1}},
    {'input': {'n': 10, 'm': 0}, 'expected': {'division_value': -1}},
])
# Given a frozen set `fset`, try to add the number 5 to it and assign the result to the variable `updated_fset`, or assign an empty set if it's not possible
check_exercise_188 = input_output_checker([
    {'input': {'fset': frozenset({1, 2, 3, 4})}, 'expected': {'updated_fset': frozenset({1, 2, 3, 4, 5})}},
    {'input': {'fset': frozenset({1, 2, 3, 4})}, 'expected': {'updated_fset': frozenset({1, 2, 3, 4, 5})}},
])
# Given a variable `x` use a try/except block to assign "positive" to the variable `number_status` if `x` is positive and "negative" if `x` is negative, handling the `AssertionError` with the message "another error".
check_exercise_189 = input_output_checker([
    {'input': {'x': 5}, 'expected': {'number_status': "positive"}},
    {'input': {'x': -5}, 'expected': {'number_status': "negative"}},
])
# Given a list of numbers `numbers`, assign to the variable `sum_of_squares` the sum of the squares of all numbers, handling any `TypeError` with the message "invalid type" and any other exception with the message "unknown error", and always assigning -1 to the variable `finalized`
check_exercise_190 = input_output_checker([
    {'input': {'numbers': [1, 2, 3]}, 'expected': {'sum_of_squares': 14, 'finalized': -1}},
    {'input': {'numbers': [1, 2, "3"]}, 'expected': {'sum_of_squares': "invalid type", 'finalized': -1}},
])
# Create a function named `multiply` that takes two numbers as parameters and returns their product.
check_exercise_191 = functions_input_output_checker(
    {
        'multiply': [
            {'input': {'a': 2, 'b': 3}, 'expected': 6},
            {'input': {'a': 5, 'b': 5}, 'expected': 25},
        ],
    },
)
# Create a function named `is_even` that takes a number `n` as a parameter and returns True if the number is even, otherwise returns False.
check_exercise_192 = functions_input_output_checker(
    {
        'is_even': [
            {'input': {'n': 2}, 'expected': True},
            {'input': {'n': 3}, 'expected': False},
        ],
    },
)
# Create a function called `find_max` that takes three numbers as parameters and returns the largest of them.
check_exercise_193 = functions_input_output_checker(
    {
        'find_max': [
            {'input': {'a': 1, 'b': 2, 'c': 3}, 'expected': 3},
            {'input': {'a': 3, 'b': 2, 'c': 1}, 'expected': 3},
        ],
    },
)
# Create a function named `reverse_string` that takes a string `text` as a parameter and returns the reversed version of that string.
check_exercise_194 = functions_input_output_checker(
    {
        'reverse_string': [
            {'input': {'text': "hello"}, 'expected': "olleh"},
            {'input': {'text': "world"}, 'expected': "dlrow"},
        ],
    },
)
# Create a function named `factorial` that takes a number as a parameter and returns its factorial.
check_exercise_195 = functions_input_output_checker(
    {
        'factorial': [
            {'input': {'n': 5}, 'expected': 120},
            {'input': {'n': 3}, 'expected': 6},
        ],
    },
)
# Create a function called `count_vowels` that takes a string `text` as a parameter and returns the number of vowels in the string.
check_exercise_196 = functions_input_output_checker(
    {
        'count_vowels': [
            {'input': {'text': "hello"}, 'expected': 2},
            {'input': {'text': "world"}, 'expected': 1},
        ],
    },
)
# Create a function called `area_of_circle` that takes the radius as a parameter and returns the area of the circle.
check_exercise_197 = functions_input_output_checker(
    {
        'area_of_circle': [
            {'input': {'radius': 5}, 'expected': math.pi * 5 ** 2},
            {'input': {'radius': 10}, 'expected': math.pi * 10 ** 2},
        ],
    },
)
# Create a function named `fibonacci` that takes a number `n` and returns the first `n` Fibonacci numbers in a list, where the first two numbers are 0 and 1.
check_exercise_198 = functions_input_output_checker(
    {
        'fibonacci': [
            {'input': {'n': 5}, 'expected': [0, 1, 1, 2, 3]},
            {'input': {'n': 7}, 'expected': [0, 1, 1, 2, 3, 5, 8]},
        ],
    },
)
# Create a function named `is_prime` that takes a number and returns True if it is a prime number, otherwise False.
check_exercise_199 = functions_input_output_checker(
    {
        'is_prime': [
            {'input': {'n': 7}, 'expected': True},
            {'input': {'n': 8}, 'expected': False},
        ],
    },
)
# Create a function `product` that takes two numbers and an optional parameter for a message, returning the message along with the product of the two numbers: "[message]: [product]".
check_exercise_200 = functions_input_output_checker(
    {
        'product': [
            {'input': {'a': 2, 'b': 3, 'message': "The product is"}, 'expected': "The product is: 6"},
            {'input': {'a': 5, 'b': 5, 'message': "Result"}, 'expected': "Result: 25"},
        ],
    },
)
# Create a function `favorite_foods` that takes a list of `foods` and returns "favorite foods are [food1], [food2], ..." where the foods are joined by commas.
check_exercise_201 = functions_input_output_checker(
    {
        'favorite_foods': [
            {'input': {'foods': ["apple", "banana", "cherry"]}, 'expected': "favorite foods are apple, banana, cherry"},
            {'input': {'foods': ["pizza", "pasta", "burger"]}, 'expected': "favorite foods are pizza, pasta, burger"},
        ],
    },
)
# create a function `full_name` that takes a first name and last name as keyword arguments and returns the full name as a string, with a space between the names.
check_exercise_202 = functions_input_output_checker(
    {
        'full_name': [
            {'input': {'first_name': "Alice", 'last_name': "Smith"}, 'expected': "Alice Smith"},
            {'input': {'first_name': "Bob", 'last_name': "Johnson"}, 'expected': "Bob Johnson"},
        ],
    },
)
# Create a function `send_email` that takes a recipient address and an optional subject (default to "No Subject") and returns a formatted email string, like "To: [recipient], Subject: [subject]".
check_exercise_203 = functions_input_output_checker(
    {
        'send_email': [
            {'input': {'recipient': "address"}, 'expected': "To: address, Subject: No Subject"},
            {'input': {'recipient': "address", 'subject': "Hello"}, 'expected': "To: address, Subject: Hello"},
        ],
    },
)
# create a function `calculate_discount` that takes a price and an optional discount rate (default to 0), returning the final price after applying the discount.
check_exercise_204 = functions_input_output_checker(
    {
        'calculate_discount': [
            {'input': {'price': 100, 'discount_rate': 0.1}, 'expected': 90},
            {'input': {'price': 200}, 'expected': 200},
        ],
    },
)
# Create a function `create_user` that takes a username and optional parameters for age and location, returning a user profile string, like "Username: [username], Age: [age], Location: [location]" assigning "None" to missing values.
check_exercise_205 = functions_input_output_checker(
    {
        'create_user': [
            {'input': {'username': "Alice", 'age': 25, 'location': "New York"}, 'expected': "Username: Alice, Age: 25, Location: New York"},
            {'input': {'username': "Bob", 'age': 30}, 'expected': "Username: Bob, Age: 30, Location: None"},
        ],
    },
)
# Create a function `increment` that takes a number and an optional step value (default to 1), returning the incremented value.
check_exercise_206 = functions_input_output_checker(
    {
        'increment': [
            {'input': {'number': 5, 'step': 2}, 'expected': 7},
            {'input': {'number': 10}, 'expected': 11},
        ],
    },
)
# Create a function `concatenate_strings` that accepts any number of string arguments and returns a single concatenated string.
check_exercise_207 = functions_input_output_checker(
    {
        'concatenate_strings': [
            {'input': {'*args': ["hello", "world"]}, 'expected': "helloworld"},
            {'input': {'*args': ["Python", "is", "fun"]}, 'expected': "Pythonisfun"},
        ],
    },
)
# Create a function `print_scores` that accepts any number of scores and returns a formatted string with all the scores, like "Scores: [score1], [score2], [score3].".
check_exercise_208 = functions_input_output_checker(
    {
        'print_scores': [
            {'input': {'*args': [90, 85, 95]}, 'expected': "Scores: 90, 85, 95."},
            {'input': {'*args': [100, 95]}, 'expected': "Scores: 100, 95."},
        ],
    },
)
# Create a function called `merge_dicts` that accepts multiple dictionaries as keyword arguments and returns a single merged dictionary.
check_exercise_209 = functions_input_output_checker(
    {
        'merge_dicts': [
            {'input': {'dict1': {"a": 1}, 'dict2': {"b": 2}}, 'expected': {"a": 1, "b": 2}},
            {'input': {'dict1': {"a": 1}, 'dict2': {"b": 2}, 'dict3': {"c": 3}}, 'expected': {"a": 1, "b": 2, "c": 3}},
        ],
    },
)
# Create a function named `calculate_average` that takes any number of scores and returns the average.
check_exercise_210 = functions_input_output_checker(
    {
        'calculate_average': [
            {'input': {'*args': [90, 85, 95]}, 'expected': 90},
            {'input': {'*args': [100, 95]}, 'expected': 97.5},
        ],
    },
)
# Create a function named `compute_class_average` that takes as input any number of dictionaries containing the name as key and a list of scores as value, and returns a dictionary with the average score of all the students.
check_exercise_211 = functions_input_output_checker(
    {
        'compute_class_average': [
            {'input': {'alice': [90, 85, 95], 'bob': [100, 95]}, 'expected': {"alice": 90, "bob": 97.5}},
            {'input': {'alice': [90, 85, 95], 'bob': [100, 95], 'charlie': [80, 75]}, 'expected': {"alice": 90, "bob": 97.5, "charlie": 77.5}},
        ],
    },
)
# Define a function `calculate_area` that takes the radius of a circle as an argument and returns the area. Include a docstring that describes the function, its parameter, and the return value.
check_exercise_212 = docstring_checker(
    {
        'function': "calculate_area",
    },
)
# Define a recursive function `factorial` that calculates the factorial of a given non-negative integer `n`.
check_exercise_213 = functions_input_output_checker(
    {
        'factorial': [
            {'input': {'n': 5}, 'expected': 120},
            {'input': {'n': 3}, 'expected': 6},
        ],
    },
)
# Create a lambda function that takes two arguments `a` and `b` and returns their product. Assign this lambda function to a variable called `multiply`.
check_exercise_214 = functions_input_output_checker(
    {
        'multiply': [
            {'input': {'a': 2, 'b': 3}, 'expected': 6},
            {'input': {'a': 5, 'b': 5}, 'expected': 25},
        ],
    },
)
# Given a list of temperatures in Celsius called `celsius_temps`, use `map` with a lambda function to convert all temperatures to Fahrenheit. Assign the result to a variable `fahrenheit_temps`.
check_exercise_215 = input_output_checker([
    {'input': {'celsius_temps': [0, 10, 20, 30]}, 'expected': {'fahrenheit_temps': [32, 50, 68, 86]}},
    {'input': {'celsius_temps': [-10, 0, 10, 20]}, 'expected': {'fahrenheit_temps': [14, 32, 50, 68]}},
])
# Given a list of numbers called `numbers`, use `filter` with a lambda function to keep only the even numbers. Assign the result to a variable `even_numbers`.
check_exercise_216 = input_output_checker([
    {'input': {'numbers': [1, 2, 3, 4, 5]}, 'expected': {'even_numbers': [2, 4]}},
    {'input': {'numbers': [2, 4, 6, 8, 10]}, 'expected': {'even_numbers': [2, 4, 6, 8, 10]}},
])
# Given a list of dictionaries called `people`, each containing 'name' and 'age' keys, use the `sorted` function with a lambda to sort the list by age in descending order.
check_exercise_217 = input_output_checker([
    {'input': {'people': [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]}, 'expected': {'sorted_people': [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]}},
    {'input': {'people': [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]}, 'expected': {'sorted_people': [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}, {"name": "Charlie", "age": 20}]}},
])
# Given a list of strings called `words`, use `sorted` with a lambda function to sort the words first by length and then alphabetically for words of the same length.
check_exercise_218 = input_output_checker([
    {'input': {'words': ["apple", "banana", "cherry"]}, 'expected': {'sorted_words': ["apple", "banana", "cherry"]}},
    {'input': {'words': ["apple", "banana", "cherry", "date"]}, 'expected': {'sorted_words': ["date", "apple", "banana", "cherry"]}},
])
# Define a function `create_greeting` that takes a arguemnt `salutation` with a default value of "Hello" and returns a function that takes a `name` argument and returns a greeting message.
check_exercise_219 = nested_functions_input_output_checker(
    {
        'create_greeting': [
            {
                'input': [
                    {'salutation': "Hi"},
                    {'name': "Ana"},
                ],
                'expected': "Hi, Ana!",
            },
            {
                'input': [
                    {},
                    {'name': "Bob"},
                ],
                'expected': "Hello, Bob!",
            },
        ],
    },
)
# Given a list of dictionaries called `products`, each containing 'name' and 'price' keys, use `max` with a lambda function to find the product with the highest price.
check_exercise_220 = input_output_checker([
    {'input': {'products': [{"name": "apple", "price": 1.99}, {"name": "banana", "price": 0.99}]}, 'expected': {'most_expensive': {"name": "apple", "price": 1.99}}},
    {'input': {'products': [{"name": "apple", "price": 1.99}, {"name": "banana", "price": 0.99}, {"name": "cherry", "price": 2.99}]}, 'expected': {'most_expensive': {"name": "cherry", "price": 2.99}}},
])
# Create a lambda function that adds two numbers and assign it to a variable `add_lambda`.
check_exercise_221 = functions_input_output_checker(
    {
        'add_lambda': [
            {'input': {'x': 2, 'y': 3}, 'expected': 5},
            {'input': {'x': 5, 'y': 5}, 'expected': 10},
        ],
    },
)
# Use a lambda function to create a function that squares a given number and assigns it to a variable `square_lambda`.
check_exercise_222 = functions_input_output_checker(
    {
        'square_lambda': [
            {'input': {'n': 2}, 'expected': 4},
            {'input': {'n': 5}, 'expected': 25},
        ],
    },
)
# Create a decorator named `log_execution` that updates the function to return the string "Function finished {value}" instead of the original return `value` of the function.
check_exercise_223 = test_decorator([
    {
        'input': {
            'func': lambda x: x + 1,
            'args': (5,),
        },
        'expected': "Function finished 6"
    },
    {
        'input': {
            'func': lambda x: x * 2,
            'args': (5,),
        },
        'expected': "Function finished 10"
    },
], 'log_execution')
# Create a decorator named `time_execution` that measures the execution time of a function and returns the string "less than 5 seconds" if the execution time is less than 5 seconds, or "more than 5 seconds" otherwise.
check_exercise_224 = test_decorator([
    {
        'input': {
            'func': lambda x: x + 1,
            'args': (5,),
        },
        'expected': "less than 5 seconds"
    },
    {
        'input': {
            'func': lambda x: x * 2,
            'args': (5,),
        },
        'expected': "less than 5 seconds"
    },
], 'time_execution')
# Create a decorator that returns a dictionary in the format {"input": *the input of the function*, "output": *the result*} for a function.
check_exercise_225 = test_decorator([
    {
        'input': {
            'func': lambda x: x + 1,
            'args': (5,),
        },
        'expected': {"input": (5,), "output": 6}
    },
    {
        'input': {
            'func': lambda x: x * 2,
            'args': (5,),
        },
        'expected': {"input": (5,), "output": 10}
    },
], 'input_output_dict')

# Create a class called `Car` with attributes `make` and `model`
check_exercise_226 = test_classes_and_methods({
    'Car': {
        'parameters': ['make', 'model'],
    },
})
# Create a class `Rectangle` with attributes `width` and `height`, and initialize them in the constructor.
check_exercise_227 = test_classes_and_methods({
    'Rectangle': {
        'parameters': ['width', 'height'],
    },
})
# Create a class `Rectangle` with attributes `width` and `height`, and a method `area` that returns the area of the rectangle.
check_exercise_228 = test_classes_and_methods({
    'Rectangle': {
        'parameters': ['width', 'height'],
        'methods': {
            'area': [
                {'init_args': {'width': 5, 'height': 10}, 'args': {}, 'expected': 50},
                {'init_args': {'width': 3, 'height': 7}, 'args': {}, 'expected': 21},
                {'init_args': {'width': 2, 'height': 4}, 'args': {}, 'expected': 8},
            ],
        },
    },
})
# Create a class `Vehicle` with attributes `brand` and `year`, then create a class `Motorcycle` that inherits from `Vehicle`
check_exercise_229 = test_classes_and_methods({
    'Vehicle': {
        'parameters': ['brand', 'year'],
    },
    'Motorcycle': {
        'subclass_of': 'Vehicle',
    },
})
# Create a class `Shape` with a method `area`, then create classes `Circle` that has a `radius` attribute and `Square` that has a `side` attribute, both with an `area` method that returns the area of the shape
check_exercise_230 = test_classes_and_methods({
    'Shape': {
        'methods': {
            'area': [],
        },
    },
    'Circle': {
        'subclass_of': 'Shape',
        'parameters': ['radius'],
        'methods': {
            'area': [
                {'init_args': {'radius': 5}, 'args': {}, 'expected': 5**2 * math.pi},
                {'init_args': {'radius': 10}, 'args': {}, 'expected': 10**2 * math.pi},
            ],
        },
    },
    'Square': {
        'subclass_of': 'Shape',
        'parameters': ['side'],
        'methods': {
            'area': [
                {'init_args': {'side': 5}, 'args': {}, 'expected': 25},
                {'init_args': {'side': 10}, 'args': {}, 'expected': 100},
            ],
        },
    },
})
# Create a class `BankAccount` with a private attribute `__balance` and methods `deposit` and `withdraw` that take an amount and update the balance and return the new balance. The `deposit` method should add the amount to the balance and the `withdraw` method should subtract the amount from the balance. The `__balance` attribute should be initialized in the constructor.
check_exercise_231 = test_classes_and_methods({
    'BankAccount': {
        'methods': {
            'deposit': [
                {'init_args': {'balance': 0}, 'args': {'amount': 100}, 'expected': 100},
                {'init_args': {'balance': 0}, 'args': {'amount': 200}, 'expected': 200},
            ],
            'withdraw': [
                {'init_args': {'balance': 100}, 'args': {'amount': 50}, 'expected': 50},
                {'init_args': {'balance': 200}, 'args': {'amount': 100}, 'expected': 100},
            ],
        },
    },
})
# Create a class `Employee` with a protected attribute `_salary` and a method `add_raise` that increases the salary by a given percentage and returns the new salary
check_exercise_232 = test_classes_and_methods({
    'Employee': {
        'methods': {
            'add_raise': [
                {'init_args': {'salary': 1000}, 'args': {'percentage': 10}, 'expected': 1100},
                {'init_args': {'salary': 2000}, 'args': {'percentage': 5}, 'expected': 2100},
            ],
        },
    },
})
# Create an abstract class `Animal` with an abstract method `make_sound`, then create concrete classes `Dog` and `Cat` that implement the method and return a string with the sound the string should be "Woof" for `Dog` and "Meow" for `Cat`
check_exercise_233 = test_classes_and_methods({
    'Animal': {
        'methods': {
            'make_sound': [],
        },
    },
    'Dog': {
        'subclass_of': 'Animal',
        'methods': {
            'make_sound': [
                {'args': {}, 'expected': "Woof"},
            ],
        },
    },
    'Cat': {
        'subclass_of': 'Animal',
        'methods': {
            'make_sound': [
                {'args': {}, 'expected': "Meow"},
            ],
        },
    },
})
# Create a class `Book` with attributes `title`, `author`, and `pages`, and initialize them in the __init__ method
check_exercise_234 = test_classes_and_methods({
    'Book': {
        'parameters': ['title', 'author', 'pages'],
    },
})
# Create a class `Book` with attributes `title`, `author`, and `pages`, and a method `__str__` that returns a string with the book information
check_exercise_235 = test_classes_and_methods({
    'Book': {
        'parameters': ['title', 'author', 'pages'],
        'methods': {
            '__str__': [
                {'init_args': {'title': "Title", 'author': "Author", 'pages': 100}, 'args': {}, 'expected': "Title by Author, 100 pages"},
                {'init_args': {'title': "Book", 'author': "Writer", 'pages': 200}, 'args': {}, 'expected': "Book by Writer, 200 pages"},
            ],
        },
    },
})
# Create a class `Person` with attributes `name` and `age`, and a method `__repr__` that returns a string in the format "Person(name=[name], age=[age])"
check_exercise_236 = test_classes_and_methods({
    'Person': {
        'parameters': ['name', 'age'],
        'methods': {
            '__repr__': [
                {'init_args': {'name': "Alice", 'age': 25}, 'args': {}, 'expected': "Person(name=Alice, age=25)"},
                {'init_args': {'name': "Bob", 'age': 30}, 'args': {}, 'expected': "Person(name=Bob, age=30)"},
            ],
        },
    },
})
# Create a class `Point` with attributes `x` and `y`, and a method `__add__` that returns a new point with the sum of the coordinates
check_exercise_237 = test_classes_and_methods({
    'Point': {
        'parameters': ['x', 'y'],
        'methods': {
            '__add__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 3, 'y': 4}},
                    'expected': {
                        'type': 'Point',
                        'attributes': {'x': 4, 'y': 6},
                    },
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': {
                        'type': 'Point',
                        'attributes': {'x': 15, 'y': 30},
                    },
                },
            ],
        },
    },
})
# Create a class `Vector` with attributes `x` and `y`, and a method `__mul__` that returns the dot product of two vectors
check_exercise_238 = test_classes_and_methods({
    'Vector': {
        'parameters': ['x', 'y'],
        'methods': {
            '__mul__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 3, 'y': 4}},
                    'expected': 11,
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': 250,
                },
            ],
        },
    },
})
# Create a class `Vector` with attributes `x` and `y`, and a method `__sub__` that returns a new vector with the difference of the coordinates
check_exercise_239 = test_classes_and_methods({
    'Vector': {
        'parameters': ['x', 'y'],
        'methods': {
            '__sub__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 3, 'y': 4}},
                    'expected': {
                        'type': 'Vector',
                        'attributes': {'x': -2, 'y': -2},
                    },
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': {
                        'type': 'Vector',
                        'attributes': {'x': -5, 'y': -10},
                    },
                },
            ],
        },
    },
})
# Create a class `Vector` with attributes `x` and `y`, and a method `__eq__` that returns True if two vectors have the same coordinates
check_exercise_240 = test_classes_and_methods({
    'Vector': {
        'parameters': ['x', 'y'],
        'methods': {
            '__eq__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 1, 'y': 2}},
                    'expected': True,
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': False,
                },
            ],
        },
    },
})
# Create a class `Vector` with attributes `x` and `y`, and a method `__len__` that returns the magnitude of the vector
check_exercise_241 = test_classes_and_methods({
    'Vector': {
        'parameters': ['x', 'y'],
        'methods': {
            '__len__': [
                {
                    'init_args': {'x': 3, 'y': 4},
                    'args': {},
                    'expected': 5,
                },
                {
                    'init_args': {'x': 5, 'y': 12},
                    'args': {},
                    'expected': 13,
                },
            ],
        },
    },
})
# Create a class `Vector` with attributes `x` and `y`, a method `__str__` that returns a string with the vector coordinates, a method `__add__` that returns a new vector with the sum of the coordinates, and a method `__mul__` that returns the dot product of two vectors
check_exercise_242 = test_classes_and_methods({
    'Vector': {
        'parameters': ['x', 'y'],
        'methods': {
            '__str__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {},
                    'expected': "(1, 2)",
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {},
                    'expected': "(5, 10)",
                },
            ],
            '__add__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 3, 'y': 4}},
                    'expected': {
                        'type': 'Vector',
                        'attributes': {'x': 4, 'y': 6},
                    },
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': {
                        'type': 'Vector',
                        'attributes': {'x': 15, 'y': 30},
                    },
                },
            ],
            '__mul__': [
                {
                    'init_args': {'x': 1, 'y': 2},
                    'args': {'other': {'x': 3, 'y': 4}},
                    'expected': 11,
                },
                {
                    'init_args': {'x': 5, 'y': 10},
                    'args': {'other': {'x': 10, 'y': 20}},
                    'expected': 250,
                },
            ],
        },
    },
})
# Create classes `Flying` and `Swimming`, then create a class `Duck` that inherits from both
check_exercise_243 = test_classes_and_methods({
    'Flying': {},
    'Swimming': {},
    'Duck': {
        'subclass_of': 'Flying',
    },
    'Duck': {
        'subclass_of': 'Swimming',
    },
})
# Create a class `Animal` with a method `move`, then create a class `Bird` that inherits from `Animal` and overrides the `move` method
check_exercise_244 = test_classes_and_methods({
    'Animal': {
        'methods': {
            'move': [],
        },
    },
    'Bird': {
        'subclass_of': 'Animal',
        'methods': {
            'move': [],
        },
    },
})
# Create a class `Counter` with a class variable that keeps track of how many instances have been created and a method `get_count` that returns the count
check_exercise_245 = test_classes_and_methods({
    'Counter': {
        'methods': {
            'get_count': [
                {'init_args': {}, 'args': {}, 'expected': 1},
                {'init_args': {}, 'args': {}, 'expected': 2},
            ],
        },
    },
})

__all__ = [
    'check_exercise_1',
    'check_exercise_2',
    'check_exercise_3',
    'check_exercise_4',
    'check_exercise_5',
    'check_exercise_6',
    'check_exercise_7',
    'check_exercise_8',
    'check_exercise_9',
    'check_exercise_10',
    'check_exercise_11',
    'check_exercise_12',
    'check_exercise_13',
    'check_exercise_14',
    'check_exercise_15',
    'check_exercise_16',
    'check_exercise_17',
    'check_exercise_18',
    'check_exercise_19',
    'check_exercise_20',
    'check_exercise_21',
    'check_exercise_22',
    'check_exercise_23',
    'check_exercise_24',
    'check_exercise_25',
    'check_exercise_26',
    'check_exercise_27',
    'check_exercise_28',
    'check_exercise_29',
    'check_exercise_30',
    'check_exercise_31',
    'check_exercise_32',
    'check_exercise_33',
    'check_exercise_34',
    'check_exercise_35',
    'check_exercise_36',
    'check_exercise_37',
    'check_exercise_38',
    'check_exercise_39',
    'check_exercise_40',
    'check_exercise_41',
    'check_exercise_42',
    'check_exercise_43',
    'check_exercise_44',
    'check_exercise_45',
    'check_exercise_46',
    'check_exercise_47',
    'check_exercise_48',
    'check_exercise_49',
    'check_exercise_50',
    'check_exercise_51',
    'check_exercise_52',
    'check_exercise_53',
    'check_exercise_54',
    'check_exercise_55',
    'check_exercise_56',
    'check_exercise_57',
    'check_exercise_58',
    'check_exercise_59',
    'check_exercise_60',
    'check_exercise_61',
    'check_exercise_62',
    'check_exercise_63',
    'check_exercise_64',
    'check_exercise_65',
    'check_exercise_66',
    'check_exercise_67',
    'check_exercise_68',
    'check_exercise_69',
    'check_exercise_70',
    'check_exercise_71',
    'check_exercise_72',
    'check_exercise_73',
    'check_exercise_74',
    'check_exercise_75',
    'check_exercise_76',
    'check_exercise_77',
    'check_exercise_78',
    'check_exercise_79',
    'check_exercise_80',
    'check_exercise_81',
    'check_exercise_82',
    'check_exercise_83',
    'check_exercise_84',
    'check_exercise_85',
    'check_exercise_86',
    'check_exercise_87',
    'check_exercise_88',
    'check_exercise_89',
    'check_exercise_90',
    'check_exercise_91',
    'check_exercise_92',
    'check_exercise_93',
    'check_exercise_94',
    'check_exercise_95',
    'check_exercise_96',
    'check_exercise_97',
    'check_exercise_98',
    'check_exercise_99',
    'check_exercise_100',
    'check_exercise_101',
    'check_exercise_102',
    'check_exercise_103',
    'check_exercise_104',
    'check_exercise_105',
    'check_exercise_106',
    'check_exercise_107',
    'check_exercise_108',
    'check_exercise_109',
    'check_exercise_110',
    'check_exercise_111',
    'check_exercise_112',
    'check_exercise_113',
    'check_exercise_114',
    'check_exercise_115',
    'check_exercise_116',
    'check_exercise_117',
    'check_exercise_118',
    'check_exercise_119',
    'check_exercise_120',
    'check_exercise_121',
    'check_exercise_122',
    'check_exercise_123',
    'check_exercise_124',
    'check_exercise_125',
    'check_exercise_126',
    'check_exercise_127',
    'check_exercise_128',
    'check_exercise_129',
    'check_exercise_130',
    'check_exercise_131',
    'check_exercise_132',
    'check_exercise_133',
    'check_exercise_134',
    'check_exercise_135',
    'check_exercise_136',
    'check_exercise_137',
    'check_exercise_138',
    'check_exercise_139',
    'check_exercise_140',
    'check_exercise_141',
    'check_exercise_142',
    'check_exercise_143',
    'check_exercise_144',
    'check_exercise_145',
    'check_exercise_146',
    'check_exercise_147',
    'check_exercise_148',
    'check_exercise_149',
    'check_exercise_150',
    'check_exercise_151',
    'check_exercise_152',
    'check_exercise_153',
    'check_exercise_154',
    'check_exercise_155',
    'check_exercise_156',
    'check_exercise_157',
    'check_exercise_158',
    'check_exercise_159',
    'check_exercise_160',
    'check_exercise_161',
    'check_exercise_162',
    'check_exercise_163',
    'check_exercise_164',
    'check_exercise_165',
    'check_exercise_166',
    'check_exercise_167',
    'check_exercise_168',
    'check_exercise_169',
    'check_exercise_170',
    'check_exercise_171',
    'check_exercise_172',
    'check_exercise_173',
    'check_exercise_174',
    'check_exercise_175',
    'check_exercise_176',
    'check_exercise_177',
    'check_exercise_178',
    'check_exercise_179',
    'check_exercise_180',
    'check_exercise_181',
    'check_exercise_182',
    'check_exercise_183',
    'check_exercise_184',
    'check_exercise_185',
    'check_exercise_186',
    'check_exercise_187',
    'check_exercise_188',
    'check_exercise_189',
    'check_exercise_190',
    'check_exercise_191',
    'check_exercise_192',
    'check_exercise_193',
    'check_exercise_194',
    'check_exercise_195',
    'check_exercise_196',
    'check_exercise_197',
    'check_exercise_198',
    'check_exercise_199',
    'check_exercise_200',
    'check_exercise_201',
    'check_exercise_202',
    'check_exercise_203',
    'check_exercise_204',
    'check_exercise_205',
    'check_exercise_206',
    'check_exercise_207',
    'check_exercise_208',
    'check_exercise_209',
    'check_exercise_210',
    'check_exercise_211',
    'check_exercise_212',
    'check_exercise_213',
    'check_exercise_214',
    'check_exercise_215',
    'check_exercise_216',
    'check_exercise_217',
    'check_exercise_218',
    'check_exercise_219',
    'check_exercise_220',
    'check_exercise_221',
    'check_exercise_222',
    'check_exercise_223',
    'check_exercise_224',
    'check_exercise_225',
    'check_exercise_226',
    'check_exercise_227',
    'check_exercise_228',
    'check_exercise_229',
    'check_exercise_230',
    'check_exercise_231',
    'check_exercise_232',
    'check_exercise_233',
    'check_exercise_234',
    'check_exercise_235',
    'check_exercise_236',
    'check_exercise_237',
    'check_exercise_238',
    'check_exercise_239',
    'check_exercise_240',
    'check_exercise_241',
    'check_exercise_242',
    'check_exercise_243',
    'check_exercise_244',
    'check_exercise_245',
]