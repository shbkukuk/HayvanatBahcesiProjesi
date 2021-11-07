import random as rd
x_max = 500
y_max = 500
alan = (x_max,y_max)
class Animal_Attributes():
    reproduction_lenght = 3
    def __init__(self, male, female, location_male, location_female):
        self.male = male
        self.female = female
        self.location_male = location_male
        self.location_female = location_female

    def creation_location(self):
        for gender in "male", "female":
            if gender == "male":
                for i in range(0, (self.male)):
                    self.location_male.append([rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])
            elif gender == "female":
                for i in range(0, (self.female)):
                    self.location_female.append([rd.randrange(0, 500, 1), rd.randrange(0, 500, 1)])

    def reproduction(self):
        for i in range(self.location_female.__len__()):
            for j in range(self.location_male.__len__()):
                if abs(self.location_female[i][0] - self.location_male[j][0]) == self.reproduction_lenght or \
                        abs(self.location_female[i][0] - self.location_male[j][0]) == self.reproduction_lenght:
                    gender = rd.choice(["male", "female"])
                    if gender == "male":
                        self.male += 1
                        print(self.male)
                    else:
                        self.female += 1
                        print(self.female)

#hareketlerin fonsiyonlarının tanımlanması
def sagsol(locations, move) :
    for index in range(locations.__len__()):
        if locations[index][0] <= alan[0]:
            locations[index][0] += move
        else :
            locations[index][0] -= move
    return  locations
def ileriasagi(locations, move) :
    for index in range(locations.__len__()):
        if locations[index][1] <= alan[0]:
            locations[index][1] += move
        else :
            locations[index][1] -= move
    return  locations

def hunting():
    pass
class sheep (Animal_Attributes):
    pass
class cow (Animal_Attributes):
    pass
class lion (Animal_Attributes):
    pass
class wolf (Animal_Attributes):
    pass
class chicken_rooster (Animal_Attributes):
    pass

