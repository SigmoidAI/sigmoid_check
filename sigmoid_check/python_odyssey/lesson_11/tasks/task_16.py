class Task16:
    """Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
    Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
    Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
    Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
    Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
    Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
    Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2, 3, 4, 5, operation='add') == 14
            assert self.func(2, 3, 4, 5, operation='sub') == -10
            assert self.func(2, 3, 4, 5, operation='mul') == 120
            assert self.func(2, 3, 4, 5, operation='div') == 0.008333333333333333
            assert self.func(-1, operation='add') == -1
            assert self.func(-1, operation='sub') == -1
            assert self.func(-1, operation='mul') == -1
            assert self.func(-1, operation='div') == -1
            assert self.func(0, operation='add') == 0
            assert self.func(0, operation='sub') == 0
            assert self.func(0, operation='mul') == 0
            assert self.func(0, operation='div') == 0
            return True
        except:
            return False
