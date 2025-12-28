import json

class PlaygroundData:
    def __init__(self):
        self.delete = False
        self.id = 0
        self.plygrd_name = ""
        self.plygrd_desc = ""
        self.tiles = []
        self.plygrd_size = 25
    
    def to_dict(self):
        return {
            "delete": self.delete,
            "id": self.id,
            "plygrd_name": self.plygrd_name,
            "plygrd_desc": self.plygrd_desc,
            "tiles": [t.to_dict() for t in self.tiles],
            "plygrd_size": self.plygrd_size,
        }

class Tile:
    def __init__(self):
        self.index = 0
        self.contain = "empty"
        self.tile_pos_x = 0
        self.tile_pos_y = 0
        self.tile_pos_z = 0
        self.tile_rot_y = 0

    def to_dict(self):
        return {
            "tile_index": self.index,
            "tile_contain": self.contain,
            "tile_pos_x": self.tile_pos_x,
            "tile_pos_y": self.tile_pos_y,
            "tile_pos_z": self.tile_pos_z,
            "tile_rot_y": self.tile_rot_y,
        }

class UserData:
    def __init__(self):
        self.username = ""
        self.curr_ply_index = 0
        self.playgrounds = []

    def to_dict(self):
        return {
            "name": self.username,
            "curr_ply_index": self.curr_ply_index,
            "playgrounds": [p.to_dict() for p in self.playgrounds]
        }
    


    
    #def to_dict(self):
    #return self.__dict__
   


