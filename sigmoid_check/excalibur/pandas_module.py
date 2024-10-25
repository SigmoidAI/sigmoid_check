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
    elif isinstance(expected, pd.Categorical):
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
                    if all_passed is False:
                        break
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
                            if not check_equality(case['expected']['output'], result):
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

# Extract DataFrame `df_social_media_metrics` subset for rows where 'Likes' exceed 'Shares' and store it in `highly_liked_posts`.
check_pandas_101 = input_output_checker([
    {
        'input': {
            'df_social_media_metrics': pd.DataFrame({
                'Likes': [100, 200, 300],
                'Shares': [150, 150, 250]
            })
        },
        'expected': {
            'highly_liked_posts': pd.DataFrame({
                'Likes': [200, 300],
                'Shares': [150, 250]
            }, index=[1, 2])
        }
    }
])

# Use DataFrame `df_product_info` to group by 'Category', computing the minimum 'Price' for each category, storing result as `min_price_by_category`.
check_pandas_102 = input_output_checker([
    {
        'input': {
            'df_product_info': pd.DataFrame({
                'Category': ['A', 'B', 'A', 'B'],
                'Price': [100, 200, 300, 400]
            })
        },
        'expected': {
            'min_price_by_category': pd.Series(
                data=[100, 200], index=['A', 'B'], name='Price', dtype='int64'
            ).rename_axis('Category')
        }
    }
])

# Apply datetime filtering on `df_online_sessions` to store sessions in the month of January 2023 in variable `january_sessions` based on 'SessionStart'.
check_pandas_103 = input_output_checker([
    {
        'input': {
            'df_online_sessions': pd.DataFrame({
                'SessionID': [1, 2, 3, 4, 5, 6],
                'SessionStart': pd.date_range(start='2023-01-01', periods=6, freq='W')
            })
        },
        'expected': {
            'january_sessions': pd.DataFrame({
                'SessionID': [1, 2, 3, 4, 5],
                'SessionStart': pd.date_range(start='2023-01-01', periods=5, freq='W')
            })
        }
    }
])

# Use DataFrame `df_employee_entries` and fill NA in 'EntryTime' with '08:00 AM', storing the result in `filled_employee_entries`.
check_pandas_104 = input_output_checker([
    {
        'input': {
            'df_employee_entries': pd.DataFrame({
                'EmployeeID': [1, 2],
                'EntryTime': ['09:00 AM', np.nan]
            })
        },
        'expected': {
            'filled_employee_entries': pd.DataFrame({
                'EmployeeID': [1, 2],
                'EntryTime': ['09:00 AM', '08:00 AM']
            })
        }
    }
])

# Drop all columns with any NA values in DataFrame `df_transaction_records`, storing cleaned version as `non_na_transactions`.
check_pandas_105 = input_output_checker([
    {
        'input': {
            'df_transaction_records': pd.DataFrame({
                'TransactionID': [1, 2],
                'Amount': [100, np.nan]
            })
        },
        'expected': {
            'non_na_transactions': pd.DataFrame({
                'TransactionID': [1, 2],
            })
        }
    }
])

# Create a Series `series_ascending` from a list of numbers [1, 2, 3, 4, 5], using these values as the indices as well.
check_pandas_106 = input_output_checker([
    {
        'input': {},
        'expected': {
            'series_ascending': pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5])
        }
    }
])

# Use the query method on DataFrame `df_financial_audit` to extract entries with 'Audit' == 'Complete' and 'Amount' > 10000, saving it as `completed_audits`.
check_pandas_107 = input_output_checker([
    {
        'input': {
            'df_financial_audit': pd.DataFrame({
                'Audit': ['Complete', 'Incomplete'],
                'Amount': [20000, 5000]
            })
        },
        'expected': {
            'completed_audits': pd.DataFrame({
                'Audit': ['Complete'],
                'Amount': [20000]
            })
        }
    }
])

# Create a custom `percent_round` function and apply it to round the 'Progress' column in DataFrame `df_student_projects` to the nearest ten, storing result as `rounded_progress`.
check_pandas_108 = input_output_checker([
    {
        'input': {
            'df_student_projects': pd.DataFrame({
                'Project': ['A', 'B'],
                'Progress': [26, 75]
            })
        },
        'expected': {
            'rounded_progress': pd.DataFrame({
                'Project': ['A', 'B'],
                'Progress': [30, 80]
            })
        }
    }
])

# Extract the elements starting from the 10th index to the 20th index from `df_user_activity`, storing the result in `sampled_user_activity`.
check_pandas_109 = input_output_checker([
    {
        'input': {
            'df_user_activity': pd.DataFrame({
                'UserID': range(1000),
                'Activity': ['Login', 'Logout'] * 500
            })
        },
        'expected': {
            'sampled_user_activity': pd.DataFrame({
                'UserID': range(10, 20),
                'Activity': ['Login', 'Logout'] * 5
            }, index=range(10, 20))
        }
    }
])

# Use advanced indexing to set all negative values in DataFrame `df_temperature_fluctuations` to zero, storing corrected DataFrame as `non_negative_temperatures`.
check_pandas_110 = input_output_checker([
    {
        'input': {
            'df_temperature_fluctuations': pd.DataFrame({
                'Temperature': [10, -5, 20, -10]
            })
        },
        'expected': {
            'non_negative_temperatures': pd.DataFrame({
                'Temperature': [10, 0, 20, 0]
            })
        }
    }
])

# With DataFrame `df_fleet_inventory`, allocate memory efficiency by converting 'Year' column to category, saving the result as `efficient_fleet_inventory`.
check_pandas_111 = input_output_checker([
    {
        'input': {
            'df_fleet_inventory': pd.DataFrame({
                'Year': [2020, 2021, 2020, 2021]
            })
        },
        'expected': {
            'efficient_fleet_inventory': pd.DataFrame({
                'Year': [2020, 2021, 2020, 2021]
            }).astype({'Year': 'category'})
        }
    }
])

# Use DataFrame `df_respiratory_data` to calculate cumulative maximum of 'Pulse' within groups of 'PatientID', storing it as `grouped_cumulative_max`.
check_pandas_112 = input_output_checker([
    {
        'input': {
            'df_respiratory_data': pd.DataFrame({
                'PatientID': [1, 1, 2, 2],
                'Pulse': [100, 110, 120, 130]
            })
        },
        'expected': {
            'grouped_cumulative_max': pd.DataFrame({
                'PatientID': [1, 1, 2, 2],
                'Pulse': [100, 110, 120, 130]
            }).groupby('PatientID')['Pulse'].cummax()
        }
    }
])

# Group DataFrame `df_weather_statistics` and apply aggregation to find both 'mean' and 'std' of 'Temperature', storing multi-aggregate result as `weather_stats`.
check_pandas_113 = input_output_checker([
    {
        'input': {
            'df_weather_statistics': pd.DataFrame({
                'City': ['A', 'A', 'B', 'B'],
                'Temperature': [10, 20, 30, 40]
            })
        },
        'expected': {
            'weather_stats': pd.DataFrame(
                {
                    'mean': {'A': 15.0, 'B': 35.0},
                    'std': {'A': 7.0710678118654755, 'B': 7.0710678118654755}
                }
            )
        }
    }
])

# Create a hierarchical index on DataFrame `df_multilayer_data` using [('Region', 'State')], saving the result as `hierarchical_multilayer`.
check_pandas_114 = input_output_checker([
    {
        'input': {
            'df_multilayer_data': pd.DataFrame({
                'Region': ['East', 'East', 'West', 'West'],
                'State': ['NY', 'NJ', 'CA', 'WA']
            })
        },
        'expected': {
            'hierarchical_multilayer': pd.DataFrame({
                'Region': ['East', 'East', 'West', 'West'],
                'State': ['NY', 'NJ', 'CA', 'WA']
            }).set_index(['Region', 'State'])
        }
    }
])

# Calculate the exponential moving average with a span of 10 on the 'Close' column in DataFrame `df_market_activity`, storing to `ema_market_activity`.
check_pandas_115 = input_output_checker([
    {
        'input': {
            'df_market_activity': pd.DataFrame({
                'Date': pd.date_range(start='2022-01-01', periods=5, freq='D'),
                'Close': [100, 110, 120, 130, 140]
            })
        },
        'expected': {
            'ema_market_activity': pd.DataFrame({
                'Date': pd.date_range(start='2022-01-01', periods=5, freq='D'),
                'Close': [100, 110, 120, 130, 140]
            })['Close'].ewm(span=10).mean()
        }
    }
])

# Create DataFrame `df_temperature_readings` for two sensors over the year using monthly datetime index, with lineaerly increasing temperature values from 20 to 30 for Sensor1 and 15 to 25 for Sensor2.
check_pandas_116 = input_output_checker([
    {
        'input': {},
        'expected': {
            'df_temperature_readings': pd.DataFrame({
            'Sensor1': np.linspace(20, 30, num=12),
            'Sensor2': np.linspace(15, 25, num=12)
        }, index=pd.date_range(start='2023-01-01', periods=12, freq='ME'))
        }
    }
])
# Use DataFrame `df_sales_tiers` to add a 'SalesTier' column assigned by binning the 'Sales' column into 'Low', 'Medium', and 'High' categories based on [0, 5000, 10000, 15000] bins, storing as `tiered_sales`.
check_pandas_117 = input_output_checker([
    {
        'input': {
            'df_sales_tiers': pd.DataFrame({
                'Sales': [1000, 6000, 12000]
            })
        },
        'expected': {
            'tiered_sales': pd.DataFrame({
                'Sales': pd.Series([1000, 6000, 12000], dtype='int64'),
                'SalesTier': pd.Categorical(['Low', 'Medium', 'High'], categories=['Low', 'Medium', 'High'], ordered=True)
            })
        }
    }
])

# Extract month at index of DataFrame `df_time_based_events`, storing them as a new column 'EventMonth' in the DataFrame.
check_pandas_118 = input_output_checker([
    {
        'input': {
            'df_time_based_events': pd.DataFrame({
                'EventDate': pd.date_range(start='2023-01-01', periods=3, freq='ME')
            }, index=pd.date_range(start='2023-01-01', periods=3, freq='ME'))
        },
        'expected': {
            'df_time_based_events': pd.DataFrame({
                'EventDate': pd.date_range(start='2023-01-01', periods=3, freq='ME'),
                'EventMonth': pd.Series(data=[1, 2, 3], dtype='int32', index=pd.date_range(start='2023-01-01', periods=3, freq='ME'))
            }, index=pd.date_range(start='2023-01-01', periods=3, freq='ME'))
        }
    }
])

# Given a DataFrame `df_tennis_matches`, select rows using .loc where 'MatchesPlayed' > 20 and store them as `consistent_players`.
check_pandas_119 = input_output_checker([
    {
        'input': {
            'df_tennis_matches': pd.DataFrame({
                'Player': ['A', 'B', 'C'],
                'MatchesPlayed': [10, 30, 20]
            })
        },
        'expected': {
            'consistent_players': pd.DataFrame({
                'Player': ['B'],
                'MatchesPlayed': [30]
            }, index=[1])
        }
    }
])

# Utilize .iloc on DataFrame `df_daily_results` to select rows by integer location, focusing on every third row, and storing result as `every_third_result`.
check_pandas_120 = input_output_checker([
    {
        'input': {
            'df_daily_results': pd.DataFrame({
                'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
                'Result': ['Win', 'Loss', 'Win', 'Loss', 'Win']
            })
        },
        'expected': {
            'every_third_result': pd.DataFrame({
                'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
                'Result': ['Win', 'Loss', 'Win', 'Loss', 'Win']
            }).iloc[::3]
        }
    }
])

# From DataFrame `df_survey_responses`, combine 'Question' and 'Answer' columns into a single 'Response' column, storing the result as a Series `consolidated_responses` in the format 'Question: Answer'.
check_pandas_121 = input_output_checker([
    {
        'input': {
            'df_survey_responses': pd.DataFrame({
                'Question': ['Q1', 'Q2', 'Q3'],
                'Answer': ['A', 'B', 'C']
            })
        },
        'expected': {
            'consolidated_responses': pd.Series(data=['Q1: A', 'Q2: B', 'Q3: C'], dtype='object')
        }
    }
])

# Use DataFrame `df_server_logs` to group by 'ServerID' and calculate the sum and max of 'ResponseTime', storing result as `server_response_summary`.
check_pandas_122 = input_output_checker([
    {
        'input': {
            'df_server_logs': pd.DataFrame({
                'ServerID': [1, 1, 2, 2],
                'ResponseTime': [100, 200, 300, 400]
            })
        },
        'expected': {
            'server_response_summary': pd.DataFrame({
                'sum': {1: 300, 2: 700},
                'max': {1: 200, 2: 400}
            })
        }
    }
])

# Modify DataFrame `df_machine_operating` by adding column 'Downtime' calculated from 'EndTime' minus 'StartTime', storing as `operations_with_downtime`.
check_pandas_123 = input_output_checker([
    {
        'input': {
            'df_machine_operating': pd.DataFrame({
                'StartTime': pd.date_range(start='2023-01-01', periods=3, freq='D'),
                'EndTime': pd.date_range(start='2023-01-02', periods=3, freq='D')
            })
        },
        'expected': {
            'operations_with_downtime': pd.DataFrame({
                'StartTime': pd.date_range(start='2023-01-01', periods=3, freq='D'),
                'EndTime': pd.date_range(start='2023-01-02', periods=3, freq='D'),
                'Downtime': pd.date_range(start='2023-01-02', periods=3, freq='D') - pd.date_range(start='2023-01-01', periods=3, freq='D')
            })
        }
    }
])

# Remove duplicate rows from DataFrame `df_patient_visits`, considering only 'PatientID' and 'VisitDate', saving unique rows as `unique_patient_visits`.
check_pandas_124 = input_output_checker([
    {
        'input': {
            'df_patient_visits': pd.DataFrame({
                'PatientID': [1, 2, 1],
                'VisitDate': ['2023-01-01', '2023-01-02', '2023-01-01']
            })
        },
        'expected': {
            'unique_patient_visits': pd.DataFrame({
                'PatientID': [1, 2],
                'VisitDate': ['2023-01-01', '2023-01-02']
            })
        }
    }
])

# Optimize data processing speed in DataFrame `df_satellite_data` by converting all text-based columns to category type, storing efficient version as `satellite_optimized`.
check_pandas_125 = input_output_checker([
    {
        'input': {
            'df_satellite_data': pd.DataFrame({
                'SatelliteID': [1, 2],
                'SatelliteName': ['A', 'B']
            })
        },
        'expected': {
            'satellite_optimized': pd.DataFrame({
                'SatelliteID': pd.Series([1, 2], dtype='int64'),
                'SatelliteName': pd.Series(['A', 'B'], dtype='category')
            })
        }
    }
])

# Use vectorized operations on DataFrame `df_temperature_logs` to convert 'TemperatureC' to Fahrenheit, storing the result in `temperature_fahrenheit`.
check_pandas_126 = input_output_checker([
    {
        'input': {
            'df_temperature_logs': pd.DataFrame({
                'TemperatureC': [0, 10, 20]
            })
        },
        'expected': {
            'temperature_fahrenheit': pd.Series({0: 32.0, 1: 50.0, 2: 68.0})
        }
    }
])

# Group DataFrame `df_streaming_data` by 'UserID' and apply a lambda function to compute total view time, storing the result as `total_view_time`.
check_pandas_127 = input_output_checker([
    {
        'input': {
            'df_streaming_data': pd.DataFrame({
                'UserID': [1, 1, 2, 2],
                'ViewTime': [100, 200, 300, 400]
            })
        },
        'expected': {
            'total_view_time': pd.Series({1: 300, 2: 700})
        }
    }
])

# Use DataFrame `df_sales_analytics` to implement cohort analysis, calculating first purchase date and cohort index, storing result in `sales_cohorts`.
check_pandas_128 = input_output_checker([
    {
        'input': {
            'df_sales_analytics': pd.DataFrame({
                'UserID': [1, 2, 1, 2],
                'PurchaseDate': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']
            })
        },
        'expected': {
            'sales_cohorts': pd.DataFrame(
                {
                    'UserID': {0: 1, 1: 2, 2: 1, 3: 2},
                    'PurchaseDate': {
                        0: '2023-01-01',
                        1: '2023-01-02',
                        2: '2023-01-01',
                        3: '2023-01-02'
                    },
                    'CohortIndex': {
                        0: '2023-01-01',
                        1: '2023-01-02', 
                        2: '2023-01-01',
                        3: '2023-01-02'
                    }
                }
            )
        }
    }
])

# In DataFrame `df_web_traffic`, apply conversion to 'Date' column from string to datetime, saving the updated DataFrame as `web_traffic_dates`.
check_pandas_129 = input_output_checker([
    {
        'input': {
            'df_web_traffic': pd.DataFrame({
                'Date': ['2023-01-01', '2023-01-02']
            })
        },
        'expected': {
            'web_traffic_dates': pd.DataFrame({
                'Date': pd.to_datetime(['2023-01-01', '2023-01-02'])
            })
        }
    }
])

# Create DataFrame `df_energy_savings` with datetime index representing bi-weekly dates over one year, filled with repetitive 5% and 10% energy savings, stored in 'SavingsPercent'.
check_pandas_130 = input_output_checker([
    {
        'input': {},
        'expected': {
            'df_energy_savings': pd.DataFrame({
                'SavingsPercent': [5, 10] * 13,
                'Date': pd.date_range(start='2023-01-01', periods=26, freq='2W')
            }).set_index('Date')
        }
    }
])

# With DataFrame `df_vehicle_data`, apply method chaining to filter 'Type' as 'SUV' and sort by 'RecallDate', saving sorted SUVs as `sorted_suvs`.
check_pandas_131 = input_output_checker([
    {
        'input': {
            'df_vehicle_data': pd.DataFrame({
                'Type': ['SUV', 'Sedan'],
                'RecallDate': ['2023-01-01', '2023-01-02']
            })
        },
        'expected': {
            'sorted_suvs': pd.DataFrame({
                'Type': ['SUV'],
                'RecallDate': ['2023-01-01']
            })
        }
    }
])

# Extract 'year' from 'DateAdmitted' in DataFrame `df_patient_admissions` using datetime operations, storing extracted years in `admission_years`.
check_pandas_132 = input_output_checker([
    {
        'input': {
            'df_patient_admissions': pd.DataFrame({
                'DateAdmitted': pd.date_range(start='2023-01-01', periods=3, freq='D')
            })
        },
        'expected': {
            'admission_years': pd.Series(data=[2023, 2023, 2023], dtype='int32')
        }
    }
])

# Process DataFrame `df_cost_analysis` by converting 'Amount' to USD using 'Currency' which contains the type like ['EUR', 'GBP'] conversion rates being EUR: 1.12 and GBP: 1.30, storing result as `cost_analysis_usd` with column 'Amount' in 'Currency' and 'AmountUSD' in USD.
check_pandas_133 = input_output_checker([
    {
        'input': {
            'df_cost_analysis': pd.DataFrame({
                'Currency': ['EUR', 'GBP'],
                'Amount': [100, 200]
            })
        },
        'expected': {
            'cost_analysis_usd': pd.DataFrame({'Currency': {0: 'EUR', 1: 'GBP'}, 'Amount': {0: 112.00000000000001, 1: 260.0}})
        }
    }
])

# In DataFrame `df_logistics_data`, use rolling window of 30 days to calculate moving average inventory level, storing as `thirty_day_moving_inventory`.
check_pandas_134 = input_output_checker([
    {
        'input': {
            'df_logistics_data': pd.DataFrame({
                'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
                'InventoryLevel': [100, 200, 300, 400, 500]
            })
        },
        'expected': {
            'thirty_day_moving_inventory': pd.DataFrame({
                'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
                'InventoryLevel': [100, 200, 300, 400, 500]
            })['InventoryLevel'].rolling(window=30).mean()
        }
    }
])

# From DataFrame `df_sports_results`, extract top three teams based on 'Scores', sorting first, saving top teams as `top_teams`.
check_pandas_135 = input_output_checker([
    {
        'input': {
            'df_sports_results': pd.DataFrame({
                'Team': ['A', 'B', 'C'],
                'Scores': [100, 200, 300]
            })
        },
        'expected': {
            'top_teams': pd.DataFrame({
                'Team': ['C', 'B', 'A'],
                'Scores': [300, 200, 100]
            }, index=[2, 1, 0])
        }
    }
])

# Use DataFrame `df_network_activity` statistics to calculate z-scores for 'Bandwidth', storing in column 'ZscoreBandwidth' as `network_with_zscore`.
check_pandas_136 = input_output_checker([
    {
        'input': {
            'df_network_activity': pd.DataFrame({
                'Bandwidth': [100, 200, 300]
            })
        },
        'expected': {
            'network_with_zscore': pd.DataFrame({
                'Bandwidth': [100, 200, 300],
                'ZscoreBandwidth': [-1.0, 0.0, 1.0]
            })
        }
    }
])

# Perform inplace boolean update of `df_market_responses` setting all 'ResponseTime' > 300 to 300, saving updated DataFrame.
check_pandas_137 = input_output_checker([
    {
        'input': {
            'df_market_responses': pd.DataFrame({
                'ResponseTime': [100, 400]
            })
        },
        'expected': {
            'df_market_responses': pd.DataFrame({
                'ResponseTime': [100, 300]
            })
        }
    }
])

# Analyze DataFrame `df_social_behaviors` applying transform with a custom function to 'EngagementRate' to normalize within each 'Group', saving result.
check_pandas_138 = input_output_checker([
    {
        'input': {
            'df_social_behaviors': pd.DataFrame({
                'Group': ['A', 'A', 'B', 'B'],
                'EngagementRate': [0.5, 0.8, 0.6, 0.9]
            })
        },
        'expected': {
            'df_social_behaviors': pd.DataFrame(
                {
                    'Group': {0: 'A', 1: 'A', 2: 'B', 3: 'B'},
                    'EngagementRate': {0: 0.5, 1: 0.8, 2: 0.6, 3: 0.9},
                    'NormalizedEngagementRate': {0: -0.7071067811865476, 1: 0.7071067811865476, 2: -0.7071067811865476, 3: 0.7071067811865476}
                }
            )
        }
    }
])

# Use DataFrame `df_product_launch` to derive 'ResponseRate' from 'Inquiries' divided by 'Sales', multiplied by 100, storing as `launch_responses`.
check_pandas_139 = input_output_checker([
    {
        'input': {
            'df_product_launch': pd.DataFrame({
                'Inquiries': [100, 200],
                'Sales': [10, 20]
            })
        },
        'expected': {
            'launch_responses': pd.DataFrame({
                'Inquiries': [100, 200],
                'Sales': [10, 20],
                'ResponseRate': [1000.0, 1000.0]
            })
        }
    }
])

# Create a function create_series_from_dict that takes a dictionary input_dict as an argument, and returns a pandas Series with the dictionary keys as the Series index.
check_pandas_140 = functions_input_output_checker({
    'create_series_from_dict': [
        {
            'input': {'input_dict': {'A': 1, 'B': 2, 'C': 3}},
            'expected': {'output': pd.Series([1, 2, 3], index=['A', 'B', 'C'])}
        },
        {
            'input': {'input_dict': {'X': 10, 'Y': 20, 'Z': 30}},
            'expected': {'output': pd.Series([10, 20, 30], index=['X', 'Y', 'Z'])}
        },
        {
            'input': {'input_dict': {'One': 100, 'Two': 200, 'Three': 300}},
            'expected': {'output': pd.Series([100, 200, 300], index=['One', 'Two', 'Three'])}
        }
    ]
})

# Define a function filter_series_positive that takes a pandas Series data_series and returns a new Series containing only the elements where the value is positive.
check_pandas_141 = functions_input_output_checker({
    'filter_series_positive': [
        {
            'input': {'data_series': pd.Series([1, -2, 3, -4, 5])},
            'expected': {'output': pd.Series([1, 3, 5], index=[0, 2, 4])}
        },
        {
            'input': {'data_series': pd.Series([-10, 20, -30, 40, -50])},
            'expected': {'output': pd.Series([20, 40], index=[1, 3])}
        },
        {
            'input': {'data_series': pd.Series([100, -200, 300, -400, 500])},
            'expected': {'output': pd.Series([100, 300, 500], index=[0, 2, 4])}
        }
    ]
})

# Develop a function `rename_dataframe_columns` that accepts a DataFrame `df` and a dictionary `column_mapping`, and returns the DataFrame with renamed columns according to the mapping.
check_pandas_142 = functions_input_output_checker({
    'rename_dataframe_columns': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [4, 5, 6]
                }),
                'column_mapping': {'A': 'X', 'B': 'Y'}
            },
            'expected': {'output': pd.DataFrame({
                'X': [1, 2, 3],
                'Y': [4, 5, 6]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'C': [10, 20, 30],
                    'D': [40, 50, 60]
                }),
                'column_mapping': {'C': 'A', 'D': 'B'}
            },
            'expected': {'output': pd.DataFrame({
                'A': [10, 20, 30],
                'B': [40, 50, 60]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'E': [100, 200, 300],
                    'F': [400, 500, 600]
                }),
                'column_mapping': {'E': 'X', 'F': 'Y'}
            },
            'expected': {'output': pd.DataFrame({
                'X': [100, 200, 300],
                'Y': [400, 500, 600]
            })}
        }
    ]
})

# Write a function `drop_nan_rows` that takes a DataFrame `input_df` and returns a new DataFrame with all rows containing any NaN values removed.
check_pandas_143 = functions_input_output_checker({
    'drop_nan_rows': [
        {
            'input': {'input_df': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [1.0],
                'B': [4.0]
            })}
        },
        {
            'input': {'input_df': pd.DataFrame({
                'C': [10, 20, np.nan],
                'D': [40, np.nan, 60]
            })},
            'expected': {'output': pd.DataFrame({
                'C': [10.0],
                'D': [40.0]
            })}
        },
        {
            'input': {'input_df': pd.DataFrame({
                'E': [100, 200, np.nan],
                'F': [400, np.nan, 600]
            })},
            'expected': {'output': pd.DataFrame({
                'E': [100.0],
                'F': [400.0]
            })}
        }
    ]
})

# Construct a function `fill_missing_with_mean` which takes a DataFrame `df` and fills missing values in each numeric column with the mean of that column, returning the modified DataFrame.
check_pandas_144 = functions_input_output_checker({
    'fill_missing_with_mean': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, np.nan],
                'B': [4, np.nan, 6]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [1.0, 2.0, 1.5],
                'B': [4.0, 5.0, 6.0]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'C': [10, 20, np.nan],
                'D': [40, np.nan, 60]
            })},
            'expected': {'output': pd.DataFrame({
                'C': [10.0, 20.0, 15.0],
                'D': [40.0, 50.0, 60.0]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'E': [100, 200, np.nan],
                'F': [400, np.nan, 600]
            })},
            'expected': {'output': pd.DataFrame({
                'E': [100.0, 200.0, 150.0],
                'F': [400.0, 500.0, 600.0]
            })}
        }
    ]
})

# Implement a function `calculate_group_means` that takes a DataFrame `df` and a column name `group_col`, grouping by `group_col`, then returning the mean of each group as a Series.
check_pandas_145 = functions_input_output_checker({
    'calculate_group_means': [
        {
            'input': {
                'df': pd.DataFrame({
                    'Group': ['A', 'A', 'B', 'B'],
                    'Value': [1, 2, 3, 4]
                }),
                'group_col': 'Group'
            },
            'expected': {'output': pd.DataFrame(
                data={'Value': [1.5, 3.5]},
                index=pd.Index(['A', 'B'], name='Group')
            )}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Group': ['X', 'X', 'Y', 'Y'],
                    'Value': [10, 20, 30, 40]
                }),
                'group_col': 'Group'
            },
            'expected': {'output': pd.DataFrame(
                data={'Value': [15.0, 35.0]},
                index=pd.Index(['X', 'Y'], name='Group')
            )}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Group': ['M', 'M', 'N', 'N'],
                    'Value': [100, 200, 300, 400]
                }),
                'group_col': 'Group'
            },
            'expected': {'output': pd.DataFrame(
                data={'Value': [150.0, 350.0]},
                index=pd.Index(['M', 'N'], name='Group')
            )}
        }
    ]
})

# Design a function `subset_dataframe_label` that accepts a DataFrame `df`, a list `rows` of row labels, and returns a subset DataFrame containing only those rows.
check_pandas_146 = functions_input_output_checker({
    'subset_dataframe_label': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [4, 5, 6]
                }),
                'rows': [0, 2]
            },
            'expected': {'output': pd.DataFrame({
                'A': [1, 3],
                'B': [4, 6]
            }, index=[0, 2])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'C': [10, 20, 30],
                    'D': [40, 50, 60]
                }),
                'rows': [0, 1]
            },
            'expected': {'output': pd.DataFrame({
                'C': [10, 20],
                'D': [40, 50]
            }, index=[0, 1])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'E': [100, 200, 300],
                    'F': [400, 500, 600]
                }),
                'rows': [1, 2]
            },
            'expected': {'output': pd.DataFrame({
                'E': [200, 300],
                'F': [500, 600]
            }, index=[1, 2])}
        }
    ]
})

# Define a function `merge_dataframes_on_key` that takes two DataFrames `df1`, `df2`, and a string `key`, merging them on the shared key column and returning the merged DataFrame.
check_pandas_147 = functions_input_output_checker({
    'merge_dataframes_on_key': [
        {
            'input': {
                'df1': pd.DataFrame({
                    'Key': ['A', 'B'],
                    'Value1': [1, 2]
                }),
                'df2': pd.DataFrame({
                    'Key': ['A', 'B'],
                    'Value2': [10, 20]
                }),
                'key': 'Key'
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['A', 'B'],
                'Value1': [1, 2],
                'Value2': [10, 20]
            })}
        },
        {
            'input': {
                'df1': pd.DataFrame({
                    'Key': ['X', 'Y'],
                    'Value1': [10, 20]
                }),
                'df2': pd.DataFrame({
                    'Key': ['X', 'Y'],
                    'Value2': [100, 200]
                }),
                'key': 'Key'
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['X', 'Y'],
                'Value1': [10, 20],
                'Value2': [100, 200]
            })}
        },
        {
            'input': {
                'df1': pd.DataFrame({
                    'Key': ['M', 'N'],
                    'Value1': [100, 200]
                }),
                'df2': pd.DataFrame({
                    'Key': ['M', 'N'],
                    'Value2': [1000, 2000]
                }),
                'key': 'Key'
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['M', 'N'],
                'Value1': [100, 200],
                'Value2': [1000, 2000]
            })}
        }
    ]
})

# Write a function `aggregate_sales_by_region` which accepts a DataFrame `sales_df` that includes columns 'Region' and 'Sales', and returns a DataFrame with the total sales per region.
check_pandas_148 = functions_input_output_checker({
    'aggregate_sales_by_region': [
        {
            'input': {'sales_df': pd.DataFrame({
                'Region': ['A', 'A', 'B', 'B'],
                'Sales': [100, 200, 300, 400]
            })},
            'expected': {'output': pd.Series({'A': 300, 'B': 700})}
        },
        {
            'input': {'sales_df': pd.DataFrame({
                'Region': ['X', 'X', 'Y', 'Y'],
                'Sales': [1000, 2000, 3000, 4000]
            })},
            'expected': {'output': pd.Series({'X': 3000, 'Y': 7000})}
        },
        {
            'input': {'sales_df': pd.DataFrame({
                'Region': ['M', 'M', 'N', 'N'],
                'Sales': [10000, 20000, 30000, 40000]
            })},
            'expected': {'output': pd.Series({'M': 30000, 'N': 70000})}
        }
    ]
})

# Implement a function `pivot_table_for_analysis` that takes a DataFrame `df` and strings `index`, `columns`, `values`, and returns a pivot table using those specifications.
check_pandas_149 = functions_input_output_checker({
    'pivot_table_for_analysis': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': ['X', 'X', 'Y', 'Y'],
                    'B': ['A', 'B', 'A', 'B'],
                    'C': [1, 2, 3, 4]
                }),
                'index': 'A',
                'columns': 'B',
                'values': 'C'
            },
            'expected': {'output': pd.DataFrame({'A': {'X': 1.0, 'Y': 3.0}, 'B': {'X': 2.0, 'Y': 4.0}})}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': ['A', 'A', 'B', 'B'],
                    'Y': ['X', 'Y', 'X', 'Y'],
                    'Z': [10, 20, 30, 40]
                }),
                'index': 'X',
                'columns': 'Y',
                'values': 'Z'
            },
            'expected': {'output': pd.DataFrame({'X': {'A': 10.0, 'B': 30.0}, 'Y': {'A': 20.0, 'B': 40.0}})}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': ['A', 'A', 'B', 'B'],
                    'N': ['X', 'Y', 'X', 'Y'],
                    'O': [100, 200, 300, 400]
                }),
                'index': 'M',
                'columns': 'N',
                'values': 'O'
            },
            'expected': {'output': pd.DataFrame({'X': {'A': 100.0, 'B': 300.0}, 'Y': {'A': 200.0, 'B': 400.0}})}
        }
    ]
})

# Create a function `calculate_rolling_average` that accepts a DataFrame `df` and an integer `window` to compute the rolling average of a numeric column `column_name`, returning the updated series.
check_pandas_150 = functions_input_output_checker({
    'calculate_rolling_average': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3, 4, 5],
                    'B': [10, 20, 30, 40, 50]
                }),
                'window': 2,
                'column_name': 'B'
            },
            'expected': {'output': pd.Series({0: np.nan, 1: 15.0, 2: 25.0, 3: 35.0, 4: 45.0})}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30, 40, 50],
                    'Y': [100, 200, 300, 400, 500]
                }),
                'window': 3,
                'column_name': 'Y'
            },
            'expected': {'output': pd.Series({0: np.nan, 1: np.nan, 2: 200.0, 3: 300.0, 4: 400.0})}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300, 400, 500],
                    'N': [1000, 2000, 3000, 4000, 5000]
                }),
                'window': 4,
                'column_name': 'N'
            },
            'expected': {'output': pd.Series({0: np.nan, 1: np.nan, 2: np.nan, 3: 2500.0, 4: 3500.0})}
        }
    ]
})

# Construct a function `resample_time_series` which takes a time-indexed DataFrame `time_df` and a frequency string `freq`, resampling the DataFrame to the new frequency and summing, returning the result.
check_pandas_151 = functions_input_output_checker({
    'resample_time_series': [
        {
            'input': {
                'time_df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }, index=pd.date_range(start='2023-01-01', periods=3, freq='D')),
                'freq': 'W'
            },
            'expected': {'output': pd.DataFrame(
                {
                    'A': {
                        pd.Timestamp('2023-01-01 00:00:00'): 1,
                        pd.Timestamp('2023-01-08 00:00:00'): 5
                    },
                    'B': {
                        pd.Timestamp('2023-01-01 00:00:00'): 10,
                        pd.Timestamp('2023-01-08 00:00:00'): 50
                    }
                }
            )}
        },
        {
            'input': {
                'time_df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }, index=pd.date_range(start='2023-01-01', periods=3, freq='D')),
                'freq': 'W'
            },
            'expected': {'output': pd.DataFrame(
                {
                    'X': {
                        pd.Timestamp('2023-01-01 00:00:00'): 10,
                        pd.Timestamp('2023-01-08 00:00:00'): 50
                    },
                    'Y': {
                        pd.Timestamp('2023-01-01 00:00:00'): 100,
                        pd.Timestamp('2023-01-08 00:00:00'): 500
                    }
                }
            )}
        },
        {
            'input': {
                'time_df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }, index=pd.date_range(start='2023-01-01', periods=3, freq='D')),
                'freq': 'W'
            },
            'expected': {'output': pd.DataFrame(
                {
                    'M': {
                        pd.Timestamp('2023-01-01 00:00:00'): 100,
                        pd.Timestamp('2023-01-08 00:00:00'): 500
                    },
                    'N': {
                        pd.Timestamp('2023-01-01 00:00:00'): 1000,
                        pd.Timestamp('2023-01-08 00:00:00'): 5000
                    }
                }
            )}
        }
    ]
})

# Write a function `expand_string_columns` that takes a DataFrame `df` and a list of columns `string_columns`, expanding each string column to lowercase, and returns the modified DataFrame.
check_pandas_152 = functions_input_output_checker({
    'expand_string_columns': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': ['Apple', 'Banana'],
                    'B': ['Cherry', 'Date']
                }),
                'string_columns': ['A', 'B']
            },
            'expected': {'output': pd.DataFrame({
                'A': ['apple', 'banana'],
                'B': ['cherry', 'date']
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': ['Elephant', 'Frog'],
                    'Y': ['Goose', 'Horse']
                }),
                'string_columns': ['X', 'Y']
            },
            'expected': {'output': pd.DataFrame({
                'X': ['elephant', 'frog'],
                'Y': ['goose', 'horse']
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': ['Iguana', 'Jaguar'],
                    'N': ['Kangaroo', 'Lion']
                }),
                'string_columns': ['M', 'N']
            },
            'expected': {'output': pd.DataFrame({
                'M': ['iguana', 'jaguar'],
                'N': ['kangaroo', 'lion']
            })}
        }
    ]
})

# Design a function `convert_to_datetime_index` that accepts a DataFrame `df` and a column name `date_col`, converting it to a DateTimeIndex, and returning the updated DataFrame.
check_pandas_153 = functions_input_output_checker({
    'convert_to_datetime_index': [
        {
            'input': {
                'df': pd.DataFrame({
                    'Date': ['2023-01-01', '2023-01-02'],
                    'Value': [10, 20]
                }),
                'date_col': 'Date'
            },
            'expected': {'output': pd.DataFrame({
                'Value': [10, 20]
            }, index=pd.Series(data=['2023-01-01', '2023-01-02'], name='Date', dtype='<M8[ns]'))}    
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Date': ['2023-02-01', '2023-02-02'],
                    'Value': [100, 200]
                }),
                'date_col': 'Date'
            },
            'expected': {'output': pd.DataFrame({
                'Value': [100, 200]
            }, index=pd.Series(data=['2023-02-01', '2023-02-02'], name='Date', dtype='<M8[ns]'))}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Date': ['2023-03-01', '2023-03-02'],
                    'Value': [1000, 2000]
                }),
                'date_col': 'Date'
            },
            'expected': {'output': pd.DataFrame({
                'Value': [1000, 2000]
            }, index=pd.Series(data=['2023-03-01', '2023-03-02'], name='Date', dtype='<M8[ns]'))}
        }
    ]
})

# Implement a function `identify_and_remove_outliers` that identifies outliers in a Series `data_series` using a specified `threshold` by removing the values outside of the `threshodl` multiplied by the standard deviation from the mean.
check_pandas_154 = functions_input_output_checker({
    'identify_and_remove_outliers': [
        {
            'input': {
                'data_series': pd.Series([1, 2, 3, 10, 20, 30]),
                'threshold': 5
            },
            'expected': {'output': pd.Series([1, 2, 3, 10, 20, 30])}
        },
        {
            'input': {
                'data_series': pd.Series([10, 20, 30, 100, 200, 300]),
                'threshold': 1
            },
            'expected': {'output': pd.Series([10, 20, 30, 100, 200])}
        },
        {
            'input': {
                'data_series': pd.Series([100, 200, 300, 1000, 2000, 3000]),
                'threshold': 0
            },
            'expected': {'output': pd.Series([], dtype='int64')}
        }
    ]
})

# Create a function `calculate_percentage_change` which computes the percentage change over time for a Series `time_series` and returns the updated Series with NaN for the first entry.
check_pandas_155 = functions_input_output_checker({
    'calculate_percentage_change': [
        {
            'input': {'time_series': pd.Series([1, 2, 3, 4, 5])},
            'expected': {'output': pd.Series({0: np.nan, 1: 1.0, 2: 0.5, 3: 0.33333333333333326, 4: 0.25})}
        },
        {
            'input': {'time_series': pd.Series([10, 20, 30, 40, 50])},
            'expected': {'output': pd.Series({0: np.nan, 1: 1.0, 2: 0.5, 3: 0.33333333333333326, 4: 0.25})}
        },
        {
            'input': {'time_series': pd.Series([100, 200, 300, 400, 500])},
            'expected': {'output': pd.Series({0: np.nan, 1: 1.0, 2: 0.5, 3: 0.33333333333333326, 4: 0.25})}
        }
    ]
})

# Define a function `categorize_based_on_values` which takes a DataFrame `df`, a column `categorical_col`, and returns a DataFrame with additional column 'Category' based on ranges in `categorical_col` with labels ['Low', 'Medium', 'High'] and bins [0, 100, 200, 300].
check_pandas_156 = functions_input_output_checker({
    'categorize_based_on_values': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'categorical_col': 'B'
            },
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30],
                'Category': pd.Categorical(['Low', 'Low', 'Low'], categories=['Low', 'Medium', 'High'], ordered=True)
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'categorical_col': 'Y'
            },
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300],
                'Category': pd.Categorical(['Low', 'Medium', 'High'], categories=['Low', 'Medium', 'High'], ordered=True)
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'categorical_col': 'N'
            },
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000],
                'Category': pd.Categorical([np.nan, np.nan, np.nan], categories=['Low', 'Medium', 'High'], ordered=True)
            })}
        }
    ]
})

# Write a function `shift_dataframe_rows` that takes a DataFrame `df` and an integer `periods`, shifting all rows by the specified number of periods and returning the DataFrame.
check_pandas_157 = functions_input_output_checker({
    'shift_dataframe_rows': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'periods': 1
            },
            'expected': {'output': pd.DataFrame({
                'A': [np.nan, 1, 2],
                'B': [np.nan, 10, 20]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'periods': 2
            },
            'expected': {'output': pd.DataFrame({
                'X': [np.nan, np.nan, 10],
                'Y': [np.nan, np.nan, 100]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'periods': 3
            },
            'expected': {'output': pd.DataFrame({
                'M': [np.nan, np.nan, np.nan],
                'N': [np.nan, np.nan, np.nan]
            })}
        }
    ]
})

# Develop a function `aggregate_and_flatten_grouped` that takes a grouped DataFrame `group_df` and returns a flattened DataFrame with 'sum' and 'count' aggregation for each group and reseted index.
check_pandas_158 = functions_input_output_checker({
    'aggregate_and_flatten_grouped': [
        {
            'input': {'group_df': pd.DataFrame({
                'Group': ['A', 'A', 'B', 'B'],
                'Value': [1, 2, 3, 4]
            }).groupby('Group')},
            'expected': {'output': pd.DataFrame(
                {
                    ('Group', ''): {0: 'A', 1: 'B'},
                    ('Value', 'sum'): {0: 3, 1: 7},
                    ('Value', 'count'): {0: 2, 1: 2}
                }
            )}
        },
        {
            'input': {'group_df': pd.DataFrame({
                'Group': ['X', 'X', 'Y', 'Y'],
                'Value': [10, 20, 30, 40]
            }).groupby('Group')},
            'expected': {'output': pd.DataFrame(
                {
                    ('Group', ''): {0: 'X', 1: 'Y'},
                    ('Value', 'sum'): {0: 30, 1: 70},
                    ('Value', 'count'): {0: 2, 1: 2}
                }
            )}
        },
        {
            'input': {'group_df': pd.DataFrame({
                'Group': ['M', 'M', 'N', 'N'],
                'Value': [100, 200, 300, 400]
            }).groupby('Group')},
            'expected': {'output': pd.DataFrame(
                {
                    ('Group', ''): {0: 'M', 1: 'N'},
                    ('Value', 'sum'): {0: 300, 1: 700},
                    ('Value', 'count'): {0: 2, 1: 2}
                }
            )}
        }
    ]
})

# Construct a function named `remove_duplicates_by_columns` that takes a DataFrame `df` and a list `subset_columns`, and removes duplicate rows based on these columns, returning the resulting DataFrame.
check_pandas_159 = functions_input_output_checker({
    'remove_duplicates_by_columns': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 2, 3],
                    'B': [10, 20, 20, 30]
                }),
                'subset_columns': ['A']
            },
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            }, index=[0, 1, 3])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 20, 30],
                    'Y': [100, 200, 200, 300]
                }),
                'subset_columns': ['X']
            },
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            }, index=[0, 1, 3])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 200, 300],
                    'N': [1000, 2000, 2000, 3000]
                }),
                'subset_columns': ['M']
            },
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            }, index=[0, 1, 3])}
        }
    ]
})

# Design a function `calculate_memory_usage` that takes a DataFrame `df` and returns the total memory usage in MB, both with and without optimizations for all columns possible.
check_pandas_160 = functions_input_output_checker({
    'calculate_memory_usage': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': (np.float64(0.000171661376953125), np.float64(4.57763671875e-05))}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': (np.float64(0.000171661376953125), np.float64(4.57763671875e-05))}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': (np.float64(0.000171661376953125), np.float64(4.57763671875e-05))}
        }
    ]
})

# Implement a function `map_values_with_dict` which accepts a DataFrame `df`, a column `target_col`, and a dictionary `value_map`, returning the updated DataFrame after mapping.
check_pandas_161 = functions_input_output_checker({
    'map_values_with_dict': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': ['X', 'Y', 'Z'],
                    'B': [10, 20, 30]
                }),
                'target_col': 'A',
                'value_map': {'X': 'Apple', 'Y': 'Banana', 'Z': 'Cherry'}
            },
            'expected': {'output': pd.DataFrame({
                'A': ['Apple', 'Banana', 'Cherry'],
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': ['A', 'B', 'C'],
                    'Y': [100, 200, 300]
                }),
                'target_col': 'X',
                'value_map': {'A': 'Apple', 'B': 'Banana', 'C': 'Cherry'}
            },
            'expected': {'output': pd.DataFrame({
                'X': ['Apple', 'Banana', 'Cherry'],
                'Y': [100, 200, 300]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': ['1', '2', '3'],
                    'N': [1000, 2000, 3000]
                }),
                'target_col': 'M',
                'value_map': {'1': 'Apple', '2': 'Banana', '3': 'Cherry'}
            },
            'expected': {'output': pd.DataFrame({
                'M': ['Apple', 'Banana', 'Cherry'],
                'N': [1000, 2000, 3000]
            })}
        }
    ]
})

# Write a function `select_top_n_rows_based_on_column` that takes a DataFrame `df`, a column `target_col`, and an integer `n`, and returns the top `n` rows sorted by `target_col`.
check_pandas_162 = functions_input_output_checker({
    'select_top_n_rows_based_on_column': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': ['X', 'Y', 'Z'],
                    'B': [10, 20, 30]
                }),
                'target_col': 'B',
                'n': 2
            },
            'expected': {'output': pd.DataFrame(
                {
                    'A': {2: 'Z', 1: 'Y'},
                    'B': {2: 30, 1: 20}
                }
            )}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': ['A', 'B', 'C'],
                    'Y': [100, 200, 300]
                }),
                'target_col': 'Y',
                'n': 2
            },
            'expected': {'output': pd.DataFrame(
                {
                    'X': {2: 'C', 1: 'B'},
                    'Y': {2: 300, 1: 200}
                }
            )}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': ['1', '2', '3'],
                    'N': [1000, 2000, 3000]
                }),
                'target_col': 'N',
                'n': 2
            },
            'expected': {'output': pd.DataFrame(
                {
                    'M': {2: '3', 1: '2'},
                    'N': {2: 3000, 1: 2000}
                }
            )}
        }
    ]
})

# Create a function `replace_substrings_in_column` that takes a DataFrame `df`, a column `text_col`, a string `old`, and a string `new`, replacing all occurrences of `old` with `new` in `text_col`.
check_pandas_163 = functions_input_output_checker({
    'replace_substrings_in_column': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': ['Apple', 'Banana', 'Cherry'],
                    'B': [10, 20, 30]
                }),
                'text_col': 'A',
                'old': 'a',
                'new': 'X'
            },
            'expected': {'output': pd.DataFrame({
                'A': ['Apple', 'BXnXnX', 'Cherry'],
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': ['Apple', 'Banana', 'Cherry'],
                    'Y': [100, 200, 300]
                }),
                'text_col': 'X',
                'old': 'a',
                'new': 'X'
            },
            'expected': {'output': pd.DataFrame(
                {
                    'X': ['Apple', 'BXnXnX', 'Cherry'],
                    'Y': [100, 200, 300]
                }
            )}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': ['Apple', 'Banana', 'Cherry'],
                    'N': [1000, 2000, 3000]
                }),
                'text_col': 'M',
                'old': 'e',
                'new': 'X'
            },
            'expected': {'output': pd.DataFrame(
                {
                    'M': ['ApplX', 'Banana', 'ChXrry'],
                    'N': [1000, 2000, 3000]
                }
            )}
        }
    ]
})

# Define a function `apply_discretization_binner` which bins Series `data_series` into a specified number of discrete intervals `n_bins` and returns the binned Series.
check_pandas_164 = functions_input_output_checker({
    'apply_discretization_binner': [
        {
            'input': {
                'data_series': pd.Series([1, 2, 3, 4, 5]),
                'n_bins': 2
            },
            'expected': {'output': pd.cut(pd.Series([1, 2, 3, 4, 5]), bins=2)}
        },
        {
            'input': {
                'data_series': pd.Series([10, 20, 30, 40, 50]),
                'n_bins': 3
            },
            'expected': {'output': pd.cut(pd.Series([10, 20, 30, 40, 50]), bins=3)}
        },
        {
            'input': {
                'data_series': pd.Series([100, 200, 300, 400, 500]),
                'n_bins': 4
            },
            'expected': {'output': pd.cut(pd.Series([100, 200, 300, 400, 500]), bins=4)}
        }
    ]
})

# Write a function `generate_descriptive_statistics` that takes a DataFrame `df` and returns a DataFrame with descriptive statistics such as mean, median, and standard deviation for all numeric columns.
check_pandas_165 = functions_input_output_checker({
    'generate_descriptive_statistics': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame(
                {
                    'A': {
                        'count': 3.0,
                        'mean': 2.0,
                        'std': 1.0,
                        'min': 1.0,
                        '25%': 1.5,
                        '50%': 2.0,
                        '75%': 2.5,
                        'max': 3.0
                    },
                    'B': {
                        'count': 3.0,
                        'mean': 20.0,
                        'std': 10.0,
                        'min': 10.0,
                        '25%': 15.0,
                        '50%': 20.0,
                        '75%': 25.0,
                        'max': 30.0
                    }
                }
            )}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame(
                {
                    'X': {
                        'count': 3.0,
                        'mean': 20.0,
                        'std': 10.0,
                        'min': 10.0,
                        '25%': 15.0,
                        '50%': 20.0,
                        '75%': 25.0,
                        'max': 30.0
                    },
                    'Y': {
                        'count': 3.0,
                        'mean': 200.0,
                        'std': 100.0,
                        'min': 100.0,
                        '25%': 150.0,
                        '50%': 200.0,
                        '75%': 250.0,
                        'max': 300.0
                    }
                }
            )}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame(
                {
                    'M': {
                        'count': 3.0,
                        'mean': 200.0,
                        'std': 100.0,
                        'min': 100.0,
                        '25%': 150.0,
                        '50%': 200.0,
                        '75%': 250.0,
                        'max': 300.0
                    },
                    'N': {
                        'count': 3.0,
                        'mean': 2000.0,
                        'std': 1000.0,
                        'min': 1000.0,
                        '25%': 1500.0,
                        '50%': 2000.0,
                        '75%': 2500.0,
                        'max': 3000.0
                    }
                }
            )}
        }
    ]
})

# Implement a function `convert_column_dtype` that accepts a DataFrame `df`, a column name `col`, and a data type `new_type`, and returns the DataFrame with `col` converted to `new_type`.
check_pandas_166 = functions_input_output_checker({
    'convert_column_dtype': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'col': 'A',
                'new_type': float
            },
            'expected': {'output': pd.DataFrame({
                'A': [1.0, 2.0, 3.0],
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'col': 'Y',
                'new_type': float
            },
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100.0, 200.0, 300.0]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'col': 'N',
                'new_type': float
            },
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000.0, 2000.0, 3000.0]
            })}
        }
    ]
})

# Develop a function `sort_dataframe_by_multiple_columns` taking DataFrame `df` and a list `columns_list` to sort the DataFrame by these columns, returning the sorted DataFrame.
check_pandas_167 = functions_input_output_checker({
    'sort_dataframe_by_multiple_columns': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'columns_list': ['A']
            },
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'columns_list': ['Y']
            },
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'columns_list': ['M']
            },
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })}
        }
    ]
})

# Create a function `create_time_based_features` which accepts a DataFrame `time_df` with a 'Timestamp' column and returns the DataFrame with new columns for hour, day, and month.
check_pandas_168 = functions_input_output_checker({
    'create_time_based_features': [
        {
            'input': {
                'time_df': pd.DataFrame({
                    'Timestamp': pd.to_datetime(['2023-01-01 10:00:00', '2023-01-02 11:00:00', '2023-01-03 12:00:00'])
                }),
            },
            'expected': {'output': pd.DataFrame({
                'Timestamp': pd.to_datetime(['2023-01-01 10:00:00', '2023-01-02 11:00:00', '2023-01-03 12:00:00']),
                'Hour': pd.Series([10, 11, 12], dtype='int32'),
                'Day': pd.Series([1, 2, 3], dtype='int32'),
                'Month': pd.Series([1, 1, 1], dtype='int32')
            })}
        },
        {
            'input': {
                'time_df': pd.DataFrame({
                    'Timestamp': pd.to_datetime(['2023-02-01 10:00:00', '2023-02-02 11:00:00', '2023-02-03 12:00:00'])
                }),
            },
            'expected': {'output': pd.DataFrame({
                'Timestamp': pd.to_datetime(['2023-02-01 10:00:00', '2023-02-02 11:00:00', '2023-02-03 12:00:00']),
                'Hour': pd.Series([10, 11, 12], dtype='int32'),
                'Day': pd.Series([1, 2, 3], dtype='int32'),
                'Month': pd.Series([2, 2, 2], dtype='int32')
            })}
        },
        {
            'input': {
                'time_df': pd.DataFrame({
                    'Timestamp': pd.to_datetime(['2023-03-01 10:00:00', '2023-03-02 11:00:00', '2023-03-03 12:00:00'])
                }),
            },
            'expected': {'output': pd.DataFrame({
                'Timestamp': pd.to_datetime(['2023-03-01 10:00:00', '2023-03-02 11:00:00', '2023-03-03 12:00:00']),
                'Hour': pd.Series([10, 11, 12], dtype='int32'),
                'Day': pd.Series([1, 2, 3], dtype='int32'),
                'Month': pd.Series([3, 3, 3], dtype='int32')
            })}
        }
    ]
})

# Create a function `analyze_sales_data` that takes a DataFrame `sales_df` with columns 'Date', 'Region', and 'Sales'. The function should: Convert 'Date' to a DateTime object; Filter out any rows where 'Sales' is negative; Group by 'Region' to calculate the total and average sales; Return a DataFrame with columns 'Region', 'TotalSales', 'AverageSales';
check_pandas_169 = functions_input_output_checker({
    'analyze_sales_data': [
        {
            'input': {
                'sales_df': pd.DataFrame({
                    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
                    'Region': ['A', 'A', 'B'],
                    'Sales': [100, 200, -300]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Region': ['A'],
                'TotalSales': [300],
                'AverageSales': [150.0]
            })}
        },
        {
            'input': {
                'sales_df': pd.DataFrame({
                    'Date': ['2023-02-01', '2023-02-02', '2023-02-03'],
                    'Region': ['B', 'B', 'C'],
                    'Sales': [100, 200, 300]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Region': ['B', 'C'],
                'TotalSales': [300, 300],
                'AverageSales': [150.0, 300.0]
            })}
        },
        {
            'input': {
                'sales_df': pd.DataFrame({
                    'Date': ['2023-03-01', '2023-03-02', '2023-03-03'],
                    'Region': ['C', 'C', 'D'],
                    'Sales': [100, 200, 300]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Region': ['C', 'D'],
                'TotalSales': [300, 300],
                'AverageSales': [150.0, 300.0]
            })}
        }
    ]
})

# Write a function `clean_and_merge_datasets` that takes two DataFrames `df_left` and `df_right`, and: Fills NA values in `df_left` with 0; Drops any duplicate rows in `df_right`; Merges the cleaned DataFrames on a common column 'Key', using an outer join; Returns the merged DataFrame sorted by 'Key';
check_pandas_170 = functions_input_output_checker({
    'clean_and_merge_datasets': [
        {
            'input': {
                'df_left': pd.DataFrame({
                    'Key': ['A', 'B', 'C'],
                    'Value': [100, np.nan, 300]
                }),
                'df_right': pd.DataFrame({
                    'Key': ['A', 'B', 'B'],
                    'Value': [10, 20, 30]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['A', 'B', 'B', 'C'],
                'Value_x': [100.0, 0.0, 0.0, 300.0],
                'Value_y': [10, 20, 30, np.nan]
            })}
        },
        {
            'input': {
                'df_left': pd.DataFrame({
                    'Key': ['X', 'Y', 'Z'],
                    'Value': [100, np.nan, 300]
                }),
                'df_right': pd.DataFrame({
                    'Key': ['X', 'Y', 'Y'],
                    'Value': [10, 20, 30]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['X', 'Y', 'Y', 'Z'],
                'Value_x': [100.0, 0.0, 0.0, 300.0],
                'Value_y': [10, 20, 30, np.nan]
            })}
        },
        {
            'input': {
                'df_left': pd.DataFrame({
                    'Key': ['M', 'N', 'O'],
                    'Value': [100, np.nan, 300]
                }),
                'df_right': pd.DataFrame({
                    'Key': ['M', 'N', 'N'],
                    'Value': [10, 20, 30]
                })
            },
            'expected': {'output': pd.DataFrame({
                'Key': ['M', 'N', 'N', 'O'],
                'Value_x': [100.0, 0.0, 0.0, 300.0],
                'Value_y': [10, 20, 30, np.nan]
            })}
        }
    ]
})

# Develop a function `process_sensor_data_batch` that receives a DataFrame `sensor_df` containing 'SensorID', 'ReadingValue', 'Timestamp'. Convert 'Timestamp' to datetime format; Ensure all 'ReadingValue' entries are non-negative; Calculate the mean and standard deviation of 'ReadingValue' for each 'SensorID'; Return a DataFrame with 'SensorID', 'MeanReading', 'StdDevReading';
check_pandas_171 = functions_input_output_checker({
    'process_sensor_data_batch': [
        {
            'input': {
                'sensor_df': pd.DataFrame({
                    'SensorID': ['A', 'A', 'B'],
                    'ReadingValue': [100, 200, -300],
                    'Timestamp': ['2023-01-01', '2023-01-02', '2023-01-03']
                })
            },
            'expected': {'output': pd.DataFrame({
                'SensorID': ['A'],
                'MeanReading': [150.0],
                'StdDevReading': [70.71067811865476]
            })}
        },
        {
            'input': {
                'sensor_df': pd.DataFrame({
                    'SensorID': ['B', 'B', 'C'],
                    'ReadingValue': [100, 200, 300],
                    'Timestamp': ['2023-02-01', '2023-02-02', '2023-02-03']
                })
            },
            'expected': {'output': pd.DataFrame({
                'SensorID': ['B', 'C'],
                'MeanReading': [150.0, 300.0],
                'StdDevReading': [70.71067811865476, np.nan]
            })}
        },
        {
            'input': {
                'sensor_df': pd.DataFrame({
                    'SensorID': ['C', 'C', 'D'],
                    'ReadingValue': [100, 200, 300],
                    'Timestamp': ['2023-03-01', '2023-03-02', '2023-03-03']
                })
            },
            'expected': {'output': pd.DataFrame({
                'SensorID': ['C', 'D'],
                'MeanReading': [150.0, 300.0],
                'StdDevReading': [70.71067811865476, np.nan]
            })}
        }
    ]
})

# Construct a function `analyze_customer_behaviors` to handle a DataFrame `customer_df` with columns 'CustomerID', 'PurchaseAmount', 'VisitTimestamp'. Convert 'VisitTimestamp' to a DateTimeIndex; Filter to include only purchases greater than a specified `min_purchase`; Group by 'CustomerID' to determine the total and count of purchases; Return a DataFrame with 'CustomerID', 'TotalPurchases', 'NumberVisits', and attach the most recent visit date;
check_pandas_172 = functions_input_output_checker({
    'analyze_customer_behaviors': [
        {
            'input': {
                'customer_df': pd.DataFrame({
                    'CustomerID': ['A', 'A', 'B'],
                    'PurchaseAmount': [100, 200, 300],
                    'VisitTimestamp': ['2023-01-01', '2023-01-02', '2023-01-03']
                }),
                'min_purchase': 150
            },
            'expected': {'output': pd.DataFrame({
                'CustomerID': ['A', 'B'],
                'TotalPurchases': [200, 300],
                'NumberVisits': [1, 1],
                'MostRecentVisit': pd.to_datetime(['2023-01-02', '2023-01-03'])
            })}
        },
        {
            'input': {
                'customer_df': pd.DataFrame({
                    'CustomerID': ['B', 'B', 'C'],
                    'PurchaseAmount': [100, 200, 300],
                    'VisitTimestamp': ['2023-02-01', '2023-02-02', '2023-02-03']
                }),
                'min_purchase': 250
            },
            'expected': {'output': pd.DataFrame({
                'CustomerID': ['C'],
                'TotalPurchases': [300],
                'NumberVisits': [1],
                'MostRecentVisit': pd.to_datetime(['2023-02-03'])
            })}
        },
        {
            'input': {
                'customer_df': pd.DataFrame({
                    'CustomerID': ['C', 'C', 'D'],
                    'PurchaseAmount': [100, 200, 300],
                    'VisitTimestamp': ['2023-03-01', '2023-03-02', '2023-03-03']
                }),
                'min_purchase': 250
            },
            'expected': {'output': pd.DataFrame({
                'CustomerID': ['D'],
                'TotalPurchases': [300],
                'NumberVisits': [1],
                'MostRecentVisit': pd.to_datetime(['2023-03-03'])
            })}
        }
    ]
})

# Create a function `transform_financial_data` that processes a DataFrame `financial_df` including columns 'AccountID', 'TransactionDate', 'Amount'. Parse 'TransactionDate' into datetime and set as index; Filter 'Amount' to exclude NaN and zero values; Extract month and year from 'TransactionDate' into new columns; Group by 'AccountID' and 'Year' to summarize monthly 'Amount' into sum and mean, returning a structured DataFrame;
check_pandas_173 = functions_input_output_checker({
    'transform_financial_data': [
        {
            'input': {
                'financial_df': pd.DataFrame({
                    'AccountID': ['A1', 'A1', 'B1'],
                    'TransactionDate': ['2023-01-15', '2023-01-20', '2023-02-10'],
                    'Amount': [100.0, 200.0, 300.0]
                })
            },
            'expected': {'output': pd.DataFrame({
                'AccountID': ['A1', 'B1'],
                'Year': pd.Series([2023, 2023], dtype='int32'),
                'Month': pd.Series([1, 2], dtype='int32'),
                'TotalAmount': [300.0, 300.0],
                'AverageAmount': [150.0, 300.0]
            })}
        },
        {
            'input': {
                'financial_df': pd.DataFrame({
                    'AccountID': ['B1', 'B1', 'C1'],
                    'TransactionDate': ['2023-03-15', '2023-03-20', '2023-03-10'],
                    'Amount': [0.0, 200.0, np.nan]
                })
            },
            'expected': {'output': pd.DataFrame({
                'AccountID': ['B1'],
                'Year': pd.Series([2023], dtype='int32'),
                'Month': pd.Series([3], dtype='int32'),
                'TotalAmount': [200.0],
                'AverageAmount': [200.0]
            })}
        },
        {
            'input': {
                'financial_df': pd.DataFrame({
                    'AccountID': ['C1', 'C1', 'D1'],
                    'TransactionDate': ['2024-01-15', '2024-01-20', '2024-01-10'],
                    'Amount': [100.0, 200.0, 300.0]
                })
            },
            'expected': {'output': pd.DataFrame({
                'AccountID': ['C1', 'D1'],
                'Year': pd.Series([2024, 2024], dtype='int32'),
                'Month': pd.Series([1, 1], dtype='int32'),
                'TotalAmount': [300.0, 300.0],
                'AverageAmount': [150.0, 300.0]
            })}
        }
    ]
})

# Implement a function `aggregate_weather_data` for a DataFrame `weather_df` with fields 'StationID', 'Temp', 'Humidity', 'ObservationTime'. Convert 'ObservationTime' to a DateTimeIndex; Filter to retain records with positive 'Temp' and 'Humidity'; Resample to daily frequency, taking the mean for each day; Return a DataFrame grouped by 'StationID' with columns for daily average 'Temp' and 'Humidity';
check_pandas_174 = functions_input_output_checker({
    'aggregate_weather_data': [
        {
            'input': {
                'weather_df': pd.DataFrame({
                    'StationID': ['S1', 'S1', 'S2'],
                    'Temp': [25.5, 26.0, 24.0],
                    'Humidity': [60.0, 65.0, 70.0],
                    'ObservationTime': ['2023-01-01 08:00', '2023-01-01 16:00', '2023-01-01 12:00']
                })
            },
            'expected': {'output': pd.DataFrame({
                'StationID': ['S1', 'S2'],
                'Date': pd.to_datetime(['2023-01-01', '2023-01-01']),
                'Temp': pd.Series([25.75, 24.0], dtype='float64'),
                'Humidity': pd.Series([62.5, 70.0], dtype='float64')
            })}
        },
        {
            'input': {
                'weather_df': pd.DataFrame({
                    'StationID': ['S2', 'S2', 'S3'],
                    'Temp': [-1.0, 22.0, 23.0],
                    'Humidity': [50.0, 55.0, -5.0],
                    'ObservationTime': ['2023-02-01 10:00', '2023-02-01 14:00', '2023-02-01 18:00']
                })
            },
            'expected': {'output': pd.DataFrame({
                'StationID': ['S2'],
                'Date': pd.to_datetime(['2023-02-01']),
                'Temp': pd.Series([22.0], dtype='float64'),
                'Humidity': pd.Series([55.0], dtype='float64'),
            })}
        },
        {
            'input': {
                'weather_df': pd.DataFrame({
                    'StationID': ['S1', 'S1', 'S2'],
                    'Temp': [28.0, 29.0, 27.0],
                    'Humidity': [75.0, 80.0, 85.0],
                    'ObservationTime': ['2023-03-01 09:00', '2023-03-01 15:00', '2023-03-02 12:00']
                })
            },
            'expected': {'output': pd.DataFrame({
                'StationID': ['S1', 'S2'],
                'Date': pd.to_datetime(['2023-03-01', '2023-03-02']),
                'Temp': pd.Series([28.5, 27.0], dtype='float64'),
                'Humidity': pd.Series([77.5, 85.0], dtype='float64'),
            })}
        }
    ]
})

# Design a function `standardize_student_record` to clean a DataFrame `student_df` featuring 'Name', 'Score', 'SubmissionDate'. Standardize 'Name' to have a capitalized first letter; Address missing 'Score' values by assigning the median score; Standardize 'SubmissionDate' to a consistent format and compute 'DaysSinceSubmission'; Return a DataFrame with standardized names, computed days since submission, and filled scores;
check_pandas_175 = functions_input_output_checker({
    'standardize_student_record': [
        {
            'input': {
                'student_df': pd.DataFrame({
                    'Name': ['john doe', 'MARY SMITH', 'bob wilson'],
                    'Score': [85.0, np.nan, 90.0],
                    'SubmissionDate': ['2024-01-15', '2024-01-16', '2024-01-17']
                }),
                'current_date': '2024-01-20'
            },
            'expected': {'output': pd.DataFrame({
                'Name': ['John Doe', 'Mary Smith', 'Bob Wilson'],
                'SubmissionDate': pd.to_datetime(['2024-01-15', '2024-01-16', '2024-01-17']),
                'DaysSinceSubmission': pd.Series([5, 4, 3], dtype='int32'),
                'Score': pd.Series([85.0, 87.5, 90.0], dtype='float64')
            })}
        },
        {
            'input': {
                'student_df': pd.DataFrame({
                    'Name': ['alice GREEN', 'TOM BROWN', 'sam black'],
                    'Score': [np.nan, np.nan, 95.0],
                    'SubmissionDate': ['2024-02-01', '2024-02-02', '2024-02-03']
                }),
                'current_date': '2024-02-05'
            },
            'expected': {'output': pd.DataFrame({
                'Name': ['Alice Green', 'Tom Brown', 'Sam Black'],
                'SubmissionDate': pd.to_datetime(['2024-02-01', '2024-02-02', '2024-02-03']),
                'DaysSinceSubmission': pd.Series([4, 3, 2], dtype='int32'),
                'Score': pd.Series([95.0, 95.0, 95.0], dtype='float64')
            })}
        },
        {
            'input': {
                'student_df': pd.DataFrame({
                    'Name': ['emma JONES', 'PETER white', 'lisa GRAY'],
                    'Score': [88.0, 92.0, np.nan],
                    'SubmissionDate': ['2024-03-10', '2024-03-11', '2024-03-12']
                }),
                'current_date': '2024-03-15'
            },
            'expected': {'output': pd.DataFrame({
                'Name': ['Emma Jones', 'Peter White', 'Lisa Gray'],
                'SubmissionDate': pd.to_datetime(['2024-03-10', '2024-03-11', '2024-03-12']),
                'DaysSinceSubmission': pd.Series([5, 4, 3], dtype='int32'),
                'Score': pd.Series([88.0, 92.0, 90.0], dtype='float64')
            })}
        }
    ]
})

# Write a function `construct_inventory_report` that takes a DataFrame `inventory_df` with 'ItemID', 'Quantity', 'RestockDate'. Parse 'RestockDate' to ensure it's in datetime format; Identify items needing restock by checking 'Quantity' against the `threshold`; Provide a summary count of items needing restock by month; Return a detailed DataFrame with 'ItemID', 'Quantity', 'DaysUntilRestock', plus a monthly summary DataFrame;
check_pandas_176 = functions_input_output_checker({
    'construct_inventory_report': [
        {
            'input': {
                'inventory_df': pd.DataFrame({
                    'ItemID': ['A101', 'A102', 'A103'],
                    'Quantity': [5, 15, 3],
                    'RestockDate': ['2024-02-01', '2024-02-15', '2024-02-28']
                }),
                'threshold': 10,
                'current_date': '2024-01-15'
            },
            'expected': {'output': {
                'details': pd.DataFrame({
                    'ItemID': ['A101', 'A102', 'A103'],
                    'Quantity': pd.Series([5, 15, 3], dtype='int32'),
                    'DaysUntilRestock': pd.Series([17, 31, 44], dtype='int32'),
                    'NeedsRestock': pd.Series([True, False, True], dtype='bool')
                }),
                'monthly_summary': pd.DataFrame({
                    'Month': pd.to_datetime(['2024-02-01']),
                    'ItemsNeedingRestock': pd.Series([2], dtype='int32')
                })
            }}
        },
        {
            'input': {
                'inventory_df': pd.DataFrame({
                    'ItemID': ['B201', 'B202', 'B203'],
                    'Quantity': [8, 12, 7],
                    'RestockDate': ['2024-03-01', '2024-04-01', '2024-03-15']
                }),
                'threshold': 9,
                'current_date': '2024-02-15'
            },
            'expected': {'output': {
                'details': pd.DataFrame({
                    'ItemID': ['B201', 'B202', 'B203'],
                    'Quantity': pd.Series([8, 12, 7], dtype='int32'),
                    'DaysUntilRestock': pd.Series([15, 46, 29], dtype='int32'),
                    'NeedsRestock': pd.Series([True, False, True], dtype='bool')
                }),
                'monthly_summary': pd.DataFrame({
                    'Month': pd.to_datetime(['2024-03-01']),
                    'ItemsNeedingRestock': pd.Series([2], dtype='int32')
                })
            }}
        },
        {
            'input': {
                'inventory_df': pd.DataFrame({
                    'ItemID': ['C301', 'C302', 'C303'],
                    'Quantity': [20, 5, 6],
                    'RestockDate': ['2024-05-01', '2024-05-15', '2024-05-30']
                }),
                'threshold': 7,
                'current_date': '2024-04-01'
            },
            'expected': {'output': {
                'details': pd.DataFrame({
                    'ItemID': ['C301', 'C302', 'C303'],
                    'Quantity': pd.Series([20, 5, 6], dtype='int32'),
                    'DaysUntilRestock': pd.Series([30, 44, 59], dtype='int32'),
                    'NeedsRestock': pd.Series([False, True, True], dtype='bool')
                }),
                'monthly_summary': pd.DataFrame({
                    'Month': pd.to_datetime(['2024-05-01']),
                    'ItemsNeedingRestock': pd.Series([2], dtype='int32')
                })
            }}
        }
    ]
})

# Develop a function `optimize_sales_forecast` that works on DataFrame `forecast_df` with columns 'Product', 'ProjectedSales', 'ForecastDate'. Convert 'ForecastDate' to DateTime format; Apply forward fill to handle missing 'ProjectedSales' values; Conduct a rolling window analysis to compute the 3-month moving average of sales; Return an extended DataFrame with moving averages along with original columns;
check_pandas_177 = functions_input_output_checker({
    'optimize_sales_forecast': [
        {
            'input': {
                'forecast_df': pd.DataFrame({
                    'Product': ['A', 'A', 'A', 'A'],
                    'ProjectedSales': [100.0, np.nan, 120.0, 130.0],
                    'ForecastDate': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01']
                })
            },
            'expected': {'output': pd.DataFrame({
                'Product': ['A', 'A', 'A', 'A'],
                'ForecastDate': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01']),
                'ProjectedSales': pd.Series([100.0, 100.0, 120.0, 130.0], dtype='float64'),
                'MovingAverage': pd.Series([100.0, 100.0, 106.67, 116.67], dtype='float64')
            })}
        },
        {
            'input': {
                'forecast_df': pd.DataFrame({
                    'Product': ['B', 'B', 'B', 'B'],
                    'ProjectedSales': [200.0, 220.0, np.nan, np.nan],
                    'ForecastDate': ['2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01']
                })
            },
            'expected': {'output': pd.DataFrame({
                'Product': ['B', 'B', 'B', 'B'],
                'ForecastDate': pd.to_datetime(['2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01']),
                'ProjectedSales': pd.Series([200.0, 220.0, 220.0, 220.0], dtype='float64'),
                'MovingAverage': pd.Series([200.0, 210.0, 213.33, 220.0], dtype='float64')
            })}
        },
        {
            'input': {
                'forecast_df': pd.DataFrame({
                    'Product': ['C', 'C', 'C', 'C', 'C'],
                    'ProjectedSales': [150.0, np.nan, 180.0, np.nan, 200.0],
                    'ForecastDate': ['2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', '2024-07-01']
                })
            },
            'expected': {'output': pd.DataFrame({
                'Product': ['C', 'C', 'C', 'C', 'C'],
                'ForecastDate': pd.to_datetime(['2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', '2024-07-01']),
                'ProjectedSales': pd.Series([150.0, 150.0, 180.0, 180.0, 200.0], dtype='float64'),
                'MovingAverage': pd.Series([150.0, 150.0, 160.0, 170.0, 186.67], dtype='float64')
            })}
        }
    ]
})


# Create a function `summarize_employee_performance` that processes DataFrame `performance_df` with 'EmployeeID', 'Score', 'ReviewDate'. Ensure 'ReviewDate' is converted into a datetime object; Replace missing 'Score' with the lowest non-zero score; Group by 'EmployeeID' to compute total and average score; Generate a DataFrame highlighting top performers with scores above a specified percentile score; Audit history, including evaluation of performance improvement over time;
check_pandas_178 = functions_input_output_checker({
    'summarize_employee_performance': [
        {
            'input': {
                'performance_df': pd.DataFrame({
                    'EmployeeID': ['E1', 'E1', 'E2'],
                    'Score': [85.0, np.nan, 90.0],
                    'ReviewDate': ['2023-01-15', '2023-07-15', '2023-01-15']
                }),
                'percentile_threshold': 75
            },
            'expected': {'output': {
                'summary': pd.DataFrame({
                    'EmployeeID': ['E1', 'E2'],
                    'TotalScore': pd.Series([170.0, 90.0], dtype='float64'),
                    'AverageScore': pd.Series([85.0, 90.0], dtype='float64'),
                    'ReviewCount': pd.Series([2, 1], dtype='int32'),
                    'IsTopPerformer': pd.Series([False, True], dtype='bool')
                }),
                'improvement': pd.DataFrame({
                    'EmployeeID': ['E1'],
                    'FirstScore': pd.Series([85.0], dtype='float64'),
                    'LastScore': pd.Series([85.0], dtype='float64'),
                    'ScoreChange': pd.Series([0.0], dtype='float64')
                })
            }}
        },
        {
            'input': {
                'performance_df': pd.DataFrame({
                    'EmployeeID': ['E2', 'E2', 'E3'],
                    'Score': [75.0, 95.0, np.nan],
                    'ReviewDate': ['2023-02-01', '2023-08-01', '2023-02-01']
                }),
                'percentile_threshold': 80
            },
            'expected': {'output': {
                'summary': pd.DataFrame({
                    'EmployeeID': ['E2', 'E3'],
                    'TotalScore': pd.Series([170.0, 75.0], dtype='float64'),
                    'AverageScore': pd.Series([85.0, 75.0], dtype='float64'),
                    'ReviewCount': pd.Series([2, 1], dtype='int32'),
                    'IsTopPerformer': pd.Series([True, False], dtype='bool')
                }),
                'improvement': pd.DataFrame({
                    'EmployeeID': ['E2'],
                    'FirstScore': pd.Series([75.0], dtype='float64'),
                    'LastScore': pd.Series([95.0], dtype='float64'),
                    'ScoreChange': pd.Series([20.0], dtype='float64')
                })
            }}
        },
        {
            'input': {
                'performance_df': pd.DataFrame({
                    'EmployeeID': ['E3', 'E3', 'E4'],
                    'Score': [80.0, 85.0, 70.0],
                    'ReviewDate': ['2023-03-01', '2023-09-01', '2023-03-01']
                }),
                'percentile_threshold': 70
            },
            'expected': {'output': {
                'summary': pd.DataFrame({
                    'EmployeeID': ['E3', 'E4'],
                    'TotalScore': pd.Series([165.0, 70.0], dtype='float64'),
                    'AverageScore': pd.Series([82.5, 70.0], dtype='float64'),
                    'ReviewCount': pd.Series([2, 1], dtype='int32'),
                    'IsTopPerformer': pd.Series([True, False], dtype='bool')
                }),
                'improvement': pd.DataFrame({
                    'EmployeeID': ['E3'],
                    'FirstScore': pd.Series([80.0], dtype='float64'),
                    'LastScore': pd.Series([85.0], dtype='float64'),
                    'ScoreChange': pd.Series([5.0], dtype='float64')
                })
            }}
        }
    ]
})

# Create a function `double_series_values` that takes a Series `input_series` and returns a Series with all values doubled.
check_pandas_179 = functions_input_output_checker({
    'double_series_values': [
        {
            'input': {'input_series': pd.Series([1, 2, 3])},
            'expected': {'output': pd.Series([2, 4, 6])}
        },
        {
            'input': {'input_series': pd.Series([10, 20, 30])},
            'expected': {'output': pd.Series([20, 40, 60])}
        },
        {
            'input': {'input_series': pd.Series([100, 200, 300])},
            'expected': {'output': pd.Series([200, 400, 600])}
        }
    ]
})

# Write a function `replace_zeros_with_mean` that takes a Series `data_series` and replaces all 0 values with the mean of the Series, returning the modified Series.
check_pandas_180 = functions_input_output_checker({
    'replace_zeros_with_mean': [
        {
            'input': {'data_series': pd.Series([1, 2, 0, 4, 5])},
            'expected': {'output': pd.Series([1, 2, 3, 4, 5])}
        },
        {
            'input': {'data_series': pd.Series([10, 20, 0, 40, 50])},
            'expected': {'output': pd.Series([10, 20, 30, 40, 50])}
        },
        {
            'input': {'data_series': pd.Series([100, 200, 0, 400, 500])},
            'expected': {'output': pd.Series([100, 200, 300, 400, 500])}
        }
    ]
})

# Design a function `standardize_column_names` that accepts a DataFrame `df` and returns it with all column names set to lowercase.
check_pandas_181 = functions_input_output_checker({
    'standardize_column_names': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame({
                'a': [1, 2, 3],
                'b': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame({
                'x': [10, 20, 30],
                'y': [100, 200, 300]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame({
                'm': [100, 200, 300],
                'n': [1000, 2000, 3000]
            })}
        }
    ]
})

# Implement a function `drop_duplicate_rows` that receives a DataFrame `df` and returns it with duplicate rows removed.
check_pandas_182 = functions_input_output_checker({
    'drop_duplicate_rows': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3, 1],
                'B': [10, 20, 30, 10]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30, 10],
                'Y': [100, 200, 300, 100]
            })},
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300, 100],
                'N': [1000, 2000, 3000, 1000]
            })},
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })}
        }
    ]
})

# Create a function `calculate_column_sums` that takes a DataFrame `df` and returns a Series containing the sum of each column.
check_pandas_183 = functions_input_output_checker({
    'calculate_column_sums': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.Series([6, 60], index=['A', 'B'])}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.Series([60, 600], index=['X', 'Y'])}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.Series([600, 6000], index=['M', 'N'])}
        }
    ]
})

# Write a function `extract_date_parts` that takes a Series `dates` of datetime objects and returns a DataFrame with columns 'Year', 'Month', and 'Day'.
check_pandas_184 = functions_input_output_checker({
    'extract_date_parts': [
        {
            'input': {'dates': pd.to_datetime([pd.Timestamp(2023, 1, 1), pd.Timestamp(2023, 2, 2), pd.Timestamp(2023, 3, 3)])},
            'expected': {'output': pd.DataFrame({
                'Year': pd.Series([2023, 2023, 2023], dtype='int32'),
                'Month': pd.Series([1, 2, 3], dtype='int32'),
                'Day': pd.Series([1, 2, 3], dtype='int32')
            })}
        },
        {
            'input': {'dates': pd.to_datetime([pd.Timestamp(2023, 4, 4), pd.Timestamp(2023, 5, 5), pd.Timestamp(2023, 6, 6)])},
            'expected': {'output': pd.DataFrame({
                'Year': pd.Series([2023, 2023, 2023], dtype='int32'),
                'Month': pd.Series([4, 5, 6], dtype='int32'),
                'Day': pd.Series([4, 5, 6], dtype='int32')
            })}
        },
        {
            'input': {'dates': pd.to_datetime([pd.Timestamp(2023, 7, 7), pd.Timestamp(2023, 8, 8), pd.Timestamp(2023, 9, 9)])},
            'expected': {'output': pd.DataFrame({
                'Year': pd.Series([2023, 2023, 2023], dtype='int32'),
                'Month': pd.Series([7, 8, 9], dtype='int32'),
                'Day': pd.Series([7, 8, 9], dtype='int32')
            })}
        }
    ]
})

# Define a function `concat_strings_in_column` that, given a DataFrame `df` and a column `text_col`, concatenates all strings in that column with a space in between, returning the result string.
check_pandas_185 = functions_input_output_checker({
    'concat_strings_in_column': [
        {
            'input': {
                'df': pd.DataFrame({
                    'Text': ['hello', ' yolo', 'olo']
                }),
                'text_col': 'Text'
            },
            'expected': {'output': 'hello  yolo olo'}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Text': ['hi', ' there', ' you']
                }),
                'text_col': 'Text'
            },
            'expected': {'output': 'hi  there  you'}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Text': ['hey', ' there', ' you']
                }),
                'text_col': 'Text'
            },
            'expected': {'output': 'hey  there  you'}
        }
    ]
})

# Implement a function `sort_by_index_descending` that accepts a DataFrame `df` and returns it sorted by its index in descending order.
check_pandas_186 = functions_input_output_checker({
    'sort_by_index_descending': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [3, 2, 1],
                'B': [30, 20, 10]
            }, index=[2, 1, 0])}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame({
                'X': [30, 20, 10],
                'Y': [300, 200, 100]
            }, index=[2, 1, 0])}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame({
                'M': [300, 200, 100],
                'N': [3000, 2000, 1000]
            }, index=[2, 1, 0])}
        }
    ]
})

# Create a function `filter_by_threshold` to take a DataFrame `df` and a column name `col`, returning a DataFrame including only rows where `col` is above a given threshold.
check_pandas_187 = functions_input_output_checker({
    'filter_by_threshold': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'col': 'A',
                'threshold': 2
            },
            'expected': {'output': pd.DataFrame({
                'A': [3],
                'B': [30]
            }, index=[2])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'col': 'Y',
                'threshold': 100
            },
            'expected': {'output': pd.DataFrame({
                'X': [20, 30],
                'Y': [200, 300]
            }, index=[1, 2])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'col': 'M',
                'threshold': 300
            },
            'expected': {'output': pd.DataFrame({
                'M': pd.Series(dtype='int64'),
                'N': pd.Series(dtype='int64')
            })}
        }
    ]
})

# Write a function `get_unique_values` that takes a DataFrame `df` and a column `col`, returning a sorted array of unique values in the specified column.
check_pandas_188 = functions_input_output_checker({
    'get_unique_values': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'col': 'A'
            },
            'expected': {'output': np.array([1, 2, 3])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'col': 'Y'
            },
            'expected': {'output': np.array([100, 200, 300])}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'col': 'M'
            },
            'expected': {'output': np.array([100, 200, 300])}
        }
    ]
})

# Develop a function `append_row_to_dataframe` that takes a DataFrame `df` and a dictionary `row_dict`, appending the dictionary as a new row, and returning the updated DataFrame.
check_pandas_189 = functions_input_output_checker({
    'append_row_to_dataframe': [
        {
            'input': {
                'df': pd.DataFrame({
                    'A': [1, 2, 3],
                    'B': [10, 20, 30]
                }),
                'row_dict': {'A': 4, 'B': 40}
            },
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3, 4],
                'B': [10, 20, 30, 40]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'X': [10, 20, 30],
                    'Y': [100, 200, 300]
                }),
                'row_dict': {'X': 40, 'Y': 400}
            },
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30, 40],
                'Y': [100, 200, 300, 400]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'M': [100, 200, 300],
                    'N': [1000, 2000, 3000]
                }),
                'row_dict': {'M': 400, 'N': 4000}
            },
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300, 400],
                'N': [1000, 2000, 3000, 4000]
            })}
        }
    ]
})

# Construct a function `reset_index_and_name` that takes a DataFrame `df` and returns it with its index reset and the name of the index set to 'NewIndex'.
check_pandas_190 = functions_input_output_checker({
    'reset_index_and_name': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame({
                'index': [0, 1, 2],
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            }, index=pd.Series([0, 1, 2], name='NewIndex'))}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame({
                'index': [0, 1, 2],
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            }, index=pd.Series([0, 1, 2], name='NewIndex'))}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame({
                'index': [0, 1, 2],
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            }, index=pd.Series([0, 1, 2], name='NewIndex'))}
        }
    ]
})

# Create a function `swap_dataframe_columns` that accepts a DataFrame `df` and two column names `col1` and `col2`, swapping the values of these columns.
check_pandas_191 = functions_input_output_checker({
    'swap_dataframe_columns': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            }), 'col1': 'A', 'col2': 'B'},
            'expected': {'output': pd.DataFrame({
                'A': [10, 20, 30],
                'B': [1, 2, 3]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            }), 'col1': 'X', 'col2': 'Y'},
            'expected': {'output': pd.DataFrame({
                'X': [100, 200, 300],
                'Y': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            }), 'col1': 'M', 'col2': 'N'},
            'expected': {'output': pd.DataFrame({
                'M': [1000, 2000, 3000],
                'N': [100, 200, 300]
            })}
        }
    ]
})

# Write a function `rename_index_label` which receives a DataFrame `df`, renames its first index label to 'FirstRow', and returns the DataFrame.
check_pandas_192 = functions_input_output_checker({
    'rename_index_label': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            }, index=['FirstRow', 1, 2])}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            }, index=['FirstRow', 1, 2])}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            }, index=['FirstRow', 1, 2])}
        }
    ]
})

# Define a function `calculate_frequency_table` that, given a DataFrame `df` and a column `cat_col`, returns a DataFrame with a frequency count of each category in `cat_col`.
check_pandas_193 = functions_input_output_checker({
    'calculate_frequency_table': [
        {
            'input': {
                'df': pd.DataFrame({
                    'Category': ['A', 'A', 'B', 'C']
                }),
                'cat_col': 'Category'
            },
            'expected': {'output': pd.DataFrame({
                'Category': ['A', 'B', 'C'],
                'count': [2, 1, 1]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Category': ['A', 'B', 'B', 'C']
                }),
                'cat_col': 'Category'
            },
            'expected': {'output': pd.DataFrame({
                'Category': ['B', 'A', 'C'],
                'count': [2, 1, 1]
            })}
        },
        {
            'input': {
                'df': pd.DataFrame({
                    'Category': ['A', 'B', 'C', 'C']
                }),
                'cat_col': 'Category'
            },
            'expected': {'output': pd.DataFrame({
                'Category': ['C', 'A', 'B'],
                'count': [2, 1, 1]
            })}
        }
    ]
})

# Implement a function `remove_negative_entries` that takes a Series `numeric_series` and returns a Series with all negative entries removed.
check_pandas_194 = functions_input_output_checker({
    'remove_negative_entries': [
        {
            'input': {'numeric_series': pd.Series([1, -2, 3])},
            'expected': {'output': pd.Series([1, 3], index=[0, 2])}
        },
        {
            'input': {'numeric_series': pd.Series([10, -20, 30])},
            'expected': {'output': pd.Series([10, 30], index=[0, 2])}
        },
        {
            'input': {'numeric_series': pd.Series([100, -200, 300])},
            'expected': {'output': pd.Series([100, 300], index=[0, 2])}
        }
    ]
})

# Write a function `sort_column_values` that takes a DataFrame `df` and column name `col`, returning `df` sorted by `col` values in ascending order.
check_pandas_195 = functions_input_output_checker({
    'sort_column_values': [
        {
            'input': {'df': pd.DataFrame({
                'A': [3, 2, 1],
                'B': [30, 20, 10]
            }), 'col': 'A'},
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            }, index=[2, 1, 0])}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [30, 20, 10],
                'Y': [300, 200, 100]
            }), 'col': 'X'},
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            }, index=[2, 1, 0])}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [300, 200, 100],
                'N': [3000, 2000, 1000]
            }), 'col': 'M'},
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            }, index=[2, 1, 0])}
        }
    ]
})

# Design a function `drop_columns_by_name` that accepts a DataFrame `df` and a list of column names `drop_cols`, removing these columns and returning the modified DataFrame.
check_pandas_196 = functions_input_output_checker({
    'drop_columns_by_name': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30],
                'C': [100, 200, 300]
            }), 'drop_cols': ['A', 'C']},
            'expected': {'output': pd.DataFrame({
                'B': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300],
                'Z': [1000, 2000, 3000]
            }), 'drop_cols': ['Y', 'Z']},
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000],
                'O': [10000, 20000, 30000]
            }), 'drop_cols': ['N', 'O']},
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300]
            })}
        }
    ]
})

# Develop a function `strip_whitespace` that takes a DataFrame `df` and trims leading and trailing whitespace from all string entries.
check_pandas_197 = functions_input_output_checker({
    'strip_whitespace': [
        {
            'input': {'df': pd.DataFrame({
                'A': [' 1', '2 ', ' 3 '],
                'B': [' 10', '20 ', ' 30']
            })},
            'expected': {'output': pd.DataFrame({
                'A': ['1', '2', '3'],
                'B': ['10', '20', '30']
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [' 10', '20 ', ' 30 '],
                'Y': [' 100', '200 ', ' 300']
            })},
            'expected': {'output': pd.DataFrame({
                'X': ['10', '20', '30'],
                'Y': ['100', '200', '300']
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [' 100', '200 ', ' 300 '],
                'N': [' 1000', '2000 ', ' 3000']
            })},
            'expected': {'output': pd.DataFrame({
                'M': ['100', '200', '300'],
                'N': ['1000', '2000', '3000']
            })}
        }
    ]
})

# Create a function `duplicate_last_column` that receives a DataFrame `df` and duplicates its last column, appending the duplicate to the right of the DataFrame.
check_pandas_198 = functions_input_output_checker({
    'duplicate_last_column': [
        {
            'input': {'df': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30]
            })},
            'expected': {'output': pd.DataFrame({
                'A': [1, 2, 3],
                'B': [10, 20, 30],
                'B_copy': [10, 20, 30]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300]
            })},
            'expected': {'output': pd.DataFrame({
                'X': [10, 20, 30],
                'Y': [100, 200, 300],
                'Y_copy': [100, 200, 300]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000]
            })},
            'expected': {'output': pd.DataFrame({
                'M': [100, 200, 300],
                'N': [1000, 2000, 3000],
                'N_copy': [1000, 2000, 3000]
            })}
        }
    ]
})

# Write a function `filter_top_n_rows_by_column` that takes a DataFrame `df`, a column `col`, and an integer `n`, returning the top n rows sorted by values in `col`.
check_pandas_199 = functions_input_output_checker({
    'filter_top_n_rows_by_column': [
        {
            'input': {'df': pd.DataFrame({
                'A': [3, 2, 1],
                'B': [30, 20, 10]
            }), 'col': 'A', 'n': 2},
            'expected': {'output': pd.DataFrame({
                'A': [3, 2],
                'B': [30, 20]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'X': [30, 20, 10],
                'Y': [300, 200, 100]
            }), 'col': 'X', 'n': 1},
            'expected': {'output': pd.DataFrame({
                'X': [30],
                'Y': [300]
            })}
        },
        {
            'input': {'df': pd.DataFrame({
                'M': [300, 200, 100],
                'N': [3000, 2000, 1000]
            }), 'col': 'M', 'n': 3},
            'expected': {'output': pd.DataFrame({
                'M': [300, 200, 100],
                'N': [3000, 2000, 1000]
            })}
        }
    ]
})

# Define a function `calculate_range_of_numeric_series` that takes a Series `numeric_series` and returns the range (max - min) of its values.
check_pandas_200 = functions_input_output_checker({
    'calculate_range_of_numeric_series': [
        {
            'input': {'numeric_series': pd.Series([1, 2, 3])},
            'expected': {'output': np.int64(2)}
        },
        {
            'input': {'numeric_series': pd.Series([10, 20, 30])},
            'expected': {'output': np.int64(20)}
        },
        {
            'input': {'numeric_series': pd.Series([100, 200, 300])},
            'expected': {'output': np.int64(200)}
        }
    ]
})