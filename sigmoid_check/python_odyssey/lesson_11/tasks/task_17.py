class Task17:
    """Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
    Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
    Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
    Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
    Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
    Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
    Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
    Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2, add=[3, 4, 5]) == 14
            assert self.func(2, sub=[3, 4, 5]) == -10
            assert self.func(2, mul=[3, 4, 5]) == 120
            assert self.func(2, div=[3, 4, 5]) == 0.008333333333333333
            assert self.func(2, add=[3, 4, 5], sub=[1, 2]) == 11
            assert self.func(2, add=[3, 4, 5], sub=[1, 2], mul=[2, 3]) == ((2+3+4+5-1-2)*2*3)
            assert self.func(2, add=[3, 4, 5], sub=[1, 2], mul=[2, 3], div=[1, 2]) == ((((2+3+4+5)-1-2)*2*3)/1)/2
            assert self.func(2, sub=[3, 4, 5], mul=[2, 3], div=[1, 2]) == ((2-3-4-5)*2*3)/1/2
            assert self.func(2, add=[3, 4, 5], mul=[2, 3], div=[1, 2]) == ((2+3+4+5)*2*3)/1/2
            assert self.func(2, add=[3, 4, 5], sub=[1, 2], div=[1, 2]) == ((((2+3)+4)+5-1-2)/1)/2
            assert self.func(2, add=[3, 4, 5], sub=[1, 2], mul=[2, 3], div=[1, 2]) == ((((((2+3)+4)+5)-1-2)*2*3)/1)/2
            assert self.func(2, div=[3, 4, 5], sub=[1, 2], mul=[2, 3], add=[1, 2]) == ((((((2/3)/4)/5-1-2)*2)*3)+1)+2
            return True
        except:
            return False
