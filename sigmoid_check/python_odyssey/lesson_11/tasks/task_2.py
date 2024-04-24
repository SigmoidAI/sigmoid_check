class Task2:
    """Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
    Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 2, 'a', 'b') == [1, 2]
            assert self.func(1, 2, 3, 4, 5) == [1, 2, 3, 4, 5]
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            assert self.func("a", "b", "c", "d", "e") == []
            assert self.func(1, 2, 3, 4, 5, "a", "b", "c", "d", "e") == [1, 2, 3, 4, 5]
            assert self.func(1, 2, 3, 4, 5, "a", "b", "c", "d", "e", 6, 7, 8, 9, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            assert self.func("2", "3", "4", "5", "6") == []
            assert self.func(1, 2, 3, 4, 5, "6", "7", "8", "9", "10") == [1, 2, 3, 4, 5]
            return True
        except:
            return False
