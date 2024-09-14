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