class PlaygroundData:
    def __init__(self):
        self.delete = False
        self.id = 0
        self.plygrd_name = ""
        self.plygrd_desc = ""
        self.tiles = []
        self.plygrd_size = 25


class Tile:
    def __init__(self):
        self.index = 0
        self.content = "empty"
        self.tile_pos_x = 0
        self.tile_pos_y = 0
        self.tile_pos_z = 0
        self.tile_rot_y = 0


class UserData:
    def __init__(self):
        self.user_id = 0
        self.playgrounds = []
    
   


