class Task10:
    """Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
    Funcția va returna toate argumentele care sunt divizibile cu `number`.
    Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 2, 3, 4, 5, number=2) == [2, 4]
            assert self.func(1, 2, 3, 4, 5, number=3) == [3]
            assert self.func(1, 2, 3, 4, 5, number=4) == [4]
            assert self.func(1, 2, 3, 4, 5, number=5) == [5]
            assert self.func(1, 2, 3, 4, 5, number=6) == []
            assert self.func(100, 120, 130, 140, 150, number=10) == [100, 120, 130, 140, 150]
            assert self.func(300, 120, 86, 93, 150, number=3) == [300, 120, 93]
            assert self.func(1, 2, 3, 4, 5, number=1) == [1, 2, 3, 4, 5]
            assert self.func(1, 2, 3, 4, 5, number=0) == []
            return True
        except:
            return False
