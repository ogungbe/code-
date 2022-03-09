#!/usr/bin/env python3

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'

class ContactList(object):
    def __init__(self, d=None):
        if d is None:
           self.d = {}

    def add(self, other):
        self.d[other.name] = other

    def remove(self, name):
        if name in self.d:
            try:
                del self.d[name]
            except KeyError:
                return

    def __str__(self):
        mylist = []
        for k, v in self.d.items():
            mylist.append(f'{v.name} {v.phone} {v.email}')
        output = '\n'.join(sorted(mylist))
        return f'Contact list\n------------\n{output}'

    def get(self, name):
        try:
            return self.d[name]
        except KeyError:
            return
