
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
import config
print(config.Config.SECRET_KEY)