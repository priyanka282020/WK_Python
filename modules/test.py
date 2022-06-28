#---convert json to python---------------#
import json
from urllib.request import ProxyBasicAuthHandler
x =  '{"name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["age"])






#--------convert python to json---------------------------------#
#python object

x = {
    "name":"pri",
    "address":"kalol",
    "age":"22"
}
y = json.dumps(x)
print(y)




#------------------String Formatting-----------------------------------------------------#
price = 500
txt = "The  bat price is {} dollars"
print(txt.format(price))

#-------multiple values-----------------#
age = 29
name= "pri"
address="kalol"

mydetails = "hiii, my name is {} my age is{} and my address is {}"
print(mydetails.format(name,age,address))
