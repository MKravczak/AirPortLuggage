import Luggage
import random
import numpy
from random import choices

names = ["John", "Jane", "Jack", "Jill", "James", "Jenny", "Jasper", "Jasmine", "Jared", "Jade"]
surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
types= ["suitcase","hiking bag","backpack"]
departures = ["New York", "Lodon", "Paris", "Berlin", "Tokyo", "Beijing", "Moscow", "Sydney", "Cairo", "Rio de Janeiro"]
baggages = []

for i in range(1,11):
    baggage = Luggage.Luggage(i,random.choice(names),random.choice(surnames),round(random.uniform(8,20),2), random.choice(departures), str((numpy.random.choice(types, 1, p=[0.7, 0.2, 0.1])[0])))
    print(baggage)
    baggages.append(baggage)



