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
                return "dead"
            else:
                self.status = "recovered"
                return "recovered"
        return None


def probability_of_contact(person_1, person_2):
    if person_1.location == person_2.location:
        return 1
    return 0


def initialise_random_people(names):
    people = []
    for name in names:
        age = random.randint(0, 99)
        location = (round(random.random(), 1), round(random.random(), 1))
        person = Person(name, age, location)
        people.append(person)
    return tuple(people)


def initialise_random_infected(people):
    infected_person = random.choice(people)
    infected_person.set_status("infected")


def run_simulation(people):
    day = 0
    while any(person.status == "infected" for person in people):
        print(f"Day {day}:")
        new_deaths = 0
        new_recoveries = 0

        for i in range(len(people)):
            if people[i].status == "infected":
                people[i].decrement_infectious_period()
                if people[i].infectious_period == 0:
                    result = people[i].rand_set_removed()
                    if result == "dead":
                        new_deaths += 1
                    elif result == "recovered":
                        new_recoveries += 1

            for j in range(i + 1, len(people)):
                if people[i].status == "infected" and people[j].status == "susceptible":
                    if probability_of_contact(people[i], people[j]) == 1:
                        if random.random() <= 0.2:
                            people[j].set_status("infected")

        for person in people:
            print(
                f"  {person.name}: {person.status}, Age: {person.age}, Location: {person.location}, Infectious period left: {person.infectious_period}")

        print(f"  New deaths today: {new_deaths}")
        print(f"  New recoveries today: {new_recoveries}")
        print("-" * 40)

        day += 1

    return


# test
names = ["A", "B", "C", "D", "E"]
people = initialise_random_people(names)
initialise_random_infected(people)

run_simulation(people)
