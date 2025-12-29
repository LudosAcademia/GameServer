from database import MysqlConnect
from main import Main
import data
import config
#this file is for testing purposes no real impact on the server


class TestClass:
    a = 23
    b = 65
    c = [[
        "apple","banana","pear"
    ],[
        32,55,37,854,37,32,15
    ],[
        "phone","car"
    ]]

#print(str(TestClass.a)  + " " + str(TestClass.b)  + " " + str(TestClass.c) )
#print(config.Config.SECRET_KEY)

#print_playgrounds(retrive_plygrd_data(13))

#Main.print_playgrounds(Main.retrive_plygrd_data(1))


#print(playgrounds[0][3])

user = data.UserData()
raw_user = MysqlConnect.SelectUser(13)
user.name = raw_user[1]
print(user.name)




"""



for plygrd in user.playgrounds:
    print()

for item in playgrounds:
    for i in item:
        print(i)


"""