inp = input("Amount is : ")
print(inp)
print(type(inp));

if(int(inp)<1000):
    disc = 5
elif(int(inp)<=5000):
   disc= 10   
else:
    disc=15
       
age = input("Enter ur age")  
print("age is ",int(age)) 
if int(age)>70:
    disc += 5
    
priv = input("Is customer privilage(Y/N) ?")
print(priv)
if priv == 'Y':
    disc += 5
        
print("Your Total discount is : ",disc)
   
   
