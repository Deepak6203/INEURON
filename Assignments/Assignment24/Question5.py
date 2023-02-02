# 5. Write a python program to delete the age property of the user.


from pprint import pprint
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('name cannot be empty')
        self._name = value

    @name.deleter
    def name(self):
        del self._name

# # pprint(Person.__dict__)
# person = Person('Deepaks')
# pprint(person.__dict__)   #{'_name': 'Deepaks'}

person = Person('Deepaks')
del person.name  #{}

print(person.name)  #AttributeError: 'Person' object has no attribute '_name'. Did you mean: 'name'?