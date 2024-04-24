class Task15:
    """Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
    Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
    Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
    Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('home', 'same', 'meme', sub_string='me') == {'contains': ['home', 'same', 'meme'], 'not_contains': []}
            assert self.func('home', 'same', 'meme', sub_string='ho') == {'contains': ['home'], 'not_contains': ['same', 'meme']}
            assert self.func('home', 'same', 'meme', sub_string='sa') == {'contains': ['same'], 'not_contains': ['home', 'meme']}
            assert self.func(sub_string='sa') == {'contains': [], 'not_contains': []}
            assert self.func('123', '456', '789', sub_string='1') == {'contains': ['123'], 'not_contains': ['456', '789']}
            assert self.func('123', '456', '789', sub_string='') == {'contains': [], 'not_contains': ['123', '456', '789']}
            assert self.func(sub_string="") == {'contains': [], 'not_contains': []}
            return True
        except:
            return False
