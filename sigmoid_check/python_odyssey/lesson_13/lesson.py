class Task1:
    """1. Avem nevoie să creezi o clasă `Produs`, aceasta trebuie să accepte 3 parametri: numele, pretul, anul_producerii
    Cu ajutorul acestei clase trebuie să fiu capabil să creeze câte obiecte doresc cu orice configurație a numelui, prețului și anul_producerii

    Exemplu utilizare:
    telefon = Produs("Iphone", 15000, 2020) # Voi putea crea un obiect utilizând anumiți parametri de intrare
    print(telefon.numele)                   # Voi putea accesa numele obiectului creat
    print(telefon.pretul)                   # Voi putea accesa pretul obiectului creat
    print(telefon.anul_producerii)          # Voi putea accesa anul producerii obiectului creat
    """
    def __init__(self, class_to_test) -> None:
        self.class_to_test = class_to_test

    def check_task(self):
        try:
            phone_test_1 = self.class_to_test('Samsung', 500, 300)
            assert phone_test_1.numele == 'Samsung', 'Asigură-te că ai creat atributul numele'
            assert phone_test_1.pretul == 500, 'Asigură-te că ai creat atributul pretul'
            assert phone_test_1.anul_producerii == 300, 'Asigură-te că ai creat atributul anul_producerii'
            return True
        except:
            return False
        
class Task2:
    """2.1Prima clasă se numește `Telefon` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `baterie_mAh` și `memorie_GB`

    De asemenea aceasta va avea o metodă numită `upgrade_memory` care va primi un parametru `new_memory` și va actualiza valoarea memoriei telefonului.
    Totodată aceasta va avea o metodă numită `upgrade_battery` care va primi un parametru `new_battery` și va actualiza valoarea bateriei telefonului.
    """
    def __init__(self, child, parent) -> None:
        self.class_to_test = child
        self.parent_class = parent

    def check_task(self):
        try:
            phone_test_1 = self.class_to_test('Samsung', 500, 300, 4000, 128)
            assert phone_test_1.baterie_mAh == 4000, 'Asigură-te că ai creat atributul baterie_mAh'
            assert phone_test_1.memorie_GB == 128, 'Asigură-te că ai creat atributul memorie_GB'
            assert issubclass(self.class_to_test, self.parent_class), 'Clasa nu mosteneste clasa parinte'
            phone_test_1.upgrade_memory(256)
            assert phone_test_1.memorie_GB == 256, 'Metoda upgrade_memory nu functioneaza'
            phone_test_1.upgrade_battery(5000)
            assert phone_test_1.baterie_mAh == 5000, 'Metoda upgrade_battery nu functioneaza'
            return True
        except:
            return False
        
class Task3:
    """2.2 A doua clasă se numește `Laptop` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `sistem_de_operare` și `procesor`

    De asemenea aceasta va avea o metodă numită `upgrade_processor` care va primi un parametru `new_processor` și va actualiza valoarea procesorului laptopului.
    Totodată aceasta va avea o metodă numită `upgrade_os` care va primi un parametru `new_os` și va actualiza valoarea sistemului de operare al laptopului.
    """
    def __init__(self, child, parent) -> None:
        self.class_to_test = child
        self.parent_class = parent

    def check_task(self):
        try:
            laptop_test_1 = self.class_to_test('Samsung', 500, 300, 'Windows', 'Intel i5')
            assert laptop_test_1.sistem_de_operare == 'Windows', 'Asigură-te că ai creat atributul sistem_de_operare'
            assert laptop_test_1.procesor == 'Intel i5', 'Asigură-te că ai creat atributul procesor'
            assert issubclass(self.class_to_test, self.parent_class), 'Clasa nu mosteneste clasa parinte'
            laptop_test_1.upgrade_processor('Intel i7')
            assert laptop_test_1.procesor == 'Intel i7', 'Metoda upgrade_processor nu functioneaza'
            laptop_test_1.upgrade_os('Windows 11')
            assert laptop_test_1.sistem_de_operare == 'Windows 11', 'Metoda upgrade_os nu functioneaza'
            return True
        except:
            return False
        
class Task4:
    """2.3 A treia clasă se numește `trotineta` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `viteza_maxima` și `autonomie_km`

    De asemenea aceasta va avea o metodă numită `upgrade_speed` care va primi un parametru `new_speed` și va actualiza valoarea vitezei maxime a trotinetei.
    Totodată aceasta va avea o metodă numită `upgrade_autonomy` care va primi un parametru `new_autonomy` și va actualiza valoarea autonomiei trotinetei.
    """
    def __init__(self, child, parent) -> None:
        self.class_to_test = child
        self.parent_class = parent

    def check_task(self):
        try:
            trotineta_test_1 = self.class_to_test('Samsung', 500, 300, 25, 30)
            assert trotineta_test_1.viteza_maxima == 25, 'Asigură-te că ai creat atributul viteza_maxima'
            assert trotineta_test_1.autonomie_km == 30, 'Asigură-te că ai creat atributul autonomie_km'
            assert issubclass(self.class_to_test, self.parent_class), 'Clasa nu mosteneste clasa parinte'
            trotineta_test_1.upgrade_speed(30)
            assert trotineta_test_1.viteza_maxima == 30, 'Metoda upgrade_speed nu functioneaza'
            trotineta_test_1.upgrade_autonomy(40)
            assert trotineta_test_1.autonomie_km == 40, 'Metoda upgrade_autonomy nu functioneaza'
            return True
        except:
            return False
        
class Task5:
    """Avem nevoie de o clasă nouă care să se numească `AppleProduct` care va moșteni clasa `Produs` și va avea un parametru în plus numit `culoare` și `produs_conectat` 
    parametrul `produs_conectat` va avea valoarea "nimic" la crearea unui produs astfel încât nu va fi necesar de menționat la crearea unui obiect nou
    De asemenea va avea o metodă numită `combine_products` care va primi un parametru `product` ce va reprezenta un alt obiect de tip `AppleProduct` care va fi salvat în parametrul `produs_conectat`
    Există o singură condiție, produsul conectat trebuie să fie de tip `AppleProduct` iar culoarea acestuia trebuie să fie aceeași cu a produsului curent.

    Exemplu utilizare:
    iphone = AppleProduct("Iphone", 15000, 2020, "negru")
    airpods = AppleProduct("Airpods", 1000, 2021, "alb")
    iphone.combine_products(airpods) # În acest caz se va returna textul "Produsul nu poate fi conectat deoarece culorile nu coincid"

    iphone = AppleProduct("Iphone", 15000, 2020, "negru")
    airpods = AppleProduct("Airpods", 1000, 2021, "negru")
    iphone.combine_products(airpods) # În acest caz se va returna textul "Produsul a fost conectat cu succes" și dacă se va printa iphone.produs_conectat se va returna obiectul airpods
    print(iphone.produs_conectat.numele) # Va returna numele produsului conectat
    print(iphone.produs_conectat.pretul) # Va returna prețul produsului conectat
    """
    def __init__(self, child, parent) -> None:
        self.class_to_test = child
        self.parent_class = parent
    
    def check_task(self):
        try:
            iphone = self.class_to_test("Iphone", 15000, 2020, "negru")
            airpods = self.class_to_test("Airpods", 1000, 2021, "alb")
            assert iphone.produs_conectat == 'nimic', 'Asigură-te că ai creat atributul produs_conectat cu valoarea default "nimic"'
            assert iphone.culoare == 'negru', 'Asigură-te că ai creat atributul culoare'
            assert issubclass(self.class_to_test, self.parent_class), 'Clasa nu mosteneste clasa parinte'
            assert iphone.combine_products(airpods) == 'Produsul nu poate fi conectat deoarece culorile nu coincid', 'Metoda combine_products nu functioneaza'
            airpods = self.class_to_test("Airpods", 1000, 2021, "negru")
            assert iphone.combine_products(airpods) == 'Produsul a fost conectat cu succes', 'Metoda combine_products nu functioneaza'
            assert iphone.produs_conectat == airpods, 'Metoda combine_products nu functioneaza'
            iphone2 = self.class_to_test("Iphone", 15000, 2020, "negru", airpods)
            assert iphone2.produs_conectat == airpods, 'Metoda combine_products nu functioneaza, parametrul produs_conectat nu este setat corect'
            return True
        except:
            return False
        
class Task6:
    """
    Avem nevoie de o clasă nouă care să se numească `GoogleProduct` care va moșteni clasa `AppleProduct` posibilitățile la ambele sunt aceleași, dar va fi nevoie de o singură schimbare.
    Produsul conectat trebuie să fie de tip `GoogleProduct` iar culoarea acestuia poate să fie diferită de a produsului curent.
    Asta ar însemna că singurul element care va necesita modificări este metoda `combine_products` care va trebui să accepte orice tip de obiect de tip `GoogleProduct`

    Exemplu utilizare:
    pixel = GoogleProduct("Pixel", 10000, 2020, "negru")
    home = GoogleProduct("Home", 500, 2021, "alb")
    pixel.combine_products(home) # În acest caz se va returna textul "Produsul a fost conectat cu succes" și dacă se va printa pixel.produs_conectat se va returna obiectul home
    print(pixel.produs_conectat.numele) # Va returna numele produsului conectat
    """
    def __init__(self, child, parent) -> None:
        self.class_to_test = child
        self.parent_class = parent

    def check_task(self):
        try:
            pixel = self.class_to_test("Pixel", 10000, 2020, "negru")
            home = self.class_to_test("Home", 500, 2021, "alb")
            assert pixel.produs_conectat == 'nimic', 'Asigură-te că ai creat atributul produs_conectat cu valoarea default "nimic"'
            assert pixel.culoare == 'negru', 'Asigură-te că ai creat atributul culoare'
            assert issubclass(self.class_to_test, self.parent_class), 'Clasa nu mosteneste clasa parinte'
            assert pixel.combine_products(home) == 'Produsul a fost conectat cu succes', 'Metoda combine_products nu functioneaza'
            assert pixel.produs_conectat == home, 'Metoda combine_products nu functioneaza'
            pixel2 = self.class_to_test("Pixel", 10000, 2020, "negru", home)
            assert pixel2.produs_conectat == home, 'Metoda combine_products nu functioneaza, parametrul produs_conectat nu este setat corect'
            return True
        except:
            return False
        
class Task7:
    """Avem nevoie de o clasă nouă pentru aceasta, ea se va numi `Magazin` și va conține doar 2 metode, `vinde_produs` și `returneaza_produs`

    Metoda `vinde_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost vândut cu succes"
    Metoda `returneaza_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost returnat cu succes"

    Exemplu utilizare:
    iphone = AppleProduct("Iphone", 15000, 2020, "negru")
    print(magazin.vinde_produs(iphone)) # Va returna textul "Produsul Iphone a fost vândut cu succes"
    print(magazin.returneaza_produs(iphone)) # Va returna textul "Produsul Iphone a fost returnat cu succes
    """
    def __init__(self, class_to_test, product_class) -> None:
        self.class_to_test = class_to_test
        self.product_class = product_class

    def check_task(self):
        try:
            magazin = self.class_to_test()
            iphone = self.product_class("Ciao", 15000, 2020)
            assert magazin.vinde_produs(iphone) == 'Produsul Ciao a fost vândut cu succes', 'Metoda vinde_produs nu functioneaza'
            assert magazin.returneaza_produs(iphone) == 'Produsul Ciao a fost returnat cu succes', 'Metoda returneaza_produs nu functioneaza'
            return True
        except:
            return False

class Lesson13:
    """Test class for checking the implementation of tasks in lesson 13 of the Python Odyssey Bootcamp."""
    def __init__(self):
        self.status_tasks = {f"task_{i}": False for i in range(1, 8)}

    def check_task(self, task_number, *args):
        task_class = globals()[f"Task{task_number}"]
        solution_task = task_class(*args)
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