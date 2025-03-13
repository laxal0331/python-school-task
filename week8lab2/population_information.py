import random
from math import exp, sqrt
from simulation_classes import Person

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

def initialise_random_contact_info(people):
    is_close_contact = []
    for i in range(len(people)):
        is_close_contact.append([False]*len(people))
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            prob = random.random()
            prob_of_contact = probability_of_contact(people[i], people[j])
            if prob <= prob_of_contact:
                is_close_contact[i][j] = True
                is_close_contact[j][i] = True
            else:
                is_close_contact[i][j] = False
                is_close_contact[j][i] = False

    return is_close_contact

def initialise_random_infected(people):
    infected_person = random.choice(people)
    infected_person.set_status('infected')