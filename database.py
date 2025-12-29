import mysql.connector
import data
import config

#it holds all the functions that actually read and write to database
class MysqlConnect:

    db = mysql.connector.connect(
    host=config.Config.DB_HOST,
    user=config.Config.DB_USER,
    passwd=config.Config.DB_PASSWORD,
    database=config.Config.DB_NAME
    )

    mycursor = db.cursor()
    #inserts playground to database using user_id, and inserts the playground with it
    def InsertPlayground(plygrd_name, plygrd_desc, user_id, plygrd_size, tiles):
        print(plygrd_size)
        MysqlConnect.mycursor.execute(
        "INSERT INTO playgrounds (plygrd_name, plygrd_desc, user_id, plygrd_size) VALUES (%s, %s, %s, %s)",
        (plygrd_name, plygrd_desc, user_id, plygrd_size))
        MysqlConnect.db.commit()
        playground_id = MysqlConnect.mycursor.lastrowid
        #MysqlConnect.TestTiles(playground_id, tiles, plygrd_size)
        MysqlConnect.InsertTiles(playground_id, tiles, plygrd_size)
        return playground_id

    #inserts one tile to database using the playground_id
    def InsertTile( plygrd_id, tile_index, tile_contain, tile_pos_x, tile_pos_y, tile_pos_z, tile_rot_y):
        MysqlConnect.mycursor.execute(
        "INSERT INTO tiles ( plygrd_id, tile_index, tile_contain, tile_pos_x, tile_pos_y, tile_pos_z, tile_rot_y) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        ( plygrd_id, tile_index, tile_contain, tile_pos_x, tile_pos_y, tile_pos_z, tile_rot_y))
        MysqlConnect.db.commit()
         

    def TestTiles(plygrd_id, tiles, len):
        for i in range(len):
            print(tiles[i])

    #inserts all the tiles using playground id and len of the playground
    def InsertTiles(plygrd_id, tiles, len):
        for i in range(len):
            MysqlConnect.InsertTile(plygrd_id, tiles[i]["tile_index"], tiles[i]["tile_contain"],  tiles[i]["tile_pos_x"],  tiles[i]["tile_pos_y"],  tiles[i]["tile_pos_z"] ,tiles[i]["tile_rot_y"]) 
        
    #selects user from mysql database and returns all the information of that user
    def SelectUser(user_id):
        MysqlConnect.mycursor.execute(
        "SELECT * FROM users WHERE id = %s",(user_id,))
        user = MysqlConnect.mycursor.fetchone()
        return user

    #selects all playgrounds with that user_id and returns it
    def SelectPlaygrounds(user_id):
        MysqlConnect.mycursor.execute(
        "SELECT * FROM playgrounds WHERE user_id = %s",(user_id,))
        playgrounds = MysqlConnect.mycursor.fetchall()
        return playgrounds
        
    #selects all tiles using playground id and returns it
    def SelectTiles(plygrd_id):
        MysqlConnect.mycursor.execute(
        "SELECT * FROM tiles WHERE plygrd_id = %s",(plygrd_id,))
        tiles = MysqlConnect.mycursor.fetchall()
        return tiles
        

"""
INSERT INTO tiles (
  plygrd_id,
  tile_index,
  tile_contain,
  tile_pos_x,
  tile_pos_y,
  tile_pos_z,
  tile_rot_y
)
VALUES (1,0,"empty", 0,0,0,0);


"""






