
# coding: utf-8

# ###  1 diena

# ## Python'as is a programming language that lets you work quickly and integrate systems more effectively (https://www.python.org/)
# Python is an interpreted high-level programming language for general-purpose programming, has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales (https://en.wikipedia.org/wiki/Python_(programming_language))
# 
# ## Pvz: https://www.python.org/about/success/
# <hr>

# #### Instaliavimo, naudojimo būdai bei jupyter notebook instaliavimas
#    ### Rekomenduojas būdas šiam kursui:
# 1. instaliuojant miniconda  https://conda.io/miniconda.html
#         dėl visa ko update: conda update conda
#         
#         Galima iškart instaliuoti įvarius: libraries, packages
#         bet geriau naudoti virtual environments (toliau vir env):
#         
#         geriausia (dėl dependencies):
#         conda create -n pavadinimas python=3 jupyter kiti
#         
#         activate vir env naudojimui:
#         activate pavadinimas
#         
#         deactivate vir env:
#         deactivate 
#         
#         nerekomenduoju, bet galima:
#         conda create -n pavadinimas anaconda python=3
# 
#     arba
#         conda create -n pavadinimas python
#         conda install -n pavadinimas scipy
#         activate pavadinimas
#         deactivate
#         conda remove -n pavadinimas --all
# 
#     arba
#         conda create -n pavadinimas python
#         conda install -n pavadinimas scipy=0.15.0
#         activate pavadinimas
#         deactivate
#         conda remove -n pavadinimas --all
#         
# #### Mažiau rekomenduojas būdas šiam kursui:
# 2. #### Instaliuoti anaconda (užima daug vietos) https://www.anaconda.com/download/#download
#     Visos komandos tinka kaip ir miniconda'ai
#     
# ### Nerekomenduoji būdai šiam kursui:
# 3. #### Tik python ir tada naudoti venv
#         python(3) -m venv /path/to/new/virtual/environment/pavadinimas
#         source /path/to/new/virtual/environment/pavadinimas/bin/activate
#         pip(3) intstall pavadinimas
#         paleidimas:
#         python -m scirtppav.py
#         deactivate
# 
# 4. #### Tik python https://www.python.org/downloads/windows/ ir be venv
#         pip(3) intstall pavadinimas
#         paleidimas:
#         python -m scirtppav.py
# <hr>

# ## Python objects, basic types, and variables
# 
# Everything in Python is an **object** and every object in Python has a **type**. Some of the basic types include:
# 
# - **`int`** (integer; a whole number with no decimal place)
#   - `10`
#   - `-3`
# - **`float`** (float; a number that has a decimal place)
#   - `7.41`
#   - `-0.006`
# - **`str`** (string; a sequence of characters enclosed in single quotes, double quotes, or triple quotes)
#   - `'this is a string using single quotes'`
#   - `"this is a string using double quotes"`
#   - `'''this is a triple quoted string using single quotes'''`
#   - `"""this is a triple quoted string using double quotes"""`
# - **`bool`** (boolean; a binary value that is either true or false)
#   - `True`
#   - `False`
# - **`NoneType`** (a special type representing the absence of a value)
#   - `None`
# <hr>

# In[1]:


# Python'o pagrindiniai tipai, kuriuos visada galima pasitikrinti panaudojus vieną iš daugelio built-in funkcijų/metodų
# Pavyzdžiai žemiau
type(3)
type(-3)
type(3.5)
type(-3.5)
type("Hello")
type('Hello')
type('''Hello''')
type("""Hello""")
type(True)
type(False)
type(None)


# In Python, a **variable** is a name you specify in your code that maps to a particular **object**, object **instance**, or value.
# 
# By defining variables, we can refer to things by names that make sense to us. Names for variables can only contain letters, underscores (`_`), or numbers (no spaces, dashes, or other characters). Variable names must start with a letter or underscore.

# In[2]:


# reikšmių (value) prisikirimas kintamąjam labai paprastas - tiesiog kintamojo pavadinimas ir reikšmės priskyrimas su "="
# ženklu. Kaip reikšmė (value) gali būti bet koks python'o objektas.
a = 3
type(a)
# naudojant python'ą command line, tiesiog type(a) nieko neparodis, būtina naudoti print() funkciją
# jupyter notebook žino, kad nurodant tik funkciją su kitamuoju ar raw tekstu, skaičiumi ar kitu tipu
# reikia automatiškai atspauzdinti


# In[3]:


# kintamųjų pavadinimo pagrindinės taisyklės: iš mažios raidės,
# kelis žodžius atskirti su "_" ir galimi skaičiai gale
list_of_names = 3
a1 = 5
a2 = 6
type(a)


# In[4]:


a = -3
type(a)


# In[5]:


a = 3.5
type(a)


# In[6]:


a = -3.5
type(a)


# In[7]:


a = "Hello"
type(a)


# In[8]:


a = 'Hello'
type(a)


# In[9]:


a = '''Hello'''
type(a)


# In[10]:


a = """Hello"""
type(a)


# In[11]:


a = True
type(a)


# In[12]:


a = False
type(a)


# #### Pažaisti su type'ais ir kintamaisiais

# In[13]:


# paprasta print'inimo funkcija/metodas, kuris leidžia output'inti ivairią string informaciją (ir skaičius)
a = 5
print(a)


# In[14]:


b = "tekstas"
print(b)


# In[15]:


c = 5.5
print(c)


# In[16]:


# input() reikalingas norint priimti duomenis iš vartotojo (user)
# informacija pateikiama teksto forma, todėl norint alikti matemetinius skaičius, reikia kovertavimą, pasidnaudojus
# built-in funkcijoms, kurios bus aptartos vėliau
b = input("čia galima įrašyti bet ką kaip klausimą/prašymą?")
print(b)


# ## Formatting strings and using placeholders
# https://www.w3schools.com/python/ref_func_print.asp
# 
# https://docs.python.org/3/tutorial/inputoutput.html

# ####  Naujausias nuo 3.6 (naudojant f"")

# In[17]:


# naujausias metodas, kaip galima print'inti informaciją, turint template ir naudojant placeholders, kurių vietoje galima
# įdėti kitamuosius
vardas = "Jonas"
pavardė = "Jonaitis"
print(f"Sveiki {vardas}, jūsų pavardė {pavardė}, geros dienos")


# #### nuo 2.6 iki 3.6 (naudojant "".format())

# In[18]:


print("Sveiki {}, jūsų pavardė {}, geros dienos".format(vardas, pavardė))


# In[19]:


# galima ir nurodyti index, pagal seką nurodytą format() skliaustuose
print("Sveiki {0}, jūsų pavardė {1}, geros dienos".format(vardas, pavardė))


# In[20]:


# galima ir sukeisti index numerius
print("Sveiki {1}, jūsų pavardė {0}, geros dienos".format(vardas, pavardė))


# ####  iki 2.6 (nerekomenduojama naudoti, naudojant %s, %d ir pan.)

# ### Užduotis 1:
# Priimti vardą, pavardę ir print'inti

# In[21]:


vardas = input("Koks jūsų vardas? ")
pavardė = input("Koks jūsų pavardė? ")
print(f"Sveiki {vardas} {pavardė}")


# ### Užduotis 2: 
# Panaudodami 1 ir 2 būdus, priimti email'ą (pvz. vardaspavardė@com.com), bet būtinai slaptažodį ir print'inti vardą ir pavardę (kaip prisijungus prie account'o).
# 
# Hint'as:
# if kažkas == kažkam and kažkas == kažkam:
#     
#     print(kažką)

# In[22]:


slaptazodis = "password"
emailas = "emailas@com.com"
vardas = "Janina"
pavardė = "Janinienė"
el_input = input("Prašome suvesti el.paštą ")
slapt_input = input("Prašome suvesti slaptažodį ")
if el_input == emailas and slapt_input == slaptazodis:
    print(f"Sveikti prisijungę {vardas} {pavardė}")


# ## Basic operators
# 
# In Python, there are different types of **operators** (special symbols) that operate on different values. Some of the basic operators include:
# 
# - arithmetic operators
#   - **`+`** (addition)
#   - **`-`** (subtraction)
#   - **`*`** (multiplication)
#   - **`/`** (division)
#   - __`**`__ (exponent)
# - assignment operators
#   - **`=`** (assign a value)
#   - **`+=`** (add and re-assign; increment)
#   - **`-=`** (subtract and re-assign; decrement)
#   - **`*=`** (multiply and re-assign)
# - comparison operators (return either `True` or `False`)
#   - **`==`** (equal to)
#   - **`!=`** (not equal to)
#   - **`<`** (less than)
#   - **`<=`** (less than or equal to)
#   - **`>`** (greater than)
#   - **`>=`** (greater than or equal to)
# 
# When multiple operators are used in a single expression, **operator precedence** determines which parts of the expression are evaluated in which order. Operators with higher precedence are evaluated first (like PEMDAS in math). Operators with the same precedence are evaluated from left to right.
# 
# - `()` parentheses, for grouping
# - `**` exponent
# - `*`, `/` multiplication and division
# - `+`, `-` addition and subtraction
# - `==`, `!=`, `<`, `<=`, `>`, `>=` comparisons
# 
# > See https://docs.python.org/3/reference/expressions.html#operator-precedence

# In[23]:


# visi matematinai veiksmai yra visiškai tokie patys kaip ir matematikoje
# Assigning some numbers to different variables
num1 = 10
num2 = -3
num3 = 7.41
num4 = -.6
num5 = 7
num6 = 3
num7 = 11.11


# In[24]:


# Addition
suma = num1 + num2
suma


# In[25]:


# Subtraction
minus = num3 + num4
minus


# In[26]:


# Multiplication
daugyba = num5 + num6
daugyba


# In[27]:


# Division
dalyba = num5 / num4
dalyba


# In[28]:


# Exponent
pakel = num5 ** num6
pakel


# In[29]:


# Increment existing variable
# norint padidinti kintamojo vertę ar pakeisti string'ą, galima taip:
num = 5
num = num + 5
print(num)


# In[30]:


# bet geriau taip:
numa = 9
numa += 3
numa


# In[31]:


# galima lygiai taip pat minisuoti
# Decrement existing variable
numm = 9
numm -= 3
numm


# In[32]:


# daugyba
# Multiply & re-assign
numd = 9
numd *= 3
numd


# In[33]:


# Assign the value of an expression to a variable
num8 = num1 + num2 * num3
num8


# In[34]:


# norint nustatyti reikšių lybybę, naudojama "==" ir gražinamos bool(ean) tipo reikšmės True ir False
# Are these two expressions equal to each other?
lyg1 = 5
lyg2 = 5
lyg1 == lyg2


# In[35]:


lyg3 = 2
lyg4 = 3
lyg1 == lyg3 + lyg4


# In[36]:


lyg3 == lyg4


# In[37]:


# "!=" leidždia daryti reverse palyginimą, kuris kartais reikalingas
# Are these two expressions not equal to each other?
lyg3 != lyg4


# In[38]:


# Is the first expression less than the second expression?
lyg3 > lyg4


# In[39]:


lyg1 = 5
lyg2 = 4
lyg1 > lyg2


# In[40]:


# Daromas palyginimas ir gale pateikima bool True arba False
# Is this expression True?
5 > 3 > 1


# In[41]:


# False, nes palygnimo atveju visos sąlygos turi būti True tipo: 5 > 3 -> True + 3 < 1 -> False -> False
5 > 3 < 1


# In[42]:


# True, nes "5 > 3 < 4" yra True, tada paiima paskutinė reikšmė 4 ir pritaikomas == 3 + 1 ir gaunam True
# Is this expression True?
5 > 3 < 4 == 3 + 1


# In[43]:


# string'o objektai gali panaudoti su matematiniai ženklais
# + tiesiog sujungia (concatenate)
# * tiesiog sujungia (concatenate)
# taip pat galima panaudooti "==" palytginimui
# "in" norint surasti string'ą kitame string'ę
# Assign some strings to different variables
simple_string1 = 'an example'
simple_string2 = "oranges "


# In[44]:


# Addition
simple_string1 + ' of using the + operator'


# In[45]:


# Notice that the string was not modified
simple_string1


# In[46]:


# Multiplication
simple_string1 * 3


# In[47]:


# This string wasn't modified either
simple_string1


# In[48]:


# Are these two expressions equal to each other?
simple_string1 == 'an example'


# In[49]:


# Add and re-assign
simple_string1 += ' that re-assigned the original string'
simple_string1


# In[50]:


# Multiply and re-assign
simple_string2 *= 3
simple_string2


# In[51]:


"ran" in simple_string2


# In[52]:


# Turėtų būti aišku, kad negalima pritaikyti minusavimo, dalybos ir mažinimo


# ###  2 diena

# ## Basic containers
# 
# > Note: **mutable** objects can be modified after creation and **immutable** objects cannot.
# 
# Containers are objects that can be used to group other objects together. The basic container types include:
# 
# - **`str`** (string: immutable; indexed by integers; items are stored in the order they were added)
#     https://realpython.com/python-strings/)
# - **`list`** (list: mutable; indexed by integers; items are stored in the order they were added) https://realpython.com/python-lists-tuples/
#   - `[3, 5, 6, 3, 'dog', 'cat', False]`
# - **`tuple`** (tuple: immutable; indexed by integers; items are stored in the order they were added) https://realpython.com/python-lists-tuples/
#    - `(3, 5, 6, 3, 'dog', 'cat', False)`
# - **`set`** (set: mutable; not indexed at all; items are NOT stored in the order they were added; can only contain immutable objects; does NOT contain duplicate objects) https://realpython.com/python-sets/
#   - `{3, 5, 6, 3, 'dog', 'cat', False}`
# - **`dict`** (dictionary: mutable; key-value pairs are indexed by immutable keys; items are NOT (nuo 3.7 ARE STORED) stored in the order they were added) https://realpython.com/python-dicts/
#   - `{'name': 'Jane', 'age': 23, 'fav_foods': ['pizza', 'fruit', 'fish']}`
#     
# IPython kernel sorts the dictionary keys for display when the dictionary is evaluated. It assumes that the ordering of items in a dict object is not significant. By contrast, it does not sort the keys in an OrderedDict.
# 
# When defining lists, tuples, or sets, use commas (,) to separate the individual items. When defining dicts, use a colon (:) to separate keys from values and commas (,) to separate the key-value pairs.
# 
# Strings, lists, and tuples are all **sequence types** that can use the `+`, `*`, `+=`, and `*=` operators.

# In[53]:


# Assign some containers to different variables
string1 = "Assign some "
list1 = [3, 5, 6, 3, 'dog', 'cat', False]
tuple1 = (3, 5, 6, 3, 'dog', 'cat', False)
set1 = {3, 5, 6, 3, 'dog', 'cat', False}
dict1 = {'name': 'Jane', 'age': 23, 'fav_foods': ['pizza', 'fruit', 'fish']}


# In[54]:


string1 * 5


# In[55]:


list1 * 2


# In[56]:


tuple1 * 3


# ## Some methods on list objects
# 
# - **`.append(item)`** to add a single item to the list
# - **`.extend([item1, item2, ...])`** to add multiple items to the list
# - **`.remove(item)`** to remove a single item from the list
# - **`.pop()`** to remove and return the item at the end of the list
# - **`.pop(index)`** to remove and return an item at an index

# In[57]:


# Items in the list object are stored in the order they were added
list1 = [3, 5, 6, 3, 'dog', 'cat', False]
list1.append("nauja reikšmė")
list1


# In[58]:


# Add and re-assign
list1 += [5, 'grapes']
list1


# In[59]:


# Multiply (gali būti tik skaičiai) and re-assign
list1 = [1, 2, 3, 4]
list1 *= 3
list1


# In[60]:


list1.append("item")
list1


# In[61]:


list1.extend(["item1", "item2"])
list1


# In[62]:


list1.remove("item")
list1


# In[63]:


list1.pop()
list1


# In[64]:


# kadangi pop() ištrina paskutinę value iš list'o ir tada reikšmę grąžina, todėl su print galima ją pamatyti
print(list1.pop())


# In[65]:


print(list1.pop(2))


# In[66]:


list1


# ## Some methods on set objects
# 
# - **`.add(item)`** to add a single item to the set
# - **`.update([item1, item2, ...])`** to add multiple items to the set
# - **`.update(set2, set3, ...)`** to add items from all provided sets to the set
# - **`.remove(item)`** to remove a single item from the set
# - **`.pop()`** to remove and return a random item from the set
# - **`.difference(set2)`** to return items in the set that are not in another set
# - **`.intersection(set2)`** to return items in both sets
# - **`.union(set2)`** to return items that are in either set
# - **`.symmetric_difference(set2)`** to return items that are only in one set (not both)
# - **`.issuperset(set2)`** does the set contain everything in the other set?
# - **`.issubset(set2)`** is the set contained in the other set?

# In[67]:


# Items in the set object are not stored in the order they were added
set1 = {12,3,4,5,6,7}
set1


# In[68]:


set1.add(8)
set1


# In[69]:


set1.update([15, "namas"])
set1


# In[70]:


set2 = {1.2, 5.6}
set3 = {"a", "b"}
set1.update(set2, set3)
set1


# In[71]:


set1.remove(5)
set1


# In[72]:


# skirtingai nuo list'o pop(), set atveju yra pašalinama random reikšmė
set1.pop()
set1


# In[73]:


print(set1.pop())


# In[74]:


# to return items in the set that are not in another set
set1 = {0, 1, 2, 3, 4, 5, 6}
set2 = {2, 3, 4, 5, 6, 7, 8, 9}
set3 = set1.difference(set2)
set3


# In[75]:


# to return items in both sets
set3 = set1.intersection(set2)
set3


# In[76]:


# to return items that are in either set
set3 = set1.union(set2) 
set3


# In[77]:


# to return items that are only in one set (not both)
set1 = {0, 1, 2, 3, 4, 5, 6}
set2 = {2, 3, 4, 5, 6, 7, 8, 9}
set3 = set1.symmetric_difference(set2)
set3


# In[78]:


# does the set contain everything in the other set? True arba False
set3 = set1.issuperset(set2) 
set3


# In[79]:


set1 = {3, 4, 5, 6}
set2 = {2, 3, 4, 5, 6, 7, 8, 9}
set3 = set2.issuperset(set1) 
set3


# In[80]:


# is the set contained in the other set?
set3 = set1.issubset(set2)
set3


# In[81]:


set1 = {1, 3, 4, 5, 6}
set2 = {2, 3, 4, 5, 6, 7, 8, 9}
set3 = set1.issuperset(set2) 
set3


# ## Some methods on dict objects
# 
# - **`.update([(key1, val1), (key2, val2), ...])`** to add multiple key-value pairs to the dict
# - **`.update(dict2)`** to add all keys and values from another dict to the dict
# - **`.pop(key)`** to remove key and return its value from the dict (error if key not found)
# - **`.pop(key, default_val)`** to remove key and return its value from the dict (or return default_val if key not found)
# - **`.get(key)`** to return the value at a specified key in the dict (or None if key not found)
# - **`.get(key, default_val)`** to return the value at a specified key in the dict (or default_val if key not found)
# - **`.keys()`** to return a list of keys in the dict
# - **`.values()`** to return a list of values in the dict
# - **`.items()`** to return a list of key-value pairs (tuples) in the dict

# In[82]:


# Items in the dict object are stored (3.7) in the order they were added
dict1 = {"key1": "value", "key2": 5, "key3":[20, 25, 30]}


# In[83]:


# value pasiekiamos taip
dict1["key1"]


# In[84]:


# return a list of keys in the dict
dict1.keys()


# In[85]:


# return a list of values in the dict
dict1.values()


# In[86]:


# return a list of key-value pairs (tuples) in the dict
dict1.items()


# In[87]:


# kaip pasiekti list'o reikšmes iš key3? Paprastai: pasirenkam key ir tada kaip ir pasirenkant reikšmę iš list'o
dict1["key3"][1]


# In[88]:


# add multiple key-value pairs to the dict  
dict1.update([("key5", "val1"), ("key6", 150)])
dict1


# In[89]:


# add all keys and values from another dict to the dict
dict2 = {"key10": "value", "key7": 115, "key8":5}
dict1.update(dict2)
dict1


# In[90]:


# remove key and return its value from the dict (error if key not found)
dict1.pop("key1")
dict1


# In[91]:


print(dict1.pop("key2"))


# In[92]:


# .pop(key, default_val) to remove key and return its value from the dict (or return default_val if key not found)
    


# In[93]:


# jei nerandama key, išmetama klaida
dict1["key11"]


# In[94]:


# return the value at a specified key in the dict (or None if key not found)  
#  bet galima naudoti .get(key)
dict1.get("key11")


# In[95]:


# jei print, grąžinama None reikšmė
print(dict1.get("key11"))


# In[96]:


# .get(key, default_val) to return the value at a specified key in the dict (or default_val if key not found)


# ## Some methods on tuple objects
# 
# - **`.count(value)`** returns the number of times a specified value appears in the tuple.
# - **`.index(value)`** finds the first occurrence of the specified value and returns index

# In[97]:


# Add and re-assign
tuple1 += (5, 'grapes')
tuple1


# ### Kiti container'iai https://docs.python.org/3/library/collections.html

# ## Accessing data in containers
# 
# For strings, lists, tuples, and dicts, we can use **subscript notation** (square brackets) to access data at an index.
# 
# - strings, lists, and tuples are indexed by integers, **starting at 0** for first item
#   - these sequence types also support accesing a range of items, known as **slicing**
#   - use **negative indexing** to start at the back of the sequence
# - dicts are indexed by their keys
# 
# > Note: sets are not indexed, so we cannot use subscript notation to access data elements.

# In[98]:


# Access the first item in a sequence
list1 = [3, 5, 6, 3, 'dog', 'cat', False]
list1[0]


# In[99]:


# Access the last item in a sequence
tuple1 = (3, 5, 6, 3, 'dog', 'cat', False)
tuple1[-1]


# In[100]:


# Access a range of items in a sequence
simple_string1 = "Access a range of items in a sequence"
simple_string1[3:8]


# In[101]:


# Access a range of items in a sequence
tuple1[:-3]


# In[102]:


# Access a range of items in a sequence
list1[4:]


# ## Python built-in functions and callables
# 
# A **function** is a Python object that you can "call" to **perform an action** or compute and **return another object**. You call a function by placing parentheses to the right of the function name. Some functions allow you to pass **arguments** inside the parentheses (separating multiple arguments with a comma). Internal to the function, these arguments are treated like variables.
# 
# Python has several useful built-in functions to help you work with different objects and/or your environment. Here is a small sample of them:
# 
# - **`type(obj)`** to determine the type of an object
# - **`len(container)`** to determine how many items are in a container
# - **`callable(obj)`** to determine if an object is callable
# - **`sorted(container)`** to return a new list from a container, with the items sorted
# - **`sum(container)`** to compute the sum of a container of numbers
# - **`min(container)`** to determine the smallest item in a container
# - **`max(container)`** to determine the largest item in a container
# - **`abs(number)`** to determine the absolute value of a number
# - **`repr(obj)`** to return a string representation of an object
# 
# > Complete list of built-in functions: https://docs.python.org/3/library/functions.html
# 
# There are also different ways of defining your own functions and callable objects that we will explore later.

# In[103]:


# jei prireikia, galima konvertuot skaičių į string'ą
a = 5
print(a)
b = str(a)
b


# In[104]:


type(b)


# In[105]:


a = "5"
b = int(a)
print(b)


# In[106]:


type(b)


# In[107]:


a + 5


# In[108]:


b + 5


# In[109]:


# tas pats kaip interger
float()


# In[110]:


# pagrindiniai container'iai turi ir funkcija, daugiausia naudojama sukuriant tuščius ir eigoje pridedant reikšmes
# arba paverčiant iš vieno container'io tipo į kitą prireikus
a = list()
a.append("a")
a


# In[111]:


l = ["a", 8, 5]
a = tuple(l)
a


# In[112]:


a = dict()
a["a"] = 5
a


# In[113]:


a = [5,6,7,7,7, "a", "a", "b"]
b = set(a)
b


# In[114]:


# Use the len() function to determine how many items are in a container
len(dict1)


# In[115]:


# Use the len() function to determine how many items are in a container
len(simple_string2)


# In[116]:


# Use the callable() function to determine if an object is callable
callable("a")


# In[117]:


# Use the callable() function to determine if an object is callable
callable(dict1)


# In[118]:


callable(str)


# In[119]:


# Use the sorted() function to return a new list from a container, with the items sorted
sorted([10, 1, 3.6, 7, 5, 2, -3])


# In[120]:


# Use the sorted() function to return a new list from a container, with the items sorted
# - notice that capitalized strings come first
sorted(['dogs', 'cats', 'zebras', 'Chicago', 'California', 'ants', 'mice'])


# In[121]:


# Use the sum() function to compute the sum of a container of numbers
sum([10, 1, 3.6, 7, 5, 2, -3])


# In[122]:


# Use the min() function to determine the smallest item in a container
min([10, 1, 3.6, 7, 5, 2, -3])


# In[123]:


# Use the min() function to determine the smallest item in a container
min(['g', 'z', 'a', 'y'])


# In[124]:


# Use the max() function to determine the largest item in a container
max([10, 1, 3.6, 7, 5, 2, -3])


# In[125]:


# Use the max() function to determine the largest item in a container
max('gibberish')


# In[126]:


# Use the abs() function to determine the absolute value of a number
abs(10)


# In[127]:


# Use the abs() function to determine the absolute value of a number
abs(-12)


# In[128]:


# Use the repr() function to return a string representation of an object
repr(set1)


# ## Python object attributes (methods and properties)
# 
# Different types of objects in Python have different **attributes** that can be referred to by name (similar to a variable). To access an attribute of an object, use a dot (`.`) after the object, then specify the attribute (i.e. `obj.attribute`)
# 
# When an attribute of an object is a callable, that attribute is called a **method**. It is the same as a function, only this function is bound to a particular object.
# 
# When an attribute of an object is not a callable, that attribute is called a **property**. It is just a piece of data about the object, that is itself another object.
# 
# The built-in `dir()` function can be used to return a list of an object's attributes.
# 
# <hr>

# ## Some methods on string objects
# 
# - **`.capitalize()`** to return a capitalized version of the string (only first char uppercase)
# - **`.upper()`** to return an uppercase version of the string (all chars uppercase)
# - **`.lower()`** to return an lowercase version of the string (all chars lowercase)
# - **`.count(substring)`** to return the number of occurences of the substring in the string
# - **`.startswith(substring)`** to determine if the string starts with the substring
# - **`.endswith(substring)`** to determine if the string ends with the substring
# - **`.replace(old, new)`** to return a copy of the string with occurences of the "old" replaced by "new"

# In[129]:


# Assign a string to a variable
a_string = 'tHis is a sTriNg'


# In[130]:


# Return a capitalized version of the string
a_string.capitalize()


# In[131]:


# Return an uppercase version of the string
a_string.upper()


# In[132]:


# Return a lowercase version of the string
a_string.lower()


# In[133]:


# Notice that the methods called have not actually modified the string
a_string


# In[134]:


# Count number of occurences of a substring in the string
a_string.count('i')


# In[135]:


# Count number of occurences of a substring in the string after a certain position
a_string.count('i', 7)


# In[136]:


# Count number of occurences of a substring in the string
a_string.count('is')


# In[137]:


# Does the string start with 'this'?
a_string.startswith('this')


# In[138]:


# Does the lowercase string start with 'this'?
a_string.lower().startswith('this')


# In[139]:


# Does the string end with 'Ng'?
a_string.endswith('Ng')


# In[140]:


# Return a version of the string with a substring replaced with something else
a_string.replace('is', 'XYZ')


# In[141]:


# Return a version of the string with a substring replaced with something else
a_string.replace('i', '!')


# In[142]:


# Return a version of the string with the first 2 occurences a substring replaced with something else
a_string.replace('i', '!', 2)


# ### 3 diena

# ## Functions, Positional arguments and keyword arguments, * args, ** kwargs, lambda
# 
# You can call a function/method in a number of different ways:
# 
# - `func()`: Call `func` with no arguments
# - `func(arg)`: Call `func` with one positional argument
# - `func(arg1, arg2)`: Call `func` with two positional arguments
# - `func(arg1, arg2, ..., argn)`: Call `func` with many positional arguments
# - `func(kwarg=value)`: Call `func` with one keyword argument 
# - `func(kwarg1=value1, kwarg2=value2)`: Call `func` with two keyword arguments
# - `func(kwarg1=value1, kwarg2=value2, ..., kwargn=valuen)`: Call `func` with many keyword arguments
# - `func(arg1, arg2, kwarg1=value1, kwarg2=value2)`: Call `func` with positonal arguments and keyword arguments
# - `obj.method()`: Same for `func`.. and every other `func` example
# 
# When using **positional arguments**, you must provide them in the order that the function defined them (the function's **signature**).
# 
# When using **keyword arguments**, you can provide the arguments you want, in any order you want, as long as you specify each argument's name.
# 
# When using positional and keyword arguments, positional arguments must come first.

# In[143]:


# python'e funkcijos aprašomos taip:
# 1) pirma eina def, kaip žymeklis, kad norime sukurti funkciją, o ne sakykim, klasę ir norim, kad ji turėtų pavadinimą
# 2) tada pavadinimas, lygiai taip pat, kaip kad reikia pavadinimo kintamiesiems
# 3) skliaustai "()", kuriuose gali ir nebūti argumentų, bet dažniausiai reikia ir jų gali būti "beliek",
# su kuriais kažką padarome kode ir pavadinimai gali būti bet kokie, bet aišku, kad geriausia jog būtų meaningful
# 4) dvitaškis ":"
# 5) tada BŪTINAS intend: 4 space arba tab
# 6) ir po to eina kodas
# 7) ir jei reikia, kad kažkokia reikšmė būtų grąžinta, pačiam kodo gale "return"
# 8) ir tada reikia initializuoti funkciją, suvedus jos pavadinimą ir atitinkamus argumentus, jei jie reikalingi.
vardas = "Jonas"
def pav():
    print(vardas)
    
pav()


# In[144]:


vardas = "Jonas"
def pav():
    return vardas
    
print(pav())


# In[145]:


# su argumentu
vardas = "Jonas"
def pav(vard):
    print(vard)
    
pav(vardas)


# In[146]:


# su argumentu
vardas = "Jonas"
pavarde = "Jonassas"

def pav(v, p):
    print(f"{v} {p}")
    
pav(vardas, pavarde)


# In[147]:


# taip pat galima naudoti keyword argumentus, kurie naudojami nustatyti kažkokią default value ir įvedus kaip keyword
# argumentą per funkcijos inicijavimą, galima ją pakeisti
diena = "trečiadienis"

def pav(d=diena):
    print(f"Sveiki šiandien {d}")
    
pav()


# In[148]:


pav("ketvirtadienis")


# In[149]:


#  galima naudoti kartu argumentus ir keyword argumentus
vardas = "Jonas"
pavarde = "Jonassas"
diena = "trečiadienis"

def pav(v, p, d=diena):
    print(f"Sveiki {v} {p}, šiandien {d}")
    
pav(vardas, pavarde)


# In[150]:


pav(vardas, pavarde, "ketvirtadienis")


# In[151]:


# lambda https://www.w3schools.com/python/python_lambda.asp
# taip pat yra anonymous funkcijos, kurioms nereikia pavadinimo, gali priimti argumentus ir tik vieną expression
# 1) pirma eina "lambda"
# 2) tada agumentas/ai
# 3) tada":"
# 4) expression'as
# dažniausiai naudojama kartu su map() ir filter().
double = lambda x: x * 2
print(double(5))


# In[152]:


daugyba = lambda x, y: x * 7
print(daugyba(5, 6))


# In[153]:


#  *args, **kwargs, naudojami, kaip nežinom tikslaus argumetų skaičiau, bet žinom, kad galima padaryti tą patį veiksmą
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')


# #### Užduotis:
# Panaudojus funkciją: panaudodami 1 ir 2 būdus (f"{}" ir "{}".format()), priimti email'ą (pvz. vardaspavardė@com.com), bet būtinai slaptažodį ir print'inti vardą ir pavardę (panašiai kaip prisijungus prie account'o)

# ## Python "for loops"
# 
# It is easy to **iterate** over a collection of items using a **for loop**. The strings, lists, tuples, sets, and dictionaries we defined are all **iterable** containers.
# 
# The for loop will go through the specified container, one item at a time, and provide a temporary variable for the current item. You can use this temporary variable like a normal variable.

# In[154]:


for i in ["a", "b"]: # gali būti tuples, listai, string, net dict
    print(i)


# #### range() https://www.w3schools.com/python/ref_func_range.asp

# In[155]:


# jei norim naudoti tam tikrą skaičių iteracijų ar specifiškai skaičius
for i in range(5):
    print(i)


# In[156]:


a = 1
for i in range(5):
    a *= 2
    print(a)


# #### enumarate() https://www.programiz.com/python-programming/methods/built-in/enumerate

# In[157]:


# jei norim žinoti ir index'ą
for i, v in enumerate(["Jonas", "Petras"]):
    print(i, v)


# In[158]:


# norint dictinary'io priskirti reikšmes, reikia naudoti zip(), kadangi norit sudaryti dictionary reikia vienu metu turėti
# tiek key, tiek value, ko negalima padaryti paprastu for loop.
dict1 = dict()
keys = ['a', 'b', 'c']
values = [1, 2, 3]
for k in keys:
    for v in values:
        dict1[k] = v
dict1


# In[159]:


for k, v in zip(keys, values):
    dict1[k] = v
dict1


# In[160]:


# bet kaip visada python'as turi palengvinimų
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)


# In[161]:


# difference between iterable and iterator https://www.geeksforgeeks.org/python-difference-iterable-iterator/

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c,v =  zip(*resultList)
print('c =', c)
print('v =', v)


# In[162]:


# Fibonacci numbers paprastas sprendimas (vienas iš daugelio)
inp = 5

a = [0, 1]

for i in range(2, (inp + 1)):
    b = a[-2] + a[-1]
    a.append(b)

for i in a[1:]:
    print(i)


# In[163]:


# Fibonacci numbers pythonic sprendimas
inp = 5
a, b = 0, 1

for i in range(inp):
    a, b = b, a + b
    print(a)


# #### Užduotis:
# Fibonacci užduotį su funkcija

# In[164]:


inp = 5

def fibonacci(sk):
    a = 0
    c = 1
    for i in range(sk):
        a, c = c, a + c
        print(a)

fibonacci(inp)


# ## Python "if statements" and "while loops"
# 
# Conditional expressions can be used with these two **conditional statements**.
# 
# The **if statement** allows you to test a condition and perform some actions if the condition evaluates to `True`. You can also provide `elif` and/or `else` clauses to an if statement to take alternative actions if the condition evaluates to `False`.
# 
# The **while loop** will keep looping until its conditional expression evaluates to `False`.
# 
# > Note: It is possible to "loop forever" when using a while loop with a conditional expression that never evaluates to `False`.
# >
# > Note: Since the **for loop** will iterate over a container of items until there are no more, there is no need to specify a "stop looping" condition.

# In[166]:


vardas = "Jonas"
pavarde = "Jonassas"
slapta = "pas"
emailas = "a@com.com"
inpslapta = input("Slaptažodis? ")
inpelpastas = input("El.paštas? ")
if slapta == inpslapta and emailas == inpelpastas:
    print(f"Sveiki prisijungę {vardas} {pavarde}")


# In[168]:


# vietoj "and" galima naudoti "or", jei norime, kad vienas iš lyginimų būtų True
vardas = "Jonas"
pavarde = "Jonassas"
slapta = "pas"
emailas = "a@com.com"
inpslapta = input("Slaptažodis? ")
inpelpastas = input("El.paštas? ")
if slapta == inpslapta or emailas == inpelpastas:
    print(f"Sveiki prisijungę {vardas} {pavarde}")


# In[169]:


vardas = "Jonas"
pavarde = "Jonassas"
slapta = "pas"
emailas = "a@com.com"
inpslapta = input("Slaptažodis? ")
inpelpastas = input("El.paštas?")
if slapta == inpslapta and emailas == inpelpastas:
    print(f"Sveiki prisijungę {vardas} {pavarde}")
else:
    print("Neteisingas slaptažodis ar el.paštas")


# In[170]:


# jei reikia daugiau palyginimų, tada naudojamas "elif"
var = 1
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
    elif var < 50:
        print("Expression value is less than 50")
else:
    print("Could not find true expression")


# #### Užduotis:
# Tą pačią užduotį, tik dar priimti amžių ir pagal amžių print'i, kad jei vartotojas per jaunas, negali prsijungti, kitu atveju, kad viskas gerai. Taip pat panaudoti ankstesnius metodus ir išpręsti įvestas klaidas pvz. jei el.paštą suveda didžiosiom raidėm, automatiškai pataisyti.

# In[171]:


vardas = "Jonas"
pavarde = "Jonassas"
slapta = "pas"
emailas = "a@com.com"
inpslapta = input("Slaptažodis? ")
inpelpastas = input("El.paštas? ")
inpriba = int(input("Amžius? "))
amzriba = 18
if slapta == inpslapta.lower() and emailas == inpelpastas.lower() and amzriba < inpriba:
    print(f"Sveiki prisijungę {vardas} {pavarde}")
else:
    print("Neteisingas slaptažodis ar el.paštas arba esate per jaunas")


# In[172]:


vardas = "Jonas"
pavarde = "Jonassas"
slapta = "pas"
emailas = "a@com.com"
inpslapta = input("Slaptažodis? ")
inpelpastas = input("El.paštas? ")
inpriba = int(input("Amžius? "))
amzriba = 18
if slapta == inpslapta.lower() and emailas == inpelpastas.lower() and amzriba < inpriba:
    print(f"Sveiki prisijungę {vardas} {pavarde}")
else:
    print("Neteisingas slaptažodis ar el.paštas arba esate per jaunas")


# In[173]:


# jei norim infinate, nuolatos vykstančio loop, naudojam "while"
# vienas iš būdu break while loops'a, kai nurodom tam tikras ribas patys
flag = True
while flag:
    print(flag)
    flag = False


# In[174]:


n = 5
while n > 0:
    n -= 1
    print(n)


# In[175]:


# kitas būdas naudojant break ir galima naudoti if/else
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')


# ### 4 diena

# ## PEP8 (https://www.python.org/dev/peps/pep-0008/)

# ### Daugiau built-in funkcijų/metodų https://www.programiz.com/python-programming/methods/built-in

# In[176]:


# map() dažniausiai naudojama kartu su lambda, nes priima funciją, bet paprasta fukcija gali turėtų tik vieną argumentą, 
# ir tada iterable ir yra iterator, todėl norint gauti reikšmes, turim panaudoti list(), set() ar tuples(). Bet 
a = [5, 6, 7, 8, 9]

def pakelimas(c):
    d = c**3
    return d

e = map(pakelimas, a)
tuple(e)


# In[177]:


a = [5, 6, 7, 8, 9]
b = map(lambda x: x * 2, a)
tuple(b)


# In[178]:


# bet su lambda galima ir keliais argumentais
f = [1, 2, 3, 4, 5]
g = map(lambda x, y: x * y, a, f)
tuple(g)


# In[179]:


# filter() method constructs an iterator from elements of an iterable for which a function returns true.
# tas pats kas (element for element in iterable if function(element))
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)


# In[180]:


# del - ištrina, pvz. kintamąjį jei nebereikia
x = "hello"
print(x) 
del x
print(x) 


# In[181]:


# galima ir iš list'o value
x = ["apple", "banana", "cherry"]
print(x)
del x[0]
print(x) 


# In[182]:


# ir dict
x = {"apple": 1, "banana": 2, "cherry": 3}
print(x)
del x["apple"]
print(x)


# In[183]:


# divmod() palengvina sveikojo skaičiaus ir liekanos skaičiavimus
print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(3, 8) = ', divmod(3, 8))
print('divmod(5, 5) = ', divmod(5, 5))
# galima ir float, bet tai sudėtingi skaičiavimai, tai mums nelabai aktualu
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(3, 8.0) = ', divmod(3, 8.0))
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))


# In[184]:


# iter() next() fukcijos, kurios padeda sukurti iterator ir su tik next() gauti sekančias reikšmes
x = ["apple", "banana", "cherry"]
b = iter(x)
print(next(b))
print(next(b))
print(next(b))


# In[185]:


# open() naudojama dirbant su failais, bet failų atidarymą dar giliau pasigilinsim vėliau


# In[186]:


# pow() palengvina pakėlimą laipsniu, pirmas skaičius, kuris keliamas ir antras - laipsnio skaičius
print(pow(2, 3))
print(pow(3, 2))


# In[187]:


# reversed() bet kokį tuple, string, list or range
# for string
seqString = 'Python'
print(list(reversed(seqString)))

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))


# In[188]:


# slice, kartais gali patogesnis būdas nei index būdu
a = ("abcdefgh")
x = slice(3, 5)
print(a[x])


# In[189]:


a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])


# In[190]:


# round() padeda su float skaičių apvalinimu
print(round(5.7587878878))
print(round(5.7587878878, 1))
print(round(5.7587878878, 2))
print(round(5.7587878878, 3))
print(round(5.7587878878, 4))
print(round(5.7587878878, 5))


# ## List, set, and dict comprehensions https://www.data-blogger.com/2017/11/16/python-list-comprehension/

# In[191]:


# comprehensions'ai - dar vienas palenginimas, kuris patogesnius for loops vienoje eilutėje
a = list()
for i in range(10):
    a.append(i)
a


# In[192]:


# bet galima ir taip:
# [expression for item in list if conditional], kur conditional yra palyginimai su ==, <(=), >(=).
b = [i for i in range(9)]
b


# In[193]:


c = [i for i in range(15) if i < 15]
c


# In[194]:


def up(a):
    return a ** 2 


d = [up(i) for i in range(15) if i < 15]
d


# In[195]:


# dar pvz.
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)


# In[196]:


# set tas pats, tik naudojami {}


# In[197]:


# kadangi dict yra key: value, todėl pradžioje kaip expression turi būti k:v (čia convention)
keys = ['a','b','c','d','e'] 
values = [1,2,3,4,5]   

D = {x: x**2 for x in [1,2,3,4,5]}
D


# In[198]:


# bet pagrindinis būdas naudojant zip()
myDict = {k:v for (k,v) in zip(keys, values)}
myDict


# #### Užduotis: gauti dict iš vardų list'o, kur "key" yra vardas, o "value" - index numeris

# In[199]:


a = ["Jonas", "Petras", "Kazys", "Joan"]
d = {v:i for i, v in enumerate(a)}
d


# ## Importing modules https://www.w3schools.com/python/python_modules.asp
# ## https://docs.python.org/3/library/

# In[200]:


# Python'as turi Core funkcianalumą, bet taip galima naudoti modulius, kuriuos labai paprasta importuoti.
# Taip daroma, kadangi ne viso programavimo kalbos funkcinualumo kiekvieną kartą reikia kuriant kodą, todėl kai prireikia
# speficinio funcianalumo, importuojmas atitinkamas modulis ir modulios funkcijos/metodai pasiekiami per ".":
# import modulio pavadinimas


# In[201]:


# datatime padeda dirbti su datomis ir laiku, kaip pvz.:
import datetime
datetime.date.today()


# In[202]:


print(datetime.date.today())


# In[203]:


# kadangi kiekvienas modulis turi fukcijas/metodus, kurių gali nereikti, todėl galima importuoti tik tą funkciją/as.
from datetime import date
today = date.today()
print(today)


# In[204]:


# taip pat, kaikurie moduliai gali turėti ilgus pavadinimus, todėl galima su kurti alias sutrunpinant. Taip pat naudoja
# ir pagal convention tam tikriems moduliams.
import datetime as d
d.date.today()


# In[205]:


# sys dirbant su sistema ir konsole, bet mums neaktualu


# In[206]:


# copy padeda dirbant su kopijomis, nes python tam tikrais kartais ne kuria kopijos, o sukuria referencą, dažniausiai 
# taip yra su kintamųjų sukųrimu.
a = ["a"]
b = a
a.append("b")
print(a)
print(b)


# In[207]:


import copy
a = ["a"]
b = copy.copy(a)
a.append("b")
print(a)
print(b)


# In[208]:


# pprint esant reikalui, jei dirbama su konsole, pagrąžina duomenų output'inimą į konsolę.


# In[209]:


# random padeda generuoti random numerius


# In[210]:


import random
print(random.random()) # Random 0.0 <= x < 1.0
print(random.randint(1,9)) # 1 <= x < 9


# In[211]:


from random import shuffle
x = [i for i in range(10)]
print(x)
shuffle(x)
print(x)


# #### Užduotis: Užduotis: gauti dict iš vardų list'o, kur "key" yra vardas, o "value" - random numeris

# In[212]:


import random

a = ["Jonas", "Petras", "Kazys", "Joan"]
l = list()

for i in range(0,len(a)):
    l.append(random.randint(i,10))

print(l)

d = {v:r for v, r in zip(a,l)}
d


# In[213]:


# csv modulis, kuris leidžia dirbti su csv failais, kadangi vėliau žaisime su failais, tai dabar tiek
# import csv


# In[214]:


# json modulis, kuris leidžia dirbti su json failais, kadangi vėliau žaisime su failais, tai dabar tiek


# In[215]:


# galima ir savo modulį: išsaugomas failas su .py. Pvz. file1.py suvedam tokį kodą:
# skaicius = 5
# def up(a):
#     return a ** 2
# tai kitam faile pvz. file2.py galima, šiam pavyzdžui file1.py turi būti tam pačiam folder'yje, bet šiaip nebūtinai
# import file1.py
# tada su "." galima pasiekti tiek fukciją, tiek kintamąjį
# a = file1.skaicius
# b = file1.up(2)


# ### 5 diena

# ## Exceptions https://realpython.com/python-exceptions/

# In[216]:


# Exceptions naudojami dirbant su error'ai, nes įvykus error'ui, programa "nulužta", bet exceptions padeda to išvengti
# Kaip matote, kodas neturi error'o kaip tokio, bet panaudojus "raise", galima kokį norime error'ą pateikti.
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


# In[218]:


sk1 = 5
sk2 = 0

def dalyba(a, b):
    return a/b

dalyba(sk1, sk2)
# Kaip matote, šios cell'ės kodo vykdymas išmetė ZeroDivisionError ir "sustojo", bet naudojant "except" galima "nulužimo"
# išvengt


# In[219]:


def sudetis(a, b):
    return a + b

try:
    dalyba(sk1, sk2)
except ZeroDivisionError as error:
    print(error)
    print(sudetis(sk1, sk2))
# Kaip matote, kodas "neužlužo" ir buvo atspaudintas error'as, nes taip nurodyta kode, bet taip pat galimas ir bet koks
# kitas kodas, kaip pvz. buvo įvykdyta funkcija sudetis ir atprint'intas rezultatas


# In[220]:


# Dabar logika tokia: su "try" pabandyk atlikti kažkokį kodą, jei klaida, su "except" "pagauk" klaidą ir arba 
# atprint'ink klaidą (dažniausiai) arba įvykdyk kitą kodą. Bet jei klaidos nėra, tada panaudojamas "else".
# Jame vėl gali būti "try"-"except" arba bet koks kitas kodas. Pavyzdyje pabandoma atidaryti .log failą 
# (working su failais yra parodytas žemiau) ir jei failo nėra, print'ina klaidą, jei yra, jį atidaro "read" mode'e
# (vėlgi žiūrėti žemiau)
# Kaip matot, jei sk2 = 0, atprint'tina "division by zero" ir 5
sk1 = 5
sk2 = 0

try:
    dalyba(sk1, sk2)
except ZeroDivisionError as error:
    print(error)
    print(sudetis(sk1, sk2))
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)


# In[221]:


# Jei sk2 != 0, atprint'tina klaidą, kad nerastas failas
sk1 = 5
sk2 = 1

try:
    dalyba(sk1, sk2)
except ZeroDivisionError as error:
    print(error)
    print(sudetis(sk1, sk2))
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)


# In[222]:


# ir galiausiai dar yra naudojamas "finally", kuris reiškia, kodas turi būti vydomas neprilausomai ar yra klaida ar ne
sk1 = 5
sk2 = 1

try:
    dalyba(sk1, sk2)
except ZeroDivisionError as error:
    print(error)
    print(sudetis(sk1, sk2))
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Čia turi patekti kodas, kuris turi būti vykdomas ne priklausomai nuo to ar yra klaidos ar ne")


# ##  Working with files, context managers and the "with statement" and
# Write, Create https://www.w3schools.com/python/python_file_write.asp
# 
# Open file https://www.w3schools.com/python/python_file_open.asp
# 
# Delete https://www.w3schools.com/python/python_file_remove.asp
# 
# Context managers https://dbader.org/blog/python-context-managers-and-with-statement

# ###### Senovinis būdas dirbti su failais yra toks:
# f = open("failaspavadinimas.txt", "mode'as") as f:
# 
# pagrindiniai mode'ai, nenurodžius default yra "r":
# 
# "r" - Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
# 
# "r+" - Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# 
# "w" - Opens a file for writing only. Overwrites the file (truncate file to zero length) if the file exists. If the file does not exist, creates a new 
# file for writing.
# 
# "w+"  - Opens a file for both writing and reading. Overwrites the existing file (truncate file to zero length) if the file exists. If the file does not exist, creates a new file for reading and writing.
# 
# "a" - Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# 
# "a+"  - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# 
# Daugiau galima pasižiūrėti čia https://www.tutorialspoint.com/python/python_files_io.htm
# 
# jei norim įrayšyti:
# 
# f.write("Galima tekstą arba duomenis, kurie išsaugoti kintamąjame")
# 
# jei norim nuskaityti:
# 
# f.read(size) - size is an optional numeric argument and this func returns a quantity of data equal to size. If size if omitted, then it reads the entire file and returns it
# 
# f.readline() - reads a single line from file with newline at the end t.y. yra iterator
# 
# f.readlines() - returns a list containing all the lines in the file aka list(iterator).
# 
# ir tada failą BŪTINA uždaryti:
# 
# f.close()

# In[223]:


a = "Galima tekstą arba duomenis, kurie išsaugoti kintamąjame, bet viskas turi būti pateikta str formatu"
b = "Galima tekstą arba duomenis, kurie išsaugoti kintamąjame"
c = "Galima tekstą arba duomenis"
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = open("file1.txt", "w")
f.write(f"{a}{b}{c}")
f.close()
# atsidarykite failą ir pasižiūrėkite, kas įrašyta
# ir čia daugiau nieko negalime padaryti, pvz. dar ir nuskaityti failą


# In[224]:


f = open("file1.txt", "w")
f.write(f"{a}\n{b}\n{c}\n")
f.close()


# In[225]:


# jei veiksmą pakartosim, tik vietoj kintamojo a, norėsim b, turime duomenis perconvertuoti į str formatą
f = open("file1.txt", "w") # faile buvusi info ištrinama (truncate)
f.write(str(d))
f.close()


# In[227]:


# pakeičiam failą nuskaitymui tolimesniam mokymuosi
f = open("file1.txt", "w")
f.write(f"{a}\n{b}\n{c}\n")
f.close()


# In[228]:


f = open("file1.txt", "r")
print((f.read()))
# print(f.readlines())
# print((f.readline()))
# print((f.readline()))
# print((f.readline()))
f.close()


# In[229]:


f = open("file1.txt", "r")
# print((f.read()))
print(f.readlines())
# print((f.readline()))
# print((f.readline()))
# print((f.readline()))
f.close()


# In[230]:


f = open("file1.txt", "r")
# print((f.read()))
# print(f.readlines())
print((f.readline()))
print((f.readline()))
print((f.readline()))
f.close()


# In[231]:


# jei norim su for loop'u
f = open("file1.txt", "r")

for i in f:
    print(i.lower())
    
f.close()


# In[232]:


# jei norim pridėti papildomą informaciją
f = open("file1.txt", "a")
f.write("Pridėtas papildomas tekstas")
f.close()


# ##### Kaip matot, kiekvieną kartą reikia atsiminti panaudoti close() kas yra labai nepatogu prisiminti daug kodinant todėl kaip visada python'as turi palengvinimą, kuris atrodo taip:
# with open("file1.txt", "a") as f:
#     
#         galioja tas pats kodas, kaip prieš tai buvusiam būdui

# ##### Užduotis: Panaudojus random modulį, sukurti failą su random skaičiumi prie pavadinimo ir įrašyti kokį nors tekstą su tuo pačiu random skaičium

# In[233]:


import random
rand = random.randint(1, 50)

with open(f"file{rand}.txt", "w") as f:
    f.write(f"Tekstas{rand}")


# ##### Užduotis: Priimti slaptažodį ir emailą bei išsaugoti faile

# In[235]:


import random
slapta = input("Slaptažodis? ")
elpastas = input("El.paštas ")

with open(f"file2.txt", "w") as f:
    f.write(f"Slaptažodis {slapta}\nEmailas {elpastas}")


# In[253]:


# csv https://realpython.com/python-csv/
import csv
with open('failas.csv', newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader) # todėl, kad reader yra iterator objektas
    print(list(csv_reader))


# In[254]:


with open('failas.csv', newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
        print(i)


# In[255]:


a = ["Jonas", "Jonaitis", "Kaunas"]
with open('failas.csv', newline="", mode='a') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(a)


# In[256]:


with open('failas.csv', newline="\n", mode='a') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(a)


# In[257]:


# json https://realpython.com/python-json/
import json

with open("naujas.json", "r") as read_file:
    data = json.load(read_file)
    print(data)


# In[258]:


# Užduotis: kad atspaudintu random value iš list'o dict viduje
import json
import random

with open("naujas.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
    for i in data.values():
        if type(i) is str:
            print(i.lower())
        elif type(i) is int:
            print(i)
        else:
            rand = random.randint(0, (len(i)-1))
            print(i[rand])


# ### 6 diena

# In[ ]:


# html? https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python


# In[ ]:


# join()


# In[ ]:


# print(":".join( map(str, b) ))        # x:2:y
# print(":".join( str(x) for x in b ))  # x:2:y


# ## Miscellaneous

# ### requarements.txt 
# 
# https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1
# 
# conda install -n pavadinimas beautiful-soup, pandas, numpy
# 

# ###  Generators ir Yield
# 
# https://www.programiz.com/python-programming/generator

# ###  Closures
# https://www.programiz.com/python-programming/closure

# ### 7 diena

# ## Webscraping

# ### 8 diena

# ## SQL
