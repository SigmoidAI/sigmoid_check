class Task1:
    """Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
    și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

    Clasa va primi ca parametru o listă de numere integer.
    - __init__ initializează clasa cu lista de numere.
    - __str__ va returna lista de numere sub formă de string.
    - __len__ va returna numărul de elemente din listă.
    - __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
    - __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
    - __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
    """
    def __init__(self, class_data_container):
        self.class_data_container = class_data_container

    def check_task(self):
        try:
            container = self.class_data_container([1, 2, 3])
            container2 = self.class_data_container([4, 5, 6])
            assert str(container) == "[1, 2, 3]"
            assert len(container) == 3
            assert container[1] == 2
            container[1] = 20
            assert container[1] == 20
            combined_container = container + container2
            assert str(combined_container) == "[1, 20, 3, 4, 5, 6]"
            return True
        except:
            return False

class Task2:
    """Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
    - `SumaContainer` va calcula suma elementelor din listă.
    - `ProdusContainer` va calcula produsul elementelor din listă.
    Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
    """
    def __init__(self, class_suma_container, class_produs_container):
        self.class_suma_container = class_suma_container
        self.class_produs_container = class_produs_container

    def check_task(self):
        try:
            suma_container = self.class_suma_container([1, 2, 3])
            produs_container = self.class_produs_container([1, 2, 3])
            assert suma_container.calculate() == 6
            assert produs_container.calculate() == 6
            return True
        except:
            return False

class Task3:
    """Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
    Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
    - __init__ va inițializa clasa cu lista de obiecte.
    - `add_container` va permite adăugarea unui nou container în listă.
    - `__call__` va returna o listă cu valorile maxime ale fiecărui container.
    """
    def __init__(self, class_data_analysis, class_data_container):
        self.class_data_analysis = class_data_analysis
        self.class_data_container = class_data_container

    def check_task(self):
        try:
            container1 = self.class_data_container([1, 2, 3])
            container2 = self.class_data_container([4, 5, 6])
            analysis = self.class_data_analysis([container1, container2])
            assert analysis() == [3, 6]
            analysis.add_container(self.class_data_container([7, 8, 9]))
            assert analysis() == [3, 6, 9]
            return True
        except:
            return False

class Task4:
    """Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
    Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
    - __init__ va inițializa clasa cu lista de obiecte.
    - `add_container` va permite adăugarea unui nou container în listă.
    - `mean` va returna media aritmetică a elementelor din toate containerele.
    - `median` va returna mediana elementelor din toate containerele.
    - `min` va returna valoarea minimă din toate containerele.
    - `sum` va returna suma elementelor din toate containerele.
    """
    def __init__(self, class_data_statistics, class_data_container):
        self.class_data_statistics = class_data_statistics
        self.class_data_container = class_data_container

    def check_task(self):
        try:
            container1 = self.class_data_container([1, 2, 3])
            container2 = self.class_data_container([4, 5, 6])
            stats = self.class_data_statistics([container1, container2])
            assert stats.mean() == 3.5
            assert stats.median() == 3.5
            assert stats.min() == 1
            assert stats.sum() == 21
            return True
        except:
            return False

class Task5:
    """Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
    - __init__ va inițializa clasa cu lista de obiecte.
    - `add_container` va permite adăugarea unui nou container în listă.
    - `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
    - `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
    - `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
    - `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
    """
    def __init__(self, class_data_filter, class_data_statistics, class_data_container):
        self.class_data_filter = class_data_filter
        self.class_data_statistics = class_data_statistics
        self.class_data_container = class_data_container

    def check_task(self):
        try:
            container1 = self.class_data_container([1, 2, 3, 0, -1, -2])
            container2 = self.class_data_container([4, 5, 6, 0, -3, -4])
            filter = self.class_data_filter([container1, container2])
            stats = self.class_data_statistics([container1, container2])
            assert sorted(filter.filter_zeros()) == sorted([1, 2, 3, -1, -2, 4, 5, 6, -3, -4])
            assert sorted(filter.filter_negatives()) == sorted([-1, -2, -3, -4])
            assert sorted(filter.filter_positives()) == sorted([1, 2, 3, 0, 4, 5, 6, 0])
            assert sorted(filter.filter_under_mean()) == sorted([1, 2, 3, 4, 5, 6])
            return True
        except:
            return False

class Lesson15:
    """Test class for checking the implementation of tasks in lesson 15 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {
            "task_1": False,
            "task_2": False,
            "task_3": False,
            "task_4": False,
            "task_5": False
        }

    def check_task_1(self, class_data_container):
        """Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
        și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

        Clasa va primi ca parametru o listă de numere integer.
        - __init__ initializează clasa cu lista de numere.
        - __str__ va returna lista de numere sub formă de string.
        - __len__ va returna numărul de elemente din listă.
        - __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
        - __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
        - __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
        """
        solution_task_1 = Task1(class_data_container)
        self.status_tasks["task_1"] = solution_task_1.check_task()
        return "Task 1: Correct! Well done." if self.status_tasks["task_1"] else "Task 1: Incorrect! Please try again."

    def check_task_2(self, class_suma_container, class_produs_container, class_data_container):
        """Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
        - `SumaContainer` va calcula suma elementelor din listă.
        - `ProdusContainer` va calcula produsul elementelor din listă.
        Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
        """
        solution_task_2 = Task2(class_suma_container, class_produs_container)
        self.status_tasks["task_2"] = solution_task_2.check_task()
        return "Task 2: Correct! Well done." if self.status_tasks["task_2"] else "Task 2: Incorrect! Please try again."

    def check_task_3(self, class_data_analysis, class_data_container):
        """Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
        Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
        - __init__ va inițializa clasa cu lista de obiecte.
        - `add_container` va permite adăugarea unui nou container în listă.
        - `__call__` va returna o listă cu valorile maxime ale fiecărui container.
        """
        solution_task_3 = Task3(class_data_analysis, class_data_container)
        self.status_tasks["task_3"] = solution_task_3.check_task()
        return "Task 3: Correct! Well done." if self.status_tasks["task_3"] else "Task 3: Incorrect! Please try again."

    def check_task_4(self, class_data_statistics, class_data_container):
        """Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
        Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
        - __init__ va inițializa clasa cu lista de obiecte.
        - `add_container` va permite adăugarea unui nou container în listă.
        - `mean` va returna media aritmetică a elementelor din toate containerele.
        - `median` va returna mediana elementelor din toate containerele.
        - `min` va returna valoarea minimă din toate containerele.
        - `sum` va returna suma elementelor din toate containerele.
        """
        solution_task_4 = Task4(class_data_statistics, class_data_container)
        self.status_tasks["task_4"] = solution_task_4.check_task()
        return "Task 4: Correct! Well done." if self.status_tasks["task_4"] else "Task 4: Incorrect! Please try again."

    def check_task_5(self, class_data_filter, class_data_statistics, class_data_container):
        """Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
        - __init__ va inițializa clasa cu lista de obiecte.
        - `add_container` va permite adăugarea unui nou container în listă.
        - `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
        - `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
        - `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
        - `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
        """
        solution_task_5 = Task5(class_data_filter, class_data_statistics, class_data_container)
        self.status_tasks["task_5"] = solution_task_5.check_task()
        return "Task 5: Correct! Well done." if self.status_tasks["task_5"] else "Task 5: Incorrect! Please try again."

    def get_completion_percentage(self):
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"
