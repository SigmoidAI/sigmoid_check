class Lesson10:
    "Test class for cheking the implementation of the tasks in lesson 10"
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 25)}

    def check_task(self, task_number, func, test_cases):
        if not callable(func):
            return f"Task {task_number}: Error - Provided argument is of type {type(func).__name__}, but a callable (a function) was expected."
        
        try:
            for test_case, expected_output in test_cases:
                student_output = func(*test_case)
                assert student_output == expected_output, \
                    f"Expected output: {expected_output}, but got: {student_output}."
            self.status_tasks[f"task_{task_number}"] = True
            return f"Exercise {task_number}: Correct! Well done."
        except AssertionError as e:
            self.status_tasks[f"task_{task_number}"] = False
            return f"Exercise {task_number}: Incorrect. {e} Please try again."
        except Exception as e:
            return f"{task_number}: Error - {e}"
            
    def check_task_1(self, func):
        """Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
        Utilizați list comprehension."""
        expected_output = [i for i in range(1, 11)]
        test_cases = [([], expected_output)]
        return self.check_task(1, func, test_cases)
        
    def check_task_2(self, func):
        """Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
        Utilizați list comprehension în proces"""
        expected_output = [i**2 for i in range(1, 11)]
        test_cases = [([], expected_output)]
        return self.check_task(2, func, test_cases)

    def check_task_3(self, func):
        """Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
        Utilizați list comprehension în proces.
        """
        expected_output = [i for i in range(1, 11) if i % 2 != 0]
        test_cases = [([], expected_output)]
        return self.check_task(3, func, test_cases)

    def check_task_4(self, func):
        """Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
        va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
        """
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected_output = [num for row in matrix for num in row]
        test_cases = [((matrix,), expected_output)]
        return self.check_task(4, func, test_cases)
        
    def check_task_5(self, func):
        """Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
        """
        n = 10
        expected_output = ["par" if i % 2 == 0 else "impar" for i in range(1, n+1)]
        test_cases = [((n,), expected_output)]
        return self.check_task(5, func, test_cases)
        
    def check_task_6(self, func):
        """Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        """
        n = 5
        expected_output = {i: i**3 for i in range(1, n+1)}
        test_cases = [((n,), expected_output)]
        return self.check_task(6, func, test_cases)
        
    def check_task_7(self, func):
        """Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
        Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
        Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
        """
        n = 50
        expected_output = {i for i in range(1, n+1) if i % 3 == 0}
        test_cases = [((n,), expected_output)]
        return self.check_task(7, func, test_cases)

    def check_task_8(self, func):
        """Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
        Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
        """
        numbers = [1, 2, 3, 4, 5]
        expected_output = sum(numbers) / len(numbers)
        test_cases = [((numbers,), expected_output)]
        return self.check_task(8, func, test_cases)
        
    def check_task_9(self, func):
        """Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
        Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
        """
        test_cases = [
            ((4,), True),
            ((5,), False)
        ]
        return self.check_task(9, func, test_cases)
        
    def check_task_10(self, func):
        """Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
        apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
        Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
        """
        name = "Ana"
        age = 32
        city = "București"
        expected_output_with_city = f"Nume: {name}, Varsta: {age}, Oras: {city}"
        expected_output_without_city = f"Nume: {name}, Varsta: {age}, Oras: None"
        test_cases = [
            ((name, age, city), expected_output_with_city),
            ((name, age), expected_output_without_city)
        ]
        return self.check_task(10, func, test_cases)
        
    def check_task_11(self, func):
        """Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
        Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
        """
        numbers = [10, 20, 30, 40, 50]
        expected_output = max(numbers)
        test_cases = [((numbers,), expected_output)]
        return self.check_task(11, func, test_cases)
        
    def check_task_12(self, func):
        """Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
        Exemplu: Pentru numărul 5 rezultatul va fi 120
        """
        number = 8
        expected_output = 40320
        test_cases = [((number,), expected_output)]
        return self.check_task(12, func, test_cases)
        
    def check_task_13(self, func):
        """Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
        Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
        """
        number_1 = 3
        number_2 = 4
        expected_output = (7, 12)
        test_cases = [
            ((number_1, number_2), expected_output)
        ]
        return self.check_task(13, func, test_cases)
        
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
        test_cases = [
            (age_1, expected_output_1),
            (age_2, expected_output_2),
            (age_3, expected_output_3)
        ]
        return self.check_task(14, func, test_cases)
        
    def check_task_15(self, func):
        """Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
        Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
        """
        string_1 = "ana"
        expected_output_1 = True
        string_2 = "test"
        expected_output_2 = False
        test_cases = [
            (string_1, expected_output_1),
            (string_2, expected_output_2)
        ]
        return self.check_task(15, func, test_cases)
        
    def check_task_16(self, func):
        """Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
        Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
        """
        string = "test"
        expected_output = string[::-1]
        test_cases = [((string,), expected_output)]
        return self.check_task(16, func, test_cases)
        
        
    def check_task_17(self, func):
        """Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
        Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
        """
        string = "Hello, World!"
        expected_output = len(string.split())
        test_cases = [((string,), expected_output)]
        return self.check_task(17, func, test_cases)
        
    def check_task_18(self, func):
        """Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
        Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
        """
        celsius = 0
        expected_output = 32.0
        test_cases = [((celsius,), expected_output)]
        return self.check_task(18, func, test_cases)
        
    def check_task_19(self, func):
        """Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
        Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 7
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        test_cases = [
            ((number_1,), expected_output_1),
            ((number_2,), expected_output_2)
        ]
        return self.check_task(19, func, test_cases)
        
    def check_task_20(self, func):
        """Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
        Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
        Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 28
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        test_cases = [
            ((number_1,), expected_output_1),
            ((number_2,), expected_output_2)
        ]
        return self.check_task(20, func, test_cases)
        
    def check_task_21(self, func):
        """Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
        Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
        Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
        """
        number_1 = 153
        expected_output_1 = True
        number_2 = 10
        expected_output_2 = False
        test_cases = [
            ((number_1,), expected_output_1),
            ((number_2,), expected_output_2)
        ]
        return self.check_task(21, func, test_cases)
        
    def check_task_22(self, func):
        """Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
        Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
        Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
        """
        number_1 = 18
        expected_output_1 = True
        number_2 = 14
        expected_output_2 = False
        test_cases = [
            ((number_1,), expected_output_1),
            ((number_2,), expected_output_2)
        ]
        return self.check_task(22, func, test_cases)
        
    def check_task_23(self, func):
        """Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
        Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
        """
        number = 5
        expected_output = [0, 1, 1, 2, 3]
        test_cases = [((number,), expected_output)]
        return self.check_task(23, func, test_cases)
        
    def check_task_24(self, func):
        """Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
        Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
        """
        number = 10
        expected_output = [1, 2, 5, 10]
        test_cases = [((number,), expected_output)]
        return self.check_task(24, func, test_cases)

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"