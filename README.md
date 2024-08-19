# sigmoid_check

sigmoid_check is a library for automation testing of Sigmoid's homeworks. It contains a set of functions that can be used to test the correctness of the homeworks.

This version of the library is designed to work with the homeworks of the bootcamp "Python Odyssey" of Sigmoid.

## How to use sigmoid_check

To use sigmoid_check for a specific homework, you need to import the library and call the functions that are relevant to the homework from the specific event that they are assigned to.

To install sigmoid_check, you can use the following command:

```bash
pip install sigmoid_check
```

# To get check the homework of the lesson_10 for the Python Odyssey bootcamp, you can use the following code:

```python
from sigmoid_check.python_odyssey.lesson_10 import Lesson_10
```

Afterwards, you have to initiate a session with the following code:

```python
session = Lesson_10()
```

Then, you can use the functions of the session object to check the homework of the lesson_10. For example, to check the first task of the homework, you can use the following code (but make sure to first create the function `task_1` in the homework file and then call the function `check_task_1` from the session object):

```python
session.check_task_1(task_1)
```

To actually print the if the task is correct or not, you can use the following code:

```python
print(session.check_task_1(task_1))
```

The above checking of the task has to be done should be done to each task of the homework, otherwise the not considered tasks will be considered as incorrect.

To check the final result of the homework, after running all the tasks, you can use the following code:

```python
print(session.get_completion_percentage())
```

With <3 from Sigmoid!

We are open for feedback. Please send your impressions to balamatiuc2@gmail.com