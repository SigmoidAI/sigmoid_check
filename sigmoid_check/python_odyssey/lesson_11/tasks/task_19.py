class Task19:
    """Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
    Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9) == {2: 1, 3: 1, 5: 1, 7: 1}
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == {2: 1, 3: 1, 5: 1, 7: 1}
            assert self.func() == {}
            assert self.func(1, 2, 2, 2, 2, 7, 7, 7, 5) == {2: 4, 5: 1, 7: 3}
            assert self.func(4, 4, 4, 4, 4) == {}
            return True
        except:
            return False
