class Task5:
    """Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
    Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
    Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
    Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
    Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(3, 1, 2, a=10, b=20) == ([1, 2, 3], [])
            assert self.func(3, 1, 2, a=10, b=20, c='a') == ([1, 2, 3], ['c'])
            assert self.func(3, 1, 2, a=10, b=20, c='a', d='b') == ([1, 2, 3], ['c', 'd'])
            assert self.func(3, 1, 2, a=10, b=20, c='a', d='b', e=30) == ([1, 2, 3], ['c', 'd'])
            assert self.func(3, 1, 2, a=10, b=20, c='a', d='b', e=30, f='c') == ([1, 2, 3], ['c', 'd', 'f'])
            assert self.func(3, 1, 2, a=10, b=20, c='a', d='b', e=30, f='c', g='d') == ([1, 2, 3], ['c', 'd', 'f', 'g'])
            assert self.func(a=10, b=20, c='a', d='b', e=30, f='c', g='d') == ([], ['c', 'd', 'f', 'g'])
            assert self.func(a=10, b=20, c='a', d='b', e=30) == ([], ['c', 'd'])
            assert self.func(a=10, b=20, c='a', d='b') == ([], ['c', 'd'])
            assert self.func(a=10, b=20, c='a') == ([], ['c'])
            assert self.func(a=10, b=20) == ([], [])
            assert self.func(a=10) == ([], [])
            assert self.func() == ([], [])
            return True
        except:
            return False
