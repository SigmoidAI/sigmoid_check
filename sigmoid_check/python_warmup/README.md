python-warmup

The idea of this module of sigmoid-check will be that anyone can refresh their skills in python, it would represent a set of exercises separated by topics in python one followed after another.

First version: will contain all exercises, arranged by skillset (first basic going towards advanced)

Here are topics and exercises with examples for them from which python_warmup will be built:

```python
print("This is a text that I want to print")
print("This is how I use it one time")
print("This is how I use it another time")
print("This is how I use it one last time just to prove that I can lol")
```

```python
print("This is a text that I want to print", end=" ")
print("This is how I use it one time", end=" ")
print("This is how I use it another time", end=" ")
print("This is how I use it one last time just to prove that I can lol")
```

```python
# Aceasta este prima ta sarcină legată de variabile în python
# Creează o variabilă numită `age` și seteaz-o la vârsta ta

# CODUL TĂU VINE MAI JOS:
age = 25
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age)
# CODUL TĂU VINE MAI SUS:

# Acum schimbă valoarea variabilei `age` la vârsta prietenului tău și afișează valoarea variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
age = 30
print(age)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `age2` și seteaz-o la valoarea variabilei `age` și afișează valoarea variabilei `age2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
age2 = age
print(age2)
# CODUL TĂU VINE MAI SUS:

# Acum șterge variabila `age` și încearcă să afișezi valoarea variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
del age
print(age)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină
```

```python
# Aceasta este a doua sarcină legată de booleeni în python
# Creați o variabilă numită `is_student` și setați-o la `True`

# CODUL TĂU VINE MAI JOS:
is_student = True
# CODUL TĂU VINE MAI SUS:

# Acum tipăriți valoarea variabilei `is_student` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(is_student)
# CODUL TĂU VINE MAI SUS:

# Acum creați o nouă variabilă numită `is_child` și setați-o la `False` și tipăriți valoarea variabilei `is_child` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
is_child = False
print(is_child)
# CODUL TĂU VINE MAI SUS:

# Acum utilizați operatorul `and` pentru a verifica dacă atât `is_student`, cât și `is_child` sunt `True` și tipăriți rezultatul folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
result_and = is_student and is_child
print(result_and)
# CODUL TĂU VINE MAI SUS:

# Acum utilizați operatorul `or` pentru a verifica dacă cel puțin una dintre `is_student` și `is_child` este `True` și tipăriți rezultatul folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
result_or = is_student or is_child
print(result_or)
# CODUL TĂU VINE MAI SUS:

# Acum utilizați operatorul `not` pentru a verifica dacă `is_student` este `False` și tipăriți rezultatul folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
result_not = not is_student
print(result_not)
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină
```

```python
# Aceasta este a treia ta sarcină legată de numere în python
# Creează o variabilă numită `number` și atribuie-i valoarea `10`

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `number2` și atribuie-i valoarea `number` și afișează valoarea variabilei `number2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number2 = number
print(number2)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `number3` și atribuie-i valoarea `4.0`

# CODUL TĂU VINE MAI JOS:
number3 = 4.0
# CODUL TĂU VINE MAI SUS:

# Acum aplică toate operațiile pe care le-ai învățat în lecție asupra variabilelor `number` și `number3` și afișează rezultatele folosind funcția `print`
# Operațiile sunt: adunare, scădere, înmulțire, împărțire, modulo, exponențiere, împărțire întreagă

# CODUL TĂU VINE MAI JOS:
print(number + number3)  # adunare
print(number - number3)  # scădere
print(number * number3)  # înmulțire
print(number / number3)  # împărțire
print(number % number3)  # modulo
print(number ** number3)  # exponențiere
print(number // number3)  # împărțire întreagă
# CODUL TĂU VINE MAI SUS:

# Creează o nouă variabilă numită `number4` și atribuie-i o valoare numerică mare într-un mod literal

# CODUL TĂU VINE MAI JOS:
number4 = 100_000_000_000
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `number4` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(number4))
# CODUL TĂU VINE MAI SUS:

# Acum convertește variabila într-un alt tip numeric pe care l-ai învățat

# CODUL TĂU VINE MAI JOS:
number4 = float(number4)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină
```

```python
# Aceasta este prima ta sarcină a lecției legată de variabile în python

# Creează o variabilă numită `age` și seteaz-o la vârsta ta

# CODUL TĂU VINE MAI JOS:
age = 25
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(age))
# CODUL TĂU VINE MAI SUS:

# Acum asigură-te că variabila `age` este de tipul float.

# CODUL TĂU VINE MAI JOS:
age = float(age)
# CODUL TĂU VINE MAI SUS:

# Creează două variabile numite `age2` și `age3` și setează-le la vârsta prietenilor tăi, ambele variabile trebuie să fie de tipul float.

# CODUL TĂU VINE MAI JOS:
age2 = 30.5
age3 = 28.3
# CODUL TĂU VINE MAI SUS:

# Acum afișează suma vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age + age2 + age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează diferența vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age - age2 - age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează produsul vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age * age2 * age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează împărțirea vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age / age2 / age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează restul împărțirii vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age % age2 % age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei tale ridicată la puterea vârstei primului prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age ** age2)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei primului prieten împărțită la puterea vârstei celui de-al doilea prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 / age3)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină
```

```python
# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

# CODUL TĂU VINE MAI JOS:
name = "Your Name"
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(name)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
name2 = name
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

# CODUL TĂU VINE MAI JOS:
print(name[-1])
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

# CODUL TĂU VINE MAI JOS:
print(name[:3])
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

# CODUL TĂU VINE MAI JOS:
print(name.upper())
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

# CODUL TĂU VINE MAI JOS:
print(name.lower())
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print(name + name2)
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

# CODUL TĂU VINE MAI JOS:
print("This is a multi-line text\nThis is the second line")
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`

# CODUL TĂU VINE MAI JOS:
print("python" in "This is a multi-line text\nThis is the second line")
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

# CODUL TĂU VINE MAI JOS:
print("This is a multi-line text\nThis is the second line".replace("a", "e"))
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

# CODUL TĂU VINE MAI JOS:
print("This is a multi-line text\nThis is the second line".split())
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print(f"{name} {name2}")
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`

# CODUL TĂU VINE MAI JOS:
print(f"{name} {name2}".endswith("!"))
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`

# CODUL TĂU VINE MAI JOS:
print(f"{name} {name2}".startswith("Hello"))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat

# CODUL TĂU VINE MAI JOS:
print(f"{name} {name2}".index("!"))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

# CODUL TĂU VINE MAI JOS:
print(f"{name} {name2}".find("o"))
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print("{0} {1}".format(name, name2))
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`

# CODUL TĂU VINE MAI JOS:
print("{0} {1}".format(name, name2) + "This is a multi-line text\nThis is the second line")
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat

# CODUL TĂU VINE MAI JOS:
print(len("{0} {1}".format(name, name2) + "This is a multi-line text\nThis is the second line"))
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină

```

```python
# Aceasta este a treia ta sarcină a lecției legată de type conversion și input-ul user-ului în python

# Creează o variabilă numită `number` și atribuie-i valoarea `10`

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum cere user-ului să introducă un număr și atribuie acea valoare variabilei `number` și afișeaz-o folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = input()
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `float` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = float(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `str` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = str(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `bool` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = bool(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină
```

```python
# Aceasta este prima ta sarcină legată de liste

# Creează o listă goală numită `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = []
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.extend([1, 2, 3, 4, 5])
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.append(6)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum șterge numărul 3 din lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.remove(3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum sortează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.sort()
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum inversează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.reverse()
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lungimea listei `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Acum selectează primele două elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Acum selectează ultimele trei elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[-3:])
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 3 la poziția 2 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.insert(2, 3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Creează o listă goală numită `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2 = []
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 6 la 10 în lista `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2.extend([6, 7, 8, 9, 10])
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers2`

# CODUL TĂU VINE MAI JOS:
print(numbers2)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă lista `numbers2` la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.extend(numbers2)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum transformă lista `numbers` într-un string și afișează-l

# CODUL TĂU VINE MAI JOS:
numbers_str = str(numbers)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste
```

```python
# Aceasta este a doua sarcină legată de tuples

# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5

# CODUL TĂU VINE MAI JOS:
numbers = (1, 2, 3, 4, 5)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la tuple `numbers`

# CODUL TĂU VINE MAI JOS:
numbers = numbers + (6,)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Afișeați primul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[0])
# CODUL TĂU VINE MAI SUS:   

# Afișeați ultimul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-1])
# CODUL TĂU VINE MAI SUS:

# Afișeați primele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Afișeați ultimele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-2:])
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Afișați suma elementelor din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(sum(numbers))
# CODUL TĂU VINE MAI SUS:

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10

# CODUL TĂU VINE MAI JOS:
numbers_list = list(numbers)
numbers_list[2] = 10
numbers = tuple(numbers_list)
# CODUL TĂU VINE MAI SUS:

# Afișați tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Ștergeți tuple `numbers`

# CODUL TĂU VINE MAI JOS:
del numbers
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste
```

```python
# Aceeasta este prima sarcină a aceestei lecții și este legată de dicționare.

# Creați un dicțioar gol

# CODUL TĂU VINE MAI JOS:
dictionary = {}
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"

# CODUL TĂU VINE MAI JOS:
dictionary["name"] = "John"
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30

# CODUL TĂU VINE MAI JOS:
dictionary["age"] = 30
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(dictionary)
# CODUL TĂU VINE MAI SUS:

# Acum ștergeți cheia "name" din dicționar

# CODUL TĂU VINE MAI JOS:
dictionary.pop("name")
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(dictionary)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()

# CODUL TĂU VINE MAI JOS:
dictionary.setdefault("city", "New York")
# CODUL TĂU VINE MAI SUS:

# Afișați toate cheile din dicționar 

# CODUL TĂU VINE MAI JOS:
print(dictionary.keys())
# CODUL TĂU VINE MAI SUS:

# Afișați toate valorile din dicționar

# CODUL TĂU VINE MAI JOS:
print(dictionary.values())
# CODUL TĂU VINE MAI SUS:

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()

# CODUL TĂU VINE MAI JOS:
print(dictionary.items())
# CODUL TĂU VINE MAI SUS:

# Afișați numărul de perechi de cheie-valoare din dicționar

# CODUL TĂU VINE MAI JOS:
print(len(dictionary))
# CODUL TĂU VINE MAI SUS:

# Extrageți valoarea unei chei inexistente fără a genera o eroare

# CODUL TĂU VINE MAI JOS:
print(dictionary.get("job"))
# CODUL TĂU VINE MAI SUS:

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()

# CODUL TĂU VINE MAI JOS:
dictionary.update({"job": "developer"})
# CODUL TĂU VINE MAI SUS:

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()

# CODUL TĂU VINE MAI JOS:
dictionary.setdefault("pizza", 10)
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(dictionary)
# CODUL TĂU VINE MAI SUS:

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()

# CODUL TĂU VINE MAI JOS:
dictionary.pop("pizza")
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(dictionary)
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate perechile de cheie-valoare din dicționar

# CODUL TĂU VINE MAI JOS:
dictionary.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(dictionary)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de dicționare
```

```python
# Aceasta este a doua ta sarcină legată de seturi

# Creați un set gol numit `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set = set()
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.add(1)
numbers_set.add(2)
numbers_set.add(3)
numbers_set.add(4)
numbers_set.add(5)
# CODUL TĂU VINE MAI SUS:

# Acum afișați setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numărul 6 la setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.add(6)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()

# CODUL TĂU VINE MAI JOS:
numbers_set.update({1, 2, 3, 4, 5})
# CODUL TĂU VINE MAI SUS:

# Extrageți numărul 3 din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.remove(3)
# CODUL TĂU VINE MAI SUS:

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare

# CODUL TĂU VINE MAI JOS:
numbers_set.discard(7)
# CODUL TĂU VINE MAI SUS:

# Verificați dacă numărul 3 există în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(3 in numbers_set)
# CODUL TĂU VINE MAI SUS:

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.intersection({4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.difference({4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.issubset({1, 2, 3, 4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print({1, 2, 3, 4, 5, 6, 7}.issubset(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.issuperset({1, 2, 3, 4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print({1, 2, 3, 4, 5, 6, 7}.issuperset(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(len(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate elementele din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters

# CODUL TĂU VINE MAI JOS:
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru a doua ta sarcină legată de seturi 
```

```python
# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print("Numărul este pozitiv")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print("Numărul este par")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 != 0:
    print("Numărul este impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "Acesta este un text"
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Textul conține cuvântul Python")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in text:
    print("Textul conține cuvântul Java")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Textul conține cuvântul Python")
elif "Java" in text:
    print("Textul conține cuvântul Java")
else:
    print("Textul nu conține niciunul dintre cuvinte")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text and "Java" in text:
    print("Textul conține cuvântul Python și cuvântul Java")
elif "Python" in text:
    print("Textul conține cuvântul Python")
elif "Java" in text:
    print("Textul conține cuvântul Java")
else:
    print("Textul nu conține niciunul dintre cuvinte")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = int(input("Introduceți un număr de la 1 la 5: "))
if number == 1:
    print("Unu")
elif number == 2:
    print("Doi")
elif number == 3:
    print("Trei")
elif number == 4:
    print("Patru")
elif number == 5:
    print("Cinci")
# CODUL TĂU VINE MAI SUS:

# Acesta a fost tot pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.
```

```python
# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in numbers:
    if num % 2 == 0:
        print(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for num in range(1, 6):
    print(num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.

```

```python
# Aceasta este sarcina pentru lecția despre list comprehensions în Python.

from sigmoid_check.python_odyssey.lesson_10 import Lesson10

# VERIFICATION PROCESS
session = Lesson10()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
Utilizați list comprehension.
"""

# CODUL TĂU VINE MAI JOS:
def task_1():
    return [i for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

# CODUL TĂU VINE MAI JOS:
def task_2():
    return [i**2 for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""

# CODUL TĂU VINE MAI JOS:
def task_3():
    return [i for i in range(1, 11) if i % 2 != 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:
def task_4(matrix):
    return [num for row in matrix for num in row]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:
def task_5(n):
    return ["par" if i % 2 == 0 else "impar" for i in range(1, n+1)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(n):
    return {i: i**3 for i in range(1, n+1)}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""

# CODUL TĂU VINE MAI JOS:
def task_7(n):
    return {i for i in range(1, n+1) if i % 3 == 0}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

# Aceste sarcini te vor ajuta să înțelegi și să aplici list comprehensions în Python pentru a crea și manipula structuri de date într-un mod eficient și concis.
```

```python
from sigmoid_check.python_odyssey import Lesson10

# VERIFICATION PROCESS
session = Lesson10()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
Utilizați list comprehension.
"""

# CODUL TĂU VINE MAI JOS:
def task_1():
    return [i for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

# CODUL TĂU VINE MAI JOS:
def task_2():
    return [i**2 for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""

# CODUL TĂU VINE MAI JOS:
def task_3():
    return [i for i in range(1, 11) if i % 2 != 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:
def task_4(matrix):
    return [num for row in matrix for num in row]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:
def task_5(n):
    return ["par" if i % 2 == 0 else "impar" for i in range(1, n+1)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(n):
    return {i: i**3 for i in range(1, n+1)}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""

# CODUL TĂU VINE MAI JOS:
def task_7(n):
    return {i for i in range(1, n+1) if i % 3 == 0}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
"""

# CODUL TĂU VINE MAI JOS:
def task_8(numbers):
    return sum(numbers) / len(numbers)
# CODUL TĂU VINE MAI SUS:


# VERIFICATION PROCESS
print(session.check_task_8(task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_9(number):
    return number % 2 == 0
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_9(task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
"""

# CODUL TĂU VINE MAI JOS:
def task_10(name, age, city=""):
    return f"Nume: {name}, Varsta: {age}, Oras: {city}"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_10(task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
"""

# CODUL TĂU VINE MAI JOS:
def task_11(numbers):
    return max(numbers)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_11(task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
Exemplu: Pentru numărul 5 rezultatul va fi 120
"""

# CODUL TĂU VINE MAI JOS:
def task_12(number):
    return 1 if number == 0 else number * task_12(number - 1)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_12(task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
"""

# CODUL TĂU VINE MAI JOS:
def task_13(a, b):
    return a+b, a*b
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_13(task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
"""

# CODUL TĂU VINE MAI JOS:
def task_14(age):
    return "minor" if age < 18 else "adult" if 18 <= age <= 65 else "senior"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_14(task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_15(string):
    return string == string[::-1]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_15(task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
"""

# CODUL TĂU VINE MAI JOS:
def task_16(string):
    return string[::-1]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_16(task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
"""

# CODUL TĂU VINE MAI JOS:
def task_17(string):
    return len(string.split())
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_17(task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
"""

# CODUL TĂU VINE MAI JOS:
def task_18(celsius):
    return celsius * 9/5 + 32
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_18(task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_19(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_19(task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_20(number):
    return number == sum(i for i in range(1, number) if number % i == 0)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_20(task_20))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_21(number):
    return number == sum(int(i) ** len(str(number)) for i in str(number))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_21(task_21))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_22(number):
    return number % sum(int(i) for i in str(number)) == 0
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_22(task_22))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
"""

# CODUL TĂU VINE MAI JOS:
def task_23(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_23(task_23))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
"""

# CODUL TĂU VINE MAI JOS:
def task_24(number):
    return [i for i in range(1, number+1) if number % i == 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_24(task_24))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

# Aceste sarcini te vor ajuta să înțelegi și să aplici list comprehensions în Python pentru a crea și manipula structuri de date într-un mod eficient și concis.
```

```python
from sigmoid_check.python_odyssey import Lesson11

# VERIFICATION PROCESS
session = Lesson11()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
Exemplu: task_1(1, 2, 3) ➞ 6
"""

# CODUL TĂU VINE MAI JOS:
def task_1(*args):
    return sum(args)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(1, task_1))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
"""

# CODUL TĂU VINE MAI JOS:
def task_2(*args):
    return [arg for arg in args if type(arg) == int]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(2, task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
Exemplu: task_3(1, 4, 5) ➞ 20
"""

# CODUL TĂU VINE MAI JOS:
def task_3(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(3, task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_4` care primește un număr arbitrar de perechi cheie-valoare și returnează un string care conține toate cheile și valorile concatenate separate de un spațiu.
Exemplu: task_4(a=1, b=2, c=3) ➞ 'a 1 b 2 c 3'
"""

# CODUL TĂU VINE MAI JOS:
def task_4(**kwargs):
    return ' '.join([f'{key} {value}' for key, value in kwargs.items()])
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(4, task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
"""

# CODUL TĂU VINE MAI JOS:
def task_5(*args, **kwargs):
    return sorted([arg for arg in args if type(arg) == int]), sorted([key for key in kwargs if type(kwargs[key]) == str])
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(5, task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword ca key și valoarea acestora ca value.
Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(**kwargs):
    return {key: value for key, value in kwargs.items()}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(6, task_6))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: `str` și `int`.
Cheia `str` va avea o listă cu toate string-urile primite ca argumente, iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
"""

# CODUL TĂU VINE MAI JOS:
def task_7(*args):
    return {'str': [arg for arg in args if type(arg) == str], 'int': [arg for arg in args if type(arg) == int]}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(7, task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
"""

# CODUL TĂU VINE MAI JOS:
def task_8(*args):
    return {'palindrom': [arg for arg in args if arg == arg[::-1]], 'non_palindrom': [arg for arg in args if arg != arg[::-1]]}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(8, task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt multipli ai lui `number`.
Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_9(*args, number):
    return [arg for arg in args if arg % number == 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(9, task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt divizibile cu `number`.
Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_10(*args, number):
    return [arg for arg in args if number % arg == 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(10, task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_11(*args):
    if len(args) < 2:
        return False
    for i in range(2, len(args)):
        if args[i] != args[i - 1] + args[i - 2]:
            return False
    return True
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(11, task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
Exemplu: task_12(2, 3, 5, 7) ➞ True
Exemplu: task_12(1, 2, 3, 4) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_12(*args):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return all([is_prime(arg) for arg in args])
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(12, task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
Exemplu: task_13('listen', 'silent') ➞ True
Exemplu: task_13('hello', 'world') ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_13(word, *args):
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    return all([is_anagram(word, arg) for arg in args])
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(13, task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
"""

# CODUL TĂU VINE MAI JOS:
def task_14(*args, sub_string):
    return [arg for arg in args if sub_string in arg]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(14, task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
"""

# CODUL TĂU VINE MAI JOS:
def task_15(*args, sub_string):
    return {'contains': [arg for arg in args if sub_string in arg], 'not_contains': [arg for arg in args if sub_string not in arg]}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(15, task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
"""

# CODUL TĂU VINE MAI JOS:
def task_16(*args, operation):
    if operation == 'add':
        return sum(args)
    if operation == 'sub':
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result
    if operation == 'mul':
        result = 1
        for arg in args:
            result *= arg
        return result
    if operation == 'div':
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(16, task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
"""

# CODUL TĂU VINE MAI JOS:
def task_17(number, **kwargs):
    result = number
    for key, value in kwargs.items():
        if key == 'add':
            result += sum(value)
        if key == 'sub':
            result -= sum(value)
        if key == 'mul':
            for arg in value:
                result *= arg
        if key == 'div':
            for arg in value:
                result /= arg
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(17, task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_18(*args):
    result = {}
    for arg in args:
        for char in arg:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(18, task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_19(*args):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    result = {}
    for arg in args:
        if is_prime(arg):
            if arg in result:
                result[arg] += 1
            else:
                result[arg] = 1
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(19, task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
Exemplu: task_20('hello', 'world') ➞ {5: 2}
Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_20(*args):
    result = {}
    for arg in args:
        if len(arg) in result:
            result[len(arg)] += 1
        else:
            result[len(arg)] = 1
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(20, task_20))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

```
    
```python
# Aceasta este sarcina pentru lecția despre clase și conceptele de bază ale programării orientate pe obiecte în Python.

from sigmoid_check.python_odyssey import Lesson13

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.5
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.5

# VERIFICATION PROCESS
session = Lesson13()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE:
Această temă va fi puțin mai diferită decât deobicei, cei de la DARWIN au apelat la serviciile noastre ca să-i ajutăm să organizeze produsele acestora.
Procesul lor de vindere a unui produs durează foarte mult din cauza la sistemul lor învechit de structurare a produselor, iar clienții sunt nemulțumiți.

Din păcate noi suntem ocupați cu procesele de organizare a Python Odyssey Camp și nu reușim la timp să realizăm sistemul nou. Dar în schimb voi puteți, aveți toate cunoștințele necesare.
Și plus la asta noi avem încredere că o să vă desurcați și o să rezolvați problema în timp util.
"""

"""
Pentru început o să ne ocupăm de dirijarea și managementul produselor.
1. Avem nevoie să creezi o clasă `Produs`, aceasta trebuie să accepte 3 parametri: numele, pretul, anul_producerii
Cu ajutorul acestei clase trebuie să fiu capabil să creeze câte obiecte doresc cu orice configurație a numelui, prețului și anul_producerii

Exemplu utilizare:
telefon = Produs("Iphone", 15000, 2020) # Voi putea crea un obiect utilizând anumiți parametri de intrare
print(telefon.numele)                   # Voi putea accesa numele obiectului creat
print(telefon.pretul)                   # Voi putea accesa pretul obiectului creat
print(telefon.anul_producerii)          # Voi putea accesa anul producerii obiectului creat
"""

# CODUL TĂU VINE MAI JOS:
class Produs:
    def __init__(self, numele, pretul, anul_producerii):
        self.numele = numele
        self.pretul = pretul
        self.anul_producerii = anul_producerii
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(1, Produs))
# VERIFICATION PROCESS

"""
DARWIN de asemenea a mai menționat că unele produse au nevoie de o descriere mai detaliată a parametrilor și informațiilor pe care le dețin.
2. Avem nevoie de trei clase noi care să moștenească clasa `Produs`:
"""

"""
2.1Prima clasă se numește `Telefon` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `baterie_mAh` și `memorie_GB`

De asemenea aceasta va avea o metodă numită `upgrade_memory` care va primi un parametru `new_memory` și va actualiza valoarea memoriei telefonului.
Totodată aceasta va avea o metodă numită `upgrade_battery` care va primi un parametru `new_battery` și va actualiza valoarea bateriei telefonului.
"""

# CODUL TĂU VINE MAI JOS:
class Telefon(Produs):
    def __init__(self, numele, pretul, anul_producerii, baterie_mAh, memorie_GB):
        super().__init__(numele, pretul, anul_producerii)
        self.baterie_mAh = baterie_mAh
        self.memorie_GB = memorie_GB

    def upgrade_memory(self, new_memory):
        self.memorie_GB = new_memory

    def upgrade_battery(self, new_battery):
        self.baterie_mAh = new_battery
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(2, Telefon, Produs))
# VERIFICATION PROCESS

"""
2.2 A doua clasă se numește `Laptop` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `sistem_de_operare` și `procesor`

De asemenea aceasta va avea o metodă numită `upgrade_processor` care va primi un parametru `new_processor` și va actualiza valoarea procesorului laptopului.
Totodată aceasta va avea o metodă numită `upgrade_os` care va primi un parametru `new_os` și va actualiza valoarea sistemului de operare al laptopului.
"""

# CODUL TĂU VINE MAI JOS:
class Laptop(Produs):
    def __init__(self, numele, pretul, anul_producerii, sistem_de_operare, procesor):
        super().__init__(numele, pretul, anul_producerii)
        self.sistem_de_operare = sistem_de_operare
        self.procesor = procesor

    def upgrade_processor(self, new_processor):
        self.procesor = new_processor

    def upgrade_os(self, new_os):
        self.sistem_de_operare = new_os
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(3, Laptop, Produs))
# VERIFICATION PROCESS

"""
2.3 A treia clasă se numește `trotineta` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `viteza_maxima` și `autonomie_km`

De asemenea aceasta va avea o metodă numită `upgrade_speed` care va primi un parametru `new_speed` și va actualiza valoarea vitezei maxime a trotinetei.
Totodată aceasta va avea o metodă numită `upgrade_autonomy` care va primi un parametru `new_autonomy` și va actualiza valoarea autonomiei trotinetei.
"""

# CODUL TĂU VINE MAI JOS:
class Trotineta(Produs):
    def __init__(self, numele, pretul, anul_producerii, viteza_maxima, autonomie_km):
        super().__init__(numele, pretul, anul_producerii)
        self.viteza_maxima = viteza_maxima
        self.autonomie_km = autonomie_km

    def upgrade_speed(self, new_speed):
        self.viteza_maxima = new_speed

    def upgrade_autonomy(self, new_autonomy):
        self.autonomie_km = new_autonomy
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(4, Trotineta, Produs))
# VERIFICATION PROCESS

"""
3 DARWIN a mai lăsat o mică notiță după ei, au menționat că mulți cumpărători sunt interesați de produsele apple și adesea acestea le combină între ele.

Avem nevoie de o clasă nouă care să se numească `AppleProduct` care va moșteni clasa `Produs` și va avea un parametru în plus numit `culoare` și `produs_conectat` 
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
"""

# CODUL TĂU VINE MAI JOS:
class AppleProduct(Produs):
    def __init__(self, numele, pretul, anul_producerii, culoare, produs_conectat="nimic"):
        super().__init__(numele, pretul, anul_producerii)
        self.culoare = culoare
        self.produs_conectat = produs_conectat

    def combine_products(self, product):
        if self.culoare != product.culoare:
            return "Produsul nu poate fi conectat deoarece culorile nu coincid"
        self.produs_conectat = product
        return "Produsul a fost conectat cu succes"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(5, AppleProduct, Produs))
# VERIFICATION PROCESS

"""
4. DARWIN și-a mai adus aminte de o chestie, și-au dat seama că cei de la Google tot au nevoie de posibilitatea de a conecta produsele între ele.

Avem nevoie de o clasă nouă care să se numească `GoogleProduct` care va moșteni clasa `AppleProduct` posibilitățile la ambele sunt aceleași, dar va fi nevoie de o singură schimbare.
Produsul conectat trebuie să fie de tip `GoogleProduct` iar culoarea acestuia poate să fie diferită de a produsului curent.
Asta ar însemna că singurul element care va necesita modificări este metoda `combine_products` care va trebui să accepte orice tip de obiect de tip `GoogleProduct`

Exemplu utilizare:
pixel = GoogleProduct("Pixel", 10000, 2020, "negru")
home = GoogleProduct("Home", 500, 2021, "alb")
pixel.combine_products(home) # În acest caz se va returna textul "Produsul a fost conectat cu succes" și dacă se va printa pixel.produs_conectat se va returna obiectul home
print(pixel.produs_conectat.numele) # Va returna numele produsului conectat

"""

# CODUL TĂU VINE MAI JOS:
class GoogleProduct(AppleProduct):
    def combine_products(self, product):
        self.produs_conectat = product
        return "Produsul a fost conectat cu succes"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(6, GoogleProduct, AppleProduct))
# VERIFICATION PROCESS

"""
5. Cei de la DARWIN chiar sunt uituci, și-au adus aminte peste 5 zile că vor avea nevoie și de o modalitate prin care să vândă produsele.

Avem nevoie de o clasă nouă pentru aceasta, ea se va numi `Magazin` și va conține doar 2 metode, `vinde_produs` și `returneaza_produs`

Metoda `vinde_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost vândut cu succes"
Metoda `returneaza_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost returnat cu succes"

Exemplu utilizare:
iphone = AppleProduct("Iphone", 15000, 2020, "negru")
print(magazin.vinde_produs(iphone)) # Va returna textul "Produsul Iphone a fost vândut cu succes"
print(magazin.returneaza_produs(iphone)) # Va returna textul "Produsul Iphone a fost returnat cu succes"
"""

# CODUL TĂU VINE MAI JOS:
class Magazin:
    def vinde_produs(self, produs):
        return f"Produsul {produs.numele} a fost vândut cu succes"

    def returneaza_produs(self, produs):
        return f"Produsul {produs.numele} a fost returnat cu succes"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(7, Magazin, Produs))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
    
```
    
```python
# Aceasta este sarcina pentru lecția despre conceptele avansate ale programării orientate pe obiecte în Python, cum ar fi super() și self, getter/setter și property, privatizarea și tipurile de metode.

from sigmoid_check.python_odyssey import Lesson14

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.7
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.7

# VERIFICATION PROCESS
session = Lesson14()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE:
O companie de tehnologie, TechSolutions, are nevoie de ajutorul nostru pentru a îmbunătăți gestionarea software-ului lor intern. 
Ei doresc să optimizeze modul în care tratează datele utilizatorilor și setările de sistem, 
respectând principiile OOP avansate pentru a asigura securitatea și modularitatea codului.
"""

"""
Pentru început vrem să asigurăm 3 tipuri de utilizatori în baza de date a companiei noastre.
Tipurile de utilizatori sunt:
1. Utilizator default - utilizatorul obișnuit care nu va avea careva drepturi de acces și va putea să utilizeze sistemul intern într-un mod limitat
2. Utilizator manager - utilizatorul care va avea drepturi de acces mai mari decât utilizatorul default și va putea să modifice setările de sistem, 
                        însă va avea restricții în ceea ce privește modificarea datelor utilizatorilor, 
                        fiind capabil doar să citească informația și nu să o modifice
3. Utilizator admin - utilizatorul care va avea toate drepturile de acces și va putea să modifice atât setările de sistem, cât și datele utilizatorilor

Iar din cauza faptului că nu dorim să replicăm aceleași metode de inițializare a utilizatorilor pentru fiecare tip de utilizator,
vrem să creăm o clasă de bază care să conțină metodele comune pentru toți utilizatorii și să moștenească aceste metode către clasele specifice tipurilor de utilizatori.

Ce trebuie să faci:
1. Creează o clasă `Utilizator` care să conțină un atribut public `nume` și un atribut protejat `_nivel_acces` cu valoarea implicită "Default".
    Clasa `Utilizator` trebuie să conțină metoda `afiseaza_nivel_acces` care să returneze string-ul "*nume-utilizator* are nivelul de acces *nivel-acces*.".
    De asemenea, clasa `Utilizator` trebuie să conțină metoda `utilizeaza_sistem` care să returneze string-ul "*nume-utilizator* poate utiliza funcții de bază ale sistemului.".

2. Creează o clasă `UtilizatorManager` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Manager".
    Clasa `UtilizatorManager` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
    De asemenea, clasa `UtilizatorManager` trebuie să conțină metoda `citeste_date_utilizator` care să returneze string-ul "*nume-utilizator* poate citi datele utilizatorilor.".

3. Creează o clasă `UtilizatorAdmin` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Admin".
    Clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
    De asemenea, clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_date_utilizator` care să returneze string-ul "*nume-utilizator* poate modifica datele utilizatorilor.".
"""

# CODUL TĂU VINE MAI JOS:
class Utilizator:
    def __init__(self, nume):
        self.nume = nume  # Public attribute, accessible to all subclasses
        self._nivel_acces = "Default"  # Protected attribute, accessible within the class and subclasses

    def afiseaza_nivel_acces(self):
        return f"{self.nume} are nivelul de acces {self._nivel_acces}."

    def utilizeaza_sistem(self):
        # Basic system usage rights for default user
        return f"{self.nume} poate utiliza funcții de bază ale sistemului."

class UtilizatorManager(Utilizator):
    def __init__(self, nume):
        super().__init__(nume)
        self._nivel_acces = "Manager"

    def modifica_setari(self):
        # Manager can modify system settings but not user data
        return f"{self.nume} poate modifica setările sistemului."

    def citeste_date_utilizator(self):
        # Manager can read user data but cannot modify it
        return f"{self.nume} poate citi datele utilizatorilor."

class UtilizatorAdmin(Utilizator):
    def __init__(self, nume):
        super().__init__(nume)
        self._nivel_acces = "Admin"

    def modifica_setari(self):
        # Admin can modify system settings
        return f"{self.nume} poate modifica setările sistemului."

    def modifica_date_utilizator(self):
        # Admin can modify user data
        return f"{self.nume} poate modifica datele utilizatorilor."
# CODUL TĂU VINE MAI SUS:


# VERIFICATION PROCESS
print(session.check_task(1, Utilizator, UtilizatorManager, UtilizatorAdmin))
# VERIFICATION PROCESS

"""
Acum că am creat clasele de utilizatori, mai avem nevoie de însăși sistemul la care acești utilizatori vor avea acces.
Sistemul va conține o clasă `Sistem` care va conține o listă de utilizatori și metode pentru a adăuga utilizatori noi, a afișa utilizatorii existenți și a verifica nivelul de acces al unui utilizator.
La sistem va avea acces doar Utilizatorii Admin așa că trebuie să ne asigurăm că aceștia vor avea metode pentru a adăuga, a modificare și a șterge datele private ale sistemului.

Ce trebuie să faci:
1. Pentru această sarcină vom crea o copie a clasei `Utilizator` de mai sus, deoarece vom avea nevoie de aceeași structură pentru a adăuga utilizatorii în sistem.
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

# CODUL TĂU VINE MAI JOS:
class user:
    def __init__(self, nume, nivel_acces="Default"):
        self._nume = nume  # Private attribute for user name
        self.__nivel_acces = nivel_acces  # Protected attribute for access level

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, valoare):
        self._nume = valoare

    @property
    def nivel_acces(self):
        return self.__nivel_acces

    @nivel_acces.setter
    def nivel_acces(self, valoare):
        self.__nivel_acces = valoare
    
 
class Sistem:
    def __init__(self):
        self.__utilizatori = {}

    def adauga_utilizator(self, utilizator):
        id_utilizator = len(self.__utilizatori) + 1
        self.__utilizatori[id_utilizator] = utilizator

    def afiseaza_utilizatori(self):
        return [utilizator.nume for utilizator in self.__utilizatori.values()]

    def verifica_nivel_acces(self, nume_utilizator):
        for utilizator in self.__utilizatori.values():
            if utilizator.nume == nume_utilizator:
                return utilizator.nivel_acces

    def modifica_name_user(self, id_utilizator, nume_utilizator):
        self.__utilizatori[id_utilizator].nume = nume_utilizator

    def sterge_utilizator(self, id_utilizator):
        del self.__utilizatori[id_utilizator]

    def modifica_nivel_acces(self, id_utilizator, nivel_acces):
        self.__utilizatori[id_utilizator].nivel_acces = nivel_acces

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(2, user, Sistem))
# VERIFICATION PROCESS

# Task 3: Privatizarea
"""
Iar pe sfârșite a rămas ulimul element al sistemului nostru, vom aveae nevoie de o simulare a unei aplicații care va permite interacțiunea cu întregul sistem.

Ce trebuie să faci:
1. Creează o clasă `TechSolutionsApp` care va conține o valoare a clasei `versiune_applicatie` cu valoarea implicită "1.0".
    Această clasă va avea nevoie de 3 metode, fiecare dintre acestea va fi utilizată pentru a simula interacțiunea cu sistemul nostru.
    De asemenea clasa va primi ca argument la inițializare o valoare ce va reprezenta versiunea aplicatiei care va fi stocată în atributul `self.versiune_aplicatie`.

    Metoda `market_view` va fi o metodă statică care nu va avea acces la self sau cls și va returna string-ul "Vizualizare piață".
    Metoda `delogat_view` va fi o metodă de clasă care va avea acces la cls și va returna string-ul "Versiunea aplicației este *versiune-aplicatie*" utilizând atributul clasei.
    Metoda `account_view` va fi o metodă de instanță care va avea acces la self și va returna string-ul "Vizualizare aplicație user *versiune-aplicatie*" utilizând atributul instanței.
"""

# CODUL TĂU VINE MAI JOS:
class TechSolutionsApp:
    versiune_aplicatie = "1.0"

    def __init__(self, versiune_aplicatie):
        self.versiune_aplicatie = versiune_aplicatie

    @staticmethod
    def market_view():
        return "Vizualizare piață"

    @classmethod
    def delogat_view(cls):
        return f"Versiunea aplicației este {cls.versiune_aplicatie}"

    def account_view(self):
        return f"Vizualizare aplicație user {self.versiune_aplicatie}"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(3, TechSolutionsApp))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

```
    
```python
# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey import Lesson15

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return str(self.lista)

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, index):
        return self.lista[index]

    def __setitem__(self, index, valoare):
        self.lista[index] = valoare

    def __add__(self, alt_container):
        return DataContainer(self.lista + alt_container.lista)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(1, DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def calculate(self):
        return sum(self.lista)
    
class ProdusContainer(DataContainer):
    def calculate(self):
        produs = 1
        for element in self.lista:
            produs *= element
        return produs
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(2, SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self, containers):
        self.containers = containers

    def add_container(self, container):
        self.containers.append(container)

    def __call__(self):
        return [max(container.lista) for container in self.containers]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(3, DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self, containers):
        self.containers = containers

    def add_container(self, container):
        self.containers.append(container)

    def mean(self):
        total = 0
        count = 0
        for container in self.containers:
            total += sum(container.lista)
            count += len(container.lista)
        return total / count

    def median(self):
        lista = []
        for container in self.containers:
            lista += container.lista
        lista.sort()
        n = len(lista)
        if n % 2 == 0:
            return (lista[n // 2 - 1] + lista[n // 2]) / 2
        return lista[n // 2]

    def min(self):
        minim = float('inf')
        for container in self.containers:
            minim = min(minim, min(container.lista))
        return minim

    def sum(self):
        total = 0
        for container in self.containers:
            total += sum(container.lista)
        return total
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(4, DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter:
    def __init__(self, containers):
        self.containers = containers

    def add_container(self, container):
        self.containers.append(container)

    def filter_zeros(self):
        lista = []
        for container in self.containers:
            lista += [element for element in container.lista if element != 0]
        return lista

    def filter_negatives(self):
        lista = []
        for container in self.containers:
            lista += [element for element in container.lista if element < 0]
        return lista

    def filter_positives(self):
        lista = []
        for container in self.containers:
            lista += [element for element in container.lista if element >= 0]
        return lista

    def filter_under_mean(self):
        mean = DataStatistics(self.containers).mean()
        lista = []
        for container in self.containers:
            lista += [element for element in container.lista if element > mean]
        return lista
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task(5, DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
    
```
        
```python
# Aceasta este sarcina pentru lecția despre funcții lambda, generatori, decoratori și gestionarea excepțiilor în Python.

from sigmoid_check.python_odyssey import Lesson16

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.9
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.9

# VERIFICATION PROCESS
session = Lesson16()
# VERIFICATION PROCESS

### Lambda Functions
"""
Creează o funcție lambda numită `task1` care adaugă 10 la un număr dat.
"""

# CODUL TĂU VINE MAI JOS
task1 = lambda x: x + 10
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(1, task1))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task2` care verifică dacă un număr este par.
"""

# CODUL TĂU VINE MAI JOS
task2 = lambda x: x % 2 == 0
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(2, task2))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task3` care înmulțește două numere.
"""

# CODUL TĂU VINE MAI JOS
task3 = lambda x, y: x * y
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(3, task3))
# VERIFICATION PROCESS

"""
Crează o funcție lambda numită `task4` care returnează lungimea unui șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task4 = lambda s: len(s)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(4, task4))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task5` care convertește un șir de caractere în majuscule.
"""

# CODUL TĂU VINE MAI JOS
task5 = lambda s: s.upper()
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(5, task5))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task6` care găsește maximul dintre trei numere.
"""

# CODUL TĂU VINE MAI JOS
task6 = lambda x, y, z: max(x, y, z)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(6 ,task6))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task7` care concatenează două șiruri de caractere cu un spațiu între ele.
"""

# CODUL TĂU VINE MAI JOS
task7 = lambda s1, s2: f"{s1} {s2}"
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(7, task7))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task8` care filtrează numerele impare dintr-o listă și le returnează.
"""

# CODUL TĂU VINE MAI JOS
task8 = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(8, task8))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task9` care calculează factorialul unui număr folosind funcția reduce din functools (google it!).
"""

# CODUL TĂU VINE MAI JOS
from functools import reduce
task9 = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(9, task9))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task10` care sortează o listă de tuple după a doua valoare din fiecare tuple.
"""

# CODUL TĂU VINE MAI JOS
task10 = lambda lst: sorted(lst, key=lambda x: x[1])
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(10, task10))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task11` care returnează rădăcina pătrată a unui număr.
"""

# CODUL TĂU VINE MAI JOS
import math
task11 = lambda x: math.sqrt(x)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(11, task11))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task12` care verifică dacă un șir de caractere este palindrom.
"""

# CODUL TĂU VINE MAI JOS
task12 = lambda s: s == s[::-1]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(12, task12))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task13` care numără numărul de vocale dintr-un șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task13 = lambda s: sum(1 for char in s if char.lower() in 'aeiou')
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(13, task13))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task14` care returnează inversul unui șir de caractere.
"""

# CODUL TĂU VINE MAI JOS
task14 = lambda s: s[::-1]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(14, task14))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task15` care filtrează toate șirurile de caractere mai lungi de 5 caractere dintr-o listă.
"""

# CODUL TĂU VINE MAI JOS
task15 = lambda lst: list(filter(lambda x: len(x) <= 5, lst))
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(15, task15))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task16` care sortează o listă de dicționare după o cheie specificată.
"""

# CODUL TĂU VINE MAI JOS
task16 = lambda lst, key: sorted(lst, key=lambda x: x[key])
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(16, task16))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task17` care găsește cel mai mare divizor comun al două numere.
"""

# CODUL TĂU VINE MAI JOS
task17 = lambda x, y: math.gcd(x, y)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(17, task17))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task18` care calculează suma pătratelor numerelor pare dintr-o listă.
"""

# CODUL TĂU VINE MAI JOS
task18 = lambda lst: sum(x ** 2 for x in lst if x % 2 == 0)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(18, task18))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task19` care verifică dacă un an dat este bisect.
"""

# CODUL TĂU VINE MAI JOS
task19 = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(19, task19))
# VERIFICATION PROCESS

"""
Creează o funcție lambda numită `task20` care găsește cel mai lung cuvânt dintr-o listă de cuvinte.
"""

# CODUL TĂU VINE MAI JOS
task20 = lambda lst: max(lst, key=len)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(20, task20))
# VERIFICATION PROCESS

### Generators
"""
Creează un generator numit `task21` care generează numere de la 1 la 10.
"""

# CODUL TĂU VINE MAI JOS
def task21():
    for i in range(1, 11):
        yield i
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(21, task21))
# VERIFICATION PROCESS

"""
Creează un generator numit `task22` care generează pătratele numerelor de la 1 la 10.
"""

# CODUL TĂU VINE MAI JOS
def task22():
    for i in range(1, 11):
        yield i ** 2
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(22, task22))
# VERIFICATION PROCESS

"""
Creează un generator numit `task23` care generează caracterele unui string primit ca input unul câte unul.
"""

# CODUL TĂU VINE MAI JOS
def task23(s):
    for char in s:
        yield char
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(23, task23))
# VERIFICATION PROCESS

"""
Creează un generator numit `task24` care generează numere pare până la un limită dată ca input.
"""

# CODUL TĂU VINE MAI JOS
def task24(limit):
    for i in range(2, limit + 1, 2):
        yield i
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(24, task24))
# VERIFICATION PROCESS

"""
Creează un generator numit `task25` care primește ca input un număr n și generează primele n numere Fibonacci.
"""

# CODUL TĂU VINE MAI JOS
def task25(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(25, task25))
# VERIFICATION PROCESS

"""
Creează un generator numit `task26` care generează numere prime până la o limită dată ca input.
"""

# CODUL TĂU VINE MAI JOS
def task26(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, limit + 1):
        if is_prime(i):
            yield i
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(26, task26))
# VERIFICATION PROCESS

"""
Creează un generator numit `task27` care generează numere într-un interval specificat start, și end cu un pas dat.
"""

# CODUL TĂU VINE MAI JOS
def task27(start, end, step):
    while start < end:
        yield start
        start += step
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(27, task27))
# VERIFICATION PROCESS

"""
Creează un generator numit `task28` care generează toate subșirurile unui șir oferit sub formă de string.
Exemplu:
pentru input-ul "ciao"
output-ul va fi: "c", "ci", "cia", "ciao", "i", "ia", "iao", "a", "ao", "o"
"""

# CODUL TĂU VINE MAI JOS
def task28(s):
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield s[i:j]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(28, task28))
# VERIFICATION PROCESS

"""
Creează un generator numit `task29` care generează factorialul numerelor de la 1 la n primind n ca input.
"""

# CODUL TĂU VINE MAI JOS
def task29(n):
    def factorial(x):
        if x == 0:
            return 1
        return x * factorial(x - 1)
    for i in range(1, n + 1):
        yield factorial(i)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(29, task29))
# VERIFICATION PROCESS

"""
Creează un generator numit `task30` care generează cifrele unui număr în ordine inversă primind numărul ca input.
"""

# CODUL TĂU VINE MAI JOS
def task30(num):
    num_str = str(num)
    for char in reversed(num_str):
        yield int(char)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(30, task30))
# VERIFICATION PROCESS

"""
Creează un generator numit `task31` care generează toate combinațiile posibile ale elementelor dintr-o listă.
Exemplu:
pentru input-ul [1, 2, 3, 4]
output-ul va fi: (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)
"""

# CODUL TĂU VINE MAI JOS
import itertools
def task31(lst):
    for i in range(1, len(lst) + 1):
        for combination in itertools.combinations(lst, i):
            yield combination
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(31, task31))
# VERIFICATION PROCESS

"""
Creează un generator numit `task32` care generează suma curentă a unei liste de numere primite ca input.
"""

# CODUL TĂU VINE MAI JOS
def task32(lst):
    total = 0
    for num in lst:
        total += num
        yield total
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(32, task32))
# VERIFICATION PROCESS

"""
Creează un generator numit `task33` care generează primele n termeni ai unei secvențe aritmetice primind a, d și n ca input unde a este primul termen, d este diferența sau pasul de creștere și n este numărul de termeni.
Exemplu:
pentru input-ul a=1, d=2, n=5
output-ul va fi: 1, 3, 5, 7, 9
"""

# CODUL TĂU VINE MAI JOS
def task33(a, d, n):
    for i in range(n):
        yield a + i * d
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(33, task33))
# VERIFICATION PROCESS

"""
Creează un generator numit `task34` care generează puterile lui 2 până la o limită dată ca input (inclusiv).
"""

# CODUL TĂU VINE MAI JOS
def task34(limit):
    n = 0
    while 2 ** n <= limit:
        yield 2 ** n
        n += 1
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(34, task34))
# VERIFICATION PROCESS

"""
Creează un generator numit `task35` care generează numere într-o secvență geometrică infinită primind a și r ca input unde a este primul termen și r este rația.
Exemplu:
pentru input-ul a=2, r=3
output-ul va fi: 2, 6, 18, 54, 162, ...
"""

# CODUL TĂU VINE MAI JOS
def task35(a, r):
    while True:
        yield a
        a *= r
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(35, task35))
# VERIFICATION PROCESS

"""
Creează un generator numit `task36` care generează permutările unei liste primite ca input.
Exemplu:
pentru input-ul [1, 2, 3]
output-ul va fi: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
"""

# CODUL TĂU VINE MAI JOS
def task36(lst):
    yield from itertools.permutations(lst)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(36, task36))
# VERIFICATION PROCESS

"""
Creează un generator numit `task37` care generează toți factorii primi ai unui număr dat ca input.
"""

# CODUL TĂU VINE MAI JOS
def task37(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            yield factor
            n //= factor
        else:
            factor += 1
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(37, task37))
# VERIFICATION PROCESS

"""
Creează un generator numit `task38` care generează reprezentarea binară a numerelor de la 1 la n primind n ca input.
"""

# CODUL TĂU VINE MAI JOS
def task38(n):
    for i in range(1, n + 1):
        yield bin(i)[2:]
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(38, task38))
# VERIFICATION PROCESS

"""
Creează un generator numit `task39` care generează toate anagramele unui șir dat ca input.
Exemplu:
pentru input-ul "abc"
output-ul va fi: "abc", "acb", "bac", "bca", "cab", "cba"
"""

# CODUL TĂU VINE MAI JOS
def task39(s):
    yield from itertools.permutations(s)
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(39, task39))
# VERIFICATION PROCESS

"""
Creează un generator numit `task40` care generează termenii unei serii matematice simple. 
De exemplu, acest generator va produce termenii unei serii în care fiecare termen este dat de formula:

termen = (-1)^n / n!

Aici, n este indexul termenului (începând de la 0), iar n! (n factorial) este produsul tuturor numerelor întregi pozitive până la n.
"""

# CODUL TĂU VINE MAI JOS
def task40():
    n = 0
    factorial = 1
    semn = 1
    while True:
        yield semn / factorial
        n += 1
        factorial *= n
        semn *= -1 
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(40, task40))
# VERIFICATION PROCESS

### Decorators
"""
Creează un decorator numit `task41` care afișează timpul de execuție al unei funcții în formatul "Execution time: x seconds".
"""

# CODUL TĂU VINE MAI JOS
import time
def task41(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(41, task41))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task42` care afișează mesaje "Before" și "After" în jurul apelului unei funcții.
"""

# CODUL TĂU VINE MAI JOS
def task42(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(42, task42))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task43` care memorează rezultatele unei funcții într-un dicționar `cache` pentru a le returna direct dacă aceleași argumente sunt folosite din nou.
"""

# CODUL TĂU VINE MAI JOS
def task43(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(43, task43))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task44` care numără de câte ori o funcție este apelată. La fiecare apel, afișează numărul de apeluri în formatul "Count: x".
"""

# CODUL TĂU VINE MAI JOS
def task44(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Count: {wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(44, task44))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task45` care convertește rezultatul unei funcții în majuscule.
"""

# CODUL TĂU VINE MAI JOS
def task45(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(45, task45))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task46` care reîncearcă o funcție dacă aceasta aruncă o excepție. Dacă funcția aruncă o excepție, decoratorul va încerca să o apeleze din nou de 3 ori.
"""

# CODUL TĂU VINE MAI JOS
def task46(func):
    def wrapper(*args, **kwargs):
        retries = 3
        while retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                retries -= 1
                print(f"Retrying... {retries} retries left")
                if retries == 0:
                    raise e
    return wrapper
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(46, task46))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task47` care adaugă o valoare specificată la valoarea returnată de o funcție primind valoarea ca input.
"""

# CODUL TĂU VINE MAI JOS
def task47(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + value
        return wrapper
    return decorator
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(47, task47))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task48` care validează tipurile argumentelor primite de o funcție și aruncă o excepție `TypeError` dacă tipurile nu sunt cele așteptate.
"""

# CODUL TĂU VINE MAI JOS
def task48(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(f"Argument {a} is not of type {t}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(48, task48))
# VERIFICATION PROCESS

"""
Creează un decorator numit `task49` care asigură că o funcție este apelată doar de utilizatori cu un anumit rol. Utilizând decoratorul, vei specifica rolul necesar pentru a apela funcția.

Aceasta va arunca o excepție `PermissionError` dacă utilizatorul nu are rolul specificat.
"""

# CODUL TĂU VINE MAI JOS
def task49(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                raise PermissionError("Unauthorized access")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# CODUL TĂU VINE MAI SUS

# VERIFICATION PROCESS
print(session.check_task(49, task49))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
```

HERE IS THE THEORETICAL PART THAT SHOULD BE COVERED, FOR SOME ELEMENTS THERE ARE EXAMPLES ABOVE, FOR OTHERS WE HAVE TO CREATE

## Python Syntax

### Quick Overview
Python syntax is designed to be clear and readable, using indentation to define code blocks.

### In-Depth Explanation
Python's syntax is what sets it apart from many other programming languages. It uses indentation (whitespace at the beginning of a line) to define code blocks, rather than curly braces or keywords. This enforces a clean and readable code style.

Key points of Python syntax:
- Statements that expect an indented block start with a colon (:)
- Indentation is typically 4 spaces (though any consistent indentation is valid)
- Lines can be continued using a backslash (\) or implicit continuation inside parentheses, brackets, or braces


```python
# This is a comment
print("Hello, World!")  # This prints a greeting

if True:
    print("This is indented")
    if False:
        print("This is nested and indented further")
    print("Back to the first indentation level")

print("Back to no indentation")

# Multi-line statement using parentheses
long_calculation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
                    11 + 12 + 13 + 14 + 15)
```


## Basic Concepts

### Quick Overview
Python is a high-level, interpreted programming language that supports multiple programming paradigms.

### In-Depth Explanation
Python is known for its simplicity and readability. It's an interpreted language, meaning code is executed line by line, rather than compiled all at once. Python supports multiple programming paradigms, including:

1. Procedural programming
2. Object-oriented programming (OOP)
3. Functional programming

Key features of Python:
- Dynamic typing: Variables can change types
- Automatic memory management with garbage collection
- Rich standard library and extensive third-party packages
- Cross-platform compatibility


```python
# Procedural
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Object-oriented
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}!"

alice = Person("Alice")
print(alice.greet())

# Functional
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print(f"Sum of squares: {sum_of_squares}")
```


## Variables

### Quick Overview
Variables in Python are names that refer to values stored in memory.

### In-Depth Explanation
In Python, variables are created when you assign a value to them. Unlike some other languages, you don't need to declare the type of a variable explicitly. Python uses dynamic typing, which means a variable can refer to different types of objects during its lifetime.

Key points about Python variables:
- Variable names are case-sensitive
- They must start with a letter or underscore, followed by letters, numbers, or underscores
- Python convention uses snake_case for variable names
- Some words are reserved and can't be used as variable names (e.g., `if`, `for`, `while`)


```python
# Creating variables
x = 5  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_student = True  # Boolean

# Printing variables
print(f"x = {x}, y = {y}, name = {name}, is_student = {is_student}")

# Changing variable types
x = "Now I'm a string"
print(f"x is now: {x}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Swapping variables
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
```


## Booleans

### Quick Overview
Booleans represent truth values: either True or False.

### In-Depth Explanation
Booleans are a fundamental data type in Python, used for logical operations and control flow. They have only two possible values: True or False. Booleans are often the result of comparison operations or logical expressions.

Key points about Booleans:
- `True` and `False` are keywords and must be capitalized
- The `bool()` function can convert other types to Boolean
- Non-empty containers and non-zero numbers are considered True
- Empty containers, zero, and None are considered False


```python
# Boolean variables
is_raining = True
is_sunny = False

# Logical operations
print(f"Is it raining and sunny? {is_raining and is_sunny}")
print(f"Is it raining or sunny? {is_raining or is_sunny}")
print(f"Is it not raining? {not is_raining}")

# Comparison operations
x = 5
y = 10
print(f"Is x less than y? {x < y}")
print(f"Is x equal to y? {x == y}")

# Boolean conversion
print(f"bool(0) is {bool(0)}")
print(f"bool(1) is {bool(1)}")
print(f"bool('') is {bool('')}")
print(f"bool('Hello') is {bool('Hello')}")
print(f"bool([]) is {bool([])}")
print(f"bool([1, 2, 3]) is {bool([1, 2, 3])}")
```


## Numbers

### Quick Overview
Python supports various numeric types, including integers, floating-point numbers, and complex numbers.

### In-Depth Explanation
Python provides several built-in numeric types:

1. Integers (int): Whole numbers, positive or negative, of unlimited size.
2. Floating-point numbers (float): Numbers with decimal points or in scientific notation.
3. Complex numbers (complex): Numbers with a real and imaginary part.

Key points about numbers in Python:
- Integer division using `/` always returns a float
- Use `//` for floor division (integer division discarding the remainder)
- The `%` operator calculates the remainder
- Scientific notation uses `e` or `E` (e.g., 1e6 = 1 * 10^6)


```python
# Integers
x = 5
y = -10
big_num = 1234567890123456789

# Floating-point numbers
pi = 3.14159
e = 2.71828
avogadro = 6.022e23  # Scientific notation

# Complex numbers
z = 3 + 4j

# Basic operations
print(f"5 + 3 = {5 + 3}")
print(f"5 - 3 = {5 - 3}")
print(f"5 * 3 = {5 * 3}")
print(f"5 / 3 = {5 / 3}")  # Always returns a float
print(f"5 // 3 = {5 // 3}")  # Floor division
print(f"5 % 3 = {5 % 3}")  # Modulo (remainder)
print(f"5 ** 3 = {5 ** 3}")  # Exponentiation

# Type conversion
int_num = int(3.14)
float_num = float(5)
complex_num = complex(3, 4)

print(f"int(3.14) = {int_num}")
print(f"float(5) = {float_num}")
print(f"complex(3, 4) = {complex_num}")
```

## Basic Operations

### Quick Overview
Python supports a wide range of operations for various data types, including arithmetic, comparison, and logical operations.

### In-Depth Explanation
Python provides operators for performing different types of operations:

1. Arithmetic operators: +, -, *, /, //, %, **
2. Comparison operators: ==, !=, <, >, <=, >=
3. Logical operators: and, or, not
4. Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
5. Bitwise operators: &, |, ^, ~, <<, >>
6. Identity operators: is, is not
7. Membership operators: in, not in

The order of operations follows the PEMDAS rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).


```python
# Arithmetic operations
a, b = 10, 3
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a // b = {a // b}")  # Floor division
print(f"a % b = {a % b}")  # Modulo
print(f"a ** b = {a ** b}")  # Exponentiation

# Comparison operations
x, y = 5, 7
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# Logical operations
p, q = True, False
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")

# Assignment operations
n = 10
n += 5  # Equivalent to: n = n + 5
print(f"n after n += 5: {n}")

# Bitwise operations
a, b = 60, 13  # 60 = 0011 1100, 13 = 0000 1101
print(f"a & b: {a & b}")   # AND
print(f"a | b: {a | b}")   # OR
print(f"a ^ b: {a ^ b}")   # XOR
print(f"~a: {~a}")         # NOT
print(f"a << 2: {a << 2}") # Left shift
print(f"a >> 2: {a >> 2}") # Right shift

# Identity operations
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")

# Membership operations
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
```


## Strings

### Quick Overview
Strings are sequences of characters, used to represent text in Python.

### In-Depth Explanation
In Python, strings are immutable sequences of Unicode characters. They can be created using single quotes (''), double quotes (""), or triple quotes (''' ''' or """ """) for multi-line strings.

Key features of strings:
- Indexing: Access individual characters using square brackets []
- Slicing: Extract substrings using slice notation [start:end:step]
- Concatenation: Join strings using the + operator
- Repetition: Repeat strings using the * operator
- Methods: Built-in functions for string manipulation (e.g., upper(), lower(), strip())
- Formatting: Using f-strings, .format() method, or % operator


```python
# Creating strings
single_quoted = 'Hello, World!'
double_quoted = "Python Programming"
multi_line = '''This is a
multi-line
string'''

# String operations
greeting = "Hello"
name = "Alice"

# Concatenation
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# Repetition
echo = "Echo! " * 3
print(echo)

# Indexing and slicing
word = "Python"
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"Substring: {word[1:4]}")
print(f"Every other character: {word[::2]}")

# String methods
text = "   python programming   "
print(f"Uppercase: {text.upper()}")
print(f"Stripped: {text.strip()}")
print(f"Capitalized: {text.capitalize()}")
print(f"Split words: {text.split()}")

# String formatting
name = "Bob"
age = 30
# Using f-strings (Python 3.6+)
print(f"{name} is {age} years old")
# Using .format() method
print("{} is {} years old".format(name, age))
# Using % operator
print("%s is %d years old" % (name, age))

# Escape characters
print("This is a line\nThis is a new line")
print("This is a \"quoted\" word")

# Raw strings
print(r"This is a raw string\n")  # \n is not interpreted as a newline
```


## Type Conversion

### Quick Overview
Type conversion (or type casting) is the process of changing an object from one data type to another.

### In-Depth Explanation
Python provides built-in functions for converting between different data types. This is useful when you need to perform operations between different types or when you want to change the way data is represented.

Common type conversion functions:
- `int()`: Convert to integer
- `float()`: Convert to float
- `str()`: Convert to string
- `bool()`: Convert to boolean
- `list()`: Convert to list
- `tuple()`: Convert to tuple
- `set()`: Convert to set
- `dict()`: Convert to dictionary

It's important to note that not all conversions are possible, and some may result in loss of information or raise exceptions.


```python
# Integer conversions
int_from_float = int(3.14)
int_from_string = int("42")
int_from_bool = int(True)
print(f"int(3.14) = {int_from_float}")
print(f"int('42') = {int_from_string}")
print(f"int(True) = {int_from_bool}")

# Float conversions
float_from_int = float(5)
float_from_string = float("3.14")
print(f"float(5) = {float_from_int}")
print(f"float('3.14') = {float_from_string}")

# String conversions
str_from_int = str(42)
str_from_float = str(3.14)
str_from_bool = str(True)
print(f"str(42) = {str_from_int}")
print(f"str(3.14) = {str_from_float}")
print(f"str(True) = {str_from_bool}")

# Boolean conversions
bool_from_int = bool(1)
bool_from_zero = bool(0)
bool_from_string = bool("Hello")
bool_from_empty_string = bool("")
print(f"bool(1) = {bool_from_int}")
print(f"bool(0) = {bool_from_zero}")
print(f"bool('Hello') = {bool_from_string}")
print(f"bool('') = {bool_from_empty_string}")

# List conversions
list_from_string = list("Python")
list_from_tuple = list((1, 2, 3))
print(f"list('Python') = {list_from_string}")
print(f"list((1, 2, 3)) = {list_from_tuple}")

# Tuple conversions
tuple_from_list = tuple([1, 2, 3])
tuple_from_string = tuple("Python")
print(f"tuple([1, 2, 3]) = {tuple_from_list}")
print(f"tuple('Python') = {tuple_from_string}")

# Set conversions
set_from_list = set([1, 2, 2, 3, 3, 3])
set_from_string = set("Mississippi")
print(f"set([1, 2, 2, 3, 3, 3]) = {set_from_list}")
print(f"set('Mississippi') = {set_from_string}")

# Dictionary conversions
dict_from_tuples = dict([('a', 1), ('b', 2)])
print(f"dict([('a', 1), ('b', 2)]) = {dict_from_tuples}")

# Complex conversions
complex_from_int = complex(5)
complex_from_float = complex(3.14)
complex_from_str = complex("3+4j")
print(f"complex(5) = {complex_from_int}")
print(f"complex(3.14) = {complex_from_float}")
print(f"complex('3+4j') = {complex_from_str}")
```


## Version Control

### Quick Overview
Version control is a system that helps track and manage changes to files over time.

### In-Depth Explanation
Version control systems (VCS) are essential tools in software development. They allow developers to:

1. Track changes to code over time
2. Revert to previous versions if needed
3. Collaborate with others on the same project
4. Maintain different versions (branches) of a project
5. Merge changes from different sources

The most popular version control system is Git, which is distributed and allows for both local and remote repositories.

Key concepts in version control:
- Repository: A container for a project that tracks all changes
- Commit: A snapshot of changes at a specific point in time
- Branch: A separate line of development
- Merge: Combining changes from different branches
- Clone: Creating a local copy of a remote repository
- Push/Pull: Sending/receiving changes to/from a remote repository


```bash
# Initialize a new Git repository
git init

# Check the status of your repository
git status

# Add files to the staging area
git add file.py

# Commit changes
git commit -m "Initial commit"

# Create a new branch
git branch feature-branch

# Switch to the new branch
git checkout feature-branch

# Make changes and commit
echo "New feature" >> feature.py
git add feature.py
git commit -m "Add new feature"

# Switch back to the main branch
git checkout main

# Merge the feature branch into main
git merge feature-branch

# Push changes to a remote repository
git push origin main

# Pull changes from a remote repository
git pull origin main
```

## Git

### Quick Overview
Git is a distributed version control system used to track changes in source code during software development.

### In-Depth Explanation
Git was created by Linus Torvalds in 2005 for development of the Linux kernel. It has since become the most widely used version control system in the world. Git is distributed, meaning that every developer's working copy of the code is also a repository that can contain the full history of all changes.

Key features of Git:
1. Branching and merging: Create separate lines of development and combine them
2. Lightweight: Fast and efficient for both small and large projects
3. Data integrity: Uses SHA-1 hashes to ensure data integrity
4. Staging area: Allows you to choose which changes to commit
5. Distributed development: Each clone is a full backup of all data

Common Git operations:
- `git init`: Initialize a new Git repository
- `git clone`: Create a copy of a remote repository
- `git add`: Add files to the staging area
- `git commit`: Record changes to the repository
- `git push`: Upload local changes to a remote repository
- `git pull`: Download and integrate changes from a remote repository
- `git branch`: List, create, or delete branches
- `git merge`: Join two or more development histories together


```bash
# Configure Git (do this once)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create a new repository
mkdir my_project
cd my_project
git init

# Create a new file and add it to the repository
echo "print('Hello, Git!')" > hello.py
git add hello.py
git commit -m "Add hello.py file"

# Check the status and history
git status
git log

# Create and switch to a new branch
git branch feature-branch
git checkout feature-branch

# Make changes, stage, and commit
echo "print('New feature')" >> hello.py
git add hello.py
git commit -m "Add new feature"

# Switch back to main branch and merge changes
git checkout main
git merge feature-branch

# Push changes to a remote repository (assuming it's set up)
git push origin main

# Pull changes from a remote repository
git pull origin main

# View differences between commits
git diff HEAD~1 HEAD

# Undo last commit (keeping changes staged)
git reset --soft HEAD~1

# Discard changes in working directory
git checkout -- hello.py
```


## GitHub

### Quick Overview
GitHub is a web-based platform that provides hosting for software development version control using Git.

### In-Depth Explanation
GitHub is a platform and cloud-based service that helps developers store and manage their code, as well as track and control changes to their code. It provides a web-based graphical interface and offers all of the distributed version control and source code management (SCM) functionality of Git, plus its own features.

Key features of GitHub:
1. Repositories: Store and organize your projects
2. Forks: Create a personal copy of someone else's project
3. Pull Requests: Propose changes to a repository
4. Issues: Track bugs, enhancements, and other requests
5. Actions: Automate workflows and CI/CD
6. Projects: Manage and track work using boards
7. Wikis: Create and store documentation
8. Gists: Share code snippets

GitHub is widely used for open-source projects and collaboration among developers. It also provides features for code review, project management, and integrations with other tools.


```bash
# Clone a repository from GitHub
git clone https://github.com/username/repository.git

# Create a new branch for your feature
git checkout -b feature-branch

# Make changes and commit
echo "New feature" >> feature.txt
git add feature.txt
git commit -m "Add new feature"

# Push the branch to GitHub
git push origin feature-branch

# Create a pull request (done through GitHub web interface)

# After pull request is merged, update local main branch
git checkout main
git pull origin main

# Delete the feature branch locally and remotely
git branch -d feature-branch
git push origin --delete feature-branch

# Fork a repository (done through GitHub web interface)

# Clone your fork
git clone https://github.com/your-username/forked-repo.git

# Add the original repository as a remote
git remote add upstream https://github.com/original-owner/original-repo.git

# Sync your fork with the original repository
git fetch upstream
git checkout main
git merge upstream/main

# Push the updated main branch to your fork
git push origin main
```


## Lists

### Quick Overview
Lists are ordered, mutable sequences of elements in Python.

### In-Depth Explanation
Lists are one of the most versatile and commonly used data structures in Python. They can contain elements of different types and are defined using square brackets []. Lists are:

1. Ordered: Elements maintain their order
2. Mutable: Can be modified after creation
3. Heterogeneous: Can contain elements of different types
4. Dynamic: Can grow or shrink in size

Key operations on lists:
- Indexing: Access elements using their position
- Slicing: Extract a portion of the list
- Appending: Add elements to the end
- Inserting: Add elements at a specific position
- Removing: Delete elements by value or index
- Sorting: Arrange elements in a specific order


```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "two", 3.0, [4, 5]]

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Slicing
print(f"First two fruits: {fruits[:2]}")

# Modifying lists
fruits[1] = "blueberry"
fruits.append("date")
fruits.insert(1, "blackberry")
fruits.extend(["elderberry", "fig"])

print(f"Modified fruits list: {fruits}")

# Removing elements
removed_fruit = fruits.pop(2)
fruits.remove("fig")

print(f"Removed fruit: {removed_fruit}")
print(f"Fruits after removal: {fruits}")

# Sorting
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Reversing
fruits.reverse()
print(f"Reversed fruits: {fruits}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")
print(f"Element at row 1, column 2: {matrix[1][2]}")
```

## Tuples

### Quick Overview
Tuples are ordered, immutable sequences of elements in Python.

### In-Depth Explanation
Tuples are similar to lists but with one key difference: they are immutable. Once a tuple is created, its elements cannot be changed. Tuples are defined using parentheses () or just commas. They are:

1. Ordered: Elements maintain their order
2. Immutable: Cannot be modified after creation
3. Heterogeneous: Can contain elements of different types
4. Hashable: Can be used as dictionary keys (if all elements are hashable)

Use cases for tuples:
- Representing fixed collections of items
- Returning multiple values from functions
- Used as dictionary keys (when lists can't be)
- Slight performance advantage over lists


```python
# Creating tuples
coordinates = (3, 4)
person = "Alice", 30, "New York"  # Parentheses are optional

# Accessing elements
print(f"X coordinate: {coordinates[0]}")
print(f"Person's name: {person[0]}")

# Tuple unpacking
name, age, city = person
print(f"{name} is {age} years old and lives in {city}")

# Tuples are immutable
try:
    coordinates[0] = 5
except TypeError as e:
    print(f"Error: {e}")

# Concatenating tuples
combined = coordinates + (5, 6)
print(f"Combined tuple: {combined}")

# Repeating tuples
repeated = coordinates * 3
print(f"Repeated tuple: {repeated}")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")
print(f"Element at index 1,0: {nested[1][0]}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Converting to and from lists
tuple_from_list = tuple([1, 2, 3])
list_from_tuple = list(coordinates)
print(f"Tuple from list: {tuple_from_list}")
print(f"List from tuple: {list_from_tuple}")
```

## Dictionaries

### Quick Overview
Dictionaries are mutable, unordered collections of key-value pairs in Python.

### In-Depth Explanation
Dictionaries are one of the most powerful and widely used data structures in Python. They allow you to store and retrieve data using unique keys. Dictionaries are:

1. Unordered: Elements don't have a specific order
2. Mutable: Can be modified after creation
3. Key-Value Pairs: Each element is a pair of key and its associated value
4. Keys must be unique and immutable

Key features of dictionaries:
- Fast lookup: Retrieving values by key is very efficient
- Flexible: Keys and values can be of different types
- Dynamic: Can grow or shrink in size
- Nestable: Can contain other dictionaries as values


```python
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")  # Using get() method

# Modifying dictionaries
person["occupation"] = "Engineer"
person["age"] = 31

# Adding multiple key-value pairs
person.update({"email": "alice@example.com", "phone": "123-456-7890"})

print(f"Updated person: {person}")

# Removing items
removed_city = person.pop("city")
del person["phone"]

print(f"Removed city: {removed_city}")
print(f"Person after removal: {person}")

# Checking for keys
if "name" in person:
    print(f"Name exists: {person['name']}")

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares}")

# Nested dictionaries
employees = {
    "Alice": {"department": "IT", "salary": 75000},
    "Bob": {"department": "HR", "salary": 65000}
}

print(f"Alice's salary: {employees['Alice']['salary']}")

# Merging dictionaries (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print(f"Merged dictionary: {merged}")
```

## Sets

### Quick Overview
Sets are unordered collections of unique elements in Python.

### In-Depth Explanation
Sets are used to store multiple items in a single variable, but unlike lists or tuples, sets are unordered and do not allow duplicate values. Sets are:

1. Unordered: Elements don't have a specific order
2. Mutable: The set itself can be modified
3. Unique Elements: No duplicates allowed
4. Heterogeneous: Can contain elements of different types (as long as they're hashable)

Key features of sets:
- Fast membership testing
- Elimination of duplicates
- Mathematical set operations (union, intersection, difference)
- Not subscriptable (can't use indexing)


```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 2, 3, 3, 4])  # Creates a set from a list

print(f"Fruits set: {fruits}")
print(f"Numbers set: {numbers}")  # Note: duplicates are removed

# Adding elements
fruits.add("date")
fruits.update(["elderberry", "fig"])

print(f"Updated fruits: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises an error if not found
fruits.discard("grape")  # Doesn't raise an error if not found
popped = fruits.pop()  # Removes and returns an arbitrary element

print(f"Fruits after removal: {fruits}")
print(f"Popped element: {popped}")

# Membership testing
print(f"Is 'apple' in fruits? {'apple' in fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2  # or set1.union(set2)
intersection = set1 & set2  # or set1.intersection(set2)
difference = set1 - set2  # or set1.difference(set2)
symmetric_difference = set1 ^ set2  # or set1.symmetric_difference(set2)

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")
print(f"Symmetric Difference: {symmetric_difference}")

# Subset and superset
set3 = {1, 2}
print(f"Is set3 a subset of set1? {set3.issubset(set1)}")
print(f"Is set1 a superset of set3? {set1.issuperset(set3)}")

# Frozen sets (immutable sets)
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # This would raise an AttributeError

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")
```

## Manipulation & Operations of Data Structures

### Quick Overview
Python provides various methods and operations to manipulate and work with different data structures efficiently.

### In-Depth Explanation
Each data structure in Python (lists, tuples, dictionaries, sets) has its own set of methods and operations. Understanding these operations is crucial for effective programming. Common operations include:

1. Adding and removing elements
2. Searching and sorting
3. Copying and cloning
4. Iterating through elements
5. Combining data structures
6. Transforming data structures

It's important to choose the right data structure and operations for your specific use case to optimize performance and readability.


```python
import copy

# List operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()
print(f"Sorted numbers: {numbers}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed numbers: {reversed_numbers}")

# Tuple operations
coordinates = (3, 4)
x, y = coordinates  # Unpacking
print(f"X: {x}, Y: {y}")

# Dictionary operations
person = {"name": "Alice", "age": 30}
person_copy = person.copy()
person_copy["name"] = "Bob"
print(f"Original: {person}")
print(f"Copy: {person_copy}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Dictionary comprehension
sentence = "hello"
char_count = {char: sentence.count(char) for char in set(sentence)}
print(f"Character count: {char_count}")

# Nested data structures
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Deep copy vs. shallow copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

original[0][0] = 99
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")  # First element is also modified
print(f"Deep copy: {deep_copy}")  # Remains unchanged

# Combining dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = dict1 | dict2
print(f"Combined dictionary: {combined}")

# Zipping iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(f"Zipped list: {people}")

# Enumerate for index and value
for index, value in enumerate(names):
    print(f"Index {index}: {value}")
```

## List Comprehension

### Quick Overview
List comprehension is a concise way to create lists in Python based on existing lists or other iterable objects.

### In-Depth Explanation
List comprehension provides a shorter syntax to create a new list based on the values of an existing list or iterable. It's often more readable and faster than using traditional for loops to create lists. The basic syntax is:

```python
new_list = [expression for item in iterable if condition]
```

Where:
- `expression` is the operation performed on each item
- `item` is the variable representing each element in the iterable
- `iterable` is the sequence, list, or other iterable object
- `condition` (optional) filters which items are included

List comprehensions can replace loops and `map()` functions with a more elegant and pythonic syntax.


```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# List comprehension with strings
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split()]
print(f"Word lengths: {word_lengths}")

# List comprehension with conditional expression
numbers = [-4, -2, 0, 2, 4]
abs_numbers = [abs(x) if x < 0 else x for x in numbers]
print(f"Absolute values: {abs_numbers}")

# List comprehension with enumerate
fruits = ['apple', 'banana', 'cherry']
enumerated_fruits = [f"{index + 1}. {fruit}" for index, fruit in enumerate(fruits)]
print(f"Enumerated fruits: {enumerated_fruits}")

# List comprehension with zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
name_age_pairs = [f"{name} is {age} years old" for name, age in zip(names, ages)]
print(f"Name-age pairs: {name_age_pairs}")

# List comprehension vs. lambda and map
numbers = [1, 2, 3, 4, 5]
squared_map = list(map(lambda x: x**2, numbers))
squared_comp = [x**2 for x in numbers]
print(f"Squared (map): {squared_map}")
print(f"Squared (comprehension): {squared_comp}")

# Nested if conditions in list comprehension
numbers = range(1, 51)
fizz_buzz = ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in numbers]
print(f"FizzBuzz: {fizz_buzz[:15]}...")  # Showing first 15 elements

# Creating a dictionary using list comprehension
squared_dict = {x: x**2 for x in range(5)}
print(f"Squared dictionary: {squared_dict}")

# List comprehension with try-except
numbers = [1, 2, 3, 'four', 5, 'six', 7, 8]
valid_squares = [x**2 for x in numbers if isinstance(x, int)]
print(f"Valid squares: {valid_squares}")

# List comprehension with custom function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 50) if is_prime(x)]
print(f"Prime numbers: {primes}")
```

## Dictionary Comprehension

### Quick Overview
Dictionary comprehension is a concise way to create dictionaries in Python based on existing iterables or dictionaries.

### In-Depth Explanation
Dictionary comprehension is similar to list comprehension but creates a dictionary instead of a list. It provides a shorter syntax to create a new dictionary based on the key-value pairs of an existing iterable or dictionary. The basic syntax is:

```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

Where:
- `key_expression` is the operation performed to generate each key
- `value_expression` is the operation performed to generate each value
- `item` is the variable representing each element in the iterable
- `iterable` is the sequence, list, or other iterable object
- `condition` (optional) filters which items are included

Dictionary comprehensions can replace loops and `dict()` constructor with a more elegant and pythonic syntax.


```python
# Basic dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared = {x: x**2 for x in numbers}
print(f"Squared dictionary: {squared}")

# Dictionary comprehension with condition
even_squared = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squared dictionary: {even_squared}")

# Dictionary comprehension from two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
name_age_dict = {name: age for name, age in zip(names, ages)}
print(f"Name-age dictionary: {name_age_dict}")

# Swapping keys and values in a dictionary
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped dictionary: {swapped}")

# Dictionary comprehension with string manipulation
sentence = "the quick brown fox jumps over the lazy dog"
word_length = {word: len(word) for word in sentence.split()}
print(f"Word length dictionary: {word_length}")

# Conditional dictionary comprehension
numbers = range(10)
odd_even = {x: 'even' if x % 2 == 0 else 'odd' for x in numbers}
print(f"Odd-even dictionary: {odd_even}")

# Dictionary comprehension with nested dictionary
nested_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
flattened = {k: v for k, v in nested_dict.items() if not isinstance(v, dict)}
flattened.update({f"{k}_{inner_k}": inner_v for k, v in nested_dict.items() if isinstance(v, dict) for inner_k, inner_v in v.items()})
print(f"Flattened dictionary: {flattened}")

# Dictionary comprehension with complex conditions
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
grade_dict = {name: 'A' if score >= 90 else 'B' if score >= 80 else 'C' for name, score in scores.items()}
print(f"Grade dictionary: {grade_dict}")

# Dictionary comprehension from enumerate
fruits = ['apple', 'banana', 'cherry']
fruit_index = {fruit: index for index, fruit in enumerate(fruits, start=1)}
print(f"Fruit index dictionary: {fruit_index}")
```

## Set Comprehension

### Quick Overview
Set comprehension is a concise way to create sets in Python based on existing iterables or sets.

### In-Depth Explanation
Set comprehension is similar to list and dictionary comprehensions but creates a set instead. It provides a shorter syntax to create a new set based on the values of an existing iterable or set. The basic syntax is:

```python
new_set = {expression for item in iterable if condition}
```

Where:
- `expression` is the operation performed on each item
- `item` is the variable representing each element in the iterable
- `iterable` is the sequence, list, or other iterable object
- `condition` (optional) filters which items are included

Set comprehensions are useful for creating sets with unique elements and performing set operations in a concise manner.


```python
# Basic set comprehension
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
print(f"Unique squares: {unique_squares}")

# Set comprehension with condition
even_squares = {x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Set comprehension with string
text = "hello world"
unique_chars = {char.upper() for char in text if char.isalpha()}
print(f"Unique characters: {unique_chars}")

# Set comprehension with multiple iterables
set1 = {1, 2, 3}
set2 = {3, 4, 5}
common_elements = {x for x in set1 if x in set2}
print(f"Common elements: {common_elements}")

# Set comprehension with nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
unique_elements = {num for row in matrix for num in row}
print(f"Unique elements from matrix: {unique_elements}")

# Set comprehension with custom function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_squares = {x**2 for x in range(20) if is_prime(x)}
print(f"Squares of prime numbers: {prime_squares}")

# Set comprehension vs. set() constructor
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_set = set(numbers)
unique_comp = {x for x in numbers}
print(f"Unique set (constructor): {unique_set}")
print(f"Unique set (comprehension): {unique_comp}")

# Set comprehension with conditional expression
numbers = range(-5, 6)
abs_unique = {abs(x) if x < 0 else x for x in numbers}
print(f"Absolute unique values: {abs_unique}")
```


## Conditional Statements

### Quick Overview
Conditional statements allow you to execute different code blocks based on specified conditions.

### In-Depth Explanation
Conditional statements in Python use the keywords `if`, `elif` (else if), and `else`. They allow you to control the flow of your program by executing different code blocks based on whether certain conditions are true or false. The basic structure is:

```python
if condition1:
    # code block executed if condition1 is True
elif condition2:
    # code block executed if condition2 is True
else:
    # code block executed if all conditions are False
```

Key points:
- Conditions are expressions that evaluate to either True or False
- The `elif` and `else` clauses are optional
- You can have multiple `elif` clauses
- Indentation is crucial in Python to define code blocks


```python
# Basic if-elif-else structure
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Nested if statements
y = 5

if x > 0:
    print("x is positive")
    if y > 0:
        print("Both x and y are positive")

# Using logical operators in conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You need to get a license")
else:
    print("You're too young to drive")

# Ternary operator (conditional expression)
is_adult = "Yes" if age >= 18 else "No"
print(f"Is adult? {is_adult}")

# Using 'in' operator for membership test
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is a fruit!")

# Using 'is' operator for identity comparison
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)  # False (different objects)
print("a is c:", a is c)  # True (same object)

# Short-circuit evaluation
def is_even(n):
    print(f"Checking if {n} is even")
    return n % 2 == 0

if x < 0 or is_even(x):
    print("x is either negative or even")

# Using any() and all() in conditions
numbers = [1, 2, 3, 4, 5]
if any(num > 10 for num in numbers):
    print("At least one number is greater than 10")
if all(num < 10 for num in numbers):
    print("All numbers are less than 10")
```

## Loops

### Quick Overview
Loops allow you to repeatedly execute a block of code.

### In-Depth Explanation
Python provides two main types of loops:
1. `for` loops: Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
2. `while` loops: Used to execute a block of code as long as a condition is true.

Key features of loops:
- The `break` statement: Exits the loop prematurely
- The `continue` statement: Skips the rest of the current iteration and moves to the next one
- The `else` clause: Executes when the loop completes normally (without a `break`)


```python
# For loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with range()
for i in range(5):
    print(f"Number {i}")

# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each inner loop

# Loop with enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Loop with zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Loop with break
for num in range(10):
    if num == 5:
        break
    print(num, end=" ")
print("\nLoop ended with break")

# Loop with continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print("\nOdd numbers printed")

# Loop with else clause
for num in range(5):
    print(num, end=" ")
else:
    print("\nLoop completed normally")

# While loop with else clause
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("\nWhile loop completed normally")

# Infinite loop with break
while True:
    response = input("Enter 'q' to quit: ")
    if response.lower() == 'q':
        break
print("Exited the infinite loop")
```

## Loop Techniques

### Quick Overview
Python provides several techniques to make looping more efficient and readable.

### In-Depth Explanation
Loop techniques in Python help you write more pythonic and efficient code. Some common techniques include:

1. `enumerate()`: Get both the index and value in a loop
2. `zip()`: Iterate over two or more sequences simultaneously
3. `reversed()`: Iterate over a sequence in reverse order
4. `sorted()`: Iterate over a sequence in sorted order
5. List comprehensions: Create lists concisely using a loop-like syntax
6. Generator expressions: Create generators for memory-efficient iteration
7. `itertools` module: Provides various functions for efficient looping

These techniques can make your code more readable and often more performant.


```python
from itertools import chain, combinations

# enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# reversed()
for fruit in reversed(fruits):
    print(fruit)

# sorted()
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
for num in sorted(set(numbers)):
    print(num, end=" ")
print()

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Generator expression
sum_of_squares = sum(x**2 for x in range(10))
print(f"Sum of squares: {sum_of_squares}")

# itertools.chain()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in chain(list1, list2):
    print(item, end=" ")
print()

# itertools.combinations()
letters = ['A', 'B', 'C']
for combo in combinations(letters, 2):
    print(combo, end=" ")
print()

# Looping over dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Looping with index and item
for i, fruit in enumerate(fruits):
    print(f"fruits[{i}] = {fruit}")

# Loop with step
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Nested loop with product
from itertools import product
for i, j in product(range(2), range(2)):
    print(f"({i}, {j})", end=" ")
print()

# Loop with flag
found = False
for num in numbers:
    if num == 5:
        found = True
        break
print(f"Found 5: {found}")

# Loop with else and break
for num in numbers:
    if num == 100:
        print("Found 100!")
        break
else:
    print("100 not found in the list")
```

## Error Handling (try/except)

### Quick Overview
Error handling allows you to gracefully manage exceptions that occur during program execution.

### In-Depth Explanation
In Python, error handling is done using try/except blocks. This mechanism allows you to:

1. Attempt to execute code that might raise an exception
2. Catch specific exceptions and handle them appropriately
3. Execute cleanup code regardless of whether an exception occurred

The basic structure is:

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Handle the exception
else:
    # Execute if no exception was raised
finally:
    # Always execute, regardless of exceptions
```

Key points:
- You can catch multiple exception types
- Use `except Exception as e` to access the exception object
- The `else` and `finally` clauses are optional
- Use `raise` to manually raise exceptions


```python
# Basic try/except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Using as to access the exception object
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# try/except/else
try:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"You entered: {num}")

# try/except/finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {x}")
finally:
    print("This always executes")

# Nested try/except
try:
    n = int(input("Enter a number: "))
    try:
        result = 10 / n
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")

# Custom exceptions
class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return n ** 0.5

try:
    result = square_root(-4)
except NegativeNumberError as e:
    print(f"Error: {e}")

# Using assert
def set_age(age):
    assert 0 < age < 120, "Invalid age"
    print(f"Age set to {age}")

try:
    set_age(150)
except AssertionError as e:
    print(f"Error: {e}")

# Context manager with error handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is FileNotFoundError:
            print(f"Error: File '{self.filename}' not found")
            return True

try:
    with FileManager("nonexistent_file.txt", "r") as f:
        content = f.read()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```


## Functions

### Quick Overview
Functions are reusable blocks of code that perform specific tasks and can accept inputs and return outputs.

### In-Depth Explanation
Functions in Python are defined using the `def` keyword, followed by the function name and parentheses containing any parameters. Functions help in organizing code, promoting reusability, and breaking down complex problems into smaller, manageable parts.

Key aspects of functions:
1. Parameters: Input values that the function can work with
2. Return statement: Specifies the output of the function
3. Docstrings: Documentation strings that describe the function's purpose and usage
4. Scope: Variables defined inside a function have local scope


```python
# Basic function definition
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# Function with multiple parameters
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameter
def power(base, exponent=2):
    """Calculate the power of a number"""
    return base ** exponent

print(power(3))      # 3^2
print(power(3, 3))   # 3^3

# Function with variable number of arguments
def sum_all(*args):
    """Sum all the numbers passed as arguments"""
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# Function with keyword arguments
def person_info(**kwargs):
    """Print information about a person"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=30, city="New York")

# Function with docstring
def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
    n (int): The number to calculate the factorial of
    
    Returns:
    int: The factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial.__doc__)  # Print the docstring

# Function with local and global variables
global_var = 10

def modify_global():
    global global_var
    global_var = 20

print(f"Before: {global_var}")
modify_global()
print(f"After: {global_var}")

# Nested functions
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # 5 + 3 = 8

# Lambda function (anonymous function)
square = lambda x: x ** 2
print(square(4))
```

## Positional/Keyword Arguments

### Quick Overview
Python allows functions to be called with positional arguments, keyword arguments, or a combination of both.

### In-Depth Explanation
When defining and calling functions in Python, you can use two types of arguments:

1. Positional arguments: Arguments that are passed in a specific order
2. Keyword arguments: Arguments that are passed with a keyword and its value

Python also provides special syntax for defining functions that can accept any number of positional or keyword arguments:

- `*args`: Collects any number of positional arguments into a tuple
- `**kwargs`: Collects any number of keyword arguments into a dictionary


```python
# Function with positional and keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Calling with positional arguments
describe_pet("dog", "Buddy")

# Calling with keyword arguments
describe_pet(animal_type="cat", pet_name="Whiskers")

# Mixing positional and keyword arguments
describe_pet("hamster", pet_name="Fuzzy")

# Function with default values and keyword arguments
def greet(name, greeting="Hello"):
    """Greet a person"""
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", greeting="Hi")

# Function with *args
def sum_all(*args):
    """Sum all the numbers passed as arguments"""
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# Function with **kwargs
def print_info(**kwargs):
    """Print information passed as keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# Function with both *args and **kwargs
def combined_example(*args, **kwargs):
    """Demonstrate both *args and **kwargs"""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, name="Alice", age=30)

# Unpacking arguments
numbers = [1, 2, 3]
print(sum_all(*numbers))  # Unpacking a list into positional arguments

person = {"name": "Bob", "age": 25}
print_info(**person)  # Unpacking a dictionary into keyword arguments

# Enforcing keyword-only arguments (Python 3+)
def kw_only_arg(*, arg1, arg2):
    """Function with keyword-only arguments"""
    print(f"arg1: {arg1}, arg2: {arg2}")

kw_only_arg(arg1="value1", arg2="value2")
# kw_only_arg("value1", "value2")  # This would raise a TypeError

# Enforcing positional-only arguments (Python 3.8+)
def pos_only_arg(arg1, arg2, /):
    """Function with positional-only arguments"""
    print(f"arg1: {arg1}, arg2: {arg2}")

pos_only_arg("value1", "value2")
# pos_only_arg(arg1="value1", arg2="value2")  # This would raise a TypeError
```

## Default Parameters

### Quick Overview
Default parameters allow you to specify default values for function arguments, making them optional when calling the function.

### In-Depth Explanation
Default parameters are defined by assigning a value to the parameter in the function definition. If an argument is not provided for a parameter with a default value, the default value is used.

Key points about default parameters:
1. They must come after non-default parameters in the function definition
2. The default value is evaluated only once, at function definition time
3. Mutable objects (like lists or dictionaries) should be used carefully as default values


```python
# Basic function with default parameter
def greet(name, greeting="Hello"):
    """Greet a person with an optional custom greeting"""
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")

# Multiple default parameters
def create_profile(name, age=30, city="Unknown"):
    """Create a user profile with optional age and city"""
    return f"Name: {name}, Age: {age}, City: {city}"

print(create_profile("Alice"))
print(create_profile("Bob", 25))
print(create_profile("Charlie", city="New York"))

# Default parameter with a function call
import time

def log_message(message, timestamp=time.time):
    """Log a message with an optional timestamp"""
    print(f"{timestamp()}: {message}")

log_message("First message")
time.sleep(1)
log_message("Second message")

# Caution with mutable default values
def add_item(item, list_of_items=[]):
    """Add an item to a list (CAUTION: mutable default value)"""
    list_of_items.append(item)
    return list_of_items

print(add_item("apple"))
print(add_item("banana"))  # The list is not empty!

# Correct way to use mutable default value
def add_item_safe(item, list_of_items=None):
    """Add an item to a list (safe version)"""
    if list_of_items is None:
        list_of_items = []
    list_of_items.append(item)
    return list_of_items

print(add_item_safe("apple"))
print(add_item_safe("banana"))  # Now it's a new list

# Default parameters with type hints (Python 3.5+)
def greet_with_type(name: str, greeting: str = "Hello") -> str:
    """Greet a person with optional custom greeting (with type hints)"""
    return f"{greeting}, {name}!"

print(greet_with_type("Alice"))
print(greet_with_type("Bob", "Hi"))

# Using None as a sentinel value
def print_info(name, age=None):
    """Print person info, with age being optional"""
    info = f"Name: {name}"
    if age is not None:
        info += f", Age: {age}"
    print(info)

print_info("Alice")
print_info("Bob", 30)

# Combining default parameters with *args and **kwargs
def flexible_function(required, *args, default="Default", **kwargs):
    """Demonstrate combining various parameter types"""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

flexible_function("Must be here", 1, 2, 3, default="Custom", key1="value1", key2="value2")
```

## *args & **kwargs

### Quick Overview
`*args` and `**kwargs` allow functions to accept an arbitrary number of positional and keyword arguments, respectively.

### In-Depth Explanation
- `*args` (Arbitrary Positional Arguments):
  - Allows a function to accept any number of positional arguments
  - The arguments are packed into a tuple inside the function
  - The name `args` is conventional, but you can use any valid name

- `**kwargs` (Arbitrary Keyword Arguments):
  - Allows a function to accept any number of keyword arguments
  - The arguments are packed into a dictionary inside the function
  - The name `kwargs` is conventional, but you can use any valid name

These constructs provide flexibility in function definitions, allowing functions to handle varying numbers of arguments.


```python
# Function with *args
def sum_all(*args):
    """Sum all the numbers passed as arguments"""
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))

# Function with **kwargs
def print_info(**kwargs):
    """Print information passed as keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print_info(title="Mr.", first_name="Bob", last_name="Smith")

# Function with both *args and **kwargs
def combined_example(*args, **kwargs):
    """Demonstrate both *args and **kwargs"""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, name="Alice", age=30)

# Using *args to unpack a list
numbers = [1, 2, 3, 4, 5]
print(sum_all(*numbers))

# Using **kwargs to unpack a dictionary
person = {"name": "Charlie", "age": 35, "city": "London"}
print_info(**person)

# Ordering of parameters with *args and **kwargs
def ordered_params(pos1, pos2, *args, kw1="default", kw2="default", **kwargs):
    print(f"pos1: {pos1}, pos2: {pos2}")
    print(f"args: {args}")
    print(f"kw1: {kw1}, kw2: {kw2}")
    print(f"kwargs: {kwargs}")

ordered_params(1, 2, 3, 4, 5, kw1="custom", kw3="extra", kw4="more")

# Using *args and **kwargs to forward arguments
def wrapper_function(*args, **kwargs):
    print("Before calling the function")
    result = combined_example(*args, **kwargs)
    print("After calling the function")
    return result

wrapper_function(1, 2, 3, name="Alice", age=30)

# Type hints with *args and **kwargs (Python 3.5+)
from typing import Any

def typed_args_kwargs(*args: Any, **kwargs: Any) -> None:
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

typed_args_kwargs(1, "two", [3, 4], name="Alice", age=30)

# Restricting keyword arguments
def restricted_kwargs(*, arg1, arg2, **kwargs):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(f"Additional kwargs: {kwargs}")

restricted_kwargs(arg1="value1", arg2="value2", extra="extra_value")
```

## Lambda Functions

### Quick Overview
Lambda functions are small, anonymous functions that can have any number of arguments but can only have one expression.

### In-Depth Explanation
Lambda functions in Python are defined using the `lambda` keyword. They are typically used for short, simple operations and are often used in combination with higher-order functions like `map()`, `filter()`, and `sorted()`. Key characteristics of lambda functions include:

1. Can be defined inline without using the `def` keyword
2. Limited to a single expression
3. Can take any number of arguments
4. Implicitly return the result of the expression
5. Useful for creating small, one-time-use functions


```python
# Basic lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted()
people = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)  # Output: [('Charlie', 22), ('Alice', 25), ('Bob', 30)]

# Lambda in list comprehension
squared_numbers_comp = [(lambda x: x ** 2)(x) for x in numbers]
print(squared_numbers_comp)  # Output: [1, 4, 9, 16, 25]

# Lambda with conditional expression
abs_numbers = list(map(lambda x: x if x >= 0 else -x, [-2, -1, 0, 1, 2]))
print(abs_numbers)  # Output: [2, 1, 0, 1, 2]

# Lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)

# Lambda with default argument
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!

# Lambda capturing variables from outer scope
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

## Decorators

### Quick Overview
Decorators are a way to modify or enhance functions or classes without directly changing their source code.

### In-Depth Explanation
Decorators in Python are a form of metaprogramming, where you can add functionality to existing code without modifying it. They are implemented as functions that take another function as an argument and return a new function with added functionality. Key points about decorators:

1. They use the `@decorator_name` syntax above the function definition
2. Can be stacked (multiple decorators on a single function)
3. Can be used with or without arguments
4. Commonly used for logging, timing, authentication, and more
5. Can be applied to both functions and classes


```python
import time
import functools

# Basic decorator
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())  # Output: HELLO, WORLD!

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

# Decorator for timing functions
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()

# Class decorator
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Initializing database connection")

# Both calls return the same instance
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# Decorator with optional arguments
def log(func=None, *, prefix=''):
    if func is None:
        return lambda f: log(f, prefix=prefix)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{prefix}Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def foo():
    print("Hello from foo")

@log(prefix='DEBUG: ')
def bar():
    print("Hello from bar")

foo()
bar()

# Method decorator
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")
    
    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}")
    
    @property
    def my_property(self):
        return "This is a property"

obj = MyClass()
MyClass.static_method()
obj.class_method()
print(obj.my_property)
```

## OOP (Object-Oriented Programming)

### Quick Overview
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes for organizing code.

### In-Depth Explanation
OOP is based on the concept of "objects" that contain data and code. The key principles of OOP are:

1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class)
2. Inheritance: Creating new classes based on existing classes, inheriting their attributes and methods
3. Polymorphism: The ability of different classes to be treated as instances of the same class through inheritance
4. Abstraction: Hiding complex implementation details and showing only the necessary features of an object

Python is an object-oriented language and supports all these OOP concepts.


```python
# Basic class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says Woof!

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack!"

# Polymorphism
def animal_sound(animal):
    print(animal.speak())

cat = Cat("Whiskers")
duck = Duck("Donald")

animal_sound(cat)  # Output: Whiskers says Meow!
animal_sound(duck)  # Output: Donald says Quack!

# Encapsulation with private attributes
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Using abstract classes
rectangle = Rectangle(5, 3)
circle = Circle(2)

print(rectangle.area())  # Output: 15
print(circle.area())  # Output: 12.56

# Multiple inheritance
class Flyable:
    def fly(self):
        print("Flying...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class FlyingFish(Flyable, Swimmable):
    pass

flying_fish = FlyingFish()
flying_fish.fly()
flying_fish.swim()

# Property decorators
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)  # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0
```


## Special Methods

### Quick Overview
Special methods (also known as magic methods or dunder methods) in Python are predefined methods that allow classes to emulate the behavior of built-in types or implement operator overloading.

### In-Depth Explanation
Special methods are surrounded by double underscores (e.g., `__init__`, `__str__`). They are automatically called by Python in specific situations. Key points about special methods:

1. They allow custom classes to integrate seamlessly with Python's built-in functions and operators.
2. Common special methods include `__init__` (constructor), `__str__` (string representation), and `__len__` (length).
3. Operator overloading is implemented using special methods (e.g., `__add__` for addition).
4. They enable classes to define their behavior for built-in operations.


```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        elif isinstance(other, int):
            return self.pages + other
        else:
            raise TypeError("Unsupported operand type for +")

# Using the special methods
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Clean Code", "Robert C. Martin", 464)

print(book1)  # __str__
print(len(book1))  # __len__
print(book1 == book2)  # __eq__
print(book1 < book2)  # __lt__
print(book1 + book2)  # __add__
print(book1 + 100)  # __add__ with int

# Other useful special methods
class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items

custom_list = CustomList([1, 2, 3, 4, 5])
print(custom_list[2])  # __getitem__
custom_list[1] = 10  # __setitem__
print(2 in custom_list)  # __contains__

for item in custom_list:  # __iter__
    print(item)
```

## File Handling

### Quick Overview
File handling in Python allows you to work with files on your computer, including reading from and writing to files.

### In-Depth Explanation
Python provides built-in functions and methods for file operations. Key aspects of file handling include:

1. Opening files using the `open()` function
2. File modes: read ('r'), write ('w'), append ('a'), and others
3. Reading from files using methods like `read()`, `readline()`, and `readlines()`
4. Writing to files using `write()` and `writelines()`
5. Proper file closing using `close()` or the `with` statement (context manager)
6. Working with different file formats (text, binary, CSV, JSON, etc.)


```python
import csv
import json

# Writing to a text file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nThis line is appended.")

# Writing to a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to a JSON file
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Reading from a JSON file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Working with binary files
with open('image.jpg', 'rb') as file:
    image_data = file.read()

with open('image_copy.jpg', 'wb') as file:
    file.write(image_data)

# Using seek() and tell()
with open('example.txt', 'r') as file:
    file.seek(7)  # Move to the 7th byte
    print(file.read(5))  # Read 5 characters
    print(file.tell())  # Get current position

# Error handling in file operations
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
```

## Virtual Environments

### Quick Overview
Virtual environments in Python are isolated environments that allow you to manage project-specific dependencies without interfering with system-wide Python installations.

### In-Depth Explanation
Virtual environments solve the problem of having different projects with conflicting package requirements. Key points about virtual environments:

1. They create an isolated Python installation for a specific project.
2. Allow installation of packages without affecting other projects or the system Python.
3. Help in maintaining consistent development environments across different machines.
4. Can be easily created, activated, deactivated, and deleted.
5. Tools like `venv` (built-in) and `virtualenv` are commonly used to create virtual environments.

```bash
# Creating a virtual environment using venv
python -m venv myenv

# Activating the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS and Linux
source myenv/bin/activate

# Deactivating the virtual environment
deactivate

# Installing packages in the virtual environment
pip install package_name

# Listing installed packages
pip list

# Freezing requirements
pip freeze > requirements.txt

# Installing from requirements file
pip install -r requirements.txt

# Deleting a virtual environment
# Simply delete the environment directory
```

```python
# Example of using a virtual environment in a Python script
import sys
print(sys.prefix)  # This will show the path to your virtual environment when activated
```

## Modules

### Quick Overview
Modules in Python are files containing Python code that can be imported and used in other Python programs.

### In-Depth Explanation
Modules help organize and reuse code by grouping related functionality. Key aspects of modules include:

1. They are created by saving Python code in a .py file.
2. Can be imported using the `import` statement.
3. Provide namespace separation to avoid naming conflicts.
4. Can contain functions, classes, and variables.
5. The `if __name__ == "__main__":` idiom is used for code that should only run when the module is executed directly.
6. Python has a rich standard library of built-in modules.


```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

if __name__ == "__main__":
    print("This will only run if the module is executed directly")
    print(add(5, 3))

# main.py
import math_operations
from math_operations import subtract, PI

print(math_operations.add(10, 5))
print(subtract(10, 5))
print(PI)

# Importing with an alias
import math_operations as mo
print(mo.add(7, 3))

# Importing everything from a module (not recommended)
from math_operations import *
print(add(4, 2))

# Built-in modules
import math
import random
import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())

# Checking available functions in a module
print(dir(math))

# Getting help on a module
help(random)
```

## Packages

### Quick Overview
Packages in Python are a way of organizing related modules into a single directory hierarchy.

### In-Depth Explanation
Packages provide a method to structure Python's module namespace using "dotted module names". Key points about packages:

1. A package is a directory containing Python modules and a special `__init__.py` file.
2. The `__init__.py` file can be empty or can contain initialization code for the package.
3. Packages can have sub-packages, creating a hierarchical structure.
4. They help in organizing large codebases and avoiding naming conflicts.
5. Can be distributed and installed using tools like pip.


```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

```python
# __init__.py
print("Initializing my_package")

# module1.py
def function1():
    return "This is function1 from module1"

# module2.py
def function2():
    return "This is function2 from module2"

# subpackage/__init__.py
print("Initializing subpackage")

# subpackage/module3.py
def function3():
    return "This is function3 from module3 in subpackage"

# Add relative imports within the package
# In my_package/module2.py
from . import module1
from .subpackage import module3

# Creating a package for distribution
# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
)

# Installing the package
# pip install .
```

```python
# Using the package
# Make sure you do the above steps and restart the kernel before running this code
import my_package
from my_package import module1
from my_package.subpackage import module3

print(module1.function1())
print(my_package.module2.function2())
print(module3.function3())
```

## PEP 8

### Quick Overview
PEP 8 is the official style guide for Python code, providing coding conventions for the Python code comprising the standard library.

### In-Depth Explanation
PEP 8 (Python Enhancement Proposal 8) aims to improve the readability and consistency of Python code. Key points of PEP 8 include:

1. Indentation: Use 4 spaces per indentation level.
2. Maximum line length: 79 characters for code, 72 for docstrings/comments.
3. Imports: Should be on separate lines and grouped.
4. Whitespace: Use blank lines to separate functions and classes, and use spaces around operators.
5. Naming conventions: lowercase with underscores for functions and variables, CamelCase for classes.
6. Comments: Should be complete sentences and up-to-date with the code.
7. Documentation strings (docstrings) for all public modules, functions, classes, and methods.


```python
"""This module demonstrates PEP 8 style guidelines."""

import os
import sys
from math import sqrt
from my_module import MyClass, my_function

CONSTANT_VALUE = 42


def calculate_something(parameter_one, parameter_two, 
                        parameter_three, parameter_four):
    """Calculate and return a value based on the given parameters.
    
    This function takes four parameters and performs a calculation.
    The exact nature of the calculation is not specified in this example.
    
    Args:
        parameter_one (int): The first parameter.
        parameter_two (int): The second parameter.
        parameter_three (int): The third parameter.
        parameter_four (int): The fourth parameter.
    
    Returns:
        int: The result of the calculation.
    """
    result = (parameter_one + parameter_two) * 
              (parameter_three + parameter_four)
    return result


class ExampleClass:
    """A class demonstrating PEP 8 conventions."""

    def __init__(self, value):
        """Initialize the class with a value."""
        self.value = value

    def do_something(self):
        """Perform an action and return a result."""
        return self.value * 2


def main():
    """Main function to demonstrate PEP 8 style."""
    example = ExampleClass(10)
    result = example.do_something()
    
    if result > CONSTANT_VALUE:
        print("Result is greater than the constant.")
    else:
        print("Result is not greater than the constant.")


if __name__ == "__main__":
    main()
```

## Code Reviews

### Quick Overview
Code reviews are systematic examinations of source code intended to find and fix mistakes overlooked in the initial development phase, improving overall code quality.

### In-Depth Explanation
Code reviews are an essential part of the software development process. They involve developers inspecting each other's code for errors, potential improvements, and adherence to coding standards. Key aspects of code reviews include:

1. Identifying bugs and logic errors
2. Ensuring code readability and maintainability
3. Verifying adherence to coding standards and best practices
4. Sharing knowledge among team members
5. Improving overall code quality and consistency
6. Providing constructive feedback to developers


Here's an example of how a code review process might look, using comments to simulate review feedback:

```python
# Original code
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

# Reviewer comments:
# 1. Consider handling the case where the input list is empty to avoid division by zero.
# 2. You could use the built-in sum() function for better readability and potentially better performance.
# 3. Add a type hint for the input parameter and return value.
# 4. Add a docstring to explain the function's purpose and parameters.

# Revised code after review
from typing import List

def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers to average.

    Returns:
        float: The average of the input numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)

# Additional reviewer comments:
# 1. Good job handling the empty list case and adding clear error messaging.
# 2. The use of sum() improves readability.
# 3. Type hints and docstring greatly improve the function's usability and understanding.
# 4. Consider adding some unit tests to verify the function's behavior.

# Example unit tests
import unittest

class TestCalculateAverage(unittest.TestCase):
    def test_normal_case(self):
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(calculate_average([42]), 42.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

if __name__ == '__main__':
    unittest.main()

# Final reviewer comment:
# Great improvements! The function is now more robust, readable, and well-documented.
# The addition of unit tests is excellent for ensuring the function works as expected.