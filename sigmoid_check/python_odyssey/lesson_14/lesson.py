class Task1:
    """1. Creează o clasă `Utilizator` care să conțină un atribut public `nume` și un atribut protejat `_nivel_acces` cu valoarea implicită "Default".
        Clasa `Utilizator` trebuie să conțină metoda `afiseaza_nivel_acces` care să returneze string-ul "*nume-utilizator* are nivelul de acces *nivel-acces*.".
        De asemenea, clasa `Utilizator` trebuie să conțină metoda `utilizeaza_sistem` care să returneze string-ul "*nume-utilizator* poate utiliza funcții de bază ale sistemului.".

    2. Creează o clasă `UtilizatorManager` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Manager".
        Clasa `UtilizatorManager` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
        De asemenea, clasa `UtilizatorManager` trebuie să conțină metoda `citeste_date_utilizator` care să returneze string-ul "*nume-utilizator* poate citi datele utilizatorilor.".

    3. Creează o clasă `UtilizatorAdmin` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Admin".
        Clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
        De asemenea, clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_date_utilizator` care să returneze string-ul "*nume-utilizator* poate modifica datele utilizatorilor.".
    """
    def __init__(self, class_user, class_user_manager, class_user_admin):
        self.class_user = class_user
        self.class_user_manager = class_user_manager
        self.class_user_admin = class_user_admin

    def check_task(self):
        try:
            user = self.class_user("User")
            user_manager = self.class_user_manager("Manager")
            user_admin = self.class_user_admin("Admin")
            assert user.afiseaza_nivel_acces() == "User are nivelul de acces Default."
            assert user.utilizeaza_sistem() == "User poate utiliza funcții de bază ale sistemului."
            assert user_manager.afiseaza_nivel_acces() == "Manager are nivelul de acces Manager."
            assert user_manager.modifica_setari() == "Manager poate modifica setările sistemului."
            assert user_manager.citeste_date_utilizator() == "Manager poate citi datele utilizatorilor."
            assert user_admin.afiseaza_nivel_acces() == "Admin are nivelul de acces Admin."
            assert user_admin.modifica_setari() == "Admin poate modifica setările sistemului."
            assert user_admin.modifica_date_utilizator() == "Admin poate modifica datele utilizatorilor."
            assert issubclass(self.class_user_manager, self.class_user)
            assert issubclass(self.class_user_admin, self.class_user)
            return True
        except:
            return False


class Task2:
    """1. Pentru această sarcină vom crea o copie a clasei `Utilizator` de mai sus, deoarece vom avea nevoie de aceeași structură pentru a adăuga utilizatorii în sistem.
    Creează o clasă `user` care să conțină un atribut privat `_nume` și un atribut protejat `__nivel_acces` cu valoarea implicită "Default".
    Acum avem nevoie de un getter și un setter pentru atributul `_nume` și `__nivel_acces` pentru a putea modifica aceste valori în afara clasei.

    2. Creează o clasă `Sistem` care va conține un atribut privat `__utilizatori` inițializat cu un dicționar gol în care cheile vor fi id-ul și valorile utilizatorii.
        Clasa `Sistem` trebuie să conțină metoda `adauga_utilizator` care va primi un obiect de tip `Utilizator` și va adăuga utilizatorul la dicționar împreună cu un nou id.
        De asemenea, clasa `Sistem` trebuie să conțină metoda `afiseaza_utilizatori` care va returna o listă cu numele utilizatorilor existenți.
        Clasa `Sistem` trebuie să conțină metoda `verifica_nivel_acces` care va primi numele unui utilizator și va returna nivelul de acces al utilizatorului respectiv.
        Clasa `Sistem` trebuie să conțină și metoda `modifica_name_user` care va primi id-ul utilizatorului și noul nume al utilizatorului și va modifica numele utilizatorului respectiv.
        Clasa `Sistem` trebuie să conțină și metoda `sterge_utilizator` care va primi id-ul utilizatorului și va șterge utilizatorul respectiv.
        Clasa `Sistem` trebuie să conțină și metoda `modifica_nivel_acces` care va primi id-ul utilizatorului și noul nivel de acces al utilizatorului și va modifica nivelul de acces al utilizatorului respectiv.
    """
    def __init__(self, class_user, class_sistem):
        self.class_user = class_user
        self.class_sistem = class_sistem

    def check_task(self):
        try:
            user = self.class_user("User")
            sistem = self.class_sistem()
            sistem.adauga_utilizator(user)
            assert sistem.afiseaza_utilizatori() == ["User"]
            assert sistem.verifica_nivel_acces("User") == "Default"
            sistem.modifica_name_user(1, "User2")
            assert sistem.afiseaza_utilizatori() == ["User2"]
            sistem.modifica_nivel_acces(1, "Manager")
            assert sistem.verifica_nivel_acces("User2") == "Manager"
            sistem.sterge_utilizator(1)
            assert sistem.afiseaza_utilizatori() == []
            return True
        except:
            return False


class Task3:
    """1. Creează o clasă `TechSolutionsApp` care va conține o valoare a clasei `versiune_applicatie` cu valoarea implicită "1.0".
        Această clasă va avea nevoie de 3 metode, fiecare dintre acestea va fi utilizată pentru a simula interacțiunea cu sistemul nostru.
        De asemenea clasa va primi ca argument la inițializare o valoare ce va reprezenta versiunea aplicatiei care va fi stocată în atributul `self.versiune_aplicatie`.

        Metoda `market_view` va fi o metodă statică care nu va avea acces la self sau cls și va returna string-ul "Vizualizare piață".
        Metoda `delogat_view` va fi o metodă de clasă care va avea acces la cls și va returna string-ul "Versiunea aplicației este *versiune-aplicatie*" utilizând atributul clasei.
        Metoda `account_view` va fi o metodă de instanță care va avea acces la self și va returna string-ul "Vizualizare aplicație user *versiune-aplicatie*" utilizând atributul instanței.
    """
    def __init__(self, class_app):
        self.class_app = class_app

    def check_task(self):
        try:
            app = self.class_app("3.0")
            assert app.market_view() == "Vizualizare piață"
            assert app.delogat_view() == "Versiunea aplicației este 1.0"
            assert app.account_view() == "Vizualizare aplicație user 3.0"
            return True
        except AssertionError:
            return False

class Lesson14:
    """Test class for checking the implementation of tasks in lesson 13 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 4)}

    def check_task(self, task_number, *args):
        """Check a specific task by its number and corresponding classes or functions."""
        task_class = globals()[f"Task{task_number}"]
        solution_task = task_class(*args)
        try:
            self.status_tasks[f"task_{task_number}"] = solution_task.check_task()
            if self.status_tasks[f"task_{task_number}"]:
                return f"Task {task_number}: Correct! Well done."
            return f"Task {task_number}: Incorrect! Please try again."
        except Exception as e:
            return f"Task {task_number}: Error!"

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"
