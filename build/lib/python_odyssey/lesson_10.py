class Lesson10:
    "Test class for cheking the implementation of the tasks in lesson 10"
    def __init__(self):
        self.status_tasks = {
            "task_1": False,
            "task_2": False,
            "task_3": False,
            "task_4": False,
            "task_5": False,
            "task_6": False,
            "task_7": False
        }
    
    def check_task_1(self, func):
        """Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
        Utilizați list comprehension."""
        expected_output = [i for i in range(1, 11)]
        try:
            student_output = func()
            if student_output == expected_output:
                self.status_tasks["task_1"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_1"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 1: Error - {e}"
        
    def check_task_2(self, func):
        """Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
        Utilizați list comprehension în proces"""
        expected_output = [i**2 for i in range(1, 11)]
        try:
            student_output = func()
            if student_output == expected_output:
                self.status_tasks["task_2"] = True
                return "Exercise 2: Correct! Well done."
            else:
                self.status_tasks["task_2"] = False
                return "Exercise 2: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 2: Error - {e}"

    def check_task_3(self, func):
        """Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
        Utilizați list comprehension în proces.
        """
        expected_output = [i for i in range(1, 11) if i % 2 != 0]
        try:
            student_output = func()
            if student_output == expected_output:
                self.status_tasks["task_3"] = True
                return "Exercise 3: Correct! Well done."
            else:
                self.status_tasks["task_3"] = False
                return "Exercise 3: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 3: Error - {e}"


    def check_task_4(self, func):
        """Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
        va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
        """
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected_output = [num for row in matrix for num in row]
        try:
            student_output = func(matrix)
            if student_output == expected_output:
                self.status_tasks["task_4"] = True
                return "Exercise 4: Correct! Well done."
            else:
                self.status_tasks["task_4"] = False
                return "Exercise 4: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 4: Error - {e}"
        
    def check_task_5(self, func):
        """Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
        """
        n = 10
        expected_output = ["par" if i % 2 == 0 else "impar" for i in range(1, n+1)]
        try:
            student_output = func(n)
            if student_output == expected_output:
                self.status_tasks["task_5"] = True
                return "Exercise 5: Correct! Well done."
            else:
                self.status_tasks["task_5"] = False
                return "Exercise 5: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 5: Error - {e}"
        
    def check_task_6(self, func):
        """Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        """
        n = 5
        expected_output = {i: i**3 for i in range(1, n+1)}
        try:
            student_output = func(n)
            if student_output == expected_output:
                self.status_tasks["task_6"] = True
                return "Exercise 6: Correct! Well done."
            else:
                self.status_tasks["task_6"] = False
                return "Exercise 6: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 6: Error - {e}"
        
    def check_task_7(self, func):
        """Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
        """
        n = 50
        expected_output = {i for i in range(1, n+1) if i % 3 == 0}
        try:
            student_output = func(n)
            if student_output == expected_output:
                self.status_tasks["task_7"] = True
                return "Exercise 7: Correct! Well done."
            else:
                self.status_tasks["task_7"] = False
                return "Exercise 7: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 7: Error - {e}"


    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / 7}%."
