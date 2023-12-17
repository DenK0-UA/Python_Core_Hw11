from datetime import datetime, timedelta

class Record:
    def __init__(self, value, birthday=None):
        self.value = value
        self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday is None:
            return None

        today = datetime.now().date()
        next_birthday = datetime(today.year, self.birthday.month, self.birthday.day).date()

        if next_birthday < today:
            next_birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day).date()

        return (next_birthday - today).days

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday):
        if new_birthday is None:
            self._birthday = None
        elif isinstance(new_birthday, datetime):
            self._birthday = new_birthday.date()
        else:
            raise ValueError("Birthday must be a datetime object")

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, n):
        for i in range(0, len(self.records), n):
            yield self.records[i:i+n]
