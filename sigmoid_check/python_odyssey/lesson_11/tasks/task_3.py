class Task3:
    """Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
    Exemplu: task_3(1, 4, 5) ➞ 20
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 4, 5) == 20
            assert self.func(1) == 1
            assert self.func(1, 2, 3) == 6
            assert self.func(1, 2, 3, 4, 5) == 120
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 3628800
            assert self.func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) == 1307674368000
            assert self.func(0, 1, 2, 3, 4, 5) == 0
            return True
        except:
            return False
