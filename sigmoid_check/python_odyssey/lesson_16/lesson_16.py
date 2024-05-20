import time
import itertools


class Task1:
    """1. Create a lambda function named `task1` that adds 10 to a given number."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(10) == 20
            return True
        except:
            return False

class Task2:
    """2. Create a lambda function named `task2` that checks if a number is even."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(4) == True
            assert self.func(5) == False
            return True
        except:
            return False

class Task3:
    """3. Create a lambda function named `task3` that multiplies two numbers."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2, 3) == 6
            assert self.func(7, 5) == 35
            return True
        except:
            return False

class Task4:
    """4. Create a lambda function named `task4` that returns the length of a string."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("test") == 4
            assert self.func("Python") == 6
            return True
        except:
            return False

class Task5:
    """5. Create a lambda function named `task5` that converts a string to uppercase."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("test") == "TEST"
            assert self.func("Python") == "PYTHON"
            return True
        except:
            return False

class Task6:
    """6. Create a lambda function named `task6` that finds the maximum of three numbers."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 2, 3) == 3
            assert self.func(10, 20, 15) == 20
            return True
        except:
            return False

class Task7:
    """7. Create a lambda function named `task7` that concatenates two strings with a space in between."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("Hello", "World") == "Hello World"
            assert self.func("Python", "Programming") == "Python Programming"
            return True
        except:
            return False

class Task8:
    """8. Create a lambda function named `task8` that filters out odd numbers from a list."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([1, 2, 3, 4, 5]) == [2, 4]
            assert self.func([10, 11, 12, 13, 14]) == [10, 12, 14]
            return True
        except:
            return False

class Task9:
    """9. Create a lambda function named `task9` that calculates the factorial of a number using reduce."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(5) == 120
            assert self.func(6) == 720
            return True
        except:
            return False

class Task10:
    """10. Create a lambda function named `task10` that sorts a list of tuples by the second value in each tuple."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([(1, 3), (2, 2), (3, 1)]) == [(3, 1), (2, 2), (1, 3)]
            assert self.func([(5, 6), (1, 9), (4, 3)]) == [(4, 3), (5, 6), (1, 9)]
            return True
        except:
            return False

class Task11:
    """11. Create a lambda function named `task11` that returns the square root of a number."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(4) == 2.0
            assert self.func(9) == 3.0
            return True
        except:
            return False

class Task12:
    """12. Create a lambda function named `task12` that checks if a string is a palindrome."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("madam") == True
            assert self.func("hello") == False
            return True
        except:
            return False

class Task13:
    """13. Create a lambda function named `task13` that counts the number of vowels in a string."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("hello") == 2
            assert self.func("education") == 5
            return True
        except:
            return False

class Task14:
    """14. Create a lambda function named `task14` that returns the reverse of a string."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("hello") == "olleh"
            assert self.func("Python") == "nohtyP"
            return True
        except:
            return False

class Task15:
    """15. Create a lambda function named `task15` that filters out all strings longer than 5 characters from a list."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(["apple", "banana", "pear"]) == ["apple", "pear"]
            assert self.func(["hello", "world", "Python"]) == ["hello", "world"]
            return True
        except:
            return False

class Task16:
    """16. Create a lambda function named `task16` that takes a list of dictionaries and sorts them by a specified key."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            lst = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
            assert self.func(lst, "age") == [{"name": "Jane", "age": 25}, {"name": "John", "age": 30}]
            assert self.func(lst, "name") == [{"name": "Jane", "age": 25}, {"name": "John", "age": 30}]
            return True
        except:
            return False

class Task17:
    """17. Create a lambda function named `task17` that finds the GCD of two numbers."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(48, 18) == 6
            assert self.func(20, 8) == 4
            return True
        except:
            return False

class Task18:
    """18. Create a lambda function named `task18` that calculates the sum of the squares of the even numbers in a list."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([1, 2, 3, 4, 5]) == 20
            assert self.func([10, 11, 12, 13, 14]) == 380
            return True
        except:
            return False

class Task19:
    """19. Create a lambda function named `task19` that checks if a given year is a leap year."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2020) == True
            assert self.func(2019) == False
            return True
        except:
            return False

class Task20:
    """20. Create a lambda function named `task20` that finds the longest word in a list of words."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(["apple", "banana", "pear"]) == "banana"
            assert self.func(["hello", "world", "Python"]) == "Python"
            return True
        except:
            return False

# Generators

class Task21:
    """21. Create a generator named `task21` that yields numbers from 1 to 10."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            assert list(gen) == list(range(1, 11))
            return True
        except:
            return False

class Task22:
    """22. Create a generator named `task22` that yields the squares of numbers from 1 to 10."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            assert list(gen) == [i ** 2 for i in range(1, 11)]
            return True
        except:
            return False

class Task23:
    """23. Create a generator named `task23` that yields the characters of a string one by one."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("test")
            assert list(gen) == list("test")
            return True
        except:
            return False

class Task24:
    """24. Create a generator named `task24` that yields even numbers up to a given limit."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(10)
            assert list(gen) == [2, 4, 6, 8, 10]
            return True
        except:
            return False

class Task25:
    """25. Create a generator named `task25` that yields the first n Fibonacci numbers."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == [0, 1, 1, 2, 3]
            return True
        except:
            return False

class Task26:
    """26. Create a generator named `task26` that yields the prime numbers up to a given limit."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(10)
            assert list(gen) == [2, 3, 5, 7]
            return True
        except:
            return False

class Task27:
    """27. Create a generator named `task27` that yields numbers in a specified range with a given step."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(0, 10, 2)
            assert list(gen) == [0, 2, 4, 6, 8]
            return True
        except:
            return False

class Task28:
    """28. Create a generator named `task28` that yields all substrings of a given string."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("abc")
            assert list(gen) == ["a", "ab", "abc", "b", "bc", "c"]
            return True
        except:
            return False

class Task29:
    """29. Create a generator named `task29` that yields the factorials of numbers from 1 to n."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == [1, 2, 6, 24, 120]
            return True
        except:
            return False

class Task30:
    """30. Create a generator named `task30` that yields the digits of a number in reverse order."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1234)
            assert list(gen) == [4, 3, 2, 1]
            return True
        except:
            return False

class Task31:
    """31. Create a generator named `task31` that yields all possible combinations of elements in a list."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3])
            expected_combinations = [
                (1,), (2,), (3,),
                (1, 2), (1, 3), (2, 3),
                (1, 2, 3)
            ]
            assert list(gen) == expected_combinations
            return True
        except:
            return False

class Task32:
    """32. Create a generator named `task32` that yields the running total of a list of numbers."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3, 4])
            assert list(gen) == [1, 3, 6, 10]
            return True
        except:
            return False

class Task33:
    """33. Create a generator named `task33` that yields the first n terms of an arithmetic sequence."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1, 2, 5)
            assert list(gen) == [1, 3, 5, 7, 9]
            return True
        except:
            return False

class Task34:
    """34. Create a generator named `task34` that yields the powers of 2 up to a given limit."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(16)
            assert list(gen) == [1, 2, 4, 8, 16]
            return True
        except:
            return False

class Task35:
    """35. Create a generator named `task35` that yields numbers in an infinite geometric sequence."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1, 2)
            result = [next(gen) for _ in range(5)]
            assert result == [1, 2, 4, 8, 16]
            return True
        except:
            return False

class Task36:
    """36. Create a generator named `task36` that yields the permutations of a list."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3])
            assert list(gen) == list(itertools.permutations([1, 2, 3]))
            return True
        except:
            return False

class Task37:
    """37. Create a generator named `task37` that yields all prime factors of a given number."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(18)
            assert list(gen) == [2, 3, 3]
            return True
        except:
            return False

class Task38:
    """38. Create a generator named `task38` that yields the binary representation of numbers from 1 to n."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == ["1", "10", "11", "100", "101"]
            return True
        except:
            return False

class Task39:
    """39. Create a generator named `task39` that yields all anagrams of a given string."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("abc")
            assert list(gen) == list(itertools.permutations("abc"))
            return True
        except:
            return False

class Task40:
    """40. Create a generator named `task40` that yields the terms of a given mathematical series (e.g., Taylor series)."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            result = [next(gen) for _ in range(5)]
            assert result == [1.0, -0.5, 0.3333333333333333, -0.25, 0.2]
            return True
        except:
            return False

# Decorators

class Task41:
    """41. Create a decorator named `task41` that logs the execution time of a function."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                time.sleep(1)
                return "Done"
            result = dummy_function()
            assert result == "Done"
            return True
        except:
            return False

class Task42:
    """42. Create a decorator named `task42` that prints "Before" and "After" messages around a function call."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "Done"
            result = dummy_function()
            assert result == "Done"
            return True
        except:
            return False

class Task43:
    """43. Create a decorator named `task43` that caches the results of a function."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function(x):
                return x + 10
            result1 = dummy_function(5)
            result2 = dummy_function(5)
            assert result1 == 15
            assert result2 == 15
            return True
        except:
            return False

class Task44:
    """44. Create a decorator named `task44` that counts the number of times a function is called."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "Done"
            result1 = dummy_function()
            result2 = dummy_function()
            assert result1 == "Done"
            assert result2 == "Done"
            return True
        except:
            return False

class Task45:
    """45. Create a decorator named `task45` that converts the output of a function to uppercase."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "done"
            result = dummy_function()
            assert result == "DONE"
            return True
        except:
            return False

class Task46:
    """46. Create a decorator named `task46` that retries a function if it raises an exception."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                raise ValueError("Test")
            dummy_function()
            return False
        except ValueError:
            return True

class Task47:
    """47. Create a decorator named `task47` that adds a specified value to the return value of a function."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func(5)
            def dummy_function(x):
                return x
            result = dummy_function(10)
            assert result == 15
            return True
        except:
            return False

class Task48:
    """48. Create a decorator named `task48` that validates the types of arguments passed to a function."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func([int, int])
            def dummy_function(x, y):
                return x + y
            result = dummy_function(5, 10)
            assert result == 15
            return True
        except:
            return False

class Task49:
    """49. Create a decorator named `task49` that ensures a function is only called by users with a specific role."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func("admin")
            def dummy_function(role):
                return "Access granted"
            result = dummy_function("admin")
            assert result == "Access granted"
            return True
        except:
            return False

class Task50:
    """50. Create a decorator named `task50` that times out a function if it runs for too long."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func(1)
            def dummy_function():
                time.sleep(2)
                return "Done"
            dummy_function()
            return False
        except TimeoutException:
            return True

class Task51:
    """51. Create a decorator named `task51` that logs the arguments and return value of a function."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function(x, y):
                return x + y
            result = dummy_function(5, 10)
            assert result == 15
            return True
        except:
            return False

class Task52:
    """52. Create a decorator named `task52` that memoizes the results of a function based on its arguments."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function(x):
                return x + 10
            result1 = dummy_function(5)
            result2 = dummy_function(5)
            assert result1 == 15
            assert result2 == 15
            return True
        except:
            return False


class Lesson16Test:
    """Test class for checking the implementation of tasks in lesson 16 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 53)}

    def check_task(self, task_number, func):
        task_class = globals()[f"Task{task_number}"]
        solution_task = task_class(func)
        try:
            self.status_tasks[f"task_{task_number}"] = solution_task.check_task()
            if self.status_tasks[f"task_{task_number}"]:
                return f"Task {task_number}: Correct! Well done."
            return f"Task {task_number}: Incorrect! Please try again."
        except:
            return f"Task {task_number}: Error!"

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"
