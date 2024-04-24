class Task12:
    """Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
    Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
    Exemplu: task_12(2, 3, 5, 7) ➞ True
    Exemplu: task_12(1, 2, 3, 4) ➞ False
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2, 3, 5, 7) == True
            assert self.func(1, 2, 3, 4) == False
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == False
            assert self.func(2, 3, 5, 7, 11, 13, 17, 19, 23, 29) == True
            assert self.func(1, 4, 6, 8, 9, 10, 12, 14, 15, 16) == False
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == False
            assert self.func(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31) == True
            assert self.func(1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18) == False
            assert self.func(0) == False
            assert self.func() == False
            assert self.func(2) == True
            return True
        except:
            return False
