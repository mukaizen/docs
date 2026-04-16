# 🐍 Python Cheatsheet — Beginner to Pro
> Aligned with **100 Days of Code™: The Complete Python Pro Bootcamp**

---

## Table of Contents

**Beginner (Days 1–15)**

1. [Print & Comments](#1-print--comments)
2. [Variables & Data Types](#2-variables--data-types)
3. [String Methods](#3-string-methods)
4. [User Input](#4-user-input)
5. [Type Conversion](#5-type-conversion)
6. [Arithmetic & Operators](#6-arithmetic--operators)
7. [Conditional Logic (if/elif/else)](#7-conditional-logic-ifelifelse)
8. [Loops — for & while](#8-loops--for--while)
9. [Lists](#9-lists)
10. [Functions](#10-functions)

**Intermediate (Days 16–40)**

11. [Return Values & Scope](#11-return-values--scope)
12. [Dictionaries & Nesting](#12-dictionaries--nesting)
13. [Tuples & Sets](#13-tuples--sets)
14. [List & Dict Comprehensions](#14-list--dict-comprehensions)
15. [Modules & Packages](#15-modules--packages)
16. [Error Handling](#16-error-handling)
17. [File I/O](#17-file-io)
18. [Classes & OOP](#18-classes--oop)
19. [Inheritance & Polymorphism](#19-inheritance--polymorphism)
20. [Decorators](#20-decorators)

**Intermediate+ (Days 41–60)**

21. [Lambda, Map, Filter, Reduce](#21-lambda-map-filter-reduce)
22. [Iterators & Generators](#22-iterators--generators)
23. [Regular Expressions](#23-regular-expressions)
24. [args & kwargs](#24-args--kwargs)
25. [Closures](#25-closures)
26. [Datetime](#26-datetime)
27. [JSON & CSV](#27-json--csv)
28. [Virtual Environments & pip](#28-virtual-environments--pip)

**Experienced / Pro (Days 61–100)**

29. [Type Hints](#29-type-hints)
30. [Dataclasses](#30-dataclasses)
31. [Context Managers](#31-context-managers)
32. [Threading & Multiprocessing](#32-threading--multiprocessing)
33. [Async / Await](#33-async--await)
34. [APIs & Requests](#34-apis--requests)
35. [Web Scraping (BeautifulSoup)](#35-web-scraping-beautifulsoup)
36. [Flask Basics](#36-flask-basics)
37. [SQLite & SQLAlchemy](#37-sqlite--sqlalchemy)
38. [Testing with pytest](#38-testing-with-pytest)
39. [Useful Built-in Functions](#39-useful-built-in-functions)
40. [Pythonic Patterns & Tips](#40-pythonic-patterns--tips)

---

# BEGINNER (Days 1–15)

---

## 1. Print & Comments

```python
print("Hello, World!")          # single-line comment
print("Name:", "Alice")         # multiple args, space-separated
print("a", "b", sep="-")        # a-b
print("line1", end=" ")         # no newline, stays on same line
print("line2")                  # line1 line2

"""
This is a
multi-line docstring / comment
"""
```

---

## 2. Variables & Data Types

```python
# Assignment
name = "Alice"          # str
age = 25                # int
height = 5.7            # float
is_student = True       # bool
nothing = None          # NoneType

# Check type
print(type(name))       # <class 'str'>

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0           # all point to same value

# Constants (convention — Python doesn't enforce)
MAX_SIZE = 100

# f-strings (Python 3.6+)
greeting = f"Hello, {name}! You are {age} years old."
print(f"Pi is approx {3.14159:.2f}")   # Pi is approx 3.14

# Older formatting styles
print("Hello, %s" % name)
print("Hello, {}".format(name))
```

---

## 3. String Methods

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"      — remove whitespace both ends
s.lstrip()          # remove left whitespace
s.rstrip()          # remove right whitespace
s.lower()           # "  hello, world!  "
s.upper()           # "  HELLO, WORLD!  "
s.title()           # "  Hello, World!  "
s.replace("World", "Python")    # "  Hello, Python!  "
s.split(",")        # ['  Hello', ' World!  ']
s.startswith("  He")            # True
s.endswith("!  ")               # True
s.find("World")     # 9  (index), -1 if not found
s.count("l")        # 3
s.strip().isdigit() # False
"42".isdigit()      # True
"abc".isalpha()     # True
",".join(["a","b","c"])  # "a,b,c"

# Slicing
s = "Hello"
s[0]        # "H"
s[-1]       # "o"
s[1:4]      # "ell"
s[:3]       # "Hel"
s[::2]      # "Hlo"   (every 2nd char)
s[::-1]     # "olleH" (reverse)

# String length
len("Hello")    # 5

# Multiline string
multi = """
line one
line two
"""
```

---

## 4. User Input

```python
name = input("What is your name? ")   # always returns str
print(f"Hello, {name}!")

age = int(input("How old are you? "))  # convert to int
```

---

## 5. Type Conversion

```python
int("42")           # 42
int(3.9)            # 3  (truncates, no rounding)
float("3.14")       # 3.14
str(100)            # "100"
bool(0)             # False
bool("")            # False
bool("hello")       # True
bool(1)             # True
list("abc")         # ['a', 'b', 'c']
```

**Falsy values:** `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`, `False`  
**Everything else is truthy.**

---

## 6. Arithmetic & Operators

```python
# Arithmetic
5 + 3     # 8    addition
5 - 3     # 2    subtraction
5 * 3     # 15   multiplication
5 / 3     # 1.666...  true division (always float)
5 // 3    # 1    floor division (integer result)
5 % 3     # 2    modulo (remainder)
5 ** 3    # 125  exponentiation

# Augmented assignment
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x //= 5   # x = 4

# Comparison
==   !=   >   <   >=   <=

# Logical
and   or   not

# Identity & Membership
x is None           # identity check
x is not None
"a" in "abc"        # True
3 in [1, 2, 3]      # True
```

---

## 7. Conditional Logic (if/elif/else)

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

# Ternary / inline
status = "pass" if score >= 60 else "fail"

# Nested conditions
if x > 0:
    if x < 100:
        print("between 0 and 100")
```

---

## 8. Loops — for & while

```python
# for loop
for i in range(5):          # 0 1 2 3 4
    print(i)

for i in range(2, 10, 2):   # 2 4 6 8
    print(i)

# Looping over sequences
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):      # index + value
    print(i, fruit)

for a, b in zip([1,2,3], ["a","b","c"]): # pair two lists
    print(a, b)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # skip this iteration
    if i == 7:
        break       # exit loop
else:               # runs if loop completed without break
    print("done")
```

---

## 9. Lists

```python
nums = [3, 1, 4, 1, 5, 9]

# Access & slicing
nums[0]         # 3
nums[-1]        # 9
nums[1:4]       # [1, 4, 1]

# Modify
nums.append(2)              # add to end
nums.insert(2, 99)          # insert 99 at index 2
nums.extend([7, 8])         # add multiple items
nums.remove(1)              # remove FIRST occurrence of 1
popped = nums.pop()         # remove & return last item
nums.pop(0)                 # remove & return item at index 0
del nums[2]                 # delete by index
nums.clear()                # empty the list

# Info
len(nums)
nums.count(1)               # occurrences of 1
nums.index(5)               # index of first 5

# Sort
nums.sort()                 # in-place ascending
nums.sort(reverse=True)     # in-place descending
sorted(nums)                # returns new sorted list
nums.reverse()              # in-place reverse

# Copy
copy1 = nums.copy()         # shallow copy
copy2 = nums[:]             # also shallow copy
import copy
deep = copy.deepcopy(nums)  # deep copy (for nested lists)

# Useful
sum(nums)
min(nums)
max(nums)
3 in nums                   # True/False membership
```

---

## 10. Functions

```python
# Basic definition
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Default parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()             # Hello, World!
greet("Bob")        # Hello, Bob!

# Return values
def add(a, b):
    return a + b

result = add(3, 4)  # 7

# Multiple return values (tuple)
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])
```

---

# INTERMEDIATE (Days 16–40)

---

## 11. Return Values & Scope

```python
# Scope: LEGB — Local, Enclosing, Global, Built-in
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # "local"

    inner()
    print(x)        # "enclosing"

outer()
print(x)            # "global"

# global keyword
counter = 0
def increment():
    global counter
    counter += 1

# nonlocal keyword
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    return count
```

---

## 12. Dictionaries & Nesting

```python
person = {"name": "Alice", "age": 25, "city": "London"}

# Access
person["name"]              # "Alice"
person.get("age")           # 25
person.get("missing", 0)    # 0  (default if key missing)

# Modify
person["age"] = 26
person["email"] = "a@b.com"         # add new key
person.update({"age": 27, "job": "dev"})  # merge

# Delete
del person["city"]
person.pop("email")         # removes & returns value
person.popitem()            # removes & returns last (key, value)

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

person.keys()               # dict_keys view
person.values()             # dict_values view
person.items()              # dict_items view

# Check membership
"name" in person            # True (checks keys)

# Nested
school = {
    "students": {
        "alice": {"grade": "A", "age": 20},
        "bob":   {"grade": "B", "age": 21},
    }
}
school["students"]["alice"]["grade"]    # "A"
```

---

## 13. Tuples & Sets

```python
# Tuples — ordered, immutable
t = (1, 2, 3)
t[0]                    # 1
a, b, c = t             # unpacking
single = (42,)          # single-element tuple (comma required)
t.count(2)
t.index(3)

# Sets — unordered, unique items, mutable
s = {1, 2, 3, 3, 2}    # {1, 2, 3}
s.add(4)
s.remove(2)             # KeyError if missing
s.discard(99)           # no error if missing
s.pop()                 # remove arbitrary element

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
a | b                   # {1,2,3,4}  union
a & b                   # {2,3}      intersection
a - b                   # {1}        difference
a ^ b                   # {1,4}      symmetric difference
a.issubset(b)
a.issuperset(b)

# frozenset — immutable set
fs = frozenset([1, 2, 3])
```

---

## 14. List & Dict Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
flat    = [n for row in [[1,2],[3,4]] for n in row]  # [[1,2],[3,4]] → [1,2,3,4]

# Dict comprehension
squared = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}
inverted = {v: k for k, v in {"a":1, "b":2}.items()}

# Set comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}  # {0, 1, 4}

# Generator expression (lazy — does not build list in memory)
total = sum(x**2 for x in range(1000000))
```

---

## 15. Modules & Packages

```python
# Import
import math
math.sqrt(16)           # 4.0
math.pi                 # 3.14159...
math.floor(3.7)         # 3
math.ceil(3.2)          # 4

# Selective import
from math import sqrt, pi
sqrt(25)                # 5.0

# Alias
import numpy as np
from datetime import datetime as dt

# Standard library highlights
import random
random.randint(1, 10)           # random int 1–10 inclusive
random.choice(["a","b","c"])    # random element
random.shuffle(my_list)         # in-place shuffle
random.sample(my_list, 3)       # 3 unique random elements

import os
os.getcwd()                     # current working directory
os.listdir(".")                 # files in directory
os.path.exists("file.txt")      # True/False
os.path.join("folder", "file")  # cross-platform path

import sys
sys.argv                        # command-line args list
sys.exit()                      # exit script

# Own module — save as mymodule.py, then:
# from mymodule import my_function
```

---

## 16. Error Handling

```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Multiple exceptions
try:
    x = int(input())
    y = 10 / x
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Can't be zero")
except (TypeError, AttributeError) as e:
    print(f"Error: {e}")
except Exception as e:     # catch-all (use sparingly)
    print(f"Unexpected: {e}")
else:
    print("No error occurred")      # runs if no exception
finally:
    print("Always runs")            # cleanup code here

# Raising exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount):
        super().__init__(f"Need {amount} more funds")
        self.amount = amount
```

---

## 17. File I/O

```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.writelines(["line1\n", "line2\n"])

# Read
with open("file.txt", "r") as f:
    content = f.read()          # entire file as string
    
with open("file.txt") as f:
    lines = f.readlines()       # list of lines (with \n)

with open("file.txt") as f:
    for line in f:              # memory-efficient line iteration
        print(line.strip())

# Append
with open("file.txt", "a") as f:
    f.write("new line\n")

# File modes
# "r"  — read (default)
# "w"  — write (overwrites)
# "a"  — append
# "rb" — read binary
# "wb" — write binary
# "r+" — read and write

# Path handling (Python 3.4+)
from pathlib import Path

p = Path("folder/subfolder/file.txt")
p.exists()
p.stem          # "file"
p.suffix        # ".txt"
p.parent        # Path("folder/subfolder")
p.read_text()
p.write_text("hello")
list(Path(".").glob("*.txt"))   # all .txt in current dir
```

---

## 18. Classes & OOP

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"

    # Comparison dunder methods
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    # Class method — receives class, not instance
    @classmethod
    def from_birth_year(cls, name, year):
        from datetime import date
        age = date.today().year - year
        return cls(name, age)

    # Static method — no self or cls
    @staticmethod
    def is_puppy(age):
        return age < 2

    # Properties — controlled attribute access
    @property
    def info(self):
        return f"{self.name} is {self.age} years old"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value


# Usage
rex = Dog("Rex", 4)
rex.bark()                      # "Rex says Woof!"
str(rex)                        # "Dog(Rex, 4)"
Dog.is_puppy(1)                 # True
buddy = Dog.from_birth_year("Buddy", 2021)
```

---

## 19. Inheritance & Polymorphism

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Polymorphism
animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())       # each calls its own speak()

# super() — call parent method
class GoldenRetriever(Dog):
    def __init__(self, name, friendly=True):
        super().__init__(name)
        self.friendly = friendly

    def speak(self):
        base = super().speak()
        return base + " *wags tail*"

# Multiple inheritance
class Flyable:
    def fly(self):
        return "I can fly!"

class FlyingDog(Dog, Flyable):
    pass

# Check inheritance
isinstance(rex, Dog)        # True
isinstance(rex, Animal)     # True
issubclass(Dog, Animal)     # True

# Abstract base classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2
```

---

## 20. Decorators

```python
# Basic decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Before function
# Hello, Alice!
# After function

# Preserving metadata with functools
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Decorator with arguments
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()    # prints "Hi!" three times

# Common built-in decorators
@staticmethod   # no self or cls
@classmethod    # receives cls
@property       # getter/setter
```

---

# INTERMEDIATE+ (Days 41–60)

---

## 21. Lambda, Map, Filter, Reduce

```python
# Lambda — anonymous one-liner function
square = lambda x: x ** 2
add    = lambda x, y: x + y
square(5)       # 25

# map — apply function to every item
nums = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, nums))         # [1, 4, 9, 16, 25]
list(map(str, nums))                    # ['1','2','3','4','5']

# filter — keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))   # [2, 4]

# reduce — accumulate to single value
from functools import reduce
product = reduce(lambda x, y: x * y, nums)  # 120  (1*2*3*4*5)

# Prefer comprehensions for readability
squares = [x**2 for x in nums]             # same as map example
evens   = [x for x in nums if x % 2 == 0] # same as filter example

# sorted with key
words = ["banana", "apple", "cherry", "date"]
sorted(words, key=lambda w: len(w))        # sort by length
sorted(words, key=lambda w: w[-1])         # sort by last letter

people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted(people, key=lambda p: p["age"])
```

---

## 22. Iterators & Generators

```python
# Iterator protocol
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(5):
    print(n)    # 1 2 3 4 5

# Generator function — lazy, memory-efficient
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)    # 5 4 3 2 1

# Generator expression
gen = (x**2 for x in range(1000000))   # no list built in memory
next(gen)       # 0
next(gen)       # 1

# yield from — delegate to sub-generator
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1,2], [3,4], [5]))  # [1,2,3,4,5]

# itertools
import itertools

itertools.count(1)              # infinite: 1, 2, 3, ...
itertools.cycle("ABC")          # infinite: A, B, C, A, B, C, ...
itertools.repeat(5, 3)          # 5, 5, 5
itertools.chain([1,2], [3,4])   # 1, 2, 3, 4
itertools.islice(gen, 5)        # take first 5 from generator
itertools.product([1,2],[3,4])  # cartesian product
itertools.combinations("ABC", 2)
itertools.permutations("ABC", 2)
list(itertools.groupby([1,1,2,2,3], key=lambda x: x))
```

---

## 23. Regular Expressions

```python
import re

text = "Phone: 07911 123456, Email: alice@example.com"

# Search — first match
match = re.search(r"\d{5} \d{6}", text)
if match:
    print(match.group())    # "07911 123456"
    print(match.start())    # index
    print(match.end())

# Find all matches
emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)

# Match — only at start of string
re.match(r"Phone", text)    # match object or None

# Substitution
clean = re.sub(r"\d", "#", text)    # replace digits with #

# Split
re.split(r"[,\s]+", "one two,three")   # ['one','two','three']

# Compile for reuse
phone_pattern = re.compile(r"(\d{5})\s(\d{6})")
m = phone_pattern.search(text)
m.group(1)      # "07911"  (first capture group)
m.group(2)      # "123456"

# Flags
re.search(r"phone", text, re.IGNORECASE)
re.MULTILINE    # ^ and $ match line start/end
re.DOTALL       # . matches newline too

# Common patterns
r"\d"           # digit
r"\D"           # non-digit
r"\w"           # word char [a-zA-Z0-9_]
r"\W"           # non-word char
r"\s"           # whitespace
r"\S"           # non-whitespace
r"^"            # start of string
r"$"            # end of string
r"."            # any char except newline
r"[abc]"        # character class
r"[^abc]"       # negated class
r"a+"           # one or more
r"a*"           # zero or more
r"a?"           # zero or one
r"a{3}"         # exactly 3
r"a{2,5}"       # between 2 and 5
r"(abc)"        # capture group
r"(?:abc)"      # non-capturing group
r"a|b"          # a or b
```

---

## 24. args & kwargs

```python
# *args — variable positional arguments (tuple)
def add(*args):
    return sum(args)

add(1, 2, 3)        # 6
add(1, 2, 3, 4, 5)  # 15

# **kwargs — variable keyword arguments (dict)
def describe(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

describe(name="Alice", age=25, city="London")

# Combined
def func(required, *args, **kwargs):
    print(required, args, kwargs)

func("a", 1, 2, 3, x=10, y=20)
# "a" (1, 2, 3) {'x': 10, 'y': 20}

# Unpacking with * and **
nums = [1, 2, 3]
print(*nums)            # 1 2 3

def add(a, b, c):
    return a + b + c

add(*nums)              # 6

config = {"sep": "-", "end": "\n"}
print("a", "b", **config)  # a-b
```

---

## 25. Closures

```python
# A closure remembers variables from its enclosing scope
def make_multiplier(n):
    def multiplier(x):
        return x * n      # n is "closed over"
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # 10
triple(5)   # 15

# Practical: counter
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
c()     # 1
c()     # 2
c()     # 3
```

---

## 26. Datetime

```python
from datetime import datetime, date, timedelta

# Current time
now = datetime.now()
today = date.today()

# Create specific datetime
dt = datetime(2024, 12, 25, 10, 30, 0)

# Formatting
dt.strftime("%d/%m/%Y %H:%M")   # "25/12/2024 10:30"
dt.strftime("%A, %B %d %Y")     # "Wednesday, December 25 2024"

# Parsing string to datetime
dt = datetime.strptime("25/12/2024", "%d/%m/%Y")

# Common format codes
# %Y  4-digit year       %m  month 01-12   %d  day 01-31
# %H  hour 00-23         %M  minute 00-59  %S  second 00-59
# %A  weekday name       %B  month name    %p  AM/PM

# Arithmetic
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
diff = datetime(2025, 1, 1) - now
diff.days           # days until new year
diff.total_seconds()

# Attributes
now.year
now.month
now.day
now.hour
now.minute
now.weekday()   # 0=Monday, 6=Sunday
```

---

## 27. JSON & CSV

```python
import json

# Dict → JSON string
data = {"name": "Alice", "scores": [10, 20, 30]}
json_str = json.dumps(data, indent=2)
print(json_str)

# JSON string → Dict
parsed = json.loads(json_str)

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON file
with open("data.json") as f:
    data = json.load(f)

# ---

import csv

# Write CSV
rows = [["name","age"], ["Alice",25], ["Bob",30]]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader / DictWriter
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25})
```

---

## 28. Virtual Environments & pip

```bash
# Create venv
python -m venv venv

# Activate
source venv/bin/activate         # macOS/Linux
venv\Scripts\activate            # Windows

# Deactivate
deactivate

# Install packages
pip install requests
pip install flask==2.3.0         # specific version
pip install -r requirements.txt  # from file

# Manage packages
pip list                         # installed packages
pip show requests                # package details
pip freeze > requirements.txt    # save current env
pip uninstall requests

# pipenv (alternative)
pip install pipenv
pipenv install requests
pipenv shell
```

---

# EXPERIENCED / PRO (Days 61–100)

---

## 29. Type Hints

```python
# Basic annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

age: int = 25
scores: list[int] = [90, 85, 78]

# Complex types (Python 3.9+ can use built-ins directly)
from typing import Optional, Union, Any, Callable, TypeVar

def find(items: list[str], query: str) -> Optional[str]:
    return next((i for i in items if query in i), None)

def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+ shorthand for Optional/Union
def process(value: int | str | None) -> str:
    return str(value) if value is not None else ""

# Callable
def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

# TypeVar for generics
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]

# TypedDict
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

# Protocol (structural subtyping / duck typing)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...
```

---

## 30. Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
p.x             # 1.0
str(p)          # "Point(x=1.0, y=2.0)"
p == Point(1.0, 2.0)   # True (auto __eq__)

@dataclass
class Player:
    name: str
    score: int = 0                          # default value
    items: list[str] = field(default_factory=list)  # mutable default

@dataclass(frozen=True)    # immutable (hashable)
class Color:
    r: int
    g: int
    b: int

@dataclass(order=True)     # adds __lt__, __gt__, etc.
class Card:
    rank: int
    suit: str

# Post-init processing
@dataclass
class Circle:
    radius: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = 3.14159 * self.radius ** 2
```

---

## 31. Context Managers

```python
# Built-in context managers
with open("file.txt") as f:
    data = f.read()

# Multiple context managers
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

# Custom class-based context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        return False    # don't suppress exceptions

with Timer() as t:
    sum(range(1_000_000))
print(f"Elapsed: {t.elapsed:.3f}s")

# Generator-based with contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup")
    try:
        yield "resource"
    finally:
        print("Teardown")

with managed_resource() as r:
    print(f"Using {r}")

# suppress exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    open("missing.txt")     # silently ignored
```

---

## 32. Threading & Multiprocessing

```python
# Threading — good for I/O-bound tasks
import threading

def download(url):
    print(f"Downloading {url}")

threads = []
for url in ["a.com", "b.com", "c.com"]:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()    # wait for all to finish

# Thread with result (use Queue)
from queue import Queue

def worker(q, url):
    q.put(f"data from {url}")

q = Queue()
t = threading.Thread(target=worker, args=(q, "example.com"))
t.start()
t.join()
result = q.get()

# Multiprocessing — good for CPU-bound tasks (bypasses GIL)
from multiprocessing import Pool

def square(n):
    return n ** 2

with Pool(processes=4) as pool:
    results = pool.map(square, range(10))
print(results)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ThreadPoolExecutor / ProcessPoolExecutor (cleaner API)
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download, url) for url in urls]
    for future in as_completed(futures):
        print(future.result())
```

---

## 33. Async / Await

```python
import asyncio

# Basic coroutine
async def greet(name):
    await asyncio.sleep(1)      # non-blocking sleep
    print(f"Hello, {name}!")

asyncio.run(greet("Alice"))

# Running multiple coroutines concurrently
async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie"),
    )

asyncio.run(main())   # all three run concurrently

# Async iteration & context managers
async def fetch(url):
    async with aiohttp.ClientSession() as session:  # pip install aiohttp
        async with session.get(url) as response:
            return await response.text()

# Tasks
async def main():
    task1 = asyncio.create_task(greet("Alice"))
    task2 = asyncio.create_task(greet("Bob"))
    await task1
    await task2

# Async generator
async def count_up(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in count_up(5):
        print(num)

# asyncio.timeout (Python 3.11+)
async def main():
    async with asyncio.timeout(5.0):
        await long_running_task()
```

---

## 34. APIs & Requests

```python
import requests

# GET request
response = requests.get("https://api.example.com/users")
response.status_code        # 200
response.json()             # parse JSON body
response.text               # raw text
response.headers            # dict of headers
response.raise_for_status() # raises HTTPError if 4xx/5xx

# Query parameters
params = {"page": 1, "limit": 10, "search": "python"}
r = requests.get("https://api.example.com/posts", params=params)
# URL: .../posts?page=1&limit=10&search=python

# POST with JSON body
payload = {"title": "My Post", "body": "Content", "userId": 1}
r = requests.post("https://api.example.com/posts", json=payload)

# Headers (auth, content-type)
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json",
}
r = requests.get(url, headers=headers)

# API key in params
r = requests.get(url, params={"api_key": "YOUR_KEY"})

# Session (reuse connection, headers)
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer TOKEN"})
    r1 = session.get(url1)
    r2 = session.get(url2)

# Error handling
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## 35. Web Scraping (BeautifulSoup)

```python
import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, "html.parser")

# Finding elements
soup.title                          # <title> tag
soup.title.string                   # title text
soup.find("h1")                     # first <h1>
soup.find("div", class_="content")  # by class
soup.find("a", id="main-link")      # by id
soup.find_all("a")                  # all <a> tags (list)
soup.find_all("p", limit=5)         # first 5 <p>

# CSS selectors
soup.select("div.container > p")    # CSS selector
soup.select_one("h1.title")

# Extracting data
tag = soup.find("a")
tag.text            # visible text
tag.get_text(strip=True)
tag["href"]         # attribute value
tag.attrs           # all attributes as dict

# Navigate tree
tag.parent
tag.children        # generator of direct children
tag.descendants     # generator of all descendants
tag.next_sibling
tag.previous_sibling

# Practical scraping pattern
def scrape_articles(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.find_all("article"):
        title = item.find("h2").get_text(strip=True)
        link  = item.find("a")["href"]
        articles.append({"title": title, "link": link})
    return articles
```

---

## 36. Flask Basics

```python
# pip install flask
from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Basic route
@app.route("/")
def home():
    return "Hello, World!"

# Route with variable
@app.route("/user/<username>")
def profile(username):
    return f"Profile: {username}"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

# Methods
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        data = request.form.get("name")
        return redirect(url_for("home"))
    return render_template("submit.html")

# JSON API endpoint
@app.route("/api/users")
def users():
    return jsonify([{"id": 1, "name": "Alice"}])

# POST JSON
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify({"created": data}), 201

# Template rendering (templates/index.html)
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", name=name)

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Not found"), 404

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 37. SQLite & SQLAlchemy

```python
# SQLite — built-in
import sqlite3

conn = sqlite3.connect("mydb.db")       # creates file if not exist
conn = sqlite3.connect(":memory:")      # in-memory DB
conn.row_factory = sqlite3.Row          # rows as dict-like objects
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        email TEXT UNIQUE,
        age   INTEGER
    )
""")

cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
               ("Alice", "alice@example.com", 25))
conn.commit()

# Multiple rows
users = [("Bob", "bob@b.com", 30), ("Charlie", "c@c.com", 22)]
cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)
conn.commit()

cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
rows = cursor.fetchall()
for row in rows:
    print(row["name"], row["age"])  # dict-like if row_factory set

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
conn.close()

# Context manager
with sqlite3.connect("mydb.db") as conn:
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM users").fetchall()

# ---
# SQLAlchemy ORM — pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///mydb.db")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)
    email = Column(String, unique=True)
    age   = Column(Integer)

    def __repr__(self):
        return f"User(name={self.name!r})"

Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Alice", email="a@b.com", age=25))
    session.commit()

    users = session.query(User).filter(User.age > 20).all()
    alice = session.query(User).filter_by(name="Alice").first()
```

---

## 38. Testing with pytest

```python
# pip install pytest
# Run: pytest             (discovers test_*.py files)
#      pytest -v          (verbose)
#      pytest -k "login"  (run tests matching "login")
#      pytest --tb=short  (shorter tracebacks)

# Basic test
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test exceptions
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Parametrize
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixtures
@pytest.fixture
def sample_user():
    return {"name": "Alice", "age": 25}

def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

# Fixture with setup/teardown
@pytest.fixture
def db_connection():
    conn = create_test_db()     # setup
    yield conn                  # provide to test
    conn.close()                # teardown

# Mocking
from unittest.mock import MagicMock, patch

def test_api_call():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"status": "ok"}
        result = my_api_function()
        assert result == {"status": "ok"}
        mock_get.assert_called_once()
```

---

## 39. Useful Built-in Functions

```python
# Numeric
abs(-5)                 # 5
round(3.14159, 2)       # 3.14
divmod(17, 5)           # (3, 2)  — quotient and remainder
pow(2, 10)              # 1024
pow(2, 10, 1000)        # 1024 % 1000 = 24  (modular exponentiation)

# Sequences
len([1,2,3])            # 3
sum([1,2,3])            # 6
min([3,1,2])            # 1
max([3,1,2])            # 3
sorted([3,1,2])         # [1,2,3]
reversed([1,2,3])       # iterator
list(reversed([1,2,3])) # [3,2,1]
zip([1,2,3], "abc")     # pairs
enumerate(["a","b"])    # (0,"a"), (1,"b")
any([False, True, False])   # True
all([True, True, True])     # True

# Type inspection
type(42)                # <class 'int'>
isinstance(42, int)     # True
isinstance(42, (int, float))  # True
hasattr(obj, "method")
getattr(obj, "attr", default)
setattr(obj, "attr", value)
dir(obj)                # list of attributes/methods
vars(obj)               # __dict__

# Iteration helpers
range(5)                # 0..4
range(2, 10, 2)         # 2,4,6,8
map(str, [1,2,3])
filter(None, [0,"",1,2])  # [1,2] — filters falsy
zip([1,2], [3,4])       # (1,3),(2,4)
enumerate(lst)
iter([1,2,3])           # iterator
next(iterator)

# Misc
hash("hello")
id(obj)                 # memory address
callable(obj)           # True if callable
repr(obj)               # developer string
print(*[1,2,3], sep=",")
input("Enter: ")
open("file.txt")
```

---

## 40. Pythonic Patterns & Tips

```python
# ── Unpacking ──────────────────────────────────────────────
first, *rest = [1, 2, 3, 4, 5]     # first=1, rest=[2,3,4,5]
*init, last  = [1, 2, 3, 4, 5]     # last=5
a, b = b, a                         # swap in one line

# ── Walrus operator := (Python 3.8+) ──────────────────────
while chunk := f.read(8192):        # assign and test
    process(chunk)

if (n := len(data)) > 10:           # avoid calling len() twice
    print(f"Too long: {n}")

# ── Chained comparisons ────────────────────────────────────
0 < x < 100             # Pythonic
0 < x and x < 100       # redundant

# ── String tricks ──────────────────────────────────────────
" ".join(["Hello", "World"])        # "Hello World"
"#" * 40                            # "########..."
name = "  Alice  "
name.strip().lower().replace(" ","_")  # chainable

# ── dict tricks ────────────────────────────────────────────
merged = {**dict1, **dict2}         # merge dicts (Python 3.5+)
merged = dict1 | dict2              # merge dicts (Python 3.9+)
{k: v for k, v in d.items() if v}  # filter falsy values
d.setdefault("key", []).append(1)  # append without KeyError

# ── Collections module ─────────────────────────────────────
from collections import defaultdict, Counter, OrderedDict, deque, namedtuple

# defaultdict — missing keys get a default
dd = defaultdict(list)
dd["key"].append(1)     # no KeyError

# Counter — count occurrences
c = Counter("abracadabra")
c.most_common(3)        # [('a',5),('b',2),('r',2)]
Counter([1,1,2,3]) + Counter([1,2,2])   # combine counts

# deque — efficient queue/stack
dq = deque([1,2,3], maxlen=5)
dq.appendleft(0)
dq.popleft()
dq.rotate(2)            # rotate right by 2

# namedtuple — lightweight, immutable record
Point = namedtuple("Point", ["x", "y"])
p = Point(1.0, 2.0)
p.x     # 1.0
p._asdict()

# ── heapq — priority queue ─────────────────────────────────
import heapq
heap = [5, 3, 1, 4, 2]
heapq.heapify(heap)     # convert list to min-heap in place
heapq.heappush(heap, 0)
smallest = heapq.heappop(heap)  # 0
heapq.nlargest(3, heap)
heapq.nsmallest(3, heap)

# ── Useful one-liners ──────────────────────────────────────
# Flatten nested list
flat = [x for row in matrix for x in row]

# Transpose matrix
transposed = list(zip(*matrix))

# Remove duplicates preserving order
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]

# Group by key
from itertools import groupby
data = sorted(data, key=lambda x: x["category"])
groups = {k: list(v) for k, v in groupby(data, key=lambda x: x["category"])}

# Safe dictionary access chain
value = data.get("user", {}).get("address", {}).get("city", "Unknown")

# ── Performance tips ───────────────────────────────────────
# Use local variable lookups inside tight loops (faster than global)
# Use generators over large lists to save memory
# Use sets for O(1) membership tests instead of lists O(n)
# Use str.join() instead of += for string concatenation in loops
# Profile with: python -m cProfile script.py
# Time snippets with: from timeit import timeit; timeit("x*x", setup="x=5", number=1_000_000)

# ── Environment variables ──────────────────────────────────
import os
api_key = os.environ.get("API_KEY", "default_value")
os.environ["MY_VAR"] = "hello"

# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()   # loads .env file into os.environ

# ── Logging ────────────────────────────────────────────────
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("Verbose detail")
logging.info("General info")
logging.warning("Something unexpected")
logging.error("Something failed")
logging.critical("System failure")
```

---

## Quick Reference Card

| Concept | Syntax |
|---|---|
| f-string | `f"Hello {name!r}"` |
| List comp | `[x*2 for x in lst if x > 0]` |
| Dict comp | `{k: v for k,v in items}` |
| Generator | `(x**2 for x in range(n))` |
| Lambda | `lambda x, y: x + y` |
| Unpack | `a, *rest = lst` |
| Walrus | `if n := len(data) > 10` |
| Ternary | `x if condition else y` |
| Swap | `a, b = b, a` |
| Merge dicts | `{**d1, **d2}` or `d1 \| d2` |
| Flatten | `[x for row in grid for x in row]` |
| Null check | `value = x if x is not None else default` |
| Type hint | `def f(x: int) -> str:` |
| Dataclass | `@dataclass` |
| Context mgr | `with open("f") as f:` |
| Decorator | `@my_decorator` |

---

*Happy coding! 🐍 — Built for 100 Days of Code Python Bootcamp learners*
