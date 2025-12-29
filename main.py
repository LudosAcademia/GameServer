from database import MysqlConnect
import data
from config import Config

#it holds the main function of the Server that handles data retrival and write
class Main:
    #takes in user id returns user object with all the information from database writen
    def retrive_plygrd_data(user_id: int):
        raw_playgrounds = MysqlConnect.SelectPlaygrounds(user_id)
        user = data.UserData()
        raw_user_data = MysqlConnect.SelectUser(user_id)
        user.username = raw_user_data[1]
        user.curr_ply_index = raw_user_data[6]
        for plygrd in raw_playgrounds:
            playground = data.PlaygroundData()
            playground.id = plygrd[0]
            playground.plygrd_name = plygrd[1]
            playground.plygrd_desc = plygrd[2]
            playground.plygrd_size = plygrd[3]
            raw_tiles = MysqlConnect.SelectTiles(playground.id)
            for tile in raw_tiles:
                new_tile = data.Tile()
                new_tile.index = tile[1]
                new_tile.contain = tile[2]
                new_tile.tile_pos_x = tile[3]
                new_tile.tile_pos_y = tile[4]
                new_tile.tile_pos_z = tile[5]
                new_tile.tile_rot_y = tile[6]
                playground.tiles.append(new_tile)
            user.playgrounds.append(playground)
        return user

    #prints the user object, for testing purposes
    def print_playgrounds(user : data.UserData):    
        for i in user.playgrounds:
            print("playground id: " + str(i.id))
            print("playground name: " + str(i.plygrd_name))
            print("playground desc: " + str(i.plygrd_desc))
            print("playground size: " + str(i.plygrd_size))
            for j in i.tiles:
                print("Tile index: " + str(j.index))
                print("Tile contain: " + str(j.contain))
                print("Tile pos x: " + str(j.tile_pos_x))
                print("Tile pos y: " + str(j.tile_pos_y ))
                print("Tile pos z: " + str(j.tile_pos_z ))
                print("Tile rot y: " + str(j.tile_rot_y ))

    #depricated
    def send_tiles_mysql(id,data,len):
        MysqlConnect.InsertTiles(id,data,len)
        MysqlConnect.db.close()
        Main.print_tiles(data,len)
    #depricated
    def send_plygrd_mysql(name,desc):
        import data
        MysqlConnect.InsertPlayground(name,desc,data.UserData.user_id)
    #testing purposes
    def print_tiles(tiles, len):
        for j in range(len):
            print("The Index: " + str(tiles.index[j]) + "The Content: " + tiles.content[j])
    #depricated
    def confirm_php_connect(payload_data):    
        import data
        data.UserData.user_id = payload_data
        #TO BE ADDED: username and other user info retrive from mysql using user_id
        print("PHP connection is established, user id recieved " + data.UserData.user_id)



    





#Insert Tiles into database


#db_contr.MysqlConnect.InsertPlayground(pName,pDesc,user_id)



"""
Comment Section

for value in mycursor:
    print(value)

for value in tiles.index:
    print("The Index: " + str(value))

for value in tiles.content:
    print("The Index: " + value)

for j in range(100):
    print("The Index: " + str(tiles.index[j]) + "The Content: " + tiles.content[j])


    
pName = "Alpha_Playground"
pDesc = "A playground for experimenting with algorithms and data structures"
user_id = 13

tiles = data.Tiles()
i = 0
len = 100

#Generate Empty Tiles
while i < len:
    tiles.index.append(i)
    tiles.content.append("empty")
    i = i + 1 


    def __init__(self):
        self.user_id = 0
        self.username = ""

        
            def __init__(self):
        self.p_name = ""
        self.p_desc = ""
"""
