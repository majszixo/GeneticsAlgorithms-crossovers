import numpy
import matplotlib
import random

class Animal:
    def __init__(self, species, offspring, survivalRate, categoryA, categoryBplus, categoryB, categoryC):
        self.species = species
        self.offspring = offspring
        self.survivalRate = survivalRate
        self.categoryA = categoryA
        self.categoryBplus = categoryBplus
        self.categoryB = categoryB
        self.categoryC = categoryC
        self.fitness = self.evaluateFitness()

    def evaluateFitness(self):
        return self.offspring * (self.survivalRate / 100) * (self.categoryA + self.categoryBplus + self.categoryB + self.categoryC) / 100
    
    def __repr__(self):
        return f"{self.species}: offspring = {self.offspring}, survival rate = {self.survivalRate}%, fitness = {self.fitness:.2f}"

def onePointCrossover(parent_1, parent_2):
    randomPointCrossover = random.randint(1,6)
    parent_1_attrs = [parent_1.offspring, parent_1.survivalRate, parent_1.categoryA, parent_1.categoryBplus, parent_1.categoryB, parent_1.categoryC]
    parent_2_attrs = [parent_2.offspring, parent_2.survivalRate, parent_2.categoryA, parent_2.categoryBplus, parent_2.categoryB, parent_2.categoryC]

    new_attributes = parent_1_attrs[:randomPointCrossover] + parent_2_attrs[randomPointCrossover:]
    return Animal(parent_1.species, *new_attributes)

def kPointCrossover(parent_1, parent_2, k):
    points = sorted(random.sample(range(1, 6), k))
    attrs = ["offspring", "survivalRate", "categoryA", "categoryBplus", "categoryB", "categoryC"]
    useParent_1 = True
    new_attributes = []
    for i in range(0,6):
        if i in points:
            useParent_1 = not useParent_1
        attr_value = getattr(parent_1 if useParent_1 else parent_2, attrs[i])
        new_attributes.append(attr_value)

    return Animal(parent_1.species, *new_attributes)

def shuffleCrossover(parent_1, parent_2):
    attrs = ["offspring", "survivalRate", "categoryA", "categoryBplus", "categoryB", "categoryC"]
    shuffled = random.sample(attrs, len(attrs))
    new_attributes = [getattr(parent_1, attr) if random.random() < 0.5 else getattr(parent_2, attr) for attr in shuffled]
    return Animal(parent_1.species, *new_attributes)

def reducedSurrogate(parent_1, parent_2):
    new_attributes = [getattr(parent_1, attr) if getattr(parent_1, attr) == getattr(parent_2, attr) else getattr(parent_2, attr) 
                       for attr in ["offspring", "survivalRate", "categoryA", "categoryBplus", "categoryB", "categoryC"] ]

    return Animal(parent_1.species, *new_attributes)
    

