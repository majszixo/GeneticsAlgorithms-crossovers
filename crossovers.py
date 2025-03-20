import numpy
import matplotlib
import random

class Animal:
    def __init__(self, species, offspring, survivalRate, categoryA, categoryBplus, categoryB, categoryC):
        self.offspring = offspring
        self.survivalRate = survivalRate
        self.categoryA = categoryA
        self.categoryBplus = categoryBplus
        self.categoryB = categoryB
        self.categoryC = categoryC
        self.fitness = self.evaluateFitness()

    def evaluateFitness(self):
        return self.offspring * (self.survivalrate / 100) * (self.categoryA + self.categoryBplus + self.categoryB + self.categoryC) / 100
    
    def __repr__(self):
        return f"{self.species}: offspring = {self.offspring}, survival rate = {self.survival_rate}%, fitness = {self.fitness:.2f}"

def onePointCrossover(parent_1, parent_2):
    randomPointCrossover = random.randint(1,6)
    parent_1_attrs = [parent_1.offspring, parent_1.survivalRate, parent_1.categoryA, parent_1.categoryBplus, parent_1.categoryB, parent_1.categoryC]
    parent_2_attrs = [parent_2.offspring, parent_2.survivalRate, parent_2.categoryA, parent_2.categoryBplus, parent_2.categoryB, parent_2.categoryC]

    new_attributes = parent_1_attrs[:randomPointCrossover] + parent_2_attrs[randomPointCrossover:]
    return Animal(parent_1.species, *new_attributes)

    

