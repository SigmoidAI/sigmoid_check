import sys
from io import StringIO
from functools import wraps

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
]

