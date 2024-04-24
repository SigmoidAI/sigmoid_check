class Task6:
    """Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword care sunt de tip string și valoarea acestora.
    Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(a=1, b=2, c=3) == {'a': 1, 'b': 2, 'c': 3}
            assert self.func(a=1) == {'a': 1}
            assert self.func(a=1, b=2, c=3, d=4, e=5) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
            assert self.func(ciao=1, bella=2, come=3, stai=4) == {'ciao': 1, 'bella': 2, 'come': 3, 'stai': 4}
            assert self.func(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
            assert self.func(a_2=1, b_2=2, c_2=3, d_2=4, e_2=5) == {'a_2': 1, 'b_2': 2, 'c_2': 3, 'd_2': 4, 'e_2': 5}
            return True
        except:
            return False
