from datetime import datetime

class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        if self._is_valid_phone(new_value):
            self._value = new_value
        else:
            raise ValueError("Invalid phone number")

    def _is_valid_phone(self, phone):
        return True


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        if self._is_valid_birthday(new_value):
            self._value = new_value
        else:
            raise ValueError("Invalid birthday")

    def _is_valid_birthday(self, birthday):
        return True


class Record:
    def __init__(self, phone=None, birthday=None):
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            return (next_birthday - today).days
        else:
            return None


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def iterator(self, n):
        for i in range(0, len(self.records), n):
            yield self.records[i:i+n]


