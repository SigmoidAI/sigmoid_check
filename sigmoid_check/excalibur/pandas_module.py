import io
import numpy as np
import pandas as pd
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
    elif isinstance(expected, pd.DataFrame):
        if expected.shape != result.shape:
            return False
        if list(expected.columns) != list(result.columns):
            return False
        if not (expected.dtypes.equals(result.dtypes)):
            return False
        if not expected.equals(result):
            return False
        if not expected.index.equals(result.index):
            return False
        if not expected.columns.equals(result.columns):
            return False
        return True
    elif isinstance(expected, pd.Series):
        if not expected.index.equals(result.index):
            return False
        return expected.equals(result)
    elif isinstance(expected, pd.Index):
        return expected.equals(result)
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
# Given a list of dictionaries `data`, create a pandas DataFrame named `df_from_dict`.
check_pandas_1 = input_output_checker([
    {
        'input': {
            'data': [
                {'A': 1, 'B': 2},
                {'A': 3, 'B': 4},
                {'A': 5, 'B': 6}
            ]
        },
        'expected': {
            'df_from_dict': pd.DataFrame({
                'A': [1, 3, 5],
                'B': [2, 4, 6]
            })
        }
    }
])

# Create a pandas Series named `series_from_list` from a list of floats `float_list`, with no index specified.
check_pandas_2 = input_output_checker([
    {
        'input': {
            'float_list': [1.1, 2.2, 3.3]
        },
        'expected': {
            'series_from_list': pd.Series([1.1, 2.2, 3.3])
        }
    }
])

# Given a dictionary `dict_data` containing country names as keys and populations as values, create a pandas Series named `country_population`, using the dictionary keys as index.
check_pandas_3 = input_output_checker([
    {
        'input': {
            'dict_data': {
                'USA': 328200000,
                'China': 1439323776,
                'India': 1380004385
            }
        },
        'expected': {
            'country_population': pd.Series([328200000, 1439323776, 1380004385], index=['USA', 'China', 'India'])
        }
    }
])

# From a pandas Series `series_population`, access the index and save it in a variable `population_index`.
check_pandas_4 = input_output_checker([
    {
        'input': {
            'series_population': pd.Series([328200000, 1439323776, 1380004385], index=['USA', 'China', 'India'])
        },
        'expected': {
            'population_index': pd.Series([328200000, 1439323776, 1380004385], index=['USA', 'China', 'India']).index
        }
    }
])

# Using a pandas Series `series_temperatures`, extract the values and store them in a variable `temperature_values`.
check_pandas_5 = input_output_checker([
    {
        'input': {
            'series_temperatures': pd.Series([25, 30, 35, 40, 45])
        },
        'expected': {
            'temperature_values': np.array([25, 30, 35, 40, 45])
        }
    }
])

# For a pandas Series `series_ages`, get the data type of the elements in the series and store it in a variable `ages_dtype`.
check_pandas_6 = input_output_checker([
    {
        'input': {
            'series_ages': pd.Series([25, 30, 35, 40, 45])
        },
        'expected': {
            'ages_dtype': np.dtype('int64')
        }
    }
])

# From a Series `series_custom_index` with a custom index, access the element with index 'A' and store it in a variable `element_A`.
check_pandas_7 = input_output_checker([
    {
        'input': {
            'series_custom_index': pd.Series([10, 20, 30], index=['A', 'B', 'C'])
        },
        'expected': {
            'element_A': np.int64(10)
        }
    }
])

# Using a pandas Series `series_items`, slice the series to contain elements with indices from 'b' to 'd', inclusive, and save it into `sliced_series`.
check_pandas_8 = input_output_checker([
    {
        'input': {
            'series_items': pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
        },
        'expected': {
            'sliced_series': pd.Series([20, 30, 40], index=['b', 'c', 'd'])
        }
    }
])

# From a Series `series_prices`, select elements with custom indices ['apple', 'banana', 'cherry'] and store them in `selected_prices`.
check_pandas_9 = input_output_checker([
    {
        'input': {
            'series_prices': pd.Series([2.5, 1.5, 3.0, 4.0], index=['apple', 'banana', 'cherry', 'date'])
        },
        'expected': {
            'selected_prices': pd.Series([2.5, 1.5, 3.0], index=['apple', 'banana', 'cherry'])
        }
    }
])

# Create a DataFrame `df_custom` from a list of lists `list_of_lists_data`, ensuring to label the columns as 'A', 'B', 'C'.
check_pandas_10 = input_output_checker([
    {
        'input': {
            'list_of_lists_data': [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        },
        'expected': {
            'df_custom': pd.DataFrame([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], columns=['A', 'B', 'C'])
        }
    }
])

# Given a list of tuples `data_tuples`, create a DataFrame named `df_from_tuples` and rename its columns to 'X', 'Y', 'Z'.
check_pandas_11 = input_output_checker([
    {
        'input': {
            'data_tuples': [
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)
            ]
        },
        'expected': {
            'df_from_tuples': pd.DataFrame([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], columns=['X', 'Y', 'Z'])
        }
    }
])

# Using DataFrame `df_sales`, access and store the column names in variable `sales_columns`.
check_pandas_12 = input_output_checker([
    {
        'input': {
            'df_sales': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Sales': [100, 200, 300]
            })
        },
        'expected': {
            'sales_columns': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Sales': [100, 200, 300]
            }).columns
        }
    }
])

# Store the index of the DataFrame `df_employees` in a variable `employees_index`.
check_pandas_13 = input_output_checker([
    {
        'input': {
            'df_employees': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 35]
            }, index=['A', 'B', 'C'])
        },
        'expected': {
            'employees_index': pd.Index(['A', 'B', 'C'])
        }
    }
])

# Retrieve the values from DataFrame `df_weather` and save them into `weather_values`.
check_pandas_14 = input_output_checker([
    {
        'input': {
            'df_weather': pd.DataFrame({
                'City': ['New York', 'Los Angeles', 'Chicago'],
                'Temperature': [25, 30, 20]
            })
        },
        'expected': {
            'weather_values': np.array([
                ['New York', 25],
                ['Los Angeles', 30],
                ['Chicago', 20]
            ])
        }
    }
])

# Determine the shape of the DataFrame `df_financials` and store it in a variable `financials_shape`.
check_pandas_15 = input_output_checker([
    {
        'input': {
            'df_financials': pd.DataFrame({
                'Company': ['A', 'B', 'C'],
                'Revenue': [100, 200, 300]
            })
        },
        'expected': {
            'financials_shape': (3, 2)
        }
    }
])

# Get the data types of each column in DataFrame `df_customer_info` and store them in a variable `customer_info_dtypes`.
check_pandas_16 = input_output_checker([
    {
        'input': {
            'df_customer_info': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 35]
            })
        },
        'expected': {
            'customer_info_dtypes': pd.Series({
                'Name': np.dtype('O'),
                'Age': np.dtype('int64')
            })
        }
    }
])

# Using the DataFrame `df_transactions`, get the first 5 rows and store them in `transactions_head`.
check_pandas_17 = input_output_checker([
    {
        'input': {
            'df_transactions': pd.DataFrame({
                'Transaction ID': [1, 2, 3, 4, 5],
                'Amount': [100, 200, 300, 400, 500]
            })
        },
        'expected': {
            'transactions_head': pd.DataFrame({
                'Transaction ID': [1, 2, 3, 4, 5],
                'Amount': [100, 200, 300, 400, 500]
            })
        }
    }
])

# Retrieve the last 3 rows from DataFrame `df_activities` and save them into `activities_tail`.
check_pandas_18 = input_output_checker([
    {
        'input': {
            'df_activities': pd.DataFrame({
                'Activity': ['A', 'B', 'C', 'D', 'E'],
                'Duration': [10, 20, 30, 40, 50]
            })
        },
        'expected': {
            'activities_tail': pd.DataFrame({
                'Activity': ['C', 'D', 'E'],
                'Duration': [30, 40, 50]
            }, index=[2, 3, 4])
        }
    }
])

# Get a summary of information about DataFrame `df_inventory`, storing the result in a variable `inventory_info`.
check_pandas_19 = input_output_checker([
    {
        'input': {
            'df_inventory': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Quantity': [100, 200, 300]
            })
        },
        'expected': {
            'inventory_info': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Quantity': [100, 200, 300]
            }).info(buf=io.StringIO())
        }
    }
])

# For the DataFrame `df_scores`, generate descriptive statistics and store them in `scores_statistics`.
check_pandas_20 = input_output_checker([
    {
        'input': {
            'df_scores': pd.DataFrame({
                'Student': ['Alice', 'Bob', 'Charlie'],
                'Score': [80, 90, 85]
            })
        },
        'expected': {
            'scores_statistics': pd.DataFrame({
                'Score': [80, 90, 85]
            }).describe()
        }
    }
])

# Use DataFrame `df_orders` to create a boolean mask `orders_non_missing`, detecting non-missing values.
check_pandas_21 = input_output_checker([    
    {
        'input': {
            'df_orders': pd.DataFrame({
                'Order ID': [1, np.nan, 3],
                'Amount': [100, 200, np.nan]
            })
        },
        'expected': {
            'orders_non_missing': pd.DataFrame({
                'Order ID': [True, False, True],
                'Amount': [True, True, False]
            })
        }
    }
])

# Drop rows with missing values in DataFrame `df_stats` and save the result into `cleaned_stats`.
check_pandas_22 = input_output_checker([
    {
        'input': {
            'df_stats': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })
        },
        'expected': {
            'cleaned_stats': pd.DataFrame({
                'A': [1.0],
                'B': [4.0]
            })
        }
    }
])

# From DataFrame `df_statistics`, drop columns with missing values and store the result into `statistics_cleaned`.
check_pandas_23 = input_output_checker([
    {
        'input': {
            'df_statistics': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })
        },
        'expected': {
            'statistics_cleaned': pd.DataFrame(index=[0, 1, 2])
        }
    }
])

# Fill missing values in DataFrame `df_grades` with 0 and store the resultant DataFrame in `filled_grades`.
check_pandas_24 = input_output_checker([
    {
        'input': {
            'df_grades': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })
        },
        'expected': {
            'filled_grades': pd.DataFrame({
                'A': [1.0, 2.0, 0.0],
                'B': [4.0, 0.0, 6.0]
            })
        }
    }
])

# Apply backward fill on DataFrame `df_sales_data` for missing values and save it into `filled_bfill_sales_data`.
check_pandas_25 = input_output_checker([
    {
        'input': {
            'df_sales_data': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })
        },
        'expected': {
            'filled_bfill_sales_data': pd.DataFrame({
                'A': [1.0, 2.0, np.nan],
                'B': [4.0, 6.0, 6.0]
            })
        }
    }
])

# Apply forward fill on DataFrame `df_attendance` and store the results in `filled_ffill_attendance`.
check_pandas_26 = input_output_checker([
    {
        'input': {
            'df_attendance': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })
        },
        'expected': {
            'filled_ffill_attendance': pd.DataFrame({
                'A': [1.0, 2.0, 2.0],
                'B': [4.0, 4.0, 6.0]
            })
        }
    }
])

# Set 'OrderID' as the index of DataFrame `df_orders_list` and save the updated DataFrame as `orders_indexed`.
check_pandas_27 = input_output_checker([
    {
        'input': {
            'df_orders_list': pd.DataFrame({
                'OrderID': [1, 2, 3],
                'Amount': [100, 200, 300]
            })
        },
        'expected': {
            'orders_indexed': pd.DataFrame({
                'Amount': [100, 200, 300]
            }, index=[1, 2, 3])
        }
    }
])

# Reset the index of a DataFrame `df_indexed_data` and store it in `df_reset_index`.
check_pandas_28 = input_output_checker([
    {
        'input': {
            'df_indexed_data': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6]
            }, index=[2, 4, 19])
        },
        'expected': {
            'df_reset_index': pd.DataFrame({
                'index': [2, 4, 19],
                'A': [1, 2, 3],
                'B': [4, 5, 6],
            }, index=[0, 1, 2])
        }
    }
])

# Create a DataFrame `df_multiindex` with hierarchical indexing from `multiindex_data_list` using levels 'Region' and 'Category'.
check_pandas_29 = input_output_checker([
    {
        'input': {
            'multiindex_data_list': {
                "Region": ["East", "East", "West", "West"],
                "Category": ["A", "B", "A", "B"],
                "Sales": [100, 200, 300, 400]
            }
        },
        'expected': {
            'df_multiindex': pd.DataFrame({
                'Sales': [100, 200, 300, 400]
            }, index=pd.MultiIndex.from_tuples([
                ('East', 'A'),
                ('East', 'B'),
                ('West', 'A'),
                ('West', 'B')
            ], names=['Region', 'Category']))
        }
    }
])

# Use DataFrame `df_exams` to filter rows with Score > 80 using boolean indexing and save it in `high_score_exams`.
check_pandas_30 = input_output_checker([
    {
        'input': {
            'df_exams': pd.DataFrame({
                'Student': ['Alice', 'Bob', 'Charlie'],
                'Score': [80, 90, 85]
            })
        },
        'expected': {
            'high_score_exams': pd.DataFrame({
                'Student': ['Bob', 'Charlie'],
                'Score': [90, 85]
            }, index=[1, 2])
        }
    }
])

# From DataFrame `df_transactions`, select the row with label 'TX005' and store it in `transaction_TX005`.
check_pandas_31 = input_output_checker([
    {
        'input': {
            'df_transactions': pd.DataFrame({
                'Amount': [100, 200, 300],
                'Date': ['2021-01-01', '2021-01-02', '2021-01-03']
            }, index=['TX001', 'TX005', 'TX003'])
        },
        'expected': {
            'transaction_TX005': pd.Series([200, '2021-01-02'], index=['Amount', 'Date'])
        }
    }
])

# Use DataFrame `df_sports` to select rows labeled ['Basketball', 'Football'] and columns labeled ['Wins', 'Losses'], storing the result in `selected_sports`.
check_pandas_32 = input_output_checker([
    {
        'input': {
            'df_sports': pd.DataFrame({
                'Wins': [10, 20, 30],
                'Losses': [5, 10, 15]
            }, index=['Basketball', 'Football', 'Soccer'])
        },
        'expected': {
            'selected_sports': pd.DataFrame({
                'Wins': [10, 20],
                'Losses': [5, 10]
            }, index=['Basketball', 'Football'])
        }
    }
])

# From DataFrame `df_catalog`, select rows where 'Category' is 'Electronics' and save them to `electronics_catalog`.
check_pandas_33 = input_output_checker([
    {
        'input': {
            'df_catalog': pd.DataFrame({
                'Product': ['Laptop', 'Phone', 'Tablet'],
                'Category': ['Electronics', 'Clothing', 'Electronics']
            })
        },
        'expected': {
            'electronics_catalog': pd.DataFrame({
                'Product': ['Laptop', 'Tablet'],
                'Category': ['Electronics', 'Electronics']
            }, index=[0, 2])
        }
    },
    {
        'input': {
            'df_catalog': pd.DataFrame({
                'Product': ['Laptop', 'Phone', 'Tablet'],
                'Category': ['Electronics', 'Electronics', 'Electronics']
            })
        },
        'expected': {
            'electronics_catalog': pd.DataFrame({
                'Product': ['Laptop', 'Phone', 'Tablet'],
                'Category': ['Electronics', 'Electronics', 'Electronics']
            }, index=[0, 1, 2])
        }
    },
    {
        'input': {
            'df_catalog': pd.DataFrame({
                'Product': ['Laptop', 'Phone', 'Tablet'],
                'Category': ['Clothing', 'Clothing', 'Clothing']
            })
        },
        'expected': {
            'electronics_catalog': pd.DataFrame({
                'Product': [],
                'Category': []
            }, dtype='object')
        }
    }
])

# For DataFrame `df_movies`, perform boolean selection where 'Genre' is 'Action' and 'Budget' > 500000, then select 'Title' and 'Revenue' columns, storing result in `selected_movies`.
check_pandas_34 = input_output_checker([
    {
        'input': {
            'df_movies': pd.DataFrame({
                'Title': ['A', 'B', 'C'],
                'Genre': ['Action', 'Drama', 'Action'],
                'Budget': [100000, 200000, 600000],
                'Revenue': [200000, 300000, 700000]
            })
        },
        'expected': {
            'selected_movies': pd.DataFrame({
                'Title': ['C'],
                'Revenue': [700000]
            }, index=[2])
        }
    },
    {
        'input': {
            'df_movies': pd.DataFrame({
                'Title': ['A', 'B', 'C'],
                'Genre': ['Action', 'Drama', 'Action'],
                'Budget': [100000, 200000, 400000],
                'Revenue': [200000, 300000, 500000]
            })
        },
        'expected': {
            'selected_movies': pd.DataFrame({
                'Title': pd.Series(dtype='object'),
                'Revenue': pd.Series(dtype='int64')
            })
        }
    },
    {
        'input': {
            'df_movies': pd.DataFrame({
                'Title': ['A', 'B', 'C'],
                'Genre': ['Drama', 'Drama', 'Drama'],
                'Budget': [100000, 200000, 600000],
                'Revenue': [200000, 300000, 700000]
            })
        },
        'expected': {
            'selected_movies': pd.DataFrame({
                'Title': pd.Series(dtype='object'),
                'Revenue': pd.Series(dtype='int64')
            })
        }
    }
])

# Using .loc, slice DataFrame `df_plants` to include rows 'Rose' through 'Tulip' and store it in `flower_slice`.
check_pandas_35 = input_output_checker([
    {
        'input': {
            'df_plants': pd.DataFrame({
                'Color': ['Red', 'Blue', 'Yellow', 'Pink', 'Purple'],
                'Type': ['Rose', 'Lily', 'Daisy', 'Tulip', 'Orchid']
            }, index=['Rose', 'Lily', 'Daisy', 'Tulip', 'Orchid'])
        },
        'expected': {
            'flower_slice': pd.DataFrame({
                'Color': ['Red', 'Blue', 'Yellow', 'Pink'],
                'Type': ['Rose', 'Lily', 'Daisy', 'Tulip']
            }, index=['Rose', 'Lily', 'Daisy', 'Tulip'])
        }
    }
])

# Use .iloc to slice DataFrame `df_students` to include the first three rows and the first two columns, saving them in `student_slice`.
check_pandas_36 = input_output_checker([
    {
        'input': {
            'df_students': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                'Age': [25, 30, 35, 40],
                'Grade': [80, 90, 85, 95]
            })
        },
        'expected': {
            'student_slice': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 35]
            })
        }
    }
])

# From DataFrame `df_reports`, use a combination of .loc and .iloc to select rows 'R102' and 'R103' and the first three columns, storing it as `report_selection`.
check_pandas_37 = input_output_checker([
    {
        'input': {
            'df_reports': pd.DataFrame({
                'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
                'Sales': [100, 200, 300],
                'Expenses': [50, 100, 150],
                'Profit': [50, 100, 150]
            }, index=['R101', 'R102', 'R103'])
        },
        'expected': {
            'report_selection': pd.DataFrame({
                'Date': ['2021-01-02', '2021-01-03'],
                'Sales': [200, 300],
                'Expenses': [100, 150]
            }, index=['R102', 'R103'])
        }
    }
])

# Modify DataFrame `df_inventory` by setting all 'Quantity' to 50 for rows labeled 'InStock' and store the modified DataFrame as `inventory_modified`.
check_pandas_38 = input_output_checker([
    {
        'input': {
            'df_inventory': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Quantity': [100, 200, 300]
            }, index=['InStock', 'OutStock', 'InStock'])
        },
        'expected': {
            'inventory_modified': pd.DataFrame({
                'Product': ['A', 'B', 'C'],
                'Quantity': [50, 200, 50]
            }, index=['InStock', 'OutStock', 'InStock'])
        }
    }
])

# Combine .loc and .iloc to modify rows 'R101' to 'R105' in 'df_revenue' setting the first column's value to 1000, storing it in `revenue_updated`.
check_pandas_39 = input_output_checker([
    {
        'input': {
            'df_revenue': pd.DataFrame({
                'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
                'Sales': [100, 200, 300, 400, 500]
            }, index=['R101', 'R102', 'R103', 'R104', 'R105'])
        },
        'expected': {
            'revenue_updated': pd.DataFrame({
                'Date': pd.Series([1000, 1000, 1000, 1000, 1000], index=['R101', 'R102', 'R103', 'R104', 'R105'], dtype='object'),
                'Sales': [100, 200, 300, 400, 500]
            }, index=['R101', 'R102', 'R103', 'R104', 'R105'])
        }
    }
])

# Using DataFrame `df_hierarchical_example`, demonstrate the use of .loc and .iloc on a DataFrame with a multiindex, saving the selection as `multiindex_selected`, selecting the row with index ('North', 'A') and column 'X'.
check_pandas_40 = input_output_checker([
    {
        'input': {
            'df_hierarchical_example': pd.DataFrame({
                'X': [100, 200, 300, 400, 500],
                'Expenses': [50, 100, 150, 200, 250]
            }, index=pd.MultiIndex.from_tuples([
                ('East', 'A'),
                ('East', 'B'),
                ('West', 'A'),
                ('West', 'B'),
                ('North', 'A')
            ], names=['Region', 'Category']))
        },
        'expected': {
            'multiindex_selected': np.int64(500)
        }
    }
])

# Concatenate DataFrames `df1` and `df2` horizontally and save the result as `concatenated_df_horizontal`.
check_pandas_41 = input_output_checker([
    {
        'input': {
            'df1': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6]
            }),
            'df2': pd.DataFrame({
                'C': [7, 8, 9],
                'D': [10, 11, 12]
            })
        },
        'expected': {
            'concatenated_df_horizontal': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9],
                'D': [10, 11, 12]
            })
        }
    }
])

# Concatenate DataFrames `df_a` and `df_b` vertically, aligning by columns, and store the result in `concatenated_df_vertical`.
check_pandas_42 = input_output_checker([
    {
        'input': {
            'df_a': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6]
            }),
            'df_b': pd.DataFrame({
                'A': [7, 8, 9],
                'B': [10, 11, 12]
            })
        },
        'expected': {
            'concatenated_df_vertical': pd.DataFrame({
                'A': [1, 2, 3, 7, 8, 9],
                'B': [4, 5, 6, 10, 11, 12]
            }, index=[0, 1, 2, 0, 1, 2])
        }
    }
])

# Merge DataFrames `df_left` and `df_right` on key 'ID', using outer method and store result in `merged_outer`.
check_pandas_43 = input_output_checker([
    {
        'input': {
            'df_left': pd.DataFrame({
                'ID': [1, 2, 3],
                'Name': ['Alice', 'Bob', 'Charlie']
            }),
            'df_right': pd.DataFrame({
                'ID': [2, 3, 4],
                'Age': [25, 30, 35]
            })
        },
        'expected': {
            'merged_outer': pd.DataFrame({
                'ID': [1, 2, 3, 4],
                'Name': ['Alice', 'Bob', 'Charlie', np.nan],
                'Age': [np.nan, 25, 30, 35]
            })
        }
    }
])

# Perform a right merge on DataFrames `df_personal` and `df_contact` based on the key 'ContactID', saving it as `merged_right`.
check_pandas_44 = input_output_checker([
    {
        'input': {
            'df_personal': pd.DataFrame({
                'ContactID': [1, 2, 3],
                'Name': ['Alice', 'Bob', 'Charlie']
            }),
            'df_contact': pd.DataFrame({
                'ContactID': [2, 3, 4],
                'Phone': ['123', '456', '789']
            })
        },
        'expected': {
            'merged_right': pd.DataFrame({
                'ContactID': [2, 3, 4],
                'Name': ['Bob', 'Charlie', np.nan],
                'Phone': ['123', '456', '789']
            })
        }
    }
])

# Join DataFrames `df_main` and `df_additional` using an inner join, saving the result in `joined_inner`.
check_pandas_45 = input_output_checker([
    {
        'input': {
            'df_main': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie']
            }, index=[1, 2, 3]),
            'df_additional': pd.DataFrame({
                'Age': [25, 30, 35]
            }, index=[2, 3, 4])
        },
        'expected': {
            'joined_inner': pd.DataFrame({
                'Name': ['Bob', 'Charlie'],
                'Age': [25, 30]
            }, index=[2, 3])
        }
    }
])

# Conduct a left join on DataFrames `df_sales_main` and `df_sales_region` on 'RegionID', storing it as `joined_left`.
check_pandas_46 = input_output_checker([
    {
        'input': {
            'df_sales_main': pd.DataFrame({
                'Sales': [100, 200, 300],
            }, index=[1, 2, 3]).rename_axis('RegionID'),
            'df_sales_region': pd.DataFrame({
                'Region': ['East', 'West', 'North']
            }, index=[2, 3, 4]).rename_axis('RegionID')
        },
        'expected': {
            'joined_left': pd.DataFrame({
                'Sales': [100, 200, 300],
                'Region': [np.nan, 'East', 'West']
            }, index=[1, 2, 3]).rename_axis('RegionID')
        }
    }
])

# Group DataFrame `df_employee` by 'Department', calculating the average 'Salary' for each group and saving it as `avg_salary_by_department`.
check_pandas_47 = input_output_checker([
    {
        'input': {
            'df_employee': pd.DataFrame({
                'Department': ['HR', 'Finance', 'HR', 'Finance'],
                'Salary': [50000, 60000, 70000, 80000]
            })
        },
        'expected': {
            'avg_salary_by_department': pd.Series({
                'Finance': 70000,
                'HR': 60000,
            }, dtype='float64', name='Salary').rename_axis('Department')
        }
    }
])

# Pivot DataFrame `df_orders` with 'OrderID' as index, 'Category' as columns, and 'Amount' as values, resulting in `pivoted_orders`.
check_pandas_48 = input_output_checker([
    {
        'input': {
            'df_orders': pd.DataFrame({
                'OrderID': [1, 2, 3, 4],
                'Category': ['A', 'B', 'A', 'B'],
                'Amount': [100, 200, 300, 400]
            })
        },
        'expected': {
            'pivoted_orders': pd.DataFrame({
                'OrderID': [1, 2, 3, 4],
                'Category': ['A', 'B', 'A', 'B'],
                'Amount': [100, 200, 300, 400]
            }).pivot(index='OrderID', columns='Category', values='Amount')
        }
    }
])

# Utilize crosstab to get a frequency table of 'Region' and 'ProductType' categories from `df_business`, storing the result as `region_product_crosstab`.
check_pandas_49 = input_output_checker([
    {
        'input': {
            'df_business': pd.DataFrame({
                'Region': ['East', 'West', 'East', 'West'],
                'ProductType': ['A', 'B', 'A', 'B']
            })
        },
        'expected': {
            'region_product_crosstab': pd.crosstab(
                index=pd.DataFrame({
                    'Region': ['East', 'West', 'East', 'West']
                })['Region'],
                columns=pd.DataFrame({
                    'ProductType': ['A', 'B', 'A', 'B']
                })['ProductType']
            )
        }
    }
])

# Reshape DataFrame `df_energy` from wide to long format using melt, and store the result in `melted_energy`.
check_pandas_50 = input_output_checker([
    {
        'input': {
            'df_energy': pd.DataFrame({
                'Year': [2020, 2021],
                'Coal': [100, 200],
                'Oil': [300, 400]
            })
        },
        'expected': {
            'melted_energy': pd.DataFrame({
                    'Year': [2020, 2021],
                    'Coal': [100, 200],
                    'Oil': [300, 400]
                }).melt(id_vars='Year', var_name='EnergyType', value_name='Consumption')
        }
    }
])

# Using DataFrame `df_product_sales`, change its structure by applying a pivot operation with 'ProductID' being the index, columns as 'Month', and 'Sales' as values, storing the result in `pivoted_sales`.
check_pandas_51 = input_output_checker([
    {
        'input': {
            'df_product_sales': pd.DataFrame({
                'ProductID': [1, 2, 3],
                'Sales': [100, 200, 300],
                'Month': ['A', 'B', 'A']
            })
        },
        'expected': {
            'pivoted_sales': pd.DataFrame({
                    'ProductID': [1, 2, 3],
                    'Sales': [100, 200, 300],
                    'Month': ['A', 'B', 'A']
                }).pivot(index='ProductID', columns='Month', values='Sales')
        }
    }
])
# Create a pandas DataFrame `df_date_range` using a date range starting from '2022-01-01' to '2023-01-01', frequency of 'MS', with columns ['Sales', 'Profit'] filled with zeros.
check_pandas_52 = input_output_checker([
    {
        'input': {},
        'expected': {
            'df_date_range': pd.DataFrame(
                0,
                index=pd.date_range(start='2022-01-01', end='2023-01-01', freq='MS'),
                columns=['Sales', 'Profit'],
            )
        }
    }
])

# Extract the year and month for each entry in DataFrame `df_date_series` with a DateTimeIndex, storing them in `years` and `months` respectively.
check_pandas_53 = input_output_checker([
    {
        'input': {
            'df_date_series': pd.DataFrame({
                'Sales': [100, 200, 300],
                'Profit': [50, 100, 150]
            }, index=pd.date_range(start='2022-01-01', periods=3, freq='MS')
            )
        },
        'expected': {
            'years': pd.Index([2022, 2022, 2022], dtype='int32'),
            'months': pd.Index([1, 2, 3], dtype='int32')
        }
    }
])

# Resample DataFrame `df_time_series` to quarterly frequency, taking the sum, and store the resulting series in `quarterly_series`.
check_pandas_54 = input_output_checker([
    {
        'input': {
            'df_time_series': pd.DataFrame({
                'Sales': [100, 200, 300, 400, 500],
                'Profit': [50, 100, 150, 200, 250]
            }, index=pd.date_range(start='2022-01-01', periods=5, freq='MS')
            )
        },
        'expected': {
            'quarterly_series': pd.DataFrame({
                'Sales': [600, 900],
                'Profit': [300, 450]
            }, index=pd.date_range(start='2022-01-01', periods=2, freq='QE')
            )
        }
    }
])

# Apply a rolling window of 7 days for the DataFrame `df_metrics`, and calculate the mean, storing it in `rolling_mean_metrics`.
check_pandas_55 = input_output_checker([
    {
        'input': {
            'df_metrics': pd.DataFrame({
                'Sales': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
            }, index=pd.date_range(start='2022-01-01', periods=10, freq='D')
            )
        },
        'expected': {
            'rolling_mean_metrics': pd.DataFrame({
                'Sales': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 400, 500, 600, 700]
            }, index=pd.date_range(start='2022-01-01', periods=10, freq='D')
            )
        }
    }
])
# Apply the function `np.log1p` to the column 'Revenue' in DataFrame `df_financial_data`, storing the updated data in `logged_df`.
check_pandas_56 = input_output_checker([
    {
        'input': {
            'df_financial_data': pd.DataFrame({
                'Revenue': [100, 200, 300, 400, 500]
            })
        },
        'expected': {
            'logged_df': pd.DataFrame({
                'Revenue': np.log1p([100, 200, 300, 400, 500])
            })
        }
    }
])

# Optimize memory usage of DataFrame `df_large` by converting column 'ID' to int32 and store as `optimized_df`.
check_pandas_57 = input_output_checker([
    {
        'input': {
            'df_large': pd.DataFrame({
                'ID': [1, 2, 3, 4, 5],
                'Sales': [100, 200, 300, 400, 500]
            })
        },
        'expected': {
            'optimized_df': pd.DataFrame({
                'ID': [1, 2, 3, 4, 5],
                'Sales': [100, 200, 300, 400, 500]
            }).astype({'ID': 'int32'})
        }
    }
])

# Convert data types of 'Price' in DataFrame `df_items` from float64 to float32 for memory efficiency, saving the result as `optimized_items`.
check_pandas_58 = input_output_checker([
    {
        'input': {
            'df_items': pd.DataFrame({
                'Item': ['A', 'B', 'C'],
                'Price': [100.0, 200.0, 300.0]
            })
        },
        'expected': {
            'optimized_items': pd.DataFrame({
                'Item': ['A', 'B', 'C'],
                'Price': [100.0, 200.0, 300.0]
            }).astype({'Price': 'float32'})
        }
    }
])

# Remove duplicate entries from DataFrame `df_database` and store the cleaned DataFrame as `unique_database`.
check_pandas_59 = input_output_checker([
    {
        'input': {
            'df_database': pd.DataFrame({
                'ID': [1, 2, 3, 4, 4],
                'Name': ['Alice', 'Bob', 'Charlie', 'David', 'David']
            })
        },
        'expected': {
            'unique_database': pd.DataFrame({
                'ID': [1, 2, 3, 4],
                'Name': ['Alice', 'Bob', 'Charlie', 'David']
            })
        }
    }
])

# Perform string operation by converting all entries in the 'Names' column of `df_attendees` to uppercase, storing the resulting DataFrame as `uppercase_attendees`.
check_pandas_60 = input_output_checker([
    {
        'input': {
            'df_attendees': pd.DataFrame({
                'Names': ['Alice', 'Bob', 'Charlie']
            })
        },
        'expected': {
            'uppercase_attendees': pd.DataFrame({
                'Names': ['ALICE', 'BOB', 'CHARLIE']
            })
        }
    }
])

# Select rows from DataFrame `df_students` using the query method to find students with 'Score' greater than 85, storing the result as `high_scorers`.
check_pandas_61 = input_output_checker([
    {
        'input': {
            'df_students': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Score': [80, 90, 85]
            })
        },
        'expected': {
            'high_scorers': pd.DataFrame({
                'Name': ['Bob'],
                'Score': [90]
            }, index=[1])
        }
    }
])

# In DataFrame `df_results`, group by 'Team', apply custom function to rank 'Score' in descending order, and store the result in `ranked_teams`.
check_pandas_62 = input_output_checker([
    {
        'input': {
            'df_results': pd.DataFrame({
                'Team': ['A', 'B', 'A', 'B'],
                'Score': [100, 200, 300, 400]
            })
        },
        'expected': {
            'ranked_teams': pd.DataFrame({
                'Team': {
                    ('A', 0): 'A',
                    ('A', 2): 'A',
                    ('B', 1): 'B',
                    ('B', 3): 'B'
                    },
                'Score': {
                    ('A', 0): 100,
                    ('A', 2): 300,
                    ('B', 1): 200,
                    ('B', 3): 400
                }, 'Rank': {
                    ('A', 0): 2.0,
                    ('A', 2): 1.0,
                    ('B', 1): 2.0,
                    ('B', 3): 1.0
                }
            })
        }
    }
])

# Perform a aggregation on DataFrame `df_data_group` for 'City' using a custom function that finds the range of 'Temperature', storing as `temperature_range`.
check_pandas_63 = input_output_checker([
    {
        'input': {
            'df_data_group': pd.DataFrame({
                'City': ['A', 'B', 'A', 'B'],
                'Temperature': [10, 20, 30, 40]
            })
        },
        'expected': {
            'temperature_range': pd.Series({
                'A': 20,
                'B': 20
            }).rename_axis('City')
        }
    }
])

# Use vectorized operations to add 10 to every element in DataFrame `df_numeric`, saving the result as `adjusted_numeric`.
check_pandas_64 = input_output_checker([
    {
        'input': {
            'df_numeric': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6]
            })
        },
        'expected': {
            'adjusted_numeric': pd.DataFrame({
                'A': [11, 12, 13],
                'B': [14, 15, 16]
            })
        }
    }
])

# Process DataFrame `df_sales_timezones` to convert the 'Timestamp' to a timezone-aware datetime, setting the timezone to 'UTC', and save as `timezone_aware_sales`.
check_pandas_65 = input_output_checker([
    {
        'input': {
            'df_sales_timezones': pd.DataFrame({
                'Timestamp': ['2022-01-01 00:00:00', '2022-01-02 00:00:00'],
                'Sales': [100, 200]
            })
        },
        'expected': {
            'timezone_aware_sales': pd.DataFrame({
                'Timestamp': pd.to_datetime(['2022-01-01 00:00:00', '2022-01-02 00:00:00']).tz_localize('UTC'),
                'Sales': [100, 200]
            })
        }
    }
])

# Create a pandas DataFrame `df_customer_reviews` from a JSON string `json_input_string`.
check_pandas_66 = input_output_checker([
    {
        'input': {
            'json_input_string': '[{"Name": "Alice", "Rating": 5}, {"Name": "Bob", "Rating": 4}]'
        },
        'expected': {
            'df_customer_reviews': pd.DataFrame({
                'Name': ['Alice', 'Bob'],
                'Rating': [5, 4]
            })
        }
    }
])

# Given a pandas Series `series_temp_investments`, access specific elements from custom indices ['A1', 'B2', 'C3'] and save them to `selected_investments`.
check_pandas_67 = input_output_checker([
    {
        'input': {
            'series_temp_investments': pd.Series([100, 200, 300], index=['A1', 'B2', 'C3'])
        },
        'expected': {
            'selected_investments': pd.Series([100, 200, 300], index=['A1', 'B2', 'C3'])
        }
    }
])

# Slice pandas Series `series_temp_readings` to return every second element, storing the result in `temp_slice_even`.
check_pandas_68 = input_output_checker([
    {
        'input': {
            'series_temp_readings': pd.Series([10, 20, 30, 40, 50])
        },
        'expected': {
            'temp_slice_even': pd.Series([10, 30, 50], index=[0, 2, 4])
        }
    }
])

# From a list of dictionaries `sensor_data_list`, create a DataFrame named `df_sensor_readings` with custom column names ['SensorID', 'Temperature', 'Humidity'].
check_pandas_69 = input_output_checker([
    {
        'input': {
            'sensor_data_list': [
                {'SensorID': 1, 'Temperature': 20, 'Humidity': 50},
                {'SensorID': 2, 'Temperature': 25, 'Humidity': 60}
            ]
        },
        'expected': {
            'df_sensor_readings': pd.DataFrame({
                'SensorID': [1, 2],
                'Temperature': [20, 25],
                'Humidity': [50, 60]
            })
        }
    }
])

# Access and display the first 10 elements of Series `series_large_dataset`, storing them in `top_ten_elements`.
check_pandas_70 = input_output_checker([
    {
        'input': {
            'series_large_dataset': pd.Series(range(100))
        },
        'expected': {
            'top_ten_elements': pd.Series(range(10))
        }
    }
])

# Use the DataFrame `df_population_data` to extract and store the indices in a variable `population_indices`.
check_pandas_71 = input_output_checker([
    {
        'input': {
            'df_population_data': pd.DataFrame({
                'City': ['A', 'B', 'C'],
                'Population': [100, 200, 300]
            }, index=['A', 'B', 'C'])
        },
        'expected': {
            'population_indices': pd.Index(['A', 'B', 'C'])
        }
    }
])

# Combine DataFrames `df_financial_2021` and `df_financial_2020` vertically, so that rows from 2021 follow those of 2020, storing result in `combined_financials`.
check_pandas_72 = input_output_checker([
    {
        'input': {
            'df_financial_2021': pd.DataFrame({
                'Date': ['2021-01-01', '2021-01-02'],
                'Sales': [100, 200]
            }),
            'df_financial_2020': pd.DataFrame({
                'Date': ['2020-01-01', '2020-01-02'],
                'Sales': [50, 150]
            })
        },
        'expected': {
            'combined_financials': pd.concat([
                pd.DataFrame({
                    'Date': ['2020-01-01', '2020-01-02'],
                    'Sales': [50, 150]
                }),
                pd.DataFrame({
                    'Date': ['2021-01-01', '2021-01-02'],
                    'Sales': [100, 200]
                })
            ])
        }
    }
])

# Merge DataFrames `df_clients` and `df_orders` with a common key 'ClientID' using the 'inner' join method, and save the result as `client_orders`.
check_pandas_73 = input_output_checker([
    {
        'input': {
            'df_clients': pd.DataFrame({
                'ClientID': [1, 2],
                'Name': ['Alice', 'Bob']
            }),
            'df_orders': pd.DataFrame({
                'ClientID': [2, 3],
                'Product': ['A', 'B']
            })
        },
        'expected': {
            'client_orders': pd.merge(
                pd.DataFrame({
                    'ClientID': [1, 2],
                    'Name': ['Alice', 'Bob']
                }),
                pd.DataFrame({
                    'ClientID': [2, 3],
                    'Product': ['A', 'B']
                }),
                on='ClientID',
                how='inner'
            )
        }
    }
])

# From DataFrame `df_commodity_prices`, locate the element where 'Commodity' is 'Gold' and 'PriceDate' is '2023-06-01', storing it in `gold_price`.
check_pandas_74 = input_output_checker([
    {
        'input': {
            'df_commodity_prices': pd.DataFrame({
                'Commodity': ['Gold', 'Silver'],
                'Price': [1000, 20],
                'PriceDate': ['2023-06-01', '2023-06-01']
            })
        },
        'expected': {
            'gold_price': pd.DataFrame({
                'Commodity': ['Gold'],
                'Price': [1000],
                'PriceDate': ['2023-06-01']
            })
        }
    }
])

# Use boolean indexing on DataFrame `df_sales_performance` to extract rows where 'Quarter' is Q1 and 'Year' >= 2022, saving the result in `performance_q1_2022`.
check_pandas_75 = input_output_checker([
    {
        'input': {
            'df_sales_performance': pd.DataFrame({
                'Year': [2021, 2022, 2022, 2023],
                'Quarter': ['Q1', 'Q1', 'Q2', 'Q1'],
                'Sales': [100, 200, 300, 400]
            })
        },
        'expected': {
            'performance_q1_2022': pd.DataFrame({
                'Year': [2022, 2023],
                'Quarter': ['Q1', 'Q1'],
                'Sales': [200, 400]
            }, index=[1, 3])
        }
    }
])

# Slice DataFrame `df_international_customers` to include rows 'France' to 'Italy' using their index labels and save it in `european_customers`.
check_pandas_76 = input_output_checker([
    {
        'input': {
            'df_international_customers': pd.DataFrame({
                'Country': ['USA', 'UK', 'France', 'Italy'],
                'Sales': [100, 200, 300, 400]
            }, index=['USA', 'UK', 'France', 'Italy'])
        },
        'expected': {
            'european_customers': pd.DataFrame({
                'Country': ['France', 'Italy'],
                'Sales': [300, 400]
            }, index=['France', 'Italy'])
        }
    }
])

# Modify DataFrame `df_shipping_list` by setting the 'CollectionDate' column of all rows before '2023-08-01' to NaT, storing the modified DataFrame as `adjusted_shipping`.
check_pandas_77 = input_output_checker([
    {
        'input': {
            'df_shipping_list': pd.DataFrame({
                'OrderID': [1, 2, 3],
                'CollectionDate': ['2023-07-01', '2023-08-01', '2023-09-01']
            })
        },
        'expected': {
            'adjusted_shipping': pd.DataFrame({
                'OrderID': [1, 2, 3],
                'CollectionDate': [pd.NaT, '2023-08-01', '2023-09-01']
            })
        }
    }
])

# Merge DataFrames `df_employee_roles` and `df_role_salaries` on 'RoleID', performing a left merge and storing result as `employee_salary_details`.
check_pandas_78 = input_output_checker([
    {
        'input': {
            'df_employee_roles': pd.DataFrame({
                'RoleID': [1, 2],
                'Role': ['Manager', 'Associate']
            }),
            'df_role_salaries': pd.DataFrame({
                'RoleID': [2, 3],
                'Salary': [50000, 60000]
            })
        },
        'expected': {
            'employee_salary_details': pd.merge(
                pd.DataFrame({
                    'RoleID': [1, 2],
                    'Role': ['Manager', 'Associate']
                }),
                pd.DataFrame({
                    'RoleID': [2, 3],
                    'Salary': [50000, 60000]
                }),
                on='RoleID',
                how='left'
            )
        }
    }
])

# Group DataFrame `df_class_scores` by 'Class' and calculate the maximum 'Score' for each class, saving the result as `max_class_scores`.
check_pandas_79 = input_output_checker([
    {
        'input': {
            'df_class_scores': pd.DataFrame({
                'Class': ['A', 'B', 'A', 'B'],
                'Score': [100, 200, 300, 400]
            })
        },
        'expected': {
            'max_class_scores': pd.Series(data=[300, 400], index=['A', 'B'], name='Score', dtype='int64').rename_axis('Class')
        }
    }
])

# Pivot DataFrame `df_sales_regions` with 'Region' as rows and 'Quarter' as columns, aggregating 'Sales' values, into `sales_pivot`.
check_pandas_80 = input_output_checker([
    {
        'input': {
            'df_sales_regions': pd.DataFrame({
                'Region': ['East', 'West', 'East', 'West'],
                'Quarter': ['Q1', 'Q1', 'Q2', 'Q2'],
                'Sales': [100, 200, 300, 400]
            })
        },
        'expected': {
            'sales_pivot': pd.pivot_table(
                pd.DataFrame({
                    'Region': ['East', 'West', 'East', 'West'],
                    'Quarter': ['Q1', 'Q1', 'Q2', 'Q2'],
                    'Sales': [100, 200, 300, 400]
                }),
                index='Region',
                columns='Quarter',
                values='Sales',
                aggfunc='sum'
            )
        }
    }
])

# Utilize a crosstab of 'CustomerType' and 'Region' from DataFrame `df_customer_data`, storing the result as `customer_region_crosstab`.
check_pandas_81 = input_output_checker([
    {
        'input': {
            'df_customer_data': pd.DataFrame({
                'CustomerType': ['A', 'B', 'A', 'B'],
                'Region': ['East', 'West', 'East', 'West']
            })
        },
        'expected': {
            'customer_region_crosstab': pd.crosstab(
                index=pd.DataFrame({
                    'CustomerType': ['A', 'B', 'A', 'B']
                })['CustomerType'],
                columns=pd.DataFrame({
                    'Region': ['East', 'West', 'East', 'West']
                })['Region']
            )
        }
    }
])

# Reshape DataFrame `df_expenses` to long format, using melt function, resulting in `melted_expenses`.
check_pandas_82 = input_output_checker([
    {
        'input': {
            'df_expenses': pd.DataFrame({
                'Date': ['2022-01-01', '2022-01-02'],
                'Rent': [1000, 1100],
                'Utilities': [200, 250]
            })
        },
        'expected': {
            'melted_expenses': pd.melt(
                pd.DataFrame({
                    'Date': ['2022-01-01', '2022-01-02'],
                    'Rent': [1000, 1100],
                    'Utilities': [200, 250]
                }),
                id_vars=['Date'],
                var_name='ExpenseType',
                value_name='Amount'
            )
        }
    }
])

# Use a pivot_table on DataFrame `df_contact_events` with 'ContactID' as index, 'EventType' as columns, and 'EventTimestamp' as values, stored in `pivoted_events`.
check_pandas_83 = input_output_checker([
    {
        'input': {
            'df_contact_events': pd.DataFrame({
                'ContactID': [1, 2, 1, 2],
                'EventType': ['Call', 'Email', 'Call', 'Email'],
                'EventTimestamp': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']
            })
        },
        'expected': {
            'pivoted_events': pd.pivot_table(
                pd.DataFrame({
                    'ContactID': [1, 2, 1, 2],
                    'EventType': ['Call', 'Email', 'Call', 'Email'],
                    'EventTimestamp': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']
                }),
                index='ContactID',
                columns='EventType',
                values='EventTimestamp',
                aggfunc='first'
            )
        }
    }
])

# Create DataFrame `df_time_events` using a DateTimeIndex from a 'start' of '2023-01-01', 'end' of '2023-12-31', and a daily frequency.
check_pandas_84 = input_output_checker([
    {
        'input': {},
        'expected': {
            'df_time_events': pd.DataFrame(index=pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'))
        }
    }
])

# Convert the time zone of the 'datetime' column in DataFrame `df_events`, from UTC to US/Eastern, storing result as `tz_adjusted_events`.
check_pandas_85 = input_output_checker([
    {
        'input': {
            'df_events': pd.DataFrame({
                'datetime': pd.date_range(start='2023-01-01', periods=5, freq='D').tz_localize('UTC')
            }
            )
        },
        'expected': {
            'tz_adjusted_events': pd.DataFrame({
                'datetime': pd.date_range(start='2023-01-01', periods=5, freq='D').tz_localize('UTC').tz_convert('US/Eastern')
            })
        }
    }
])

# Calculate the weekly rolling sum on DataFrame `df_financial_changes` for 'ChangeAmount', storing the result in `weekly_rolling_sum`.
check_pandas_86 = input_output_checker([
    {
        'input': {
            'df_financial_changes': pd.DataFrame({
                'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
                'ChangeAmount': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
            })
        },
        'expected': {
            'weekly_rolling_sum': pd.Series(data = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 2800, 3500, 4200, 4900], name='ChangeAmount', dtype='float64', index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        }
    }
])

# Use the apply function along with a custom lambda to multiply the 'Rating' column by 2 in DataFrame `df_movie_ratings`, saving it as `scaled_ratings`.
check_pandas_87 = input_output_checker([
    {
        'input': {
            'df_movie_ratings': pd.DataFrame({
                'Movie': ['A', 'B', 'C'],
                'Rating': [5, 4, 3]
            })
        },
        'expected': {
            'scaled_ratings': pd.DataFrame({
                'Movie': ['A', 'B', 'C'],
                'Rating': [10, 8, 6]
            })
        }
    }
])

# Convert DataFrame `df_sequential` column 'Order' from int64 to int16 for memory efficiency, saving result as `optimized_sequential`.
check_pandas_88 = input_output_checker([
    {
        'input': {
            'df_sequential': pd.DataFrame({
                'Order': [1, 2, 3, 4, 5],
                'Item': ['A', 'B', 'C', 'D', 'E']
            })
        },
        'expected': {
            'optimized_sequential': pd.DataFrame({
                'Order': [1, 2, 3, 4, 5],
                'Item': ['A', 'B', 'C', 'D', 'E']
            }).astype({'Order': 'int16'})
        }
    }
])

# Remove duplicate entries based on 'Email' in DataFrame `df_email_contacts`, storing deduplicated DataFrame as `unique_email_contacts`.
check_pandas_89 = input_output_checker([
    {
        'input': {
            'df_email_contacts': pd.DataFrame({
                'Email': ['first@gmail.com', 'second@gmail.com', 'first@gmail.com'],
                'Name': ['Alice', 'Bob', 'Charlie']
            })
        },
        'expected': {
            'unique_email_contacts': pd.DataFrame({
                'Email': ['first@gmail.com', 'second@gmail.com'],
                'Name': ['Alice', 'Bob']
            })
        }
    }
])

# Perform string operation by replacing all occurrences of 'Inc.' with 'Incorporated' in the 'Company_Name' column of `df_business_registry`, storing result in `updated_business_registry`.
check_pandas_90 = input_output_checker([
    {
        'input': {
            'df_business_registry': pd.DataFrame({
                'Company_Name': ['ABC Inc.', 'XYZ Inc.']
            })
        },
        'expected': {
            'updated_business_registry': pd.DataFrame({
                'Company_Name': ['ABC Incorporated', 'XYZ Incorporated']
            })
        }
    }
])

# Select entries from DataFrame `df_jobs` with 'Role' ending in 'Engineer' using the query method, saving result as `engineer_roles`.
check_pandas_91 = input_output_checker([
    {
        'input': {
            'df_jobs': pd.DataFrame({
                'Role': ['Software Engineer', 'Data Analyst', 'Network Engineer']
            })
        },
        'expected': {
            'engineer_roles': pd.DataFrame({
                'Role': ['Software Engineer', 'Network Engineer']
            }, index=[0, 2])
        }
    }
])

# Group DataFrame `df_market_data` by 'Sector' and aggregate 'MarketCap' using the custom function to find the median, saving in `median_market_cap`.
check_pandas_92 = input_output_checker([
    {
        'input': {
            'df_market_data': pd.DataFrame({
                'Sector': ['Tech', 'Finance', 'Tech', 'Finance'],
                'MarketCap': [100, 200, 300, 400]
            })
        },
        'expected': {
            'median_market_cap': pd.Series(data=[300, 200], index=['Finance', 'Tech'], dtype='float64').rename_axis('MarketCap')
        }
    }
])

# Use vectorized operations on DataFrame `df_portfolio`, to multiply every element in 'Shares' column by its corresponding 'Price', saving the result in `portfolio_value`.
check_pandas_93 = input_output_checker([
    {
        'input': {
            'df_portfolio': pd.DataFrame({
                'Shares': [10, 20, 30],
                'Price': [100, 200, 300]
            })
        },
        'expected': {
            'portfolio_value': pd.DataFrame({
                'Shares': [10, 20, 30],
                'Price': [100, 200, 300]
            }).prod(axis=1)
        }
    }
])

# Add a 'ProfitMargin' column to DataFrame `df_sales_figures`, calculated as ('Profit' / 'Revenue') * 100 using vectorized operations, saving as `sales_with_margin`.
check_pandas_94 = input_output_checker([
    {
        'input': {
            'df_sales_figures': pd.DataFrame({
                'Revenue': [100, 200, 300],
                'Profit': [50, 100, 150]
            })
        },
        'expected': {
            'sales_with_margin': pd.DataFrame({
                'Revenue': [100, 200, 300],
                'Profit': [50, 100, 150],
                'ProfitMargin': [50.0, 50.0, 50.0]
            })
        }
    }
])

# Sort DataFrame `df_graduates` by 'GPA' in descending order, saving sorted DataFrame as `sorted_graduates`.
check_pandas_95 = input_output_checker([
    {
        'input': {
            'df_graduates': pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'GPA': [3.5, 3.2, 3.8]
            })
        },
        'expected': {
            'sorted_graduates': pd.DataFrame({
                'Name': ['Charlie', 'Alice', 'Bob'],
                'GPA': [3.8, 3.5, 3.2]
            }, index=[2, 0, 1])
        }
    }
])

# Filter DataFrame `df_emissions` for 'Country' is 'USA' and 'Year' before 2000 using boolean conditions, saving result as `us_emissions_pre2000`.
check_pandas_96 = input_output_checker([
    {
        'input': {
            'df_emissions': pd.DataFrame({
                'Country': ['USA', 'USA', 'China'],
                'Year': [1990, 2000, 1990]
            })
        },
        'expected': {
            'us_emissions_pre2000': pd.DataFrame({
                'Country': ['USA'],
                'Year': [1990]
            })
        }
    }
])

# Calculate the cumulative sum of 'Purchases' in DataFrame `df_shopper_history` grouped by 'Year', storing the result in `yearly_cumulative_purchases`.
check_pandas_97 = input_output_checker([
    {
        'input': {
            'df_shopper_history': pd.DataFrame({
                'Year': [2021, 2021, 2022, 2022],
                'Purchases': [100, 200, 300, 400]
            })
        },
        'expected': {
            'yearly_cumulative_purchases': pd.DataFrame({
                'Year': [2021, 2021, 2022, 2022],
                'Purchases': [100, 200, 300, 400]
            }).groupby('Year')['Purchases'].cumsum()
        }
    }
])

# Create DataFrame `df_series_fan_following` with integers between 1000 and 5000 equally separated, indexed by monthly dates starting from '2022-01-01', till '2022-05-01', with column name 'Fans' and frequency 'MS'.
check_pandas_98 = input_output_checker([
    {
        'input': {},
        'expected': {
            'df_series_fan_following': pd.DataFrame({
                'Fans': np.linspace(1000, 5000, 5, dtype='int'),
                'Date': pd.date_range(start='2022-01-01', periods=5, freq='MS')
            }).set_index('Date')
        }
    }
])

# Calculate difference in 'ClosingPrice' from previous day in DataFrame `df_stock_prices`, storing result as `closing_price_diff`.
check_pandas_99 = input_output_checker([
    {
        'input': {
            'df_stock_prices': pd.DataFrame({
                'Date': pd.date_range(start='2022-01-01', periods=5, freq='D'),
                'ClosingPrice': [100, 110, 120, 130, 140]
            })
        },
        'expected': {
            'closing_price_diff': pd.DataFrame({
                'Date': pd.date_range(start='2022-01-01', periods=5, freq='D'),
                'ClosingPrice': [100, 110, 120, 130, 140]
            })['ClosingPrice'].diff()
        }
    }
])

# Merge DataFrames `df_social_media_insights` and `df_campaign_performance` on 'CampaignID', using outer method saving result as `merged_campaign_data`.
check_pandas_100 = input_output_checker([
    {
        'input': {
            'df_social_media_insights': pd.DataFrame({
                'CampaignID': [1, 2],
                'Clicks': [100, 200]
            }),
            'df_campaign_performance': pd.DataFrame({
                'CampaignID': [2, 3],
                'Conversions': [10, 20]
            })
        },
        'expected': {
            'merged_campaign_data': pd.merge(
                pd.DataFrame({
                    'CampaignID': [1, 2],
                    'Clicks': [100, 200]
                }),
                pd.DataFrame({
                    'CampaignID': [2, 3],
                    'Conversions': [10, 20]
                }),
                on='CampaignID',
                how='outer'
            )
        }
    }
])
