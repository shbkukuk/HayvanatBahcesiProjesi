from models.hunter import Hunter
from  models.animal import *

hunter = Hunter()

sheeps =sheep(female=15, male=15, location_male=[], location_female=[])
cows = cow(female=15, male=15, location_male=[], location_female=[])
wolfs = wolf(female=5, male=5, location_male=[], location_female=[],hunt_lenght=5)
lions = lion(female=4, male=4, location_male=[], location_female=[],hunt_lenght=4)
chickens_roosters = chicken_rooster(female=15, male=15, location_male=[], location_female=[])
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
#Avlanma
for m, f in zip(range(sheeps.female), range(sheeps.male)):
    if abs(hunter.location[0][0] - sheeps.location_female[m][0]) <= hunter.hunt or \
            abs(hunter.location[0][1] - sheeps.location_female[m][1]) <= hunter.hunt:
        sheeps.female -= 1
        if sheeps.female == 0:
            break
    elif abs(hunter.location[0][0] - sheeps.location_male[f][0]) <= hunter.hunt or \
            abs(hunter.location[0][1] - sheeps.location_male[f][1]) <= hunter.hunt:
        sheeps.male -= 1
        if sheeps.male == 0:
            break
print(sheeps.female, sheeps.male)
for m,f in zip (range(cows.female),range(cows.male)):
    if abs(hunter.location[0][0] - cows.location_female[m][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - cows.location_female[m][1]) <= hunter.hunt:
        cows.female -= 1
        if sheeps.female == 0:
            break
    elif abs(hunter.location[0][0] - cows.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - cows.location_male[f][1]) <= hunter.hunt:
        cows.male -= 1
        if sheeps.male == 0:
            break
print(cows.male,cows.female)
for m,f in zip (range(wolfs.female),range(wolfs.male)):
    if abs(hunter.location[0][0] - wolfs.location_female[m][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - wolfs.location_female[m][1]) <= hunter.hunt:
        wolfs.female -= 1
        if sheeps.female == 0:
            break
    elif abs(hunter.location[0][0] - wolfs.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - wolfs.location_male[f][1]) <= hunter.hunt:
        wolfs.male -= 1
        if sheeps.male == 0:
            break
print(wolfs.male,wolfs.female)
for m,f in zip (range(lions.female),range(lions.male)):
    if abs(hunter.location[0][0] - lions.location_female[m][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - lions.location_female[m][1]) <= hunter.hunt:
        lions.female -= 1
        if sheeps.female == 0:
            break
    elif abs(hunter.location[0][0] - lions.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - lions.location_male[f][1]) <= hunter.hunt:
        lions.male -= 1
        if sheeps.male == 0:
            break
print(lions.male,lions.female)




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


