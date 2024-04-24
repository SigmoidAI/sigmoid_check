class Task1:
    """Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
    Exemplu: task_1(1, 2, 3) ➞ 6
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, -4, 5) == 2
            assert self.func(1) == 1
            assert self.func(1, 2, 3) == 6
            assert self.func(1, 2, 3, 4, 5) == 15
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) == 120
            return True
        except:
            return False
