class Task20:
    """Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
    Exemplu: task_20('hello', 'world') ➞ {5: 2}
    Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('hello', 'world') == {5: 2}
            assert self.func('hello', 'world', 'python') == {5: 2, 6: 1}
            assert self.func('hello', 'world', 'python', 'java') == {5: 2, 6: 1, 4: 1}
            assert self.func('hello', 'world', 'python', 'java', 'ruby') == {5: 2, 6: 1, 4: 2}
            assert self.func() == {}
            assert self.func("aaaaaaaaa") == {9: 1}
            return True
        except:
            return False
