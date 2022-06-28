#f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f=open("myfile.txt","r")
# print(f.read())
# f.close()


#----open , read , readline , write, close---------------------------------#
# x- create  , r - read , w=write , a - append #



#class 
class demo:
    x=5 ;
    y=10;
    c=x+y;
#p is object of class
p = demo();
print(p.c);




class test:
    def __init__(self, firstname) -> None:
        self.fname=firstname;
    def printname(self):
        print(self.fname)

p = test("priyanka")
p.printname();


