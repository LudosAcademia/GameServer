import database

class Main:

    def send_tiles_mysql(id,data,len):
        database.MysqlConnect.InsertTiles(id,data,len)
        database.MysqlConnect.db.close()
        Main.print_tiles(data,len)

    def send_plygrd_mysql(name,desc):
        import data
        database.MysqlConnect.InsertPlayground(name,desc,data.UserData.user_id)

    def print_tiles(tiles, len):
        for j in range(len):
            print("The Index: " + str(tiles.index[j]) + "The Content: " + tiles.content[j])

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
