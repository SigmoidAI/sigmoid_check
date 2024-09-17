import sys
from io import StringIO
from functools import wraps

def create_checker(expected_output=None, expected_variables=None, test_cases=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if test_cases:
                all_passed = True
                implemented = False
                for i, (inputs, expected) in enumerate(test_cases, 1):
                    old_stdout = sys.stdout
                    sys.stdout = captured_output = StringIO()

                    try:
                        func(*inputs)
                        output = captured_output.getvalue().strip()
                        sys.stdout = old_stdout

                        if output:
                            implemented = True

                        if str(output) == str(expected):
                            print(f"✅ Test case {i} passed!")
                        else:
                            print(f"❌ Test case {i} failed.")
                            all_passed = False

                    except Exception as e:
                        sys.stdout = old_stdout
                        print(f"❌ Test case {i} failed due to an error.")
                        all_passed = False

                if not implemented:
                    print("❌ The exercise has not been implemented yet. Please complete the exercise.")
                elif all_passed:
                    print("🎉 Congratulations! All test cases passed.")
                else:
                    print("❗ Some test cases failed. Keep working on your solution.")
            else:
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()

                try:
                    result = func(*args, **kwargs)
                    output = captured_output.getvalue().strip()
                    sys.stdout = old_stdout

                    if expected_variables is not None:
                        if not isinstance(result, dict):
                            print("❌ The exercise function should return a dictionary of variables to check.")
                            return
                        for var_name, expected_value in expected_variables.items():
                            if var_name not in result:
                                print(f"❌ The variable '{var_name}' is missing.")
                            elif result[var_name] == expected_value:
                                print(f"✅ Great job! The variable '{var_name}' has the correct value: {result[var_name]}")
                            else:
                                print(f"❌ Oops! The variable '{var_name}' has the wrong value. Expected: {expected_value}, Got: {result[var_name]}")

                    elif expected_output is not None:
                        expected_str = str(expected_output)
                        output_str = str(output)
                        if output_str == expected_str:
                            print(f"✅ Great job! The output is correct: {output}")
                        else:
                            print(f"❌ Oops! The output is incorrect. Expected: {expected_output}, Got: {output}")

                    else:
                        print(f"Function output: {output}")

                except NameError:
                    sys.stdout = old_stdout
                    print("❌ The exercise has not been implemented yet. Please complete the exercise.")
                except Exception as e:
                    sys.stdout = old_stdout
                    print(f"❌ An error occurred: {str(e)}")

            return None

        return wrapper
    return decorator

# print the text "Hello, World!" to the console;
check_exercise_1 = create_checker(expected_output="Hello, World!")
# print the result of 3 + 5;
check_exercise_2 = create_checker(expected_output=8)
# create a variable called "name" and assign it the value "John";
check_exercise_3 = create_checker(expected_variables={"name": "John"})
# print the text "Hello, John!" to the console using the variable `name`;
check_exercise_4 = create_checker(test_cases=[
    (("John",), "Hello, John!"),
    (("Alice",), "Hello, Alice!"),
    (("Bob",), "Hello, Bob!"),
])
# create a variable called "age" and assign it the value 25;
check_exercise_5 = create_checker(expected_variables={"age": 25})
# print the text "John is 25 years old" to the console using the variables `name` and `age`
check_exercise_6 = create_checker(test_cases=[
    (("John", 25), "John is 25 years old"),
    (("Alice", 30), "Alice is 30 years old"),
    (("Bob", 40), "Bob is 40 years old"),
])
# create a variable called "is_old" and assign it the value True;
check_exercise_7 = create_checker(expected_variables={"is_old": True})


__all__ = [
    'check_exercise_1',
    'check_exercise_2',
    'check_exercise_3',
    'check_exercise_4',
    'check_exercise_5',
    'check_exercise_6',
    'check_exercise_7',
]