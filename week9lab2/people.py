from abc import ABC, abstractmethod
class Person(ABC):
    all_statuses = ['domestic', 'international']

    def __init__(self, name, ID, status):
        self.name = name
        self.ID = ID
        self.status = status

    @abstractmethod
    def verify_id(self):
        pass

    def verify_status(self):
        if self.status in Person.all_statuses:
            return True
        return False


class Student(Person):
    def __init__(self, name, ID, status, units_completed, units_enrolled):
        super().__init__(name, ID, status)
        self.units_completed = units_completed
        self.units_enrolled = units_enrolled

    def verify_id(self):
        return self.ID % 7 == 0

    def is_enrolled(self):
        return len(self.units_enrolled) > 0

    def is_ready_to_graduate(self):
        return len(self.units_completed) >= 4


class Academic(Person):
    def __init__(self, name, ID, status, units_taught):
        super().__init__(name, ID, status)
        self.units_taught = units_taught

    def verify_id(self):
        return self.ID % 11 == 0

    def is_teaching(self, unit):
        return unit in self.units_taught
