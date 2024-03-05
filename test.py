#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

import sys
from functools import reduce

print(sys.version_info)
print(sys.version)

'''
import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
'''

# name = input('please enter your name: ')

# print('name:','\n'+name)
print(r'''line1,
line2,
line3''')

print(11//3)
print('\u4e2d\u6587')
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
s[2][1]


# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


s={1,2,3,4,5,6,7,8,9,10}
s.add((1, 2, 3))
# s.add([2, 3])
print(s)

print(math.pi)


abs(100)


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,'dddd   ', y)




def quadratic(a, b, c):
    sqrtValue = math.sqrt(b ** 2 - 4 * a * c)
    if sqrtValue > 0:
        x1 = (-b + sqrtValue) / (2 * a)
        x2 = (-b - sqrtValue) / (2 * a)
        return x1, x2
    elif sqrtValue == 0:
        x1 = (-b + sqrtValue) / (2 * a)
        return x1
    else:
        return None

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))



def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, city='Beijing',job='Engineer')


def mul(*x):
    mulv=1
    if len(x) == 0:
        raise TypeError('no input')
    for i in x:
        mulv=mulv*i

    return mulv

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(list(map(char2num, '13579')))


def normalize(name):
    def lowerstr(str):
        return str.lower()
    def upperstrFirst(str):
        return str[0].upper() + str[1:]

    return map(upperstrFirst,map(lowerstr, name))

print(list(normalize(['adam', 'LISA', 'barT'])))
# print(list(normalize()))

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(self,animal):
        animal.run()
        animal.run()

class Rob(object):
    def run(self):
        print('Rob is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(Animal,Rob):
    # pass
    def run(self):
        Rob.run(self)
        print('Timer is running...')

t=Tortoise()
t.run()
time=Timer()
t.run_twice(Timer())
time.run()

print(dir(object))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')