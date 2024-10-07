import numpy as np
from functools import wraps

def check_equality(expected, result):
    """
    Function to check that two variables are equal, then return a boolean.
    The function compare all elements including nested structures and arrays, ensuring that all elements are equal.
    """
    if type(expected) != type(result):
        return False
    if isinstance(expected, dict):
        if len(expected) != len(result):
            return False
        for key in expected:
            if key not in result:
                return False
            if not check_equality(expected[key], result[key]):
                return False
        return True
    elif isinstance(expected, list):
        if len(expected) != len(result):
            return False
        for i in range(len(expected)):
            if not check_equality(expected[i], result[i]):
                return False
        return True
    elif isinstance(expected, np.ndarray):
        if expected.all() != result.all():
            return False
        return True
    elif isinstance(expected, tuple):
        if len(expected) != len(result):
            return False
        for i in range(len(expected)):
            if not check_equality(expected[i], result[i]):
                return False
        return True
    else:
        return expected == result

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
                    if not check_equality(case['expected'], result):
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
                            if check_equality(result, case['expected']):
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

# TASKS:
# Given a list of integers `int_list`, create a NumPy array named `array_from_list`.
check_numpy_1 = input_output_checker([
    {
        'input': {'int_list': [1, 2, 3, 4, 5]},
        'expected': {'array_from_list': np.array([1, 2, 3, 4, 5])}
    },
    {
        'input': {'int_list': [10, 20, 30, 40, 50]},
        'expected': {'array_from_list': np.array([10, 20, 30, 40, 50])}
    },
    {
        'input': {'int_list': [100, 200, 300, 400, 500]},
        'expected': {'array_from_list': np.array([100, 200, 300, 400, 500])}
    }
])

# Given two NumPy arrays `array1` and `array2` of the same shape, save their element-wise addition to `added_array`.
check_numpy_2 = input_output_checker([
    {
        'input': {'array1': np.array([1, 2, 3, 4, 5]), 'array2': np.array([5, 4, 3, 2, 1])},
        'expected': {'added_array': np.array([6, 6, 6, 6, 6])}
    },
    {
        'input': {'array1': np.array([10, 20, 30, 40, 50]), 'array2': np.array([50, 40, 30, 20, 10])},
        'expected': {'added_array': np.array([60, 60, 60, 60, 60])}
    },
    {
        'input': {'array1': np.array([100, 200, 300, 400, 500]), 'array2': np.array([500, 400, 300, 200, 100])},
        'expected': {'added_array': np.array([600, 600, 600, 600, 600])}
    }
])
# Given two NumPy arrays `arrayA` and `arrayB`, calculate the element-wise subtraction of `arrayB` from `arrayA` and store the result in `subtracted_array`.
check_numpy_3 = input_output_checker([
    {
        'input': {'arrayA': np.array([1, 2, 3, 4, 5]), 'arrayB': np.array([5, 4, 3, 2, 1])},
        'expected': {'subtracted_array': np.array([-4, -2, 0, 2, 4])}
    },
    {
        'input': {'arrayA': np.array([10, 20, 30, 40, 50]), 'arrayB': np.array([50, 40, 30, 20, 10])},
        'expected': {'subtracted_array': np.array([-40, -20, 0, 20, 40])}
    },
    {
        'input': {'arrayA': np.array([100, 200, 300, 400, 500]), 'arrayB': np.array([500, 400, 300, 200, 100])},
        'expected': {'subtracted_array': np.array([-400, -200, 0, 200, 400])}
    }
])
# Given two NumPy arrays `num_array1` and `num_array2` of the same shape, find their element-wise multiplication and store in `multiplied_array`.
check_numpy_4 = input_output_checker([
    {
        'input': {'num_array1': np.array([1, 2, 3, 4, 5]), 'num_array2': np.array([5, 4, 3, 2, 1])},
        'expected': {'multiplied_array': np.array([5, 8, 9, 8, 5])}
    },
    {
        'input': {'num_array1': np.array([10, 20, 30, 40, 50]), 'num_array2': np.array([50, 40, 30, 20, 10])},
        'expected': {'multiplied_array': np.array([500, 800, 900, 800, 500])}
    },
    {
        'input': {'num_array1': np.array([100, 200, 300, 400, 500]), 'num_array2': np.array([500, 400, 300, 200, 100])},
        'expected': {'multiplied_array': np.array([50000, 80000, 90000, 80000, 50000])}
    }
])
# Given two NumPy arrays `dividend_array` and `divisor_array` of the same shape, perform element-wise division and assign the result to `divided_array`.
check_numpy_5 = input_output_checker([
    {
        'input': {'dividend_array': np.array([1, 2, 3, 4, 5]), 'divisor_array': np.array([5, 4, 3, 2, 1])},
        'expected': {'divided_array': np.array([0.2, 0.5, 1, 2, 5])}
    },
    {
        'input': {'dividend_array': np.array([10, 20, 30, 40, 50]), 'divisor_array': np.array([50, 40, 30, 20, 10])},
        'expected': {'divided_array': np.array([0.2, 0.5, 1, 2, 5])}
    },
    {
        'input': {'dividend_array': np.array([100, 200, 300, 400, 500]), 'divisor_array': np.array([500, 400, 300, 200, 100])},
        'expected': {'divided_array': np.array([0.2, 0.5, 1, 2, 5])}
    }
])
# Given a NumPy array `base_array` and a scalar `exponent`, compute the element-wise exponentiation and store the result in `exponentiated_array`.
check_numpy_6 = input_output_checker([
    {
        'input': {'base_array': np.array([1, 2, 3, 4, 5]), 'exponent': 2},
        'expected': {'exponentiated_array': np.array([1, 4, 9, 16, 25])}
    },
    {
        'input': {'base_array': np.array([10, 20, 30, 40, 50]), 'exponent': 3},
        'expected': {'exponentiated_array': np.array([1000, 8000, 27000, 64000, 125000])}
    },
    {
        'input': {'base_array': np.array([100, 200, 300, 400, 500]), 'exponent': 4},
        'expected': {'exponentiated_array': np.array([100000000, 16000000000, 81000000000, 256000000000, 625000000000])}
    }
])
# Given a list of numbers `float_list`, create a NumPy array named `float_array` with a float data type.
check_numpy_7 = input_output_checker([
    {
        'input': {'float_list': [1.0, 2.0, 3.0, 4.0, 5.0]},
        'expected': {'float_array': np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)}
    },
    {
        'input': {'float_list': [10.0, 20.0, 30.0, 40.0, 50.0]},
        'expected': {'float_array': np.array([10.0, 20.0, 30.0, 40.0, 50.0], dtype=float)}
    },
    {
        'input': {'float_list': [100.0, 200.0, 300.0, 400.0, 500.0]},
        'expected': {'float_array': np.array([100.0, 200.0, 300.0, 400.0, 500.0], dtype=float)}
    }
])
# Use the list of lists `matrix_data` to create a 2-dimensional NumPy array named `matrix`.
check_numpy_8 = input_output_checker([
    {
        'input': {'matrix_data': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]},
        'expected': {'matrix': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}
    },
    {
        'input': {'matrix_data': [[10, 20, 30], [40, 50, 60], [70, 80, 90]]},
        'expected': {'matrix': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])}
    },
    {
        'input': {'matrix_data': [[100, 200, 300], [400, 500, 600], [700, 800, 900]]},
        'expected': {'matrix': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])}
    }
])
# Given a NumPy array `original_array` and the new shape tuple `new_shape`, reshape the array and store it in `reshaped_array`.
check_numpy_9 = input_output_checker([
    {
        'input': {'original_array': np.array([1, 2, 3, 4, 5, 6]), 'new_shape': (2, 3)},
        'expected': {'reshaped_array': np.array([[1, 2, 3], [4, 5, 6]])}
    },
    {
        'input': {'original_array': np.array([10, 20, 30, 40, 50, 60]), 'new_shape': (3, 2)},
        'expected': {'reshaped_array': np.array([[10, 20], [30, 40], [50, 60]])}
    },
    {
        'input': {'original_array': np.array([100, 200, 300, 400, 500, 600]), 'new_shape': (6, 1)},
        'expected': {'reshaped_array': np.array([[100], [200], [300], [400], [500], [600]])}
    }
])
# Using NumPy's `arange`, generate an array named `range_array` from 0 to `end` with a step of `step`.
check_numpy_10 = input_output_checker([
    {
        'input': {'end': 5, 'step': 1},
        'expected': {'range_array': np.arange(0, 5, 1)}
    },
    {
        'input': {'end': 10, 'step': 2},
        'expected': {'range_array': np.arange(0, 10, 2)}
    },
    {
        'input': {'end': 15, 'step': 3},
        'expected': {'range_array': np.arange(0, 15, 3)}
    }
])
# Use NumPy's `linspace` to create an array named `linspace_array` with `num_points` evenly spaced points between `start` and `stop`.
check_numpy_11 = input_output_checker([
    {
        'input': {'start': 0, 'stop': 10, 'num_points': 5},
        'expected': {'linspace_array': np.linspace(0, 10, 5)}
    },
    {
        'input': {'start': 0, 'stop': 20, 'num_points': 10},
        'expected': {'linspace_array': np.linspace(0, 20, 10)}
    },
    {
        'input': {'start': 0, 'stop': 30, 'num_points': 15},
        'expected': {'linspace_array': np.linspace(0, 30, 15)}
    }
])
# Create a NumPy array named `zero_array` with a shape specified by `shape` filled with zeros.
check_numpy_12 = input_output_checker([
    {
        'input': {'shape': (2, 3)},
        'expected': {'zero_array': np.zeros((2, 3))}
    },
    {
        'input': {'shape': (3, 2)},
        'expected': {'zero_array': np.zeros((3, 2))}
    },
    {
        'input': {'shape': (4, 4)},
        'expected': {'zero_array': np.zeros((4, 4))}
    }
])
# Create a NumPy array named `ones_array` with a shape given by `shape` filled with ones.
check_numpy_13 = input_output_checker([
    {
        'input': {'shape': (2, 3)},
        'expected': {'ones_array': np.ones((2, 3))}
    },
    {
        'input': {'shape': (3, 2)},
        'expected': {'ones_array': np.ones((3, 2))}
    },
    {
        'input': {'shape': (4, 4)},
        'expected': {'ones_array': np.ones((4, 4))}
    }
])
# Given a size `n`, generate an identity matrix named `identity_matrix` of size `n x n`.
check_numpy_14 = input_output_checker([
    {
        'input': {'n': 2},
        'expected': {'identity_matrix': np.eye(2)}
    },
    {
        'input': {'n': 3},
        'expected': {'identity_matrix': np.eye(3)}
    },
    {
        'input': {'n': 4},
        'expected': {'identity_matrix': np.eye(4)}
    }
])
# Given a NumPy array `matrix_array`, extract its shape and assign it to `array_shape`.
check_numpy_15 = input_output_checker([
    {
        'input': {'matrix_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'array_shape': (3, 3)}
    },
    {
        'input': {'matrix_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'array_shape': (3, 3)}
    },
    {
        'input': {'matrix_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'array_shape': (3, 3)}
    }
])
# Determine the number of dimensions of the NumPy array `dim_array` and store it in `num_dimensions`.
check_numpy_16 = input_output_checker([
    {
        'input': {'dim_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'num_dimensions': 1}
    },
    {
        'input': {'dim_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'num_dimensions': 2}
    },
    {
        'input': {'dim_array': np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])},
        'expected': {'num_dimensions': 3}
    }
])
# Calculate the total number of elements in the NumPy array `elements_array` and store it in `total_elements`.
check_numpy_17 = input_output_checker([
    {
        'input': {'elements_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'total_elements': 5}
    },
    {
        'input': {'elements_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'total_elements': 9}
    },
    {
        'input': {'elements_array': np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])},
        'expected': {'total_elements': 12}
    }
])
# Assign the data type of elements in the NumPy array `type_array` to the variable `element_type`.
check_numpy_18 = input_output_checker([
    {
        'input': {'type_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'element_type': np.dtype('int64')}
    },
    {
        'input': {'type_array': np.array([1.0, 2.0, 3.0, 4.0, 5.0])},
        'expected': {'element_type': np.dtype('float64')}
    },
    {
        'input': {'type_array': np.array(['a', 'b', 'c', 'd', 'e'])},
        'expected': {'element_type': np.dtype('<U1')}
    }
])
# Compute the memory size (in bytes) of each element in the array `memory_array` and assign it to `element_size`.
check_numpy_19 = input_output_checker([
    {
        'input': {'memory_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'element_size': 8}
    },
    {
        'input': {'memory_array': np.array([1.0, 2.0, 3.0, 4.0, 5.0])},
        'expected': {'element_size': 8}
    },
    {
        'input': {'memory_array': np.array(['a', 'b', 'c', 'd', 'e'])},
        'expected': {'element_size': 4}
    }
])
# Convert the integer NumPy array `int_array` to a float array and save it in `float_converted_array`.
check_numpy_20 = input_output_checker([
    {
        'input': {'int_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'float_converted_array': np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)}
    },
    {
        'input': {'int_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'float_converted_array': np.array([10.0, 20.0, 30.0, 40.0, 50.0], dtype=float)}
    },
    {
        'input': {'int_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'float_converted_array': np.array([100.0, 200.0, 300.0, 400.0, 500.0], dtype=float)}
    }
])
# Given a NumPy array `access_array` and an index `index`, assign the element at that index to `selected_element`.
check_numpy_21 = input_output_checker([
    {
        'input': {'access_array': np.array([1, 2, 3, 4, 5]), 'index': 2},
        'expected': {'selected_element': np.int64(3)}
    },
    {
        'input': {'access_array': np.array([10, 20, 30, 40, 50]), 'index': 4},
        'expected': {'selected_element': np.int64(50)}
    },
    {
        'input': {'access_array': np.array([100, 200, 300, 400, 500]), 'index': 0},
        'expected': {'selected_element': np.int64(100)}
    }
])
# Given a NumPy array `slice_array`, extract a slice using `start` and `end` indices, and store it in `sliced_array`.
check_numpy_22 = input_output_checker([
    {
        'input': {'slice_array': np.array([1, 2, 3, 4, 5]), 'start': 1, 'end': 4},
        'expected': {'sliced_array': np.array([2, 3, 4])}
    },
    {
        'input': {'slice_array': np.array([10, 20, 30, 40, 50]), 'start': 0, 'end': 3},
        'expected': {'sliced_array': np.array([10, 20, 30])}
    },
    {
        'input': {'slice_array': np.array([100, 200, 300, 400, 500]), 'start': 2, 'end': 5},
        'expected': {'sliced_array': np.array([300, 400, 500])}
    }
])
# Increase each element of `one_d_array` by 5 and store the result in `increased_array`.
check_numpy_23 = input_output_checker([
    {
        'input': {'one_d_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'increased_array': np.array([6, 7, 8, 9, 10])}
    },
    {
        'input': {'one_d_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'increased_array': np.array([15, 25, 35, 45, 55])}
    },
    {
        'input': {'one_d_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'increased_array': np.array([105, 205, 305, 405, 505])}
    }
])
# Double the values in the 2D array `multi_d_array` and save it in `doubled_array`.
check_numpy_24 = input_output_checker([
    {
        'input': {'multi_d_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'doubled_array': np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])}
    },
    {
        'input': {'multi_d_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'doubled_array': np.array([[20, 40, 60], [80, 100, 120], [140, 160, 180]])}
    },
    {
        'input': {'multi_d_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'doubled_array': np.array([[200, 400, 600], [800, 1000, 1200], [1400, 1600, 1800]])}
    }
])
# Given a NumPy array `mask_array` and a `mask_value`, create `filtered_array` containing only the elements of `mask_array` that are greater than `mask_value`.
check_numpy_25 = input_output_checker([
    {
        'input': {'mask_array': np.array([1, 2, 3, 4, 5]), 'mask_value': 3},
        'expected': {'filtered_array': np.array([4, 5])}
    },
    {
        'input': {'mask_array': np.array([10, 20, 30, 40, 50]), 'mask_value': 30},
        'expected': {'filtered_array': np.array([40, 50])}
    },
    {
        'input': {'mask_array': np.array([100, 200, 300, 400, 500]), 'mask_value': 200},
        'expected': {'filtered_array': np.array([300, 400, 500])}
    }
])
# Apply masking to the 2D array `multi_mask_array` that keeps all elements greater than the 'condition_value' and store the satisfying elements in `masked_array_2d`.
check_numpy_26 = input_output_checker([
    {
        'input': {'multi_mask_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 'condition_value': 5},
        'expected': {'masked_array_2d': np.array([6, 7, 8, 9])}
    },
    {
        'input': {'multi_mask_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), 'condition_value': 40},
        'expected': {'masked_array_2d': np.array([50, 60, 70, 80, 90])}
    },
    {
        'input': {'multi_mask_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]]), 'condition_value': 800},
        'expected': {'masked_array_2d': np.array([900])}
    }
])
# Calculate the sum of elements for each column of a 2D array `sum_2d_array` and store it in `column_sums`.
check_numpy_27 = input_output_checker([
    {
        'input': {'sum_2d_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'column_sums': np.array([12, 15, 18])}
    },
    {
        'input': {'sum_2d_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'column_sums': np.array([120, 150, 180])}
    },
    {
        'input': {'sum_2d_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'column_sums': np.array([1200, 1500, 1800])}
    }
])
# Find the minimum value in the NumPy array `min_array` and assign it to `min_value`.
check_numpy_28 = input_output_checker([
    {
        'input': {'min_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'min_value': np.int64(1)}
    },
    {
        'input': {'min_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'min_value': np.int64(10)}
    },
    {
        'input': {'min_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'min_value': np.int64(100)}
    }
])
# Find the maximum value in the NumPy array `max_array` and assign it to `max_value`.
check_numpy_29 = input_output_checker([
    {
        'input': {'max_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'max_value': np.int64(5)}
    },
    {
        'input': {'max_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'max_value': np.int64(50)}
    },
    {
        'input': {'max_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'max_value': np.int64(500)}
    }
])
# Calculate the mean of `mean_array` and store it in `mean_value`.
check_numpy_30 = input_output_checker([
    {
        'input': {'mean_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'mean_value': np.float64(3.0)}
    },
    {
        'input': {'mean_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'mean_value': np.float64(30.0)}
    },
    {
        'input': {'mean_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'mean_value': np.float64(300.0)}
    }
])
# Calculate the standard deviation of the NumPy array `std_array` and assign it to `std_dev`.
check_numpy_31 = input_output_checker([
    {
        'input': {'std_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'std_dev': np.array([1, 2, 3, 4, 5]).std()}
    },
    {
        'input': {'std_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'std_dev': np.array([10, 20, 30, 40, 50]).std()}
    },
    {
        'input': {'std_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'std_dev': np.array([100, 200, 300, 400, 500]).std()}
    }
])
# Compute the square root of each element in `sqrt_array` using `np.sqrt()` and save the result in `sqrt_result`.
check_numpy_32 = input_output_checker([
    {
        'input': {'sqrt_array': np.array([1, 4, 9, 16, 25])},
        'expected': {'sqrt_result': np.array([1., 2., 3., 4., 5.])}
    },
    {
        'input': {'sqrt_array': np.array([100, 400, 900, 1600, 2500])},
        'expected': {'sqrt_result': np.array([10., 20., 30., 40., 50.])}
    },
    {
        'input': {'sqrt_array': np.array([10000, 40000, 90000, 160000, 250000])},
        'expected': {'sqrt_result': np.array([100., 200., 300., 400., 500.])}
    }
])
# Calculate the exponential of each element in `exp_array` with `np.exp()` and store it in `exp_result`.
check_numpy_33 = input_output_checker([
    {
        'input': {'exp_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'exp_result': np.array([2.71828183, 7.3890561, 20.08553692, 54.59815003, 148.4131591])}
    },
    {
        'input': {'exp_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'exp_result': np.array([22026.4657948, 485165195.4, 106864745815.7, 2.353852668e+17, 5.184705528e+20])}
    },
    {
        'input': {'exp_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'exp_result': np.array([2.688117142e+43, 7.225973768e+86, 1.9424264e+130, 5.22146985e+173, 1.403592217e+217])}
    }
])
# Compute the natural logarithm of each element in `log_array` with `np.log()` and save it in `log_result`.
check_numpy_34 = input_output_checker([
    {
        'input': {'log_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'log_result': np.array([0., 0.69314718, 1.09861229, 1.38629436, 1.60943791])}
    },
    {
        'input': {'log_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'log_result': np.array([2.30258509, 2.99573227, 3.40119738, 3.68887945, 3.91202301])}
    },
    {
        'input': {'log_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'log_result': np.array([4.60517019, 5.29831737, 5.70378247, 5.99146455, 6.2146081])}
    }
])
# Calculate the sine of each element in `sin_array` using `np.sin()` and store the result in `sin_result`.
check_numpy_35 = input_output_checker([
    {
        'input': {'sin_array': np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])},
        'expected': {'sin_result': np.array([0., 0.5, 0.70710678, 0.8660254, 1.])}
    },
    {
        'input': {'sin_array': np.array([0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi])},
        'expected': {'sin_result': np.array([0., 0.8660254, 1., 0.8660254, 0.])}
    },
    {
        'input': {'sin_array': np.array([0, 2*np.pi/3, np.pi, 4*np.pi/3, 3*np.pi/2])},
        'expected': {'sin_result': np.array([0., 0.8660254, 0., -0.8660254, -1.])}
    }
])
# Compute the cosine of `cos_array` with `np.cos()` and save it in `cos_result`.
check_numpy_36 = input_output_checker([
    {
        'input': {'cos_array': np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])},
        'expected': {'cos_result': np.cos(np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]))}
    },
    {
        'input': {'cos_array': np.array([0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi])},
        'expected': {'cos_result': np.cos(np.array([0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi]))}
    },
    {
        'input': {'cos_array': np.array([0, 2*np.pi/3, np.pi, 4*np.pi/3, 3*np.pi/2])},
        'expected': {'cos_result': np.cos(np.array([0, 2*np.pi/3, np.pi, 4*np.pi/3, 3*np.pi/2]))}
    }
])
# Calculate the tangent of each element in `tan_array` using `np.tan()` and save it in `tan_result`.
check_numpy_37 = input_output_checker([
    {
        'input': {'tan_array': np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])},
        'expected': {'tan_result': np.array([0., 0.57735027, 1., 1.73205081, np.inf])}
    },
    {
        'input': {'tan_array': np.array([0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi])},
        'expected': {'tan_result': np.array([0., 1.73205081, np.inf, -1.73205081, 0.])}
    },
    {
        'input': {'tan_array': np.array([0, 2*np.pi/3, np.pi, 4*np.pi/3, 3*np.pi/2])},
        'expected': {'tan_result': np.array([0., -1.73205081, 0., 1.73205081, np.inf])}
    }
])
# Transpose the 2D array `transpose_array` using `np.transpose()` and store in `transposed_array`.
check_numpy_38 = input_output_checker([
    {
        'input': {'transpose_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'transposed_array': np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])}
    },
    {
        'input': {'transpose_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'transposed_array': np.array([[10, 40, 70], [20, 50, 80], [30, 60, 90]])}
    },
    {
        'input': {'transpose_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'transposed_array': np.array([[100, 400, 700], [200, 500, 800], [300, 600, 900]])}
    }
])
# Compute the dot product of `vector1` and `vector2` using `np.dot()` and assign the result to `dot_product_result`.
check_numpy_39 = input_output_checker([
    {
        'input': {'vector1': np.array([1, 2, 3]), 'vector2': np.array([4, 5, 6])},
        'expected': {'dot_product_result': np.int64(32)}
    },
    {
        'input': {'vector1': np.array([10, 20, 30]), 'vector2': np.array([40, 50, 60])},
        'expected': {'dot_product_result': np.int64(3200)}
    },
    {
        'input': {'vector1': np.array([100, 200, 300]), 'vector2': np.array([400, 500, 600])},
        'expected': {'dot_product_result': np.int64(320000)}
    }
])
# Calculate the inverse of the square matrix `square_matrix` using `np.linalg.inv()` and store it in `inverse_matrix`.
check_numpy_40 = input_output_checker([
    {
        'input': {'square_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'inverse_matrix': np.array([[-2., 1.], [1.5, -0.5]])}
    },
    {
        'input': {'square_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'inverse_matrix': np.array([[-4., 2.], [3., -1.]])}
    },
    {
        'input': {'square_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'inverse_matrix': np.array([[-4., 2.], [3., -1.]])}
    }
])
# Find the determinant of the square matrix `det_matrix` using `np.linalg.det()` and assign it to `determinant_value`.
check_numpy_41 = input_output_checker([
    {
        'input': {'det_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'determinant_value': np.linalg.det(np.array([[1, 2], [3, 4]]))}
    },
    {
        'input': {'det_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'determinant_value': np.linalg.det(np.array([[10, 20], [30, 40]]))}
    },
    {
        'input': {'det_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'determinant_value': np.linalg.det(np.array([[100, 200], [300, 400]]) )}
    }
])
# Concatenate `array_x` and `array_y` vertically using `np.concatenate()` and save the result in `concat_vertical`.
check_numpy_42 = input_output_checker([
    {
        'input': {'array_x': np.array([[1, 2], [3, 4]]), 'array_y': np.array([[5, 6], [7, 8]])},
        'expected': {'concat_vertical': np.array([[1, 2], [3, 4], [5, 6], [7, 8]])}
    },
    {
        'input': {'array_x': np.array([[10, 20], [30, 40]]), 'array_y': np.array([[50, 60], [70, 80]])},
        'expected': {'concat_vertical': np.array([[10, 20], [30, 40], [50, 60], [70, 80]])}
    },
    {
        'input': {'array_x': np.array([[100, 200], [300, 400]]), 'array_y': np.array([[500, 600], [700, 800]])},
        'expected': {'concat_vertical': np.array([[100, 200], [300, 400], [500, 600], [700, 800]])}
    }
])
# Stack `stack_array1` and `stack_array2` horizontally using `np.hstack()` and assign it to `stacked_horizontal`.
check_numpy_43 = input_output_checker([
    {
        'input': {'stack_array1': np.array([[1, 2], [3, 4]]), 'stack_array2': np.array([[5, 6], [7, 8]])},
        'expected': {'stacked_horizontal': np.array([[1, 2, 5, 6], [3, 4, 7, 8]])}
    },
    {
        'input': {'stack_array1': np.array([[10, 20], [30, 40]]), 'stack_array2': np.array([[50, 60], [70, 80]])},
        'expected': {'stacked_horizontal': np.array([[10, 20, 50, 60], [30, 40, 70, 80]])}
    },
    {
        'input': {'stack_array1': np.array([[100, 200], [300, 400]]), 'stack_array2': np.array([[500, 600], [700, 800]])},
        'expected': {'stacked_horizontal': np.array([[100, 200, 500, 600], [300, 400, 700, 800]])}
    }
])
# Add a scalar `scalar_value` to each element of `broadcast_array` using broadcasting and store in `broadcast_result`.
check_numpy_44 = input_output_checker([
    {
        'input': {'broadcast_array': np.array([[1, 2], [3, 4]]), 'scalar_value': 5},
        'expected': {'broadcast_result': np.array([[6, 7], [8, 9]])}
    },
    {
        'input': {'broadcast_array': np.array([[10, 20], [30, 40]]), 'scalar_value': 50},
        'expected': {'broadcast_result': np.array([[60, 70], [80, 90]])}
    },
    {
        'input': {'broadcast_array': np.array([[100, 200], [300, 400]]), 'scalar_value': 500},
        'expected': {'broadcast_result': np.array([[600, 700], [800, 900]])}
    }
])
# Given a 1D array `small_array` and a 2D array `large_array`, utilize broadcasting to add them and store the result in `broadcast_sum`.
check_numpy_45 = input_output_checker([
    {
        'input': {'small_array': np.array([1, 2]), 'large_array': np.array([[3, 4], [5, 6]])},
        'expected': {'broadcast_sum': np.array([[4, 6], [6, 8]])}
    },
    {
        'input': {'small_array': np.array([10, 20]), 'large_array': np.array([[30, 40], [50, 60]])},
        'expected': {'broadcast_sum': np.array([[40, 60], [60, 80]])}
    },
    {
        'input': {'small_array': np.array([100, 200]), 'large_array': np.array([[300, 400], [500, 600]])},
        'expected': {'broadcast_sum': np.array([[400, 600], [600, 800]])}
    }
])
# Subtract a scalar value `scalar_sub` from each element of `two_d_array`.
check_numpy_46 = input_output_checker([
    {
        'input': {'two_d_array': np.array([[1, 2], [3, 4]]), 'scalar_sub': 1},
        'expected': {'two_d_array': np.array([[0, 1], [2, 3]])}
    },
    {
        'input': {'two_d_array': np.array([[10, 20], [30, 40]]), 'scalar_sub': 10},
        'expected': {'two_d_array': np.array([[0, 10], [20, 30]])}
    },
    {
        'input': {'two_d_array': np.array([[100, 200], [300, 400]]), 'scalar_sub': 100},
        'expected': {'two_d_array': np.array([[0, 100], [200, 300]])}
    }
])
# Given dimensions `dim1`, `dim2`, and `dim3`, create a 3D NumPy array named `random_int_array` containing random integers between 0 and 10.
check_numpy_47 = input_output_checker([
    {
        'input': {'dim1': 2, 'dim2': 3, 'dim3': 4},
        'expected': {'random_int_array': np.random.randint(0, 10, (2, 3, 4))}
    },
    {
        'input': {'dim1': 3, 'dim2': 4, 'dim3': 5},
        'expected': {'random_int_array': np.random.randint(0, 10, (3, 4, 5))}
    },
    {
        'input': {'dim1': 4, 'dim2': 5, 'dim3': 6},
        'expected': {'random_int_array': np.random.randint(0, 10, (4, 5, 6))}
    }
])
# Convert the 2D array `multi_array` into a 1D array named `flattened`.
check_numpy_48 = input_output_checker([
    {
        'input': {'multi_array': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'flattened': np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])}
    },
    {
        'input': {'multi_array': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'flattened': np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])}
    },
    {
        'input': {'multi_array': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'flattened': np.array([100, 200, 300, 400, 500, 600, 700, 800, 900])}
    }
])
# Given a NumPy array `nonzero_array`, use `np.nonzero()` to find indices of non-zero elements and assign them to `nonzero_indices`.
check_numpy_49 = input_output_checker([
    {
        'input': {'nonzero_array': np.array([1, 0, 2, 0, 3])},
        'expected': {'nonzero_indices': (np.array([0, 2, 4]),)}
    },
    {
        'input': {'nonzero_array': np.array([0, 1, 0, 2, 0, 3])},
        'expected': {'nonzero_indices': (np.array([1, 3, 5]),)}
    },
    {
        'input': {'nonzero_array': np.array([0, 0, 1, 0, 2, 0, 3])},
        'expected': {'nonzero_indices': (np.array([2, 4, 6]),)}
    }
])
# Create a diagonal matrix `diagonal_matrix` with the given 1D array `diag_elements` using `np.diag()`.
check_numpy_50 = input_output_checker([
    {
        'input': {'diag_elements': np.array([1, 2, 3])},
        'expected': {'diagonal_matrix': np.diag([1, 2, 3])}
    },
    {
        'input': {'diag_elements': np.array([10, 20, 30])},
        'expected': {'diagonal_matrix': np.diag([10, 20, 30])}
    },
    {
        'input': {'diag_elements': np.array([100, 200, 300])},
        'expected': {'diagonal_matrix': np.diag([100, 200, 300])}
    }
])
# Update values in `conditional_array` to `new_value` where the condition `np.where_condition` is satisfied, and save it in `updated_array`.
check_numpy_51 = input_output_checker([
    {
        'input': {'conditional_array': np.array([1, 2, 3, 4, 5]), 'np_where_condition': np.array([True, False, True, False, True]), 'new_value': 10},
        'expected': {'updated_array': np.array([10, 2, 10, 4, 10])}
    },
    {
        'input': {'conditional_array': np.array([10, 20, 30, 40, 50]), 'np_where_condition': np.array([False, True, False, True, False]), 'new_value': 100},
        'expected': {'updated_array': np.array([10, 100, 30, 100, 50])}
    },
    {
        'input': {'conditional_array': np.array([100, 200, 300, 400, 500]), 'np_where_condition': np.array([True, False, True, False, True]), 'new_value': 1000},
        'expected': {'updated_array': np.array([1000, 200, 1000, 400, 1000])}
    }
])
# Given two arrays `max_array_a` and `max_array_b`, compute the element-wise maximum and store it in `element_max`.
check_numpy_52 = input_output_checker([
    {
        'input': {'max_array_a': np.array([1, 2, 3, 4, 5]), 'max_array_b': np.array([5, 4, 3, 2, 1])},
        'expected': {'element_max': np.array([5, 4, 3, 4, 5])}
    },
    {
        'input': {'max_array_a': np.array([10, 20, 30, 40, 50]), 'max_array_b': np.array([50, 40, 30, 20, 10])},
        'expected': {'element_max': np.array([50, 40, 30, 40, 50])}
    },
    {
        'input': {'max_array_a': np.array([100, 200, 300, 400, 500]), 'max_array_b': np.array([500, 400, 300, 200, 100])},
        'expected': {'element_max': np.array([500, 400, 300, 400, 500])}
    }
])
# Calculate the cumulative sum of elements in `cumsum_array` and assign it to `cumulative_sum`.
check_numpy_53 = input_output_checker([
    {
        'input': {'cumsum_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'cumulative_sum': np.array([1, 3, 6, 10, 15])}
    },
    {
        'input': {'cumsum_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'cumulative_sum': np.array([10, 30, 60, 100, 150])}
    },
    {
        'input': {'cumsum_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'cumulative_sum': np.array([100, 300, 600, 1000, 1500])}
    }
])
# Extract unique elements from the NumPy array `unique_array` and store them in `unique_elements`.
check_numpy_54 = input_output_checker([
    {
        'input': {'unique_array': np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])},
        'expected': {'unique_elements': np.array([1, 2, 3, 4, 5])}
    },
    {
        'input': {'unique_array': np.array([10, 20, 30, 40, 50, 10, 20, 30, 40, 50])},
        'expected': {'unique_elements': np.array([10, 20, 30, 40, 50])}
    },
    {
        'input': {'unique_array': np.array([100, 200, 300, 400, 500, 100, 200, 300, 400, 500])},
        'expected': {'unique_elements': np.array([100, 200, 300, 400, 500])}
    }
])
# Sort the array `sort_array` in ascending order and assign it to `sorted_array`.
check_numpy_55 = input_output_checker([
    {
        'input': {'sort_array': np.array([5, 4, 3, 2, 1])},
        'expected': {'sorted_array': np.array([1, 2, 3, 4, 5])}
    },
    {
        'input': {'sort_array': np.array([50, 40, 30, 20, 10])},
        'expected': {'sorted_array': np.array([10, 20, 30, 40, 50])}
    },
    {
        'input': {'sort_array': np.array([500, 400, 300, 200, 100])},
        'expected': {'sorted_array': np.array([100, 200, 300, 400, 500])}
    }
])
# Compute the intersection of two arrays `intersect_array1` and `intersect_array2` and save it in `intersection`.
check_numpy_56 = input_output_checker([
    {
        'input': {'intersect_array1': np.array([1, 2, 3, 4, 5]), 'intersect_array2': np.array([5, 4, 3, 2, 1])},
        'expected': {'intersection': np.array([1, 2, 3, 4, 5])}
    },
    {
        'input': {'intersect_array1': np.array([10, 20, 30, 40, 50]), 'intersect_array2': np.array([50, 40, 30, 20, 10])},
        'expected': {'intersection': np.array([10, 20, 30, 40, 50])}
    },
    {
        'input': {'intersect_array1': np.array([100, 200, 300, 400, 500]), 'intersect_array2': np.array([500, 400, 300, 200, 100])},
        'expected': {'intersection': np.array([100, 200, 300, 400, 500])}
    }
])
# Join `join_array1`, `join_array2`, and `join_array3` along a new axis using `np.stack()` and store it in `joined_array`.
check_numpy_57 = input_output_checker([
    {
        'input': {'join_array1': np.array([1, 2, 3]), 'join_array2': np.array([4, 5, 6]), 'join_array3': np.array([7, 8, 9])},
        'expected': {'joined_array': np.stack((np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])))}
    },
    {
        'input': {'join_array1': np.array([10, 20, 30]), 'join_array2': np.array([40, 50, 60]), 'join_array3': np.array([70, 80, 90])},
        'expected': {'joined_array': np.stack((np.array([10, 20, 30]), np.array([40, 50, 60]), np.array([70, 80, 90])))}
    },
    {
        'input': {'join_array1': np.array([100, 200, 300]), 'join_array2': np.array([400, 500, 600]), 'join_array3': np.array([700, 800, 900])},
        'expected': {'joined_array': np.stack((np.array([100, 200, 300]), np.array([400, 500, 600]), np.array([700, 800, 900])))}
    }
])
# Split `split_array` into `num_splits` parts using `np.array_split()` and assign the result to `split_parts`.
check_numpy_58 = input_output_checker([
    {
        'input': {'split_array': np.array([1, 2, 3, 4, 5, 6]), 'num_splits': 3},
        'expected': {'split_parts': np.array_split(np.array([1, 2, 3, 4, 5, 6]), 3)}
    },
    {
        'input': {'split_array': np.array([10, 20, 30, 40, 50, 60]), 'num_splits': 3},
        'expected': {'split_parts': np.array_split(np.array([10, 20, 30, 40, 50, 60]), 3)}
    },
    {
        'input': {'split_array': np.array([100, 200, 300, 400, 500, 600]), 'num_splits': 3},
        'expected': {'split_parts': np.array_split(np.array([100, 200, 300, 400, 500, 600]), 3)}
    }
])
# Count elements in `count_array` that are greater than `threshold` and assign the count to `greater_count`.
check_numpy_59 = input_output_checker([
    {
        'input': {'count_array': np.array([1, 2, 3, 4, 5]), 'threshold': 3},
        'expected': {'greater_count': np.int64(2)}
    },
    {
        'input': {'count_array': np.array([10, 20, 30, 40, 50]), 'threshold': 30},
        'expected': {'greater_count': np.int64(2)}
    },
    {
        'input': {'count_array': np.array([100, 200, 300, 400, 500]), 'threshold': 300},
        'expected': {'greater_count': np.int64(2)}
    }
])
# Rotate the 2D array `rotate_array` 90 degrees counterclockwise using `np.rot90()` and store it in `rotated_array`.
check_numpy_60 = input_output_checker([
    {
        'input': {'rotate_array': np.array([[1, 2], [3, 4]])},
        'expected': {'rotated_array': np.rot90(np.array([[1, 2], [3, 4]]))}
    },
    {
        'input': {'rotate_array': np.array([[10, 20], [30, 40]])},
        'expected': {'rotated_array': np.rot90(np.array([[10, 20], [30, 40]]))}
    },
    {
        'input': {'rotate_array': np.array([[100, 200], [300, 400]])},
        'expected': {'rotated_array': np.rot90(np.array([[100, 200], [300, 400]]))}
    }
])
# Create an array named `random_float_array` with shape `float_shape` containing random floats between 0 and 1.
check_numpy_61 = input_output_checker([
    {
        'input': {'float_shape': (2, 3)},
        'expected': {'random_float_array': np.random.rand(2, 3)}
    },
    {
        'input': {'float_shape': (3, 4)},
        'expected': {'random_float_array': np.random.rand(3, 4)}
    },
    {
        'input': {'float_shape': (4, 5)},
        'expected': {'random_float_array': np.random.rand(4, 5)}
    }
])
# Compute the median of `median_array` and store it in `median_value`.
check_numpy_62 = input_output_checker([
    {
        'input': {'median_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'median_value': np.float64(3.0)}
    },
    {
        'input': {'median_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'median_value': np.float64(30.0)}
    },
    {
        'input': {'median_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'median_value': np.float64(300.0)}
    }
])
# Given a complex NumPy array `complex_array`, extract its real and imaginary parts into `real_part` and `imag_part`.
check_numpy_63 = input_output_checker([
    {
        'input': {'complex_array': np.array([1 + 2j, 3 + 4j, 5 + 6j])},
        'expected': {'real_part': np.array([1, 3, 5]), 'imag_part': np.array([2, 4, 6])}
    },
    {
        'input': {'complex_array': np.array([10 + 20j, 30 + 40j, 50 + 60j])},
        'expected': {'real_part': np.array([10, 30, 50]), 'imag_part': np.array([20, 40, 60])}
    },
    {
        'input': {'complex_array': np.array([100 + 200j, 300 + 400j, 500 + 600j])},
        'expected': {'real_part': np.array([100, 300, 500]), 'imag_part': np.array([200, 400, 600])}
    }
])
# Normalize the array `norm_array` to have values between 0 and 1, storing the result in `normalized_array`.
check_numpy_64 = input_output_checker([
    {
        'input': {'norm_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'normalized_array': np.array([0., 0.25, 0.5, 0.75, 1.])}
    },
    {
        'input': {'norm_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'normalized_array': np.array([0., 0.25, 0.5, 0.75, 1.])}
    },
    {
        'input': {'norm_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'normalized_array': np.array([0., 0.25, 0.5, 0.75, 1.])}
    }
])
# Replace negative elements in `replace_array` with `new_value` using `np.where()` and store in `replaced_array`.
check_numpy_65 = input_output_checker([
    {
        'input': {'replace_array': np.array([1, -2, 3, -4, 5]), 'new_value': 0},
        'expected': {'replaced_array': np.where(np.array([1, -2, 3, -4, 5]) < 0, 0, np.array([1, -2, 3, -4, 5]))}
    },
    {
        'input': {'replace_array': np.array([10, -20, 30, -40, 50]), 'new_value': 0},
        'expected': {'replaced_array': np.where(np.array([10, -20, 30, -40, 50]) < 0, 0, np.array([10, -20, 30, -40, 50]))}
    },
    {
        'input': {'replace_array': np.array([100, -200, 300, -400, 500]), 'new_value': 0},
        'expected': {'replaced_array': np.where(np.array([100, -200, 300, -400, 500]) < 0, 0, np.array([100, -200, 300, -400, 500]))}
    }
])
# Calculate the row-wise total sum for `axis_sum_array` and assign the output to `row_sums`.
check_numpy_66 = input_output_checker([
    {
        'input': {'axis_sum_array': np.array([[1, 2], [3, 4], [5, 6]])},
        'expected': {'row_sums': np.sum(np.array([[1, 2], [3, 4], [5, 6]]), axis=1)}
    },
    {
        'input': {'axis_sum_array': np.array([[10, 20], [30, 40], [50, 60]])},
        'expected': {'row_sums': np.sum(np.array([[10, 20], [30, 40], [50, 60]]), axis=1)}
    },
    {
        'input': {'axis_sum_array': np.array([[100, 200], [300, 400], [500, 600]])},
        'expected': {'row_sums': np.sum(np.array([[100, 200], [300, 400], [500, 600]]), axis=1)}
    }
])
# Produce a matrix `random_matrix` with `matrix_shape` dimensions and random integers from 0 to 100.
check_numpy_67 = input_output_checker([
    {
        'input': {'matrix_shape': (2, 3)},
        'expected': {'random_matrix': (2, 3), "random_values": np.False_}
    },
    {
        'input': {'matrix_shape': (3, 4)},
        'expected': {'random_matrix': (3, 4), "random_values": np.False_}
    },
    {
        'input': {'matrix_shape': (4, 5)},
        'expected': {'random_matrix': (4, 5), "random_values": np.False_}
    }
])
# Raise each element in `base_power_array` to a power specified in `exp_power_array`, element-wise, and store in `powered_array`.
check_numpy_68 = input_output_checker([
    {
        'input': {'base_power_array': np.array([1, 2, 3, 4, 5]), 'exp_power_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'powered_array': np.array([1, 4, 27, 256, 3125])}
    },
    {
        'input': {'base_power_array': np.array([10, 20, 30, 40, 50]), 'exp_power_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'powered_array': np.array([10, 400, 27000, 2560000, 312500000])}
    },
    {
        'input': {'base_power_array': np.array([100, 200, 300, 400, 500]), 'exp_power_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'powered_array': np.array([100, 40000, 2700000, 256000000, 31250000000])}
    }
])
# Detect NaN elements within `nan_array` using `np.isnan()` and assign the position to `nan_indices`.
check_numpy_69 = input_output_checker([
    {
        'input': {'nan_array': np.array([1, np.nan, 3, 4, 5])},
        'expected': {'nan_indices': np.isnan(np.array([1, np.nan, 3, 4, 5]))}
    },
    {
        'input': {'nan_array': np.array([10, np.nan, 30, 40, 50])},
        'expected': {'nan_indices': np.isnan(np.array([10, np.nan, 30, 40, 50]))}
    },
    {
        'input': {'nan_array': np.array([100, np.nan, 300, 400, 500])},
        'expected': {'nan_indices': np.isnan(np.array([100, np.nan, 300, 400, 500]))}
    }
])
# Replace `NaN` values in `nan_replace_array` with `specific_value` and create `nan_replaced_array`.
check_numpy_70 = input_output_checker([
    {
        'input': {'nan_replace_array': np.array([1, np.nan, 3, 4, 5]), 'specific_value': 0},
        'expected': {'nan_replaced_array': np.nan_to_num(np.array([1, np.nan, 3, 4, 5]), nan=0)}
    },
    {
        'input': {'nan_replace_array': np.array([10, np.nan, 30, 40, 50]), 'specific_value': 0},
        'expected': {'nan_replaced_array': np.nan_to_num(np.array([10, np.nan, 30, 40, 50]), nan=0)}
    },
    {
        'input': {'nan_replace_array': np.array([100, np.nan, 300, 400, 500]), 'specific_value': 0},
        'expected': {'nan_replaced_array': np.nan_to_num(np.array([100, np.nan, 300, 400, 500]), nan=0)}
    }
])
# Construct an upper triangular version of `triangular_matrix` using `np.triu()`.
check_numpy_71 = input_output_checker([
    {
        'input': {'triangular_matrix': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'upper_triangular': np.triu(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))}
    },
    {
        'input': {'triangular_matrix': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'upper_triangular': np.triu(np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]))}
    },
    {
        'input': {'triangular_matrix': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'upper_triangular': np.triu(np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]]))}
    }
])
# Calculate the `percentile_value` percentile of elements in `percentile_array` and set the result to `percentile_result`.
check_numpy_72 = input_output_checker([
    {
        'input': {'percentile_array': np.array([1, 2, 3, 4, 5]), 'percentile_value': 50},
        'expected': {'percentile_result': np.percentile(np.array([1, 2, 3, 4, 5]), 50)}
    },
    {
        'input': {'percentile_array': np.array([10, 20, 30, 40, 50]), 'percentile_value': 50},
        'expected': {'percentile_result': np.percentile(np.array([10, 20, 30, 40, 50]), 50)}
    },
    {
        'input': {'percentile_array': np.array([100, 200, 300, 400, 500]), 'percentile_value': 50},
        'expected': {'percentile_result': np.percentile(np.array([100, 200, 300, 400, 500]), 50)}
    }
])
# Calculate the trace (sum of diagonals) of the matrix `trace_matrix` using `np.trace()`.
check_numpy_73 = input_output_checker([
    {
        'input': {'trace_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'trace_value': np.array([[1, 2], [3, 4]]).trace()}
    },
    {
        'input': {'trace_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'trace_value': np.array([[10, 20], [30, 40]]).trace()}
    },
    {
        'input': {'trace_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'trace_value': np.array([[100, 200], [300, 400]]).trace()}
    }
])
# Compute the index of the maximum value in `index_max_array` and store it in `max_index`.
check_numpy_74 = input_output_checker([
    {
        'input': {'index_max_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'max_index': np.argmax(np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'index_max_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'max_index': np.argmax(np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'index_max_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'max_index': np.argmax(np.array([100, 200, 300, 400, 500]))}
    }
])
# Find the index of the minimum value in `index_min_array` and assign it to `min_index`.
check_numpy_75 = input_output_checker([
    {
        'input': {'index_min_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'min_index': np.argmin(np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'index_min_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'min_index': np.argmin(np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'index_min_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'min_index': np.argmin(np.array([100, 200, 300, 400, 500]))}
    }
])
# Perform an element-wise comparison of `compare_array1` and `compare_array2` using `np.equal()` and assign to `comparison_result`.
check_numpy_76 = input_output_checker([
    {
        'input': {'compare_array1': np.array([1, 2, 3, 4, 5]), 'compare_array2': np.array([5, 4, 3, 2, 1])},
        'expected': {'comparison_result': np.equal(np.array([1, 2, 3, 4, 5]), np.array([5, 4, 3, 2, 1]))}
    },
    {
        'input': {'compare_array1': np.array([10, 20, 30, 40, 50]), 'compare_array2': np.array([50, 40, 30, 20, 10])},
        'expected': {'comparison_result': np.equal(np.array([10, 20, 30, 40, 50]), np.array([50, 40, 30, 20, 10]))}
    },
    {
        'input': {'compare_array1': np.array([100, 200, 300, 400, 500]), 'compare_array2': np.array([500, 400, 300, 200, 100])},
        'expected': {'comparison_result': np.equal(np.array([100, 200, 300, 400, 500]), np.array([500, 400, 300, 200, 100]))}
    }
])
# Perform the matrix multiplication between two arrays `mat_mult_a` and `mat_mult_b` and store the result in `matrix_product`.
check_numpy_77 = input_output_checker([
    {
        'input': {'mat_mult_a': np.array([[1, 2], [3, 4]]), 'mat_mult_b': np.array([[5, 6], [7, 8]])},
        'expected': {'matrix_product': np.matmul(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))}
    },
    {
        'input': {'mat_mult_a': np.array([[10, 20], [30, 40]]), 'mat_mult_b': np.array([[50, 60], [70, 80]])},
        'expected': {'matrix_product': np.matmul(np.array([[10, 20], [30, 40]]), np.array([[50, 60], [70, 80]]))}
    },
    {
        'input': {'mat_mult_a': np.array([[100, 200], [300, 400]]), 'mat_mult_b': np.array([[500, 600], [700, 800]])},
        'expected': {'matrix_product': np.matmul(np.array([[100, 200], [300, 400]]), np.array([[500, 600], [700, 800]]))}
    }
])
# Extract the diagonal of `diag_matrix` using `np.diag()` and store it in `matrix_diagonal`.
check_numpy_78 = input_output_checker([
    {
        'input': {'diag_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'matrix_diagonal': np.diag(np.array([[1, 2], [3, 4]]))}
    },
    {
        'input': {'diag_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'matrix_diagonal': np.diag(np.array([[10, 20], [30, 40]]))}
    },
    {
        'input': {'diag_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'matrix_diagonal': np.diag(np.array([[100, 200], [300, 400]]))}
    }
])
# Clip `clip_array` such that all its values fall between `min_clip` and `max_clip`, saving the result in `clipped_array`.
check_numpy_79 = input_output_checker([
    {
        'input': {'clip_array': np.array([1, 2, 3, 4, 5]), 'min_clip': 2, 'max_clip': 4},
        'expected': {'clipped_array': np.clip(np.array([1, 2, 3, 4, 5]), 2, 4)}
    },
    {
        'input': {'clip_array': np.array([10, 20, 30, 40, 50]), 'min_clip': 20, 'max_clip': 40},
        'expected': {'clipped_array': np.clip(np.array([10, 20, 30, 40, 50]), 20, 40)}
    },
    {
        'input': {'clip_array': np.array([100, 200, 300, 400, 500]), 'min_clip': 200, 'max_clip': 400},
        'expected': {'clipped_array': np.clip(np.array([100, 200, 300, 400, 500]), 200, 400)}
    }
])
# Flip `flip_array` along the specified axis `flip_axis` using `np.flip()` and assign to `flipped_array`.
check_numpy_80 = input_output_checker([
    {
        'input': {'flip_array': np.array([[1, 2], [3, 4]]), 'flip_axis': 0},
        'expected': {'flipped_array': np.flip(np.array([[1, 2], [3, 4]]), axis=0)}
    },
    {
        'input': {'flip_array': np.array([[10, 20], [30, 40]]), 'flip_axis': 1},
        'expected': {'flipped_array': np.flip(np.array([[10, 20], [30, 40]]), axis=1)}
    },
    {
        'input': {'flip_array': np.array([[100, 200], [300, 400]]), 'flip_axis': 0},
        'expected': {'flipped_array': np.flip(np.array([[100, 200], [300, 400]]), axis=0)}
    }
])
# Simulate rolling a six-sided die `num_rolls` times to generate an array `dice_rolls`.
check_numpy_81 = input_output_checker([
    {
        'input': {'num_rolls': 10},
        'expected': {'dice_rolls': np.random.randint(1, 7, 10)}
    },
    {
        'input': {'num_rolls': 20},
        'expected': {'dice_rolls': np.random.randint(1, 7, 20)}
    },
    {
        'input': {'num_rolls': 30},
        'expected': {'dice_rolls': np.random.randint(1, 7, 30)}
    }
])
# Given two arrays `logical_array_a` and `logical_array_b`, perform a logical `and` operation and save result in `logical_and_result`.
check_numpy_82 = input_output_checker([
    {
        'input': {'logical_array_a': np.array([True, False, True, False, True]), 'logical_array_b': np.array([True, True, False, False, True])},
        'expected': {'logical_and_result': np.logical_and(np.array([True, False, True, False, True]), np.array([True, True, False, False, True]))}
    },
    {
        'input': {'logical_array_a': np.array([False, True, False, True, False]), 'logical_array_b': np.array([True, False, True, False, True])},
        'expected': {'logical_and_result': np.logical_and(np.array([False, True, False, True, False]), np.array([True, False, True, False, True]))}
    },
    {
        'input': {'logical_array_a': np.array([True, False, True, False, True]), 'logical_array_b': np.array([False, True, False, True, False])},
        'expected': {'logical_and_result': np.logical_and(np.array([True, False, True, False, True]), np.array([False, True, False, True, False]))}
    }
])
# Reverse the elements in `reverse_array` and store the result in `reversed_array`.
check_numpy_83 = input_output_checker([
    {
        'input': {'reverse_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'reversed_array': np.flip(np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'reverse_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'reversed_array': np.flip(np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'reverse_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'reversed_array': np.flip(np.array([100, 200, 300, 400, 500]))}
    }
])
# Compute the cross-product of vectors `vector_a` and `vector_b` and store it in `cross_product_result`.
check_numpy_84 = input_output_checker([
    {
        'input': {'vector_a': np.array([1, 0, 0]), 'vector_b': np.array([0, 1, 0])},
        'expected': {'cross_product_result': np.cross(np.array([1, 0, 0]), np.array([0, 1, 0]))}
    },
    {
        'input': {'vector_a': np.array([0, 1, 0]), 'vector_b': np.array([0, 0, 1])},
        'expected': {'cross_product_result': np.cross(np.array([0, 1, 0]), np.array([0, 0, 1]))}
    },
    {
        'input': {'vector_a': np.array([1, 0, 0]), 'vector_b': np.array([0, 0, 1])},
        'expected': {'cross_product_result': np.cross(np.array([1, 0, 0]), np.array([0, 0, 1]))}
    }
])
# Use `np.vstack()` to vertically stack `vert_stack_a` and `vert_stack_b` and assign to `vertically_stacked`.
check_numpy_85 = input_output_checker([
    {
        'input': {'vert_stack_a': np.array([1, 2, 3]), 'vert_stack_b': np.array([4, 5, 6])},
        'expected': {'vertically_stacked': np.vstack((np.array([1, 2, 3]), np.array([4, 5, 6])))}
    },
    {
        'input': {'vert_stack_a': np.array([10, 20, 30]), 'vert_stack_b': np.array([40, 50, 60])},
        'expected': {'vertically_stacked': np.vstack((np.array([10, 20, 30]), np.array([40, 50, 60])))}
    },
    {
        'input': {'vert_stack_a': np.array([100, 200, 300]), 'vert_stack_b': np.array([400, 500, 600])},
        'expected': {'vertically_stacked': np.vstack((np.array([100, 200, 300]), np.array([400, 500, 600])))}
    }
])
# Create a `checkered_matrix` of size `check_size` with alternating zeros and ones.
check_numpy_86 = input_output_checker([
    {
        'input': {'check_size': (3, 3)},
        'expected': {'checkered_matrix': np.kron([[1, 0], [0, 1]], np.ones((3, 3)))}
    },
    {
        'input': {'check_size': (4, 4)},
        'expected': {'checkered_matrix': np.kron([[1, 0], [0, 1]], np.ones((4, 4)))}
    },
    {
        'input': {'check_size': (5, 5)},
        'expected': {'checkered_matrix': np.kron([[1, 0], [0, 1]], np.ones((5, 5)))}
    }
])
# Determine the rank of `rank_matrix` using `np.linalg.matrix_rank()`.
check_numpy_87 = input_output_checker([
    {
        'input': {'rank_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'matrix_rank': np.linalg.matrix_rank(np.array([[1, 2], [3, 4]]))}
    },
    {
        'input': {'rank_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'matrix_rank': np.linalg.matrix_rank(np.array([[10, 20], [30, 40]]))}
    },
    {
        'input': {'rank_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'matrix_rank': np.linalg.matrix_rank(np.array([[100, 200], [300, 400]]))}
    }
])
# Extract all non-diagonal elements from `non_diag_matrix` and store them in `off_diagonal`.
check_numpy_88 = input_output_checker([
    {
        'input': {'non_diag_matrix': np.array([[1, 2], [3, 4]])},
        'expected': {'off_diagonal': np.delete(np.array([[1, 2], [3, 4]]), [0, 3])}
    },
    {
        'input': {'non_diag_matrix': np.array([[10, 20], [30, 40]])},
        'expected': {'off_diagonal': np.delete(np.array([[10, 20], [30, 40]]), [0, 3])}
    },
    {
        'input': {'non_diag_matrix': np.array([[100, 200], [300, 400]])},
        'expected': {'off_diagonal': np.delete(np.array([[100, 200], [300, 400]]), [0, 3])}
    }
])
# Create a boolean mask `boolean_mask` for the array `mask_less_array` with elements less than `threshold_value`.
check_numpy_89 = input_output_checker([
    {
        'input': {'mask_less_array': np.array([1, 2, 3, 4, 5]), 'threshold_value': 3},
        'expected': {'boolean_mask': np.array([True, True, False, False, False])}
    },
    {
        'input': {'mask_less_array': np.array([10, 20, 30, 40, 50]), 'threshold_value': 30},
        'expected': {'boolean_mask': np.array([True, True, False, False, False])}
    },
    {
        'input': {'mask_less_array': np.array([100, 200, 300, 400, 500]), 'threshold_value': 300},
        'expected': {'boolean_mask': np.array([True, True, False, False, False])}
    }
])
# Compute the cumulative product of `cumprod_array` and assign the result to `cumulative_product`.
check_numpy_90 = input_output_checker([
    {
        'input': {'cumprod_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'cumulative_product': np.cumprod(np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'cumprod_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'cumulative_product': np.cumprod(np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'cumprod_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'cumulative_product': np.cumprod(np.array([100, 200, 300, 400, 500]))}
    }
])
# Calculate the absolute differences between `abs_diff_a1` and `abs_diff_a2`, storing the result in `absolute_diff`.
check_numpy_91 = input_output_checker([
    {
        'input': {'abs_diff_a1': np.array([1, 2, 3, 4, 5]), 'abs_diff_a2': np.array([5, 4, 3, 2, 1])},
        'expected': {'absolute_diff': np.abs(np.array([1, 2, 3, 4, 5]) - np.array([5, 4, 3, 2, 1]))}
    },
    {
        'input': {'abs_diff_a1': np.array([10, 20, 30, 40, 50]), 'abs_diff_a2': np.array([50, 40, 30, 20, 10])},
        'expected': {'absolute_diff': np.abs(np.array([10, 20, 30, 40, 50]) - np.array([50, 40, 30, 20, 10]))}
    },
    {
        'input': {'abs_diff_a1': np.array([100, 200, 300, 400, 500]), 'abs_diff_a2': np.array([500, 400, 300, 200, 100])},
        'expected': {'absolute_diff': np.abs(np.array([100, 200, 300, 400, 500]) - np.array([500, 400, 300, 200, 100]))}
    }
])
# Check if `elem_equal_a` and `elem_equal_b` are element-wise equal and store the boolean result in `elementwise_equality`.
check_numpy_92 = input_output_checker([
    {
        'input': {'elem_equal_a': np.array([1, 2, 3, 4, 5]), 'elem_equal_b': np.array([1, 2, 3, 4, 5])},
        'expected': {'elementwise_equality': np.array_equal(np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'elem_equal_a': np.array([10, 20, 30, 40, 50]), 'elem_equal_b': np.array([10, 20, 30, 40, 50])},
        'expected': {'elementwise_equality': np.array_equal(np.array([10, 20, 30, 40, 50]), np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'elem_equal_a': np.array([100, 200, 300, 400, 500]), 'elem_equal_b': np.array([100, 200, 300, 400, 500])},
        'expected': {'elementwise_equality': np.array_equal(np.array([100, 200, 300, 400, 500]), np.array([100, 200, 300, 400, 500]))}
    }
])
# Create `filtered_within_range` by extracting values from `range_filter_array` that are between `lower_bound` and `upper_bound`.
check_numpy_93 = input_output_checker([
    {
        'input': {'range_filter_array': np.array([1, 2, 3, 4, 5]), 'lower_bound': 2, 'upper_bound': 4},
        'expected': {'filtered_within_range': np.extract((np.array([1, 2, 3, 4, 5]) >= 2) & (np.array([1, 2, 3, 4, 5]) <= 4), np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'range_filter_array': np.array([10, 20, 30, 40, 50]), 'lower_bound': 20, 'upper_bound': 40},
        'expected': {'filtered_within_range': np.extract((np.array([10, 20, 30, 40, 50]) >= 20) & (np.array([10, 20, 30, 40, 50]) <= 40), np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'range_filter_array': np.array([100, 200, 300, 400, 500]), 'lower_bound': 200, 'upper_bound': 400},
        'expected': {'filtered_within_range': np.extract((np.array([100, 200, 300, 400, 500]) >= 200) & (np.array([100, 200, 300, 400, 500]) <= 400), np.array([100, 200, 300, 400, 500]))}
    }
])
# Multiply a 1D array `broad_1d` with each row of a 2D array `broad_2d`, and store the result in `broadcast_mult_result`.
check_numpy_94 = input_output_checker([
    {
        'input': {'broad_1d': np.array([1, 2, 3]), 'broad_2d': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'broadcast_mult_result': np.array([1, 4, 9]) * np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}
    },
    {
        'input': {'broad_1d': np.array([10, 20, 30]), 'broad_2d': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'broadcast_mult_result': np.array([10, 40, 90]) * np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])}
    },
    {
        'input': {'broad_1d': np.array([100, 200, 300]), 'broad_2d': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'broadcast_mult_result': np.array([100, 400, 900]) * np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])}
    }
])
# Multiply a 1D array `broad_1d` with each row of a 2D array `broad_2d`, and store the result in `broadcast_mult_result`.
check_numpy_95 = input_output_checker([
    {
        'input': {'broad_1d': np.array([1, 2, 3]), 'broad_2d': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'broadcast_mult_result': np.array([1, 2, 3]) * np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}
    },
    {
        'input': {'broad_1d': np.array([10, 20, 30]), 'broad_2d': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'broadcast_mult_result': np.array([10, 20, 30]) * np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])}
    },
    {
        'input': {'broad_1d': np.array([100, 200, 300]), 'broad_2d': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'broadcast_mult_result': np.array([100, 200, 300]) * np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])}
    }
])
# Apply logarithm base 10 to `log10_array` using `np.log10()` and save the result in `log10_result`.
check_numpy_96 = input_output_checker([
    {
        'input': {'log10_array': np.array([1, 2, 3, 4, 5])},
        'expected': {'log10_result': np.log10(np.array([1, 2, 3, 4, 5]))}
    },
    {
        'input': {'log10_array': np.array([10, 20, 30, 40, 50])},
        'expected': {'log10_result': np.log10(np.array([10, 20, 30, 40, 50]))}
    },
    {
        'input': {'log10_array': np.array([100, 200, 300, 400, 500])},
        'expected': {'log10_result': np.log10(np.array([100, 200, 300, 400, 500]))}
    }
])
# Form a lower triangular matrix from `lower_tri_matrix` using `np.tril()`.
check_numpy_97 = input_output_checker([
    {
        'input': {'lower_tri_matrix': np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])},
        'expected': {'lower_triangular': np.tril(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))}
    },
    {
        'input': {'lower_tri_matrix': np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])},
        'expected': {'lower_triangular': np.tril(np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]))}
    },
    {
        'input': {'lower_tri_matrix': np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])},
        'expected': {'lower_triangular': np.tril(np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]]))}
    }
])
# Determine if there are any `True` elements in `bool_array`, assigning the result to `any_true`.
check_numpy_98 = input_output_checker([
    {
        'input': {'bool_array': np.array([True, False, True, False, True])},
        'expected': {'any_true': np.any(np.array([True, False, True, False, True]))}
    },
    {
        'input': {'bool_array': np.array([False, True, False, True, False])},
        'expected': {'any_true': np.any(np.array([False, True, False, True, False]))}
    },
    {
        'input': {'bool_array': np.array([True, False, True, False, True])},
        'expected': {'any_true': np.any(np.array([True, False, True, False, True]))}
    }
])
# Check if all elements in `bool_check_array` are `True`, and store the result in `all_true`.
check_numpy_99 = input_output_checker([
    {
        'input': {'bool_check_array': np.array([True, False, True, False, True])},
        'expected': {'all_true': np.all(np.array([True, False, True, False, True]))}
    },
    {
        'input': {'bool_check_array': np.array([False, True, False, True, False])},
        'expected': {'all_true': np.all(np.array([False, True, False, True, False]))}
    },
    {
        'input': {'bool_check_array': np.array([True, False, True, False, True])},
        'expected': {'all_true': np.all(np.array([True, False, True, False, True]))}
    }
])
# Given two vectors `cos_vector_a` and `cos_vector_b`, calculate the cosine similarity and store it in `cosine_similarity`.
check_numpy_100 = input_output_checker([
    {
        'input': {'cos_vector_a': np.array([1, 0, -1]), 'cos_vector_b': np.array([-1, 0, 1])},
        'expected': {'cosine_similarity': np.dot(np.array([1, 0, -1]), np.array([-1, 0, 1])) / (np.linalg.norm(np.array([1, 0, -1])) * np.linalg.norm(np.array([-1, 0, 1])))}
    },
    {
        'input': {'cos_vector_a': np.array([0, 1, 0]), 'cos_vector_b': np.array([1, 0, 0])},
        'expected': {'cosine_similarity': np.dot(np.array([0, 1, 0]), np.array([1, 0, 0])) / (np.linalg.norm(np.array([0, 1, 0])) * np.linalg.norm(np.array([1, 0, 0])))}
    },
    {
        'input': {'cos_vector_a': np.array([1, 1, 1]), 'cos_vector_b': np.array([1, 1, 1])},
        'expected': {'cosine_similarity': np.dot(np.array([1, 1, 1]), np.array([1, 1, 1])) / (np.linalg.norm(np.array([1, 1, 1])) * np.linalg.norm(np.array([1, 1, 1])))}
    }
])
# Create a function named `reverse_sort_numpy` that takes a NumPy array `arr`, reverses it, removes duplicate elements using NumPy, and returns a sorted version of the array.
check_numpy_101 = functions_input_output_checker({
    'reverse_sort_numpy': [
        {
            'input': {'arr': np.array([1, 2, 3, 4, 5])},
            'expected': {'output': np.sort(np.unique(np.array([1, 2, 3, 4, 5])[::-1]))}
        },
        {
            'input': {'arr': np.array([10, 20, 30, 40, 50])},
            'expected': {'output': np.sort(np.unique(np.array([10, 20, 30, 40, 50])[::-1]))}
        },
        {
            'input': {'arr': np.array([100, 200, 300, 400, 500])},
            'expected': {'output': np.sort(np.unique(np.array([100, 200, 300, 400, 500])[::-1]))}
        }
    ]
})
# Write a function `normalize_scale_numpy` that takes a NumPy array `arr` and a range `min_val`, `max_val`. Use NumPy to normalize the array to the range [0, 1], then scale it to the given range, and return the resulting array.
check_numpy_102 = functions_input_output_checker({
    'normalize_scale_numpy': [
        {
            'input': {'arr': np.array([1, 2, 3, 4, 5]), 'min_val': 0, 'max_val': 1},
            'expected': {'output': ((np.array([1, 2, 3, 4, 5]) - np.min(np.array([1, 2, 3, 4, 5]))) / (np.max(np.array([1, 2, 3, 4, 5])) - np.min(np.array([1, 2, 3, 4, 5])))) * (1 - 0) + 0}
        },
        {
            'input': {'arr': np.array([10, 20, 30, 40, 50]), 'min_val': 0, 'max_val': 1},
            'expected': {'output': ((np.array([10, 20, 30, 40, 50]) - np.min(np.array([10, 20, 30, 40, 50]))) / (np.max(np.array([10, 20, 30, 40, 50])) - np.min(np.array([10, 20, 30, 40, 50])))) * (1 - 0) + 0}
        },
        {
            'input': {'arr': np.array([100, 200, 300, 400, 500]), 'min_val': 0, 'max_val': 1},
            'expected': {'output': ((np.array([100, 200, 300, 400, 500]) - np.min(np.array([100, 200, 300, 400, 500]))) / (np.max(np.array([100, 200, 300, 400, 500])) - np.min(np.array([100, 200, 300, 400, 500])))) * (1 - 0) + 0}
        }
    ]
})# Develop a function `filter_average_numpy` that takes a NumPy array `data` and a threshold `limit`. Use NumPy to filter elements greater than `limit`, compute their average, and return this average.
check_numpy_103 = functions_input_output_checker({
    'filter_average_numpy': [
        {
            'input': {'data': np.array([1, 2, 3, 4, 5]), 'limit': 3},
            'expected': {'output': np.mean(np.array([4, 5]))}
        },
        {
            'input': {'data': np.array([10, 20, 30, 40, 50]), 'limit': 30},
            'expected': {'output': np.mean(np.array([40, 50]))}
        },
        {
            'input': {'data': np.array([100, 200, 300, 400, 500]), 'limit': 200},
            'expected': {'output': np.mean(np.array([300, 400, 500]))}
        }
    ]
})
# Create a function `capitalize_count_numpy` that converts a NumPy array of strings `sentence_array` to capitalize each string's first letter, counts the number of elements, and returns a tuple containing the modified array and the count.
check_numpy_104 = functions_input_output_checker({
    'capitalize_count_numpy': [
        {
            'input': {'sentence_array': np.array(['hello', 'world', 'python', 'numpy'])},
            'expected': {'output': (np.array(['Hello', 'World', 'Python', 'Numpy']), 4)}
        },
        {
            'input': {'sentence_array': np.array(['data', 'science', 'machine', 'learning'])},
            'expected': {'output': (np.array(['Data', 'Science', 'Machine', 'Learning']), 4)}
        },
        {
            'input': {'sentence_array': np.array(['deep', 'learning', 'artificial', 'intelligence'])},
            'expected': {'output': (np.array(['Deep', 'Learning', 'Artificial', 'Intelligence']), 4)}
        }
    ]
})
# Implement a function `clean_categorize_numpy` that processes a NumPy array of strings `items` by stripping spaces and converting to lowercase with NumPy operations, classifying them into 'short' if under 5 characters or 'long' otherwise, returning the counts in a dictionary.
check_numpy_105 = functions_input_output_checker({
    'clean_categorize_numpy': [
        {
            'input': {'items': np.array(['  apple', 'Banana ', '  orange', '  pear  '])},
            'expected': {'output': {'short': 2, 'long': 2}}
        },
        {
            'input': {'items': np.array(['  cat', 'dog ', '  bird', '  fish  '])},
            'expected': {'output': {'short': 2, 'long': 2}}
        },
        {
            'input': {'items': np.array(['  car', 'bus ', '  train', '  plane  '])},
            'expected': {'output': {'short': 2, 'long': 2}}
        }
    ]
})
# Write a function `remove_outliers_stats_numpy` that takes a NumPy array `num_array`, removes outliers more than two standard deviations from the mean using NumPy, and returns a dictionary with 'mean', 'std', and 'filtered' keys.
check_numpy_106 = functions_input_output_checker({
    'remove_outliers_stats_numpy': [
        {
            'input': {'num_array': np.array([10, 12, 12, 13, 12, 100])},
            'expected': {'output': {
                'mean': np.mean(np.array([10, 12, 12, 13, 12])),
                'std': np.std(np.array([10, 12, 12, 13, 12])),
                'filtered': np.array([10, 12, 12, 13, 12])
            }}
        },
        {
            'input': {'num_array': np.array([5, 6, 7, 8, 1000])},
            'expected': {'output': {
                'mean': np.mean(np.array([5, 6, 7, 8])),
                'std': np.std(np.array([5, 6, 7, 8])),
                'filtered': np.array([5, 6, 7, 8])
            }}
        },
        {
            'input': {'num_array': np.array([15, 16, 15, 14, 15, -300])},
            'expected': {'output': {
                'mean': np.mean(np.array([15, 16, 15, 14, 15])),
                'std': np.std(np.array([15, 16, 15, 14, 15])),
                'filtered': np.array([15, 16, 15, 14, 15])
            }}
        }
    ]
})
# Create a function `unique_sorted_numpy` that accepts a NumPy array `word_arr`. Use NumPy to remove duplicates, sort them alphabetically, and return the sorted array.
check_numpy_107 = functions_input_output_checker({
    'unique_sorted_numpy': [
        {
            'input': {'word_arr': np.array(['banana', 'apple', 'orange', 'banana'])},
            'expected': {'output': np.array(['apple', 'banana', 'orange'])}
        },
        {
            'input': {'word_arr': np.array(['dog', 'cat', 'cat', 'bird'])},
            'expected': {'output': np.array(['bird', 'cat', 'dog'])}
        },
        {
            'input': {'word_arr': np.array(['zebra', 'lion', 'elephant', 'zebra', 'lion'])},
            'expected': {'output': np.array(['elephant', 'lion', 'zebra'])}
        }
    ]
})
# Implement a function `format_join_numpy` that takes a NumPy array of strings `words_array`, uses NumPy to title case each word, filter words less than 4 characters, and joins them with a hyphen, returning the final string.
check_numpy_108 = functions_input_output_checker({
    'format_join_numpy': [
        {
            'input': {'words_array': np.array(['apple', 'not', 'Orange', 'peAR'])},
            'expected': {'output': 'Apple-Orange-Pear'}
        },
        {
            'input': {'words_array': np.array(['hi', 'there', 'WORLD'])},
            'expected': {'output': 'There-World'}
        },
        {
            'input': {'words_array': np.array(['sun', 'moon', 'Star'])},
            'expected': {'output': 'Moon-Star'}
        }
    ]
})
# Write a function `classify_numbers_numpy` that takes a NumPy array `nums`. Use NumPy functions to detect prime numbers and separate them from non-prime numbers, returning both as arrays.
check_numpy_109 = functions_input_output_checker({
    'classify_numbers_numpy': [
        {
            'input': {'nums': np.array([2, 3, 4, 5, 10])},
            'expected': {'output': (np.array([2, 3, 5]), np.array([4, 10]))}
        },
        {
            'input': {'nums': np.array([11, 13, 15, 17, 18])},
            'expected': {'output': (np.array([11, 13, 17]), np.array([15, 18]))}
        },
        {
            'input': {'nums': np.array([1, 19, 20, 23, 24])},
            'expected': {'output': (np.array([19, 23]), np.array([1, 20, 24]))}
        }
    ]
})
# Develop a function `flatten_filter_numpy` that accepts a NumPy array of arrays `list_of_arrays`, flattens it using NumPy, filters out numbers less than 10 using NumPy, and returns the filtered flat array.
check_numpy_110 = functions_input_output_checker({
    'flatten_filter_numpy': [
        {
            'input': {'list_of_arrays': np.array([[1, 15], [3, 20], [5, 30]])},
            'expected': {'output': np.array([15, 20, 30])}
        },
        {
            'input': {'list_of_arrays': np.array([[5, 7], [10, 11], [9, 13]])},
            'expected': {'output': np.array([10, 11, 13])}
        },
        {
            'input': {'list_of_arrays': np.array([[8, 8], [20, 21]])},
            'expected': {'output': np.array([20, 21])}
        }
    ]
})
# Create a function `square_filter_negatives_numpy` that takes a NumPy array `arr`, squares each element using NumPy array operations, removes negative elements, and returns the resulting array.
check_numpy_111 = functions_input_output_checker({
    'square_filter_negatives_numpy': [
        {
            'input': {'arr': np.array([-3, -1, 0, 2, 4])},
            'expected': {'output': np.array([0, 4, 16])}
        },
        {
            'input': {'arr': np.array([-5, -2, 7, 1])},
            'expected': {'output': np.array([49, 1])}
        },
        {
            'input': {'arr': np.array([3, 2, 1, 0])},
            'expected': {'output': np.array([9, 4, 1, 0])}
        }
    ]
})
# Implement a function `divide_round_numpy` that takes a NumPy array `values` and a divisor `d`. Divide each element using NumPy, round to two decimal places, and return the resulting array.
check_numpy_112 = functions_input_output_checker({
    'divide_round_numpy': [
        {
            'input': {'values': np.array([10, 20, 30, 40]), 'd': 3},
            'expected': {'output': np.round(np.array([10, 20, 30, 40]) / 3, 2)}
        },
        {
            'input': {'values': np.array([100, 200, 300]), 'd': 7},
            'expected': {'output': np.round(np.array([100, 200, 300]) / 7, 2)}
        },
        {
            'input': {'values': np.array([5, 10, 15]), 'd': 2},
            'expected': {'output': np.round(np.array([5, 10, 15]) / 2, 2)}
        }
    ]
})
# Write a function `zip_sum_numpy` that takes two NumPy arrays `array1` and `array2`, adds each corresponding element (pair) using NumPy, and returns a new array of these sums.
check_numpy_113 = functions_input_output_checker({
    'zip_sum_numpy': [
        {
            'input': {'array1': np.array([1, 2, 3]), 'array2': np.array([4, 5, 6])},
            'expected': {'output': np.array([5, 7, 9])}
        },
        {
            'input': {'array1': np.array([10, 20, 30]), 'array2': np.array([1, 1, 1])},
            'expected': {'output': np.array([11, 21, 31])}
        },
        {
            'input': {'array1': np.array([2, 3]), 'array2': np.array([5, 7])},
            'expected': {'output': np.array([7, 10])}
        }
    ]
})
# Create a function `binary_classification_numpy` that takes an array `classes` with values `0` and `1`. Use NumPy to count each, calculate their percentages, and return a dictionary with this data.
check_numpy_114 = functions_input_output_checker({
    'binary_classification_numpy': [
        {
            'input': {'classes': np.array([0, 0, 1, 1, 1, 0, 1])},
            'expected': {'output': {'0': 3/7 * 100, '1': 4/7 * 100}}
        },
        {
            'input': {'classes': np.array([1, 1, 1, 1])},
            'expected': {'output': {'0': 0.0, '1': 100.0}}
        },
        {
            'input': {'classes': np.array([0, 0, 0, 0])},
            'expected': {'output': {'0': 100.0, '1': 0.0}}
        }
    ]
})
# Develop a function `parse_convert_dates_numpy` that processes a NumPy array of date strings `date_strs` in `MM/DD/YYYY` format, converting them into `YYYY-MM-DD` using NumPy, sorting them, and returning the sorted array.
check_numpy_115 = functions_input_output_checker({
    'parse_convert_dates_numpy': [
        {
            'input': {'date_strs': np.array(['12/25/2022', '01/01/2021', '11/11/2022'])},
            'expected': {'output': np.array(['2021-01-01', '2022-11-11', '2022-12-25'])}
        },
        {
            'input': {'date_strs': np.array(['06/15/2020', '12/24/2019', '10/31/2021'])},
            'expected': {'output': np.array(['2019-12-24', '2020-06-15', '2021-10-31'])}
        },
        {
            'input': {'date_strs': np.array(['09/09/2021', '02/28/2020', '07/04/2023'])},
            'expected': {'output': np.array(['2020-02-28', '2021-09-09', '2023-07-04'])}
        }
    ]
})
# Implement a function `interleave_double_numpy` that accepts two NumPy arrays `arr1` and `arr2`. Use NumPy to interleave elements, double elements from `arr2`, and return the final array.
check_numpy_116 = functions_input_output_checker({
    'interleave_double_numpy': [
        {
            'input': {'arr1': np.array([1, 3, 5]), 'arr2': np.array([2, 4, 6])},
            'expected': {'output': np.array([1, 4, 3, 8, 5, 12])}
        },
        {
            'input': {'arr1': np.array([0, 7]), 'arr2': np.array([2, 5])},
            'expected': {'output': np.array([0, 4, 7, 10])}
        },
        {
            'input': {'arr1': np.array([9]), 'arr2': np.array([10])},
            'expected': {'output': np.array([9, 20])}
        }
    ]
})
# Write a function `group_count_numpy` that takes a NumPy array of strings `str_arr`. Use NumPy to group by length, calculate the occurrence count of each length, and return a dictionary with lengths as keys and counts as values.
check_numpy_117 = functions_input_output_checker({
    'group_count_numpy': [
        {
            'input': {'str_arr': np.array(['hi', 'hello', 'hi', 'world'])},
            'expected': {'output': {2: 2, 5: 2}}
        },
        {
            'input': {'str_arr': np.array(['abc', 'de', 'fghi', 'jklm', 'no'])},
            'expected': {'output': {3: 1, 2: 2, 4: 2}}
        },
        {
            'input': {'str_arr': np.array(['cat', 'fish', 'dog', 'ant'])},
            'expected': {'output': {3: 3, 4: 1}}
        }
    ]
})
# Create a function `remove_false_combine_numpy` that processes two NumPy boolean arrays `bool_arr1` and `bool_arr2`. Remove `False` entries using NumPy, concatenate them, and return the combined array.
check_numpy_118 = functions_input_output_checker({
    'remove_false_combine_numpy': [
        {
            'input': {'bool_arr1': np.array([True, False, True]), 'bool_arr2': np.array([False, True])},
            'expected': {'output': np.array([True, True, True])}
        },
        {
            'input': {'bool_arr1': np.array([True, True, False]), 'bool_arr2': np.array([True, False])},
            'expected': {'output': np.array([True, True, True])}
        },
        {
            'input': {'bool_arr1': np.array([False, False]), 'bool_arr2': np.array([True])},
            'expected': {'output': np.array([True])}
        }
    ]
})
# Develop a function `check_palindrome_reverse_numpy` that takes a NumPy array of strings `strs`, uses NumPy to filter out non-alphabetic, checks for palindromes, and returns the strings in reverse order.
check_numpy_119 = functions_input_output_checker({
    'check_palindrome_reverse_numpy': [
        {
            'input': {'strs': np.array(['madam', 'step', 'on', 'no', 'pets'])},
            'expected': {'output': np.array(['step', 'pets'])}
        },
        {
            'input': {'strs': np.array(['radar', 'hello', 'world', 'level'])},
            'expected': {'output': np.array(['level', 'radar'])}
        },
        {
            'input': {'strs': np.array(['notapalindrome', 'civic'])},
            'expected': {'output': np.array(['civic'])}
        }
    ]
})
# Implement a function `find_duplicates_unique_numpy` that accepts a NumPy array `elements`, identifies duplicates using NumPy, separates from unique elements, and returns a tuple of duplicate and unique arrays.
check_numpy_120 = functions_input_output_checker({
    'find_duplicates_unique_numpy': [
        {
            'input': {'elements': np.array([1, 2, 3, 2, 4, 1])},
            'expected': {'output': (np.array([1, 2]), np.array([3, 4]))}
        },
        {
            'input': {'elements': np.array([10, 20, 20, 30, 40, 40])},
            'expected': {'output': (np.array([20, 40]), np.array([10, 30]))}
        },
        {
            'input': {'elements': np.array([5, 5, 5, 7, 8, 8])},
            'expected': {'output': (np.array([5, 8]), np.array([7]))}
        }
    ]
})
# Write a function `scale_match_numpy` that takes two NumPy arrays `arr_a` and `arr_b`, scales each by their respective maximum with NumPy, and returns `True` if they are identical, otherwise `False`.
check_numpy_121 = functions_input_output_checker({
    'scale_match_numpy': [
        {
            'input': {'arr_a': np.array([1, 2, 3]), 'arr_b': np.array([2, 4, 6])},
            'expected': {'output': True}
        },
        {
            'input': {'arr_a': np.array([5, 10, 15]), 'arr_b': np.array([6, 12, 18])},
            'expected': {'output': True}
        },
        {
            'input': {'arr_a': np.array([4, 8, 12]), 'arr_b': np.array([1, 2, 3])},
            'expected': {'output': False}
        }
    ]
})
# Create a function `calculate_ratios_sort_numpy` that takes two NumPy arrays `numers` and `denoms`. Calculate ratios using NumPy, sort them, and return a new array of sorted ratios.
check_numpy_122 = functions_input_output_checker({
    'calculate_ratios_sort_numpy': [
        {
            'input': {'numers': np.array([1, 3, 5]), 'denoms': np.array([2, 2, 2])},
            'expected': {'output': np.sort(np.array([0.5, 1.5, 2.5]))}
        },
        {
            'input': {'numers': np.array([10, 20, 40]), 'denoms': np.array([10, 10, 10])},
            'expected': {'output': np.sort(np.array([1, 2, 4]))}
        },
        {
            'input': {'numers': np.array([7, 14, 21]), 'denoms': np.array([3, 7, 11])},
            'expected': {'output': np.sort(np.array([7/3, 14/7, 21/11]))}
        }
    ]
})
# Develop a function `decode_filter_numpy` that processes a NumPy array `codes`, decodes using NumPy string operations, filters messages containing digits, and returns the cleaned array.
check_numpy_123 = functions_input_output_checker({
    'decode_filter_numpy': [
        {
            'input': {'codes': np.array(['TH1s', 'is', '4', 'test'])},
            'expected': {'output': np.array(['is', 'test'])}
        },
        {
            'input': {'codes': np.array(['H3llo', 'World', '42Bye'])},
            'expected': {'output': np.array(['World'])}
        },
        {
            'input': {'codes': np.array(['numpy123', 'rocks', '456'])},
            'expected': {'output': np.array(['rocks'])}
        }
    ]
})
# Implement a function `sync_sum_json_numpy` that takes two JSON-like dictionaries `data1` and `data2`, synchronizes with NumPy by common keys, sums values, and returns the resulting dictionary.
check_numpy_124 = functions_input_output_checker({
    'sync_sum_json_numpy': [
        {
            'input': {
                'data1': {'a': 1, 'b': 2, 'c': 3},
                'data2': {'b': 3, 'c': 4, 'd': 5}
            },
            'expected': {'output': {'b': 5, 'c': 7}}
        },
        {
            'input': {
                'data1': {'x': 10, 'y': 20},
                'data2': {'y': 25, 'z': 30}
            },
            'expected': {'output': {'y': 45}}
        },
        {
            'input': {
                'data1': {'m': 5, 'n': 15},
                'data2': {'m': 10, 'n': 15, 'o': 20}
            },
            'expected': {'output': {'m': 15, 'n': 30}}
        }
    ]
})
# Write a function `tokenize_compare_numpy` that takes two NumPy string arrays `para1` and `para2`, tokenizes using NumPy, calculates the set difference with NumPy, and returns a list of unique words in one array.
check_numpy_125 = functions_input_output_checker({
    'tokenize_compare_numpy': [
        {
            'input': {'para1': np.array(['hello world']), 'para2': np.array(['world peace'])},
            'expected': {'output': sorted(set(['hello']) - set(['world']))}
        },
        {
            'input': {'para1': np.array(['data science']), 'para2': np.array(['machine learning'])},
            'expected': {'output': sorted(set(['data', 'science']) - set(['machine', 'learning']))}
        },
        {
            'input': {'para1': np.array(['AI revolution']), 'para2': np.array(['revolution AI future'])},
            'expected': {'output': sorted(set([]))}
        }
    ]
})

