import random as rd
from  models import hunter
x_max = 500
y_max = 500
area = (x_max, y_max)
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
                        #print(self.male)
                    else:
                        self.female += 1
                        #print(self.female)
    def hunter_hunting(self):
        while True:
            try:
                for m, f in zip(range(self.female), range(self.male)):
                    if abs(hunter.Hunter.location[0][0] - self.location_female[m][0]) <= hunter.Hunter.hunt or \
                            abs(hunter.Hunter.location[0][1] -self.location_female[m][1]) <= hunter.Hunter.hunt:
                        self.female -= 1
                        if self.female == 0:
                            break
                    elif abs(hunter.Hunter.location[0][0] - self.location_male[f][0]) <= hunter.Hunter.hunt or \
                            abs(hunter.Hunter.location[0][1] - self.location_male[f][1]) <= hunter.Hunter.hunt:
                        self.male -= 1
                        if self.male == 0:
                            break
                return print(self.male,self.female)
            except(IndexError):
                pass

#hareketlerin fonsiyonlarının tanımlanması
def right_left(locations, move) :
    for index in range(locations.__len__()):
        if locations[index][0] <= area[0]:
            locations[index][0] += move
        else :
            locations[index][0] -= move
    return  locations
def forward_backward(locations, move) :
    for index in range(locations.__len__()):
        if locations[index][1] <= area[0]:
            locations[index][1] += move
        else :
            locations[index][1] -= move
    return  locations

class sheep (Animal_Attributes):
    pass
class cow (Animal_Attributes):
    pass
class lion (Animal_Attributes):
    def __init__(self, male, female, location_male, location_female,hunt_lenght):
        Animal_Attributes.__init__(self, male, female, location_male, location_female)
        self.hunt_lenght =hunt_lenght
class wolf (Animal_Attributes):
    def __init__(self, male, female, location_male, location_female,hunt_lenght):
        Animal_Attributes.__init__(self, male, female, location_male, location_female)
        self.hunt_lenght =hunt_lenght
class chicken_rooster (Animal_Attributes):
    pass

