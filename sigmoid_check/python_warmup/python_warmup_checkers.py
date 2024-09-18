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
]

