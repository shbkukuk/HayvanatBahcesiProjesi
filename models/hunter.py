import random as rd

class Hunter():
    move = 1
    hunt = 8
    location = [[rd.randrange(1, 500, 1), rd.randrange(1, 500, 1)]]

"""for i in range(sheeps.female):
    for j,k in zip(range(wolfs.female),range(wolfs.male)):
        for l,m in zip(range(lions.female),range(lions.male)):
            if abs(sheeps.location_female[i][0]-hunter.location[0][0]) == 8 or \
                    abs(sheeps.location_female[i][1] - hunter.location[0][1]) == 8:
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(sheeps.location_female[i][0]-wolfs.location_female[j][0]) == wolfs.hunt_lenght or \
                    abs(sheeps.location_female[i][1] - wolfs.location_female[j][1]) == wolfs.hunt_lenght or \
                abs(sheeps.location_female[i][0]-wolfs.location_male[k][0]) == wolfs.hunt_lenght or \
                    abs(sheeps.location_female[i][1] - wolfs.location_male[k][1]) == wolfs.hunt_lenght :
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
            elif abs(sheeps.location_female[i][0]-lions.location_female[k][0]) == lions.hunt_lenght or \
                    abs(sheeps.location_female[i][1] - lions.location_female[k][1]) == lions.hunt_lenght or \
                abs(sheeps.location_female[i][0]-lions.location_male[k][0]) == wolfs.hunt_lenght or \
                    abs(sheeps.location_female[i][1] - lions.location_male[k][1]) == wolfs.hunt_lenght :
                sheeps.female -= 1
                if sheeps.female == 0:
                    break
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
        if wolfs.female == 0:
            break
    elif abs(hunter.location[0][0] - wolfs.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - wolfs.location_male[f][1]) <= hunter.hunt:
        wolfs.male -= 1
        if wolfs.male == 0:
            break
print(wolfs.male,wolfs.female)
for m,f in zip (range(lions.female),range(lions.male)):
    if abs(hunter.location[0][0] - lions.location_female[m][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - lions.location_female[m][1]) <= hunter.hunt:
        lions.female -= 1
        if lions.female == 0:
            break
    elif abs(hunter.location[0][0] - lions.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - lions.location_male[f][1]) <= hunter.hunt:
        lions.male -= 1
        if lions.male == 0:
            break
print(lions.male,lions.female)
for m,f in zip (range(chickens_roosters.female),range(chickens_roosters.male)):
    if abs(hunter.location[0][0] - chickens_roosters.location_female[m][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - chickens_roosters.location_female[m][1]) <= hunter.hunt:
        chickens_roosters.female -= 1
        if chickens_roosters.female == 0:
            break
    elif abs(hunter.location[0][0] - chickens_roosters.location_male[f][0]) <= hunter.hunt or \
        abs(hunter.location[0][1] - chickens_roosters.location_male[f][1]) <= hunter.hunt:
        chickens_roosters.male -= 1
        if chickens_roosters.male == 0:
            break
print(chickens_roosters.male,chickens_roosters.female)
"""