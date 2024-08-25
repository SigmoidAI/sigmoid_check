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
    def __init__(self, class_suma_container, class_produs_container, class_data_container):
        self.class_suma_container = class_suma_container
        self.class_produs_container = class_produs_container
        self.class_data_container = class_data_container

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
        self.status_tasks = {f"task_{i}": False for i in range(1, 6)}

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
        completed = sum([1 for task in self.status_tasks if self.status_tasks[task]])
        return f"Your completion percentage is {completed * 100 / len(self.status_tasks)}%"

class DataContainer:
    def __init__(self, data):
        """
        Initializează clasa cu o listă de numere integer.
        """
        self.data = data

    def __str__(self):
        """
        Returnează lista de numere sub formă de string.
        """
        return str(self.data)

    def __len__(self):
        """
        Returnează numărul de elemente din listă.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Permite accesarea elementelor din listă folosind indexul.
        """
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Permite modificarea elementelor din listă folosind indexul.
        """
        self.data[index] = value

    def __add__(self, other):
        """
        Permite combinarea a două instanțe de DataContainer într-o singură instanță.
        """
        if isinstance(other, DataContainer):
            combined_data = self.data + other.data
            return DataContainer(combined_data)
        raise TypeError("Can only add another DataContainer instance.")