import random
class Person:
    death_probabilities = [
        0.0000236,
        0.00000581,
        0.0000279,
        0.000120,
        0.000297,
        0.00106,
        0.00377,
        0.0166,
        0.0639,
        0.140
    ]

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.status = "susceptible"
        self.location = location
        self.infectious_period = 0

    def set_status(self, status):
        self.status = status
        if status == "infected":
            self.infectious_period = random.randint(3, 15)

    def decrement_infectious_period(self):
        if self.infectious_period > 0:
            self.infectious_period -= 1

    def rand_set_removed(self):
        if self.status == "infected":
            age_bracket = self.age // 10
            death_probability = Person.death_probabilities[age_bracket]
            if random.random() < death_probability:
                self.status = "dead"
            else:
                self.status = "recovered"

