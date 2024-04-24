class Task18:
    """Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
    Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('hello', 'world') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
            assert self.func('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
            assert self.func('world') == {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
            assert self.func('hello', 'world', 'hello') == {'h': 2, 'e': 2, 'l': 6, 'o': 3, 'w': 1, 'r': 1, 'd': 1}
            assert self.func('hello', 'world', 'hello', 'world') == {'h': 2, 'e': 2, 'l': 6, 'o': 4, 'w': 2, 'r': 2, 'd': 2}
            assert self.func() == {}
            assert self.func("aaaaaaaaa") == {'a': 9}
            return True
        except:
            return False
