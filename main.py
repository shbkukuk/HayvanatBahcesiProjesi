from models.hunter import Hunter
from  models.animal import *

hunter = Hunter()

sheeps =sheep(female=15, male=15, location_male=[], location_female=[])
cows = cow(female=15, male=15, location_male=[], location_female=[])
wolfs = wolf(female=15, male=15, location_male=[], location_female=[])
lions = lion(female=15, male=15, location_male=[], location_female=[])
chickens_roosters = chicken_rooster(female=15, male=15, location_male=[], location_female=[])
# random belirtilen alanda konumlandırma
sheeps.creation_location()
cows.creation_location()
lions.creation_location()
wolfs.creation_location()
chickens_roosters.creation_location()
#hunt
#üreme
sheeps.reproduction()
#hareketler
sagsol(locations=hunter.location, move=hunter.move)
sagsol(locations=sheeps.location_male, move=2)
sagsol(locations=sheeps.location_female, move=2)
sagsol(locations=cows.location_male, move=2)
sagsol(locations=cows.location_female, move=2)
sagsol(locations=wolfs.location_male, move=3)
sagsol(locations=wolfs.location_female, move=3)
sagsol(locations=lions.location_male, move=4)
sagsol(locations=lions.location_female, move=4)
sagsol(locations=chickens_roosters.location_male, move=1)
sagsol(locations=chickens_roosters.location_female, move=1)

ileriasagi(locations=hunter.location, move=hunter.move)
ileriasagi(locations=sheeps.location_male, move=2)
ileriasagi(locations=sheeps.location_female, move=2)
ileriasagi(locations=cows.location_male, move=2)
ileriasagi(locations=cows.location_female, move=2)
ileriasagi(locations=wolfs.location_male, move=3)
ileriasagi(locations=wolfs.location_female, move=3)
ileriasagi(locations=lions.location_male, move=4)
ileriasagi(locations=lions.location_female, move=4)
ileriasagi(locations=chickens_roosters.location_male, move=1)
ileriasagi(locations=chickens_roosters.location_female, move=1)


