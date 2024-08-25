class Lesson10:
    "Test class for cheking the implementation of the tasks in lesson 10"
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 25)}
    
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_2"] = False
                return "Exercise 1: Incorrect. Please try again."
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_3"] = False
                return "Exercise 1: Incorrect. Please try again."
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_4"] = False
                return "Exercise 1: Incorrect. Please try again."
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_5"] = False
                return "Exercise 1: Incorrect. Please try again."
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_6"] = False
                return "Exercise 1: Incorrect. Please try again."
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
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_7"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 7: Error - {e}"

    def check_task_8(self, func):
        """Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
        Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
        """
        numbers = [1, 2, 3, 4, 5]
        expected_output = sum(numbers) / len(numbers)
        try:
            student_output = func(numbers)
            if student_output == expected_output:
                self.status_tasks["task_8"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_8"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 8: Error - {e}"
        
    def check_task_9(self, func):
        """Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
        Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
        """
        number_1 = 4
        expected_output_1 = number_1 % 2 == 0
        number_2 = 5
        expected_output_2 = number_2 % 2 == 0
        try:
            student_output_1 = func(number_1)
            student_output_2 = func(number_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_9"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_9"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 9: Error - {e}"
        
    def check_task_10(self, func):
        """Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
        apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
        Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
        """
        name = "Ana"
        age = 32
        city = "București"
        expected_output = f"Nume: {name}, Varsta: {age}, Oras: {city}"
        try:
            student_output = func(name, age, city)
            if student_output == expected_output:
                self.status_tasks["task_10"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_10"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 10: Error - {e}"
        
    def check_task_11(self, func):
        """Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
        Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
        """
        numbers = [10, 20, 30, 40, 50]
        expected_output = max(numbers)
        try:
            student_output = func(numbers)
            if student_output == expected_output:
                self.status_tasks["task_11"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_11"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 11: Error - {e}"
        
    def check_task_12(self, func):
        """Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
        Exemplu: Pentru numărul 5 rezultatul va fi 120
        """
        number = 8
        expected_output = 40320
        try:
            student_output = func(number)
            if student_output == expected_output:
                self.status_tasks["task_12"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_12"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 12: Error - {e}"
        
    def check_task_13(self, func):
        """Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
        Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
        """
        number_1 = 3
        number_2 = 4
        expected_output = (7, 12)
        try:
            student_output = func(number_1, number_2)
            if student_output == expected_output:
                self.status_tasks["task_13"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_13"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 13: Error - {e}"
        
    def check_task_14(self, func):
        """Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
        Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
        """
        age_1 = 65
        expected_output_1 = "adult"
        age_2 = 17
        expected_output_2 = "minor"
        age_3 = 66
        expected_output_3 = "senior"
        try:
            student_output_1 = func(age_1)
            student_output_2 = func(age_2)
            student_output_3 = func(age_3)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2 and student_output_3 == expected_output_3:
                self.status_tasks["task_14"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_14"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 14: Error - {e}"
        
    def check_task_15(self, func):
        """Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
        Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
        """
        string_1 = "ana"
        expected_output_1 = True
        string_2 = "test"
        expected_output_2 = False
        try:
            student_output_1 = func(string_1)
            student_output_2 = func(string_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_15"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_15"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 15: Error - {e}"
        
    def check_task_16(self, func):
        """Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
        Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
        """
        string = "test"
        expected_output = string[::-1]
        try:
            student_output = func(string)
            if student_output == expected_output:
                self.status_tasks["task_16"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_16"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 16: Error - {e}"
        
    def check_task_17(self, func):
        """Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
        Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
        """
        string = "Hello, World!"
        expected_output = len(string.split())
        try:
            student_output = func(string)
            if student_output == expected_output:
                self.status_tasks["task_17"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_17"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 17: Error - {e}"
        
    def check_task_18(self, func):
        """Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
        Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
        """
        celsius = 0
        expected_output = 32.0
        try:
            student_output = func(celsius)
            if student_output == expected_output:
                self.status_tasks["task_18"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_18"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 18: Error - {e}"
        
    def check_task_19(self, func):
        """Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
        Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 7
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        try:
            student_output_1 = func(number_1)
            student_output_2 = func(number_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_19"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_19"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 19: Error - {e}"
        
    def check_task_20(self, func):
        """Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
        Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
        Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 28
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        try:
            student_output_1 = func(number_1)
            student_output_2 = func(number_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_20"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_20"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 20: Error - {e}"
        
    def check_task_21(self, func):
        """Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
        Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
        Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 153
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        try:
            student_output_1 = func(number_1)
            student_output_2 = func(number_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_21"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_21"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 21: Error - {e}"
        
    def check_task_22(self, func):
        """Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
        Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
        Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
        """
        number_1 = 18
        expected_output_1 = True
        number_2 = 14
        expected_output_2 = False
        try:
            student_output_1 = func(number_1)
            student_output_2 = func(number_2)
            if student_output_1 == expected_output_1 and student_output_2 == expected_output_2:
                self.status_tasks["task_22"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_22"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 22: Error - {e}"
        
    def check_task_23(self, func):
        """Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
        Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
        """
        number = 5
        expected_output = [0, 1, 1, 2, 3]
        try:
            student_output = func(number)
            if student_output == expected_output:
                self.status_tasks["task_23"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_23"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 23: Error - {e}"
        
    def check_task_24(self, func):
        """Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
        Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
        """
        number = 10
        expected_output = [1, 2, 5, 10]
        try:
            student_output = func(number)
            if student_output == expected_output:
                self.status_tasks["task_24"] = True
                return "Exercise 1: Correct! Well done."
            else:
                self.status_tasks["task_24"] = False
                return "Exercise 1: Incorrect. Please try again."
        except Exception as e:
            return f"Exercise 24: Error - {e}"


    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"