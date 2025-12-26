import mysql.connector
import data
import config

class MysqlConnect:

    db = mysql.connector.connect(
    host=config.Config.DB_HOST,
    user=config.Config.DB_USER,
    passwd=config.Config.DB_PASSWORD,
    database=config.Config.DB_NAME
    )

    mycursor = db.cursor()

    def InsertPlayground(pName,pDesc,user_id):
        MysqlConnect.mycursor.execute(
        "INSERT INTO playgrounds (p_name, p_desc, user_id) VALUES (%s, %s, %s)",
        (pName, pDesc, user_id))
        MysqlConnect.db.commit()


    def InsertTile(playground_id,tile_index,tile_content):
        MysqlConnect.mycursor.execute(
        "INSERT INTO tiles (playground_id, tile_index, tile_contain) VALUES (%s, %s, %s)",
        (playground_id, tile_index, tile_content))
        MysqlConnect.db.commit()
         

    def InsertTiles(playground_id, tiles: data.PlaygroundData, len):
        for i in range(len):
            MysqlConnect.InsertTile(playground_id, tiles.tiles_index[i], tiles.tiles_content[i]) 
        


    def SelectUser(user_id):
        MysqlConnect.mycursor.execute(
        "SELECT * FROM users WHERE id = %s",(user_id))
        user = MysqlConnect.mycursor.fetchone()
        print(user)


    def SelectPlayground(playground_id):
        MysqlConnect.mycursor.execute(
        "SELECT * FROM users WHERE id = %s",(playground_id))
        playground = MysqlConnect.mycursor.fetchone()
        print(playground)
                       

        









