#list is changable
# a =  [1,2,3,4,56,78,12]
# n = len(a)
# for i in range(0,n):
#     print(a[i])
    
    
    
    
#set is immutable
# a = {1,2,3,4,5}     
# n = len(a)
# for i in range(0,n):
#     print(a[i])
    
    
    
    
#-------------------------odd-even------------------#
# num = [29,39,43,12,34]
# n = len(num)
# for i in range(0,n):
#     if(i % 2 == 0):
#         print("Number is odd")
#     else:
#         print("number is even")
        
        
    
    
#-------------------vowel occurs or not------------------------#

# str = "PRIYANKA"
# n = len(str)
# for i in range(0,n):
#     if(str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
#         print("Vowel occurs")
#     else:
#         print("no vowel is there")
        
        
#---second way-------#        
# for i in range(0,n):
#     if str[i] in ['A','E','I','O','U']:
#         print("Vowel occurs")
#     else:
#         print("no vowel is there")
 
 
 
#------value is not change because it is call by value-------#
def fun(p):
    p = 20
if __name__== "__main__":
    print("entry point here")
    a = 10
    fun(a)
    print(a)