import math
print("Hello World ")
print("*" * 10)

x = 1
print("hello")

# variable declare and data type
x = 1
student_count = 1000
rating = 4.9
is_publishedh = False
course_name = "English"

# multiple line in a sigle variable
course_material = """
    syllabal
    noun
    pronoun
    article
"""

# value assign in variable
x = 1
y = 2

x, y = 1, 2
# like other programming language
x = y = z = 10

print(course_material)
print(z, y, z)
print(type(z))

# python is a dynamic language as it doesn't need to declare it's varriable type
student = "kausar"
roll = 5
status = True
# type annotation from python 3.6
age = 10
age = "hello variable"
print(age)

# function return memory location

k = 3
print(id(k))

k = k+1
print(id(k))

course = "Python Programming"

print(course[1:3])

print(id(course[0]))

print(id(course[1]))

message = 'python "programming" '
print(message)
backSlash = "python \"programming "
print(backSlash)

lineEscape = """
    Python
    this
    is new
    line break
"""
print(lineEscape)

lineBreak = "hello \nPython"
print(lineBreak)

first = "mahabububr"
last = "rahman"

full = first + " " + last

print(full)

full = f"{len(first)} { (2+7)}"

print(full)

print(course.lower())
print(course.upper())
print(course.title())

print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "-"))
print("Programming" in course)
print("Programming" not in course)


# numbers

# to convert in binary
# 0b is the short form of binary
y = 0b10
print(y)
# convert through function
x = 10
print(bin(x))

#convert in hexa

x = 0x12c
print(hex(x))

# imaginary number in math with python

a = 2 + 5j
print(a)

# arithmetic operator

a = 10 + 3
b = 10 - 3
c = 10 * 2
d = 10 / 3
e = 10 // 3
f = 10 ** 3
print(e)

# augmented operator
x = 50
x = x + 1
x += 1
print(x)

# there is no constant in python. all are variable. Use Upper Case to make undersatand
# this variable is used as constant

PI = 3.14

print(round(PI))

print(abs(PI))

print(math.floor(PI))

m = input(" x: ")
n = input(" y: ")

print(int(m) + int(n))

print(int(m))
print(float(m))
print(bool(m))

# Falsy values in python
# ""
# 0
# []
# None (null in other language)


myAge = 17
if myAge >= 18:
    print("adult")
elif myAge <= 17:
    print("Child")

# operator

name = ""
if not name:
    print("Name is empty")


name = ""
if not name.strip():
    print("Name is empty")
