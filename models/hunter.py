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
"""