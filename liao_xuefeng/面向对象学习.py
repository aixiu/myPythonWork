
#!/usr/bin/env python
# -*- coding: utf-8 -*-

std1 = {'name': 'Michael', 'score': 98}
std1 = {'name': 'Bob', 'score': 81}

def print_score(std):
    print('%s: %s' %(std['name'], std['score']))


print_score(std1)


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

print(isinstance(dog, Animal))