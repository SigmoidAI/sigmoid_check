class Task13:
    """Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
    Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
    Exemplu: task_13('listen', 'silent') ➞ True
    Exemplu: task_13('hello', 'world') ➞ False
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('listen', 'silent') == True
            assert self.func('hello', 'world') == False
            assert self.func('listen', 'silent', 'hello', 'world') == False
            assert self.func('listen', 'silent', 'enlist', 'silent') == False
            assert self.func('listen', 'silent', 'enlist', 'silent', 'listen', 'silent') == True
            assert self.func('listen', 'silent', 'enlist', 'silent', 'listen', 'silent', 'listen', 'silent') == True
            assert self.func() == False
            assert self.func('listen') == False
            assert self.func('listen', 'silent', 'enlist', 'silent', 'listen', 'silent', 'listen') == False
            assert self.func('listen', 'silent', 'enlist', 'silent', 'listen', 'silent', 'listen', 'silent', 'listen') == False
            assert self.func("listen", "silent", "listen", "silent", "listen", "silent", "listen", "silent", "listen", "silent") == True
            return True
        except:
            return False
