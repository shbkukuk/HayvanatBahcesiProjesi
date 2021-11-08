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
while count:
    #Üreme
    sheeps.reproduction()
    cows.reproduction()
    lions.reproduction()
    wolfs.reproduction()
    chickens_roosters.reproduction()
    #Avlanma-Insan
    sheeps.hunter_hunting()
    sheeps.hunter_hunting()
    cows.hunter_hunting()
    lions.hunter_hunting()
    wolfs.hunter_hunting()
    chickens_roosters.hunter_hunting()
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
    for m,f in zip (range(lions.female),range(lions.male)):
        for j,k in zip(range(sheeps.female),range(sheeps.male)):
            if abs(lions.location_female[m][0] - sheeps.location_female[j][0]) <= lions.hunt_lenght or \
                abs(lions.location_female[m][1] - sheeps.location_female[j][1]) <= lions.hunt_lenght:
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(lions.location_male[m][0] - sheeps.location_male[j][0]) <= lions.hunt_lenght or \
                abs(lions.location_male[m][1] - sheeps.location_male[j][1]) <= lions.hunt_lenght:
                sheeps.male -= 1
                if sheeps.male == 0:
                    break
            elif abs(lions.location_male[m][0] - sheeps.location_female[j][0]) <= lions.hunt_lenght or \
                abs(lions.location_male[m][1] - sheeps.location_female[j][1]) <= lions.hunt_lenght:
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(lions.location_female[m][0] - sheeps.location_male[j][0]) <= lions.hunt_lenght or \
                abs(lions.location_female[m][1] - sheeps.location_male[j][1]) <= lions.hunt_lenght:
                sheeps.male -= 1
                if sheeps.male == 0:
                    break
    #Avlanma-kurt
    for m,f in zip (range(wolfs.female),range(wolfs.male)):
        for j,k in zip(range(chickens_roosters.female),range(chickens_roosters.male)):
            if abs(wolfs.location_female[m][0] - chickens_roosters.location_female[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_female[m][1] - chickens_roosters.location_female[j][1]) <= wolfs.hunt_lenght:
                chickens_roosters.female -= 1
                if chickens_roosters.female == 0:
                    break
            elif abs(wolfs.location_male[m][0] - chickens_roosters.location_male[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_male[m][1] - chickens_roosters.location_male[j][1]) <= wolfs.hunt_lenght:
                chickens_roosters.male -= 1
                if chickens_roosters.male == 0:
                    break
            elif abs(wolfs.location_male[m][0] - chickens_roosters.location_female[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_male[m][1] - chickens_roosters.location_female[j][1]) <= wolfs.hunt_lenght:
                chickens_roosters.female -= 1
                if chickens_roosters.female == 0:
                    break
            elif abs(wolfs.location_female[m][0] - chickens_roosters.location_male[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_female[m][1] - chickens_roosters.location_male[j][1]) <= wolfs.hunt_lenght:
                chickens_roosters.male -= 1
                if chickens_roosters.male == 0:
                    break
    for m,f in zip (range(wolfs.female),range(wolfs.male)):
        for j,k in zip(range(sheeps.female),range(sheeps.male)):
            if abs(wolfs.location_female[m][0] - sheeps.location_female[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_female[m][1] - sheeps.location_female[j][1]) <= wolfs.hunt_lenght:
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(wolfs.location_male[m][0] - sheeps.location_male[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_male[m][1] - sheeps.location_male[j][1]) <= wolfs.hunt_lenght:
                sheeps.male -= 1
                if sheeps.male == 0:
                    break
            elif abs(wolfs.location_male[m][0] - sheeps.location_female[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_male[m][1] - sheeps.location_female[j][1]) <= wolfs.hunt_lenght:
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(wolfs.location_female[m][0] - sheeps.location_male[j][0]) <= wolfs.hunt_lenght or \
                abs(wolfs.location_female[m][1] - sheeps.location_male[j][1]) <= wolfs.hunt_lenght:
                sheeps.male -= 1
                if sheeps.male == 0:
                    break

    #hareketler

    count = right_left(locations=hunter.location, move=hunter.move)
    count = right_left(locations=sheeps.location_male, move=2)
    count = right_left(locations=sheeps.location_female, move=2)
    count = right_left(locations=cows.location_male, move=2)
    count = right_left(locations=cows.location_female, move=2)
    count = right_left(locations=wolfs.location_male, move=3)
    count = right_left(locations=wolfs.location_female, move=3)
    count = right_left(locations=lions.location_male, move=4)
    count = right_left(locations=lions.location_female, move=4)
    count = right_left(locations=chickens_roosters.location_male, move=1)
    count = right_left(locations=chickens_roosters.location_female, move=1)

    count= forward_backward(locations=hunter.location, move=hunter.move)
    count =forward_backward(locations=sheeps.location_male, move=2)
    count =forward_backward(locations=sheeps.location_female, move=2)
    count =forward_backward(locations=cows.location_male, move=2)
    count =forward_backward(locations=cows.location_female, move=2)
    count =forward_backward(locations=wolfs.location_male, move=3)
    count =forward_backward(locations=wolfs.location_female, move=3)
    count =forward_backward(locations=lions.location_male, move=4)
    count = forward_backward(locations=lions.location_female, move=4)
    count = forward_backward(locations=chickens_roosters.location_male, move=1)
    count = forward_backward(locations=chickens_roosters.location_female, move=1)

else:

    print("""
    **************************************************************
    The number of animals at the end of the movement of 1000 units
    **************************************************************
    Sheep {} male {} female,
    wolf  {} male {} female,
    Lion {} male {} female,
    Cow {} male {} female,
    Chicken {},
    Roaster {}."""
     .format(sheeps.male,sheeps.female,wolfs.male,wolfs.female,lions.male,lions.female,cows.male,cows.female,chickens_roosters.female,chickens_roosters.male))