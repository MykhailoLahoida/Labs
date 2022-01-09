"""
Create a class NOTEBOOK, which contains the name, surname, number phone and birthday of person. Define methods of access to these fields and overload operations:
"+" - for adding a new element;
"-" - for deleting an element;
"*" - for searching for an element in the Notebook on one of the data fields.
"""
import datetime
class Note:
    def __init__(self, name, surname, phone, birthday):
        if not isinstance(name, str):
            raise TypeError("Name is a string")
        elif not isinstance(surname, str):
            raise TypeError("Surname is a string")
        elif not isinstance(phone, str):
            raise TypeError("Phone is a string")
        elif not isinstance(birthday, datetime.datetime):
            raise TypeError("The date is a datetime.datetime value")
        elif (datetime.datetime.now() - birthday).days < 0:
            raise ValueError("You are from future?")
        else:
            self.__name = name
            self.__surname = surname
            self.__phone = phone
            self.__birthday = birthday

    @property
    def printer(self):
        return 'Name: ' + self.name + ', Surname: ' + self.surname + ', Phone: ' + self.phone\
               + ', Birthday: ' + str(self.birthday)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    @property
    def birthday(self):
        return self.__birthday

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is a string")
        else:
            self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname is a string")
        else:
            self.__surname = surname

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone is a string")
        self.__phone = phone

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, datetime.datetime):
            raise TypeError("The date is a datetime.datetime value")
        elif (datetime.datetime.now() - birthday).days < 0:
            raise ValueError("You are from future?")
        self.__birthday = birthday

class Notebook:
    def __init__(self):
        self.notes = []

    def __add__(self, other):
        if not isinstance(other, Note):
            raise TypeError("The notes must be instance of class 'Note'!")
        self.notes.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Index must is a integer number")
        if other < 0:
            raise TypeError("Index is not negative")
        self.notes.pop(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError("Searching data is a string")
        for info in self.notes:
            if info.name == other or info.surname == other or info.phone == other or info.birthday == other:
                return self.notes[self.notes.index(info)]

        return None

    @property
    def show(self):
        final = []
        for i in range(len(self.notes)):
            final.append(self.notes[i].printer)
        return final

if __name__ == "__main__":
    Misha = Note("Mykhailo", "Lahoida", "+380998888898", datetime.datetime(2003, 7, 9))
    Vasyl = Note("Vasyl", "Pupkin", "380999999999", datetime.datetime(2000, 1, 1))
    Ivan = Note("Ivan", "Ivanov", "380399999999", datetime.datetime(1999, 1, 1))
    Copybook = Notebook()
    Copybook += Misha
    Copybook += Vasyl
    Copybook += Ivan
    for i in range(len(Copybook.show)):
        print(Copybook.show[i])
    print('\n')
    Copybook -= 1
    for i in range(len(Copybook.show)):
        print(Copybook.show[i])
    print('\n')
    Search = "Ivanov"
    Copybook *= Search
    print('Find: ', Copybook.printer)

