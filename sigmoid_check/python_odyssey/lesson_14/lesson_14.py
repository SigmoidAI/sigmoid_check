class Task1:
    pass


class Task2:
    pass


class Task3:
    pass


class Lesson14:
    """Test class for checking the implementation of tasks in lesson 13 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {
            "task_1": False,
            "task_2": False,
            "task_3": False,
        }

    def check_task_1(self, class_user, class_user_manager, class_user_admin):
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
        try:
            solution_task_1 = Task1(class_user, class_user_manager, class_user_admin)
            self.status_tasks["task_1"] = solution_task_1.check_task()
            if self.status_tasks["task_1"]:
                return "Task 1: Correct! Well done."
            return "Task 1: Incorrect! Please try again."
        except AssertionError as e:
            return f"Task 1: Error! {e}"
        
    def check_task_2(self, class_user, class_sistem):
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
        try:
            solution_task_2 = Task2(class_user, class_sistem)
            self.status_tasks["task_2"] = solution_task_2.check_task()
            if self.status_tasks["task_2"]:
                return "Task 2: Correct! Well done."
            return "Task 2: Incorrect! Please try again."
        except AssertionError as e:
            return f"Task 2: Error! {e}"

    def check_task_3(self, class_app):
        """1. Creează o clasă `TechSolutionsApp` care va conține o valoare a clasei `versiune_applicatie` cu valoarea implicită "1.0".
        Această clasă va avea nevoie de 3 metode, fiecare dintre acestea va fi utilizată pentru a simula interacțiunea cu sistemul nostru.

        Metoda `market_view` va fi o metodă statică care nu va avea acces la self sau cls și va returna string-ul "Vizualizare piață".
        Metoda `delogat_view` va fi o metodă de clasă care va avea acces la cls și va returna string-ul "Versiunea aplicației este *versiune-aplicatie*" utilizând atributul clasei.
        Metoda `account_view` va fi o metodă de instanță care va avea acces la self și va returna string-ul "Vizualizare aplicație user *versiune-aplicatie*" utilizând atributul instanței.
        """
        try:
            solution_task_3 = Task3(class_app)
            self.status_tasks["task_3"] = solution_task_3.check_task()
            if self.status_tasks["task_3"]:
                return "Task 3: Correct! Well done."
            return "Task 3: Incorrect! Please try again."
        except AssertionError as e:
            return f"Task 3: Error! {e}"

    def get_completion_percentage(self):
        """Return the completion percentage of the tasks"""
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"