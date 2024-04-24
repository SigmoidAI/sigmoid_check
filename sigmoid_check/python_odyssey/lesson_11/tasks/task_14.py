class Task14:
    """Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
    Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
    Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('home', 'same', 'meme', sub_string="me") == ['home', 'meme', 'same']
            assert self.func('home', 'same', 'meme', sub_string="ho") == ['home']
            assert self.func('home', 'same', 'meme', sub_string="sa") == ['same']
            assert self.func(sub_string="sa") == []
            assert self.func("123", "456", "789", sub_string="1") == ["123"]
            assert self.func("123", "456", "789", sub_string="") == []
            return True
        except:
            return False
