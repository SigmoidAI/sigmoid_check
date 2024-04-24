from tasks.task_1 import Task1
from tasks.task_2 import Task2
from tasks.task_3 import Task3
from tasks.task_4 import Task4
from tasks.task_5 import Task5
from tasks.task_6 import Task6
from tasks.task_7 import Task7
from tasks.task_8 import Task8
from tasks.task_9 import Task9
from tasks.task_10 import Task10
from tasks.task_11 import Task11
from tasks.task_12 import Task12
from tasks.task_13 import Task13
from tasks.task_14 import Task14
from tasks.task_15 import Task15
from tasks.task_16 import Task16
from tasks.task_17 import Task17
from tasks.task_18 import Task18
from tasks.task_19 import Task19
from tasks.task_20 import Task20


class Lesson11:
    """Test class for checking the implementation of tasks in lesson 11 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {
            "task_1": False,
            "task_2": False,
            "task_3": False,
            "task_4": False,
            "task_5": False,
            "task_6": False,
            "task_7": False,
            "task_8": False,
            "task_9": False,
            "task_10": False,
            "task_11": False,
            "task_12": False,
            "task_13": False,
            "task_14": False,
            "task_15": False,
            "task_16": False,
            "task_17": False,
            "task_18": False,
            "task_19": False,
            "task_20": False,
        }

    def check_task_1(self, func):
        """Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
        Exemplu: task_1(1, 2, 3) ➞ 6
        """
        try:
            solution_task_1 = Task1(func)
            self.status_tasks["task_1"] = solution_task_1.check_task()
            if self.status_tasks["task_1"]:
                return "Task 1: Correct! Well done."
            return "Task 1: Incorrect! Please try again."
        except Exception as e:
            return f"Task 1: Error! {e}"
        
    def check_task_2(self, func):
        """Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
        Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
        """
        try:
            solution_task_2 = Task2(func)
            self.status_tasks["task_2"] = solution_task_2.check_task()
            if self.status_tasks["task_2"]:
                return "Task 2: Correct! Well done."
            return "Task 2: Incorrect! Please try again."
        except Exception as e:
            return f"Task 2: Error! {e}"

    def check_task_3(self, func):
        """Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
        Exemplu: task_3(1, 4, 5) ➞ 20
        """
        try:
            solution_task_3 = Task3(func)
            self.status_tasks["task_3"] = solution_task_3.check_task()
            if self.status_tasks["task_3"]:
                return "Task 3: Correct! Well done."
            return "Task 3: Incorrect! Please try again."
        except Exception as e:
            return f"Task 3: Error! {e}"
    
    def check_task_4(self, func):
        """Task: Creați o funcție cu numele `task_4` care primește un număr arbitrar de perechi cheie-valoare și returnează un string care conține toate cheile și valorile concatenate separate de un spațiu.
        Exemplu: task_4(a=1, b=2, c=3) ➞ 'a 1 b 2 c 3'
        """
        try:
            solution_task_4 = Task4(func)
            self.status_tasks["task_4"] = solution_task_4.check_task()
            if self.status_tasks["task_4"]:
                return "Task 4: Correct! Well done."
            return "Task 4: Incorrect! Please try again."
        except Exception as e:
            return f"Task 4: Error! {e}"
    
    def check_task_5(self, func):
        """Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
        Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
        Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
        Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
        Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
        """
        try:
            solution_task_5 = Task5(func)
            self.status_tasks["task_5"] = solution_task_5.check_task()
            if self.status_tasks["task_5"]:
                return "Task 5: Correct! Well done."
            return "Task 5: Incorrect! Please try again."
        except Exception as e:
            return f"Task 5: Error! {e}"

    def check_task_6(self, func):
        """Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword care sunt de tip string și valoarea acestora.
        Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
        """
        try:
            solution_task_6 = Task6(func)
            self.status_tasks["task_6"] = solution_task_6.check_task()
            if self.status_tasks["task_6"]:
                return "Task 6: Correct! Well done."
            return "Task 6: Incorrect! Please try again."
        except Exception as e:
            return f"Task 6: Error! {e}"
    
    def check_task_7(self, func):
        """Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: `str` și `int`.
        Cheia `str` va avea o listă cu toate string-urile primite ca argumente, iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
        Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
        """
        try:
            solution_task_7 = Task7(func)
            self.status_tasks["task_7"] = solution_task_7.check_task()
            if self.status_tasks["task_7"]:
                return "Task 7: Correct! Well done."
            return "Task 7: Incorrect! Please try again."
        except Exception as e:
            return f"Task 7: Error! {e}"
    
    def check_task_8(self, func):
        """Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
        Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
        Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
        """
        try:
            solution_task_8 = Task8(func)
            self.status_tasks["task_8"] = solution_task_8.check_task()
            if self.status_tasks["task_8"]:
                return "Task 8: Correct! Well done."
            return "Task 8: Incorrect! Please try again."
        except Exception as e:
            return f"Task 8: Error! {e}"
    
    def check_task_9(self, func):
        """Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
        Funcția va returna toate argumentele care sunt multipli ai lui `number`.
        Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
        """
        try:
            solution_task_9 = Task9(func)
            self.status_tasks["task_9"] = solution_task_9.check_task()
            if self.status_tasks["task_9"]:
                return "Task 9: Correct! Well done."
            return "Task 9: Incorrect! Please try again."
        except Exception as e:
            return f"Task 9: Error! {e}"
    
    def check_task_10(self, func):
        """Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
        Funcția va returna toate argumentele care sunt divizibile cu `number`.
        Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
        """
        try:
            solution_task_10 = Task10(func)
            self.status_tasks["task_10"] = solution_task_10.check_task()
            if self.status_tasks["task_10"]:
                return "Task 10: Correct! Well done."
            return "Task 10: Incorrect! Please try again."
        except Exception as e:
            return f"Task 10: Error! {e}"

    def check_task_11(self, func):
        """Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
        Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
        Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
        Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
        """
        try:
            solution_task_11 = Task11(func)
            self.status_tasks["task_11"] = solution_task_11.check_task()
            if self.status_tasks["task_11"]:
                return "Task 11: Correct! Well done."
            return "Task 11: Incorrect! Please try again."
        except Exception as e:
            return f"Task 11: Error! {e}"
    
    def check_task_12(self, func):
        """Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
        Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
        Exemplu: task_12(2, 3, 5, 7) ➞ True
        Exemplu: task_12(1, 2, 3, 4) ➞ False
        """
        try:
            solution_task_12 = Task12(func)
            self.status_tasks["task_12"] = solution_task_12.check_task()
            if self.status_tasks["task_12"]:
                return "Task 12: Correct! Well done."
            return "Task 12: Incorrect! Please try again."
        except Exception as e:
            return f"Task 12: Error! {e}"
    
    def check_task_13(self, func):
        """Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
        Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
        Exemplu: task_13('listen', 'silent') ➞ True
        Exemplu: task_13('hello', 'world') ➞ False
        """
        try:
            solution_task_13 = Task13(func)
            self.status_tasks["task_13"] = solution_task_13.check_task()
            if self.status_tasks["task_13"]:
                return "Task 13: Correct! Well done."
            return "Task 13: Incorrect! Please try again."
        except Exception as e:
            return f"Task 13: Error! {e}"
    
    def check_task_14(self, func):
        """Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
        Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
        Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
        """
        try:
            solution_task_14 = Task14(func)
            self.status_tasks["task_14"] = solution_task_14.check_task()
            if self.status_tasks["task_14"]:
                return "Task 14: Correct! Well done."
            return "Task 14: Incorrect! Please try again."
        except Exception as e:
            return f"Task 14: Error! {e}"
    
    def check_task_15(self, func):
        """Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
        Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
        Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
        Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
        """
        try:
            solution_task_15 = Task15(func)
            self.status_tasks["task_15"] = solution_task_15.check_task()
            if self.status_tasks["task_15"]:
                return "Task 15: Correct! Well done."
            return "Task 15: Incorrect! Please try again."
        except Exception as e:
            return f"Task 15: Error! {e}"
    
    def check_task_16(self, func):
        """Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
        Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
        Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
        Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
        Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
        Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
        Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
        """
        try:
            solution_task_16 = Task16(func)
            self.status_tasks["task_16"] = solution_task_16.check_task()
            if self.status_tasks["task_16"]:
                return "Task 16: Correct! Well done."
            return "Task 16: Incorrect! Please try again."
        except Exception as e:
            return f"Task 16: Error! {e}"
    
    def check_task_17(self, func):
        """Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
        Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
        Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
        Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
        Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
        Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
        Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
        Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
        """
        try:
            solution_task_17 = Task17(func)
            self.status_tasks["task_17"] = solution_task_17.check_task()
            if self.status_tasks["task_17"]:
                return "Task 17: Correct! Well done."
            return "Task 17: Incorrect! Please try again."
        except Exception as e:
            return f"Task 17: Error! {e}"
    
    def check_task_18(self, func):
        """Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
        Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
        """
        try:
            solution_task_18 = Task18(func)
            self.status_tasks["task_18"] = solution_task_18.check_task()
            if self.status_tasks["task_18"]:
                return "Task 18: Correct! Well done."
            return "Task 18: Incorrect! Please try again."
        except Exception as e:
            return f"Task 18: Error! {e}"
    
    def check_task_19(self, func):
        """Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
        Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
        """
        try:
            solution_task_19 = Task19(func)
            self.status_tasks["task_19"] = solution_task_19.check_task()
            if self.status_tasks["task_19"]:
                return "Task 19: Correct! Well done."
            return "Task 19: Incorrect! Please try again."
        except Exception as e:
            return f"Task 19: Error! {e}"
    
    def check_task_20(self, func):
        """Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
        Exemplu: task_20('hello', 'world') ➞ {5: 2}
        Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
        """
        try:
            solution_task_20 = Task20(func)
            self.status_tasks["task_20"] = solution_task_20.check_task()
            if self.status_tasks["task_20"]:
                return "Task 20: Correct! Well done."
            return "Task 20: Incorrect! Please try again."
        except Exception as e:
            return f"Task 20: Error! {e}"

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"