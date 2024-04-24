class Task8:
    """Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
    Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
    Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func('madam', 'hello', 'level', 'world') == {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
            assert self.func('madam', 'hello', 'level', 'world', 'civic') == {'palindrom': ['madam', 'level', 'civic'], 'non_palindrom': ['hello', 'world']}
            assert self.func('madam', 'hello', 'level', 'world', 'civic', 'radar') == {'palindrom': ['madam', 'level', 'civic', 'radar'], 'non_palindrom': ['hello', 'world']}
            assert self.func("cai", "ciao", "bella", "come", "stai") == {'palindrom': [], 'non_palindrom': ['cai', 'ciao', 'bella', 'come', 'stai']}
            assert self.func("cai", "ciao", "bella", "come", "stai", "radar") == {'palindrom': ['radar'], 'non_palindrom': ['cai', 'ciao', 'bella', 'come', 'stai']}
            assert self.func("", "") == {'palindrom': [], 'non_palindrom': []}
            assert self.func("a", "b") == {'palindrom': [], 'non_palindrom': ['a', 'b']}
            assert self.func() == {'palindrom': [], 'non_palindrom': []}
            return True
        except:
            return False
