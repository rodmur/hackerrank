#!/usr/bin/python3

import operator

class Student(object):
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
     
    def __str__(self):
        return '%s has marks %s' %(self.name, self.marks)

students = [ Student(0, 'Foo', 30), Student(1, 'Bar', 95), Student(2, 'Baz', 80)]
 
best_student = max(students, key=operator.attrgetter('marks')) # don't forget the quotes
print(best_student)
