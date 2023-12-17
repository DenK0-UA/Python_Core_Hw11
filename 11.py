from datetime import datetime, timedelta


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
        if not isinstance(new_value, str):
            raise ValueError("Phone number must be a string")
        if not new_value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self._value = new_value


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        if new_value is not None:
            try:
                datetime.strptime(new_value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(
                    "Invalid birthday format. Use YYYY-MM-DD or leave it empty.")
        self._value = new_value


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value is None:
            return None
        today = datetime.today().date()
        next_birthday = datetime.strptime(
            self.birthday.value, "%Y-%m-%d").date().replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days


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
