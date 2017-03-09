#!/usr/bin/python3

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else: 
            current = self.head
            while current.next: 
                 current = current.next
            current.next = node


mylist = LinkedList()
T = int(input())

for i in range(T):
    data=int(input())
    mylist.insert(data)
mylist.display()
