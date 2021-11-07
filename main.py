from models.hunter import Hunter
from  models.animal import *

hunter = Hunter()
sheeps =sheep(female=15, male=15, location_male=[], location_female=[])
cows = cow(female=15, male=15, location_male=[], location_female=[])
wolfs = wolf(female=5, male=5, location_male=[], location_female=[],hunt_lenght=5)
lions = lion(female=4, male=4, location_male=[], location_female=[],hunt_lenght=4)
chickens_roosters = chicken_rooster(female=10, male=10, location_male=[], location_female=[])
# random belirtilen alanda konumlandırma
sheeps.creation_location()
cows.creation_location()
lions.creation_location()
wolfs.creation_location()
chickens_roosters.creation_location()
#Üreme
sheeps.reproduction()
cows.reproduction()
lions.reproduction()
wolfs.reproduction()
chickens_roosters.reproduction()
#Avlanma-Insan
"""sheeps.hunter_hunting()
sheeps.hunter_hunting()
cows.hunter_hunting()
lions.hunter_hunting()
wolfs.hunter_hunting()
chickens_roosters.hunter_hunting()"""
#Avlanma-aslan

for m,f in zip (range(lions.female),range(lions.male)):
    for j,k in zip(range(cows.female),range(cows.male)):
        if abs(lions.location_female[m][0] - cows.location_female[j][0]) <= lions.hunt_lenght or \
            abs(lions.location_female[m][1] - cows.location_female[j][1]) <= lions.hunt_lenght:
            cows.female -= 1
            if cows.female == 0:
                break
        elif abs(lions.location_male[m][0] - cows.location_male[j][0]) <= lions.hunt_lenght or \
            abs(lions.location_male[m][1] - cows.location_male[j][1]) <= lions.hunt_lenght:
            cows.male -= 1
            if cows.male == 0:
                break
        elif abs(lions.location_male[m][0] - cows.location_female[j][0]) <= lions.hunt_lenght or \
            abs(lions.location_male[m][1] - cows.location_female[j][1]) <= lions.hunt_lenght:
            cows.female -= 1
            if cows.female == 0:
                break
        elif abs(lions.location_female[m][0] - cows.location_male[j][0]) <= lions.hunt_lenght or \
            abs(lions.location_female[m][1] - cows.location_male[j][1]) <= lions.hunt_lenght:
            cows.male -= 1
            if cows.male == 0:
                break
print(cows.male,cows.female)
#hareketler
right_left(locations=hunter.location, move=hunter.move)
right_left(locations=sheeps.location_male, move=2)
right_left(locations=sheeps.location_female, move=2)
right_left(locations=cows.location_male, move=2)
right_left(locations=cows.location_female, move=2)
right_left(locations=wolfs.location_male, move=3)
right_left(locations=wolfs.location_female, move=3)
right_left(locations=lions.location_male, move=4)
right_left(locations=lions.location_female, move=4)
right_left(locations=chickens_roosters.location_male, move=1)
right_left(locations=chickens_roosters.location_female, move=1)

forward_backward(locations=hunter.location, move=hunter.move)
forward_backward(locations=sheeps.location_male, move=2)
forward_backward(locations=sheeps.location_female, move=2)
forward_backward(locations=cows.location_male, move=2)
forward_backward(locations=cows.location_female, move=2)
forward_backward(locations=wolfs.location_male, move=3)
forward_backward(locations=wolfs.location_female, move=3)
forward_backward(locations=lions.location_male, move=4)
forward_backward(locations=lions.location_female, move=4)
forward_backward(locations=chickens_roosters.location_male, move=1)
forward_backward(locations=chickens_roosters.location_female, move=1)


