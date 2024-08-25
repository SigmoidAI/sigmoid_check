import time
import itertools


class Task1:
    """Creează o funcție lambda numită `task1` care adaugă 10 la un număr dat."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(10) == 20
            return True
        except:
            return False

class Task2:
    """Creează o funcție lambda numită `task2` care verifică dacă un număr este par."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(4) == True
            assert self.func(5) == False
            return True
        except:
            return False

class Task3:
    """Creează o funcție lambda numită `task3` care înmulțește două numere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2, 3) == 6
            assert self.func(7, 5) == 35
            return True
        except:
            return False

class Task4:
    """Crează o funcție lambda numită `task4` care returnează lungimea unui șir de caractere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("test") == 4
            assert self.func("Python") == 6
            return True
        except:
            return False

class Task5:
    """Creează o funcție lambda numită `task5` care convertește un șir de caractere în majuscule."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("test") == "TEST"
            assert self.func("Python") == "PYTHON"
            return True
        except:
            return False

class Task6:
    """Creează o funcție lambda numită `task6` care găsește maximul dintre trei numere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(1, 2, 3) == 3
            assert self.func(10, 20, 15) == 20
            return True
        except:
            return False

class Task7:
    """Creează o funcție lambda numită `task7` care concatenează două șiruri de caractere cu un spațiu între ele."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("Hello", "World") == "Hello World"
            assert self.func("Python", "Programming") == "Python Programming"
            return True
        except:
            return False

class Task8:
    """Creează o funcție lambda numită `task8` care filtrează numerele impare dintr-o listă și le returnează."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([1, 2, 3, 4, 5]) == [2, 4]
            assert self.func([10, 11, 12, 13, 14]) == [10, 12, 14]
            return True
        except:
            return False

class Task9:
    """Creează o funcție lambda numită `task9` care calculează factorialul unui număr folosind funcția reduce din functools (google it!)."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(5) == 120
            assert self.func(6) == 720
            return True
        except:
            return False

class Task10:
    """Creează o funcție lambda numită `task10` care sortează o listă de tuple după a doua valoare din fiecare tuple."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([(1, 3), (2, 2), (3, 1)]) == [(3, 1), (2, 2), (1, 3)]
            assert self.func([(5, 6), (1, 9), (4, 3)]) == [(4, 3), (5, 6), (1, 9)]
            return True
        except:
            return False

class Task11:
    """Creează o funcție lambda numită `task11` care returnează rădăcina pătrată a unui număr."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(4) == 2.0
            assert self.func(9) == 3.0
            return True
        except:
            return False

class Task12:
    """Creează o funcție lambda numită `task12` care verifică dacă un șir de caractere este palindrom."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("madam") == True
            assert self.func("hello") == False
            return True
        except:
            return False

class Task13:
    """Creează o funcție lambda numită `task13` care numără numărul de vocale dintr-un șir de caractere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("hello") == 2
            assert self.func("education") == 5
            return True
        except:
            return False

class Task14:
    """Creează o funcție lambda numită `task14` care returnează inversul unui șir de caractere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func("hello") == "olleh"
            assert self.func("Python") == "nohtyP"
            return True
        except:
            return False

class Task15:
    """Creează o funcție lambda numită `task15` care filtrează toate șirurile de caractere mai lungi de 5 caractere dintr-o listă."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(["apple", "banana", "pear"]) == ["apple", "pear"]
            assert self.func(["hello", "world", "Python"]) == ["hello", "world"]
            return True
        except:
            return False

class Task16:
    """Creează o funcție lambda numită `task16` care sortează o listă de dicționare după o cheie specificată."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            lst = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
            assert self.func(lst, "age") == [{"name": "Jane", "age": 25}, {"name": "John", "age": 30}]
            assert self.func(lst, "name") == [{"name": "Jane", "age": 25}, {"name": "John", "age": 30}]
            return True
        except:
            return False

class Task17:
    """Creează o funcție lambda numită `task17` care găsește cel mai mare divizor comun al două numere."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(48, 18) == 6
            assert self.func(20, 8) == 4
            return True
        except:
            return False

class Task18:
    """Creează o funcție lambda numită `task18` care calculează suma pătratelor numerelor pare dintr-o listă."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func([1, 2, 3, 4, 5]) == 20
            assert self.func([10, 11, 12, 13, 14]) == 440
            return True
        except:
            return False

class Task19:
    """Creează o funcție lambda numită `task19` care verifică dacă un an dat este bisect."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(2020) == True
            assert self.func(2019) == False
            return True
        except:
            return False

class Task20:
    """Creează o funcție lambda numită `task20` care găsește cel mai lung cuvânt dintr-o listă de cuvinte."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            assert self.func(["apple", "banana", "pear"]) == "banana"
            assert self.func(["hello", "world", "Python"]) == "Python"
            return True
        except:
            return False

# Generators

class Task21:
    """Creează un generator numit `task21` care generează numere de la 1 la 10."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            assert list(gen) == list(range(1, 11))
            return True
        except:
            return False

class Task22:
    """Creează un generator numit `task22` care generează pătratele numerelor de la 1 la 10."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            assert list(gen) == [i ** 2 for i in range(1, 11)]
            return True
        except:
            return False

class Task23:
    """Creează un generator numit `task23` care generează caracterele unui string primit ca input unul câte unul."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("test")
            assert list(gen) == list("test")
            return True
        except:
            return False

class Task24:
    """Creează un generator numit `task24` care generează numere pare până la un limită dată ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(10)
            assert list(gen) == [2, 4, 6, 8, 10]
            return True
        except:
            return False

class Task25:
    """Creează un generator numit `task25` care primește ca input un număr n și generează primele n numere Fibonacci."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == [0, 1, 1, 2, 3]
            return True
        except:
            return False

class Task26:
    """Creează un generator numit `task26` care generează numere prime până la o limită dată ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(10)
            assert list(gen) == [2, 3, 5, 7]
            return True
        except:
            return False

class Task27:
    """Creează un generator numit `task27` care generează numere într-un interval specificat start, și end cu un pas dat."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(0, 10, 2)
            assert list(gen) == [0, 2, 4, 6, 8]
            return True
        except:
            return False

class Task28:
    """Creează un generator numit `task28` care generează toate subșirurile unui șir oferit sub formă de string.
    Exemplu:
    pentru input-ul "ciao"
    output-ul va fi: "c", "ci", "cia", "ciao", "i", "ia", "iao", "a", "ao", "o"
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("abc")
            assert list(gen) == ["a", "ab", "abc", "b", "bc", "c"]
            return True
        except:
            return False

class Task29:
    """Creează un generator numit `task29` care generează factorialul numerelor de la 1 la n primind n ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == [1, 2, 6, 24, 120]
            return True
        except:
            return False

class Task30:
    """Creează un generator numit `task30` care generează cifrele unui număr în ordine inversă primind numărul ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1234)
            assert list(gen) == [4, 3, 2, 1]
            return True
        except:
            return False

class Task31:
    """Creează un generator numit `task31` care generează toate combinațiile posibile ale elementelor dintr-o listă.
    Exemplu:
    pentru input-ul [1, 2, 3, 4]
    output-ul va fi: (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3])
            expected_combinations = [
                (1,), (2,), (3,),
                (1, 2), (1, 3), (2, 3),
                (1, 2, 3)
            ]
            assert list(gen) == expected_combinations
            return True
        except:
            return False

class Task32:
    """Creează un generator numit `task32` care generează suma curentă a unei liste de numere primite ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3, 4])
            assert list(gen) == [1, 3, 6, 10]
            return True
        except:
            return False

class Task33:
    """Creează un generator numit `task33` care generează primele n termeni ai unei secvențe aritmetice primind a, d și n ca input unde a este primul termen, d este diferența sau pasul de creștere și n este numărul de termeni.
    Exemplu:
    pentru input-ul a=1, d=2, n=5
    output-ul va fi: 1, 3, 5, 7, 9
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1, 2, 5)
            assert list(gen) == [1, 3, 5, 7, 9]
            return True
        except:
            return False

class Task34:
    """Creează un generator numit `task34` care generează puterile lui 2 până la o limită dată ca input (inclusiv)."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(16)
            assert list(gen) == [1, 2, 4, 8, 16]
            return True
        except:
            return False

class Task35:
    """Creează un generator numit `task35` care generează numere într-o secvență geometrică infinită primind a și r ca input unde a este primul termen și r este rația.
    Exemplu:
    pentru input-ul a=2, r=3
    output-ul va fi: 2, 6, 18, 54, 162, ...
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(1, 2)
            result = [next(gen) for _ in range(5)]
            assert result == [1, 2, 4, 8, 16]
            return True
        except:
            return False

class Task36:
    """Creează un generator numit `task36` care generează permutările unei liste primite ca input.
    Exemplu:
    pentru input-ul [1, 2, 3]
    output-ul va fi: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func([1, 2, 3])
            assert list(gen) == list(itertools.permutations([1, 2, 3]))
            return True
        except:
            return False

class Task37:
    """Creează un generator numit `task37` care generează toți factorii primi ai unui număr dat ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(18)
            assert list(gen) == [2, 3, 3]
            return True
        except:
            return False

class Task38:
    """Creează un generator numit `task38` care generează reprezentarea binară a numerelor de la 1 la n primind n ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func(5)
            assert list(gen) == ["1", "10", "11", "100", "101"]
            return True
        except:
            return False

class Task39:
    """Creează un generator numit `task39` care generează toate anagramele unui șir dat ca input.
    Exemplu:
    pentru input-ul "abc"
    output-ul va fi: "abc", "acb", "bac", "bca", "cab", "cba"
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func("abc")
            assert list(gen) == list(itertools.permutations("abc"))
            return True
        except:
            return False

class Task40:
    """Creează un generator numit `task40` care generează termenii unei serii matematice simple. 
    De exemplu, acest generator va produce termenii unei serii în care fiecare termen este dat de formula:

    termen = (-1)^n / n!

    Aici, n este indexul termenului (începând de la 0), iar n! (n factorial) este produsul tuturor numerelor întregi pozitive până la n.
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            gen = self.func()
            result = [next(gen) for _ in range(5)]
            print(result)
            assert result == [1.0, -1.0, 0.5, -0.16666666666666666, 0.041666666666666664]
            return True
        except:
            return False
# Decorators

class Task41:
    """Creează un decorator numit `task41` care afișează timpul de execuție al unei funcții în formatul "Execution time: x seconds"."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                time.sleep(1)
                return "Done"
            result = dummy_function()
            assert result == "Done"
            return True
        except:
            return False

class Task42:
    """Creează un decorator numit `task42` care afișează mesaje "Before" și "After" în jurul apelului unei funcții."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "Done"
            result = dummy_function()
            assert result == "Done"
            return True
        except:
            return False

class Task43:
    """Creează un decorator numit `task43` care memorează rezultatele unei funcții într-un dicționar `cache` pentru a le returna direct dacă aceleași argumente sunt folosite din nou."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function(x):
                return x + 10
            result1 = dummy_function(5)
            result2 = dummy_function(5)
            assert result1 == 15
            assert result2 == 15
            return True
        except:
            return False

class Task44:
    """Creează un decorator numit `task44` care numără de câte ori o funcție este apelată. La fiecare apel, afișează numărul de apeluri în formatul "Count: x"."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "Done"
            result1 = dummy_function()
            result2 = dummy_function()
            assert result1 == "Done"
            assert result2 == "Done"
            return True
        except:
            return False

class Task45:
    """Creează un decorator numit `task45` care convertește rezultatul unei funcții în majuscule."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                return "done"
            result = dummy_function()
            assert result == "DONE"
            return True
        except:
            return False

class Task46:
    """Creează un decorator numit `task46` care reîncearcă o funcție dacă aceasta aruncă o excepție. Dacă funcția aruncă o excepție, decoratorul va încerca să o apeleze din nou de 3 ori."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func
            def dummy_function():
                raise ValueError("Test")
            dummy_function()
            return False
        except ValueError:
            return True

class Task47:
    """Creează un decorator numit `task47` care adaugă o valoare specificată la valoarea returnată de o funcție primind valoarea ca input."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func(5)
            def dummy_function(x):
                return x
            result = dummy_function(10)
            assert result == 15
            return True
        except:
            return False

class Task48:
    """Creează un decorator numit `task48` care validează tipurile argumentelor primite de o funcție și aruncă o excepție `TypeError` dacă tipurile nu sunt cele așteptate."""
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func([int, int])
            def dummy_function(x, y):
                return x + y
            result = dummy_function(5, 10)
            assert result == 15
            return True
        except:
            return False

class Task49:
    """Creează un decorator numit `task49` care asigură că o funcție este apelată doar de utilizatori cu un anumit rol. Utilizând decoratorul, vei specifica rolul necesar pentru a apela funcția.

    Aceasta va arunca o excepție `PermissionError` dacă utilizatorul nu are rolul specificat.
    """
    def __init__(self, func):
        self.func = func

    def check_task(self):
        try:
            @self.func("admin")
            def dummy_function():
                return "Done"
            dummy_function("user")
            return False
        except PermissionError:
            print("PermissionError")
            return True


class Lesson16:
    """Test class for checking the implementation of tasks in lesson 16 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 50)}

    def check_task(self, task_number, func):
        task_class = globals()[f"Task{task_number}"]
        solution_task = task_class(func)
        try:
            self.status_tasks[f"task_{task_number}"] = solution_task.check_task()
            if self.status_tasks[f"task_{task_number}"]:
                return f"Task {task_number}: Correct! Well done."
            return f"Task {task_number}: Incorrect! Please try again."
        except:
            return f"Task {task_number}: Error!"

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"
