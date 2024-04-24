class Task11:
    """Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
    Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
    Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
    Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 1, 2, 3, 5, 8) == True
            assert self.func(1, 1, 2, 3, 5, 9) == False
            assert self.func(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144) == True
            assert self.func(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 145) == False
            assert self.func(1, 2, 34 , 55, 89, 144) == False
            assert self.func(1, 1) == True
            assert self.func(1, 1, 3) == True
            assert self.func(0) == False
            assert self.func() == False
            return True
        except:
            return False
