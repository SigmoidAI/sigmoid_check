import sys
from io import StringIO
from functools import wraps

def create_checker(expected_output=None, expected_variables=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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
                print("❌ The exercise has not been implemented yet. Please complete the exercise.")

            # Don't return anything to avoid UnboundLocalError
            return None

        return wrapper
    return decorator

# Example checkers
check_exercise_1 = create_checker(expected_output="Hello, World!")
check_exercise_2 = create_checker(expected_output=8)
check_exercise_3 = create_checker(expected_variables={"name": "John"})

# Export all checkers
__all__ = ['check_exercise_1', 'check_exercise_2', 'check_exercise_3']