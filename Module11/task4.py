# Магия
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None

class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None

class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

class Storm:
    pass

class Steam:
    pass

class Dirt:
    pass

class Lightning:
    pass

class Dust:
    pass

class Lava:
    pass

water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(water + air) # Storm
print(water + fire) # Steam
print(water + earth) # Dirt
print(air + fire) # Lightning
print(air + earth) # Dust
print(fire + earth) # Lava