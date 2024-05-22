class Room:
    def __init__(self, name, tools, treasure, description):
        self.name = name
        self.tools = tools
        self.treasure = treasure
        self.description = description

    def __str__(self):
        return self.name

shaft = Room('shaft', 'basic pickaxe', 0, 'the mineshaft. '
             + 'The shaft is the only place you can move vertically')
weak_stone = Room('weak stone', 'basic pickaxe', 1, 'an area of weak stone. '
                  + 'You can mine through it with just a basic pickaxe. ')

stone = Room('stone', 'upgraded pickaxe', 1, 'an area of hardened stone. '
              + 'You can only mine through it with an upgraded pickaxe')
gas_pockets = Room('gas pockets', 'basic pickaxe', 1, 'an area of weak stone. You can hear' +
                  'a hissing from somewhere close. You can mine through the stone with just a basic pickaxe. ')
abandoned_shaft = Room('abandoned shaft', 'basic pickaxe', 3, 'an old abandoned mineshaft. It appears deserted. ')
damp_cave = Room('damp_cave', 'basic pickaxe', 1, 'dimly lit cave. '
                  + 'There are puddles in low spots, '
                  + 'stalagtites and stalagmites extend from '
                  + 'the ceiling and floor. ')
crystal_cave = Room('crystal cave', 'basic pickaxe', 3, 'a large cave with waist '
                     + ' high water. Crystals grow from the '
                     + 'ceilings and floors. ')
flooded_cave = Room('flooded cave', 'scuba_gear', 2, 'a flooded cave. '
                     + 'You will need scuba gear to pass '
                     + 'through it. ')