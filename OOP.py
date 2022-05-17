# Object Oriented Programming

class Employee:
    __name = Akash
    __id = 192
    __Salary = 1000

    def __init__(self,name,id,salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

     def set_name(self, name):
         self.__name = name
     def get_name(self):
        return self.__name
    def set_name(self, id):
         self.__id = id
     def get_name(self):
        return self.__id

akash = Employee()
akash.set_name('akash')
print(akash.get_name())

akash = Employee('harry',420,700000000)

print(harry.get_salary())