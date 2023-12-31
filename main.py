from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits and contain only numbers")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value=None):
        if value is not None:
            value = self._validate_birthday(value)
        super().__init__(value)

    def _validate_birthday(self, value):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(
                "Invalid birthday format. Please use the format 'YYYY-MM-DD'")

    @Field.value.setter
    def value(self, new_value):
        if new_value is not None:
            self.__value = self._validate_birthday(new_value)


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break
        else:
            raise ValueError("Phone number does not exist")

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
        else:
            raise ValueError("Phone number does not exist")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def days_to_birthday(self):
        if self.birthday.value is None:
            return None
        today = datetime.today().date()
        next_birthday = datetime(
            today.year, self.birthday.value.month, self.birthday.value.day).date()
        if next_birthday < today:
            next_birthday = datetime(
                today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
        return (next_birthday - today).days

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __iter__(self):
        return self.iterator()

    def iterator(self, N=1):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield [str(record) for record in records[i:i+N]]
