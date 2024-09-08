from os import name


print ("'hello world'")
print ('420')
# number a kono koma na dileo hbe
'''pip and module ki?
module holo kono package
pip holo package manager
module holo kono package a jodi kichu ja devloper ra create korche for our better use
module 2 types
1.built in module
2.user module
'''

x=('okcool') #string

print (x)

y= 430
print (type(y))

z=["apple", "orange", "cherry"] #list is mutable    
print (type(z))

a=('apple', 'orange', 'cherry') #tuple cz first bracket if it is on third breacket thn it will be listed here and tuple data type is immutable
print(type(a))

b={'apple', 'orange', 'cherry'} #set cz it will be second bracket
print (type(b))

ran= range(4)
for i in ran:
    print (i)

    
c=b"hello world"

print (c)



#string type data type
YourName = "John"
MyName="trot"
print ("my name is " + MyName + ' '+YourName)

#string in format

username ="eshan"
roll ="10"
print (f"{username},{roll}")

#binary type data type

'''byte array is mutable and byte is immutable format'''

XList=[1,2,3,4,5,6,7,8,9,10]
l=bytes(XList)   #mainly image type changable er jonnno bytes needed 
print (type(l))

 #byte array is mutable and byte is immutable format


XList=[1,2,3,4,5,6,7,8,9,10]
l=bytearray(XList) 
l[1]=100
print (l[1])


#swapping
ty=5
th=7

ty,th=th,ty
print ('this value is now ty', ty)


#username input

'''username =input('enter the username:')
password =input('enter the password:')

print (username, password)'''


#type casting

num="123"
print (type(float(num)))

#list type
li=[1,2,3]
li[1]=7
print(li[1])

#add list 
List = ['apple', 'orange', 'banana']
List.append('mango')
print(List)

List.insert(2,'cherry ')
print(List)


#remove list
List.remove('apple')
print(List)


del List[0] 
print(List)

List.pop(2)
print(List)


#loop

LoopList =[1,2,3]
#for i in LoopList:  
   #print(i)'''

    #range check

#for i in range(len(LoopList)):
 #   print(i)

#while loop

y=0
while y<len(LoopList):
     print(LoopList[y])  #length dia amra pura loop list k call korchi r ptint  a[y] dia index call korchi r ptint a
     y=y+1 

#double the number

P=[1,2,3,4,6,5,8,7,9,11,10]
for i in P:
    print (i*2 )

d= [i*2 for i in P]
print (d)

#sort and reverse the list
P.sort()
print(P)

P.sort(reverse=True)
print(P)


#copy list

P2=P.copy()
print(P2)
print(P)

#add list
w1=[4,6,7]
w2=[8,1,9]

w1.extend(w2)
print (w1)

#matrix
PrakashList =[
    [1,2,3]
,[4,5,6]
]   
print(PrakashList[0][2])

#tuple

bro=(1,2,3,4,5,6)
print (type(bro))
print(bro[-1])
print (bro[2:5])


#python update tuples

ab=list(bro) #convert to list
ab[5]=7      #change the value of index number
bro=tuple(ab)  #bro save the value of ab and  make it tuple again
print(bro)  #then print bro

(*a,)=bro
print(a) #then print

#for i in bro:
 #print(i)
cool=('true','bru','blue','green')
#m=1
#while m< len(cool):
 #m = m + 1
 #print(cool[m])

print(cool*2)

we=(3,4,5,6,7,8,8,8, 9,10,11,12,13,14)
do=we.count(8)     #count refers to the number ofvalue the how much numbers have
print(do)      #index refers to occurances of the specified the value
do=we.index(8) 
print(do) 

#set function
boom={1,2,3,4,5,6}
nice={101,102,104}

#for i in boom:
#print(i)
#print(4 in boom)

#add set

#boom.add(9)
#print(boom)

#boom.update(nice)
#print(boom)

#remove set
#d=boom.pop()
#print(d)
#boom.remove(6)
#print(boom)
del boom #it will show error message cause this function are not available
nice.clear() #clear will show set() message
print(nice)

 #dictionary

arnica = {
     "not":{
         "location": "k",
         "age":  "browser"
     },
     "year" : 1981
}
 #print(arindam["not"]["age"])
#de= arnica.get("not")
        
#de=arnica.keys()  #keys are only identified the key like here not
#fx=arnica.values()  #values are only identified the values inside the key
#fx=arnica.items() #items are only identified the values inside the key
#print(fx)            
#print(de)

#if "not"  in arnica:
    #print("yes,it is exist") 

#new value updated

#arnica["year"]= 2005

#arnica.update({"year": 3000})
#print(arnica["year"])

#pop remove items
#arnica.pop("year") #specrifc pop 
#arnica.popitem()  #last item pop
#print(arnica)

#function of loop
 
#for wx in arnica:  #print only key
  #  print(wx)

#for wx in arnica:
 #   print(arnica[wx])  #print all values

#for wx in arnica.values():
 #    print(wx)

 #     for wx in arnica.keys():
   #          print(wx)
 
#for wx,wy in arnica.items(): #for keys and values use items
 #   print(wx,wy)

#copy items
#myDict=arnica.copy()
#print(myDict)
#dz=dict(arnica)
#print(dz)

a=100
b=120
if a>b:
    print("a amar boro")
#else :
 #   print("a amar chooto")
 b>a:
    print("a amar chooto")

    #mainly else does not require any conditions where elif does

    buchi=0
    while buchi <10 :
     print("buchi is choto", buchi)
     buchi=buchi+1

er=["a", "b", "c"]    
for sd in er :
  if sd=="b":
      break
print(sd)

#function type

def MyFunction(a,b):
    sum=a+b
    print(sum)
MyFunction(20,50)

def Pokufun():
    print("MyFunction") #calling function
Pokufun()


#breakpoint
dhuru=[1,2,3,4,5,6,7,8]
#for v in range(len(dhuru)):
 #if v == 5 :
#break
#print(v) #two different values and different output

for v in dhuru:
      
   print(v)
    
def tri_recursion():
      print("cooldown")
      tri_recursion()
     #tri_recursion()


x=lambda a,b,c,d : (a+b)/(c-d)
print(x(20,30,50,70 ))


#inheritance

class Prak :  
   name="cool"
   date="31.03.2020"

class Ach (Prak):
        roll=""
        age=""

   # def __init__(self): 
   #    self.date = ""  

# Creating an instance of the Prak class
#   
n = Ach()  

# Printing the attributes  
print(n.name)  
print(n.date)

 
 #iteration and next 

r=[1,2,3,4,5,6,7,8,9]
m=iter(r)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))


#date time format
#import datetime

#xt=datetime.datetime.now()
#print(xt.strftime("%A"))


#regular expression

#import re        #reg ex should be followed on w3school

#text2="ki obotha sobar,VALO tO"
#a=re.findall("[a-zA-Z]",text2)
#print(a)


#try and except
#print("ok")
#try:
 # print(x)
#except NameError:
 ## print("Variable x is not defined")
#except:
 # print("Something else went wrong")

#read and open file

#reading=open('bro.text','r')

#print(reading.read())

#Wri=open("bro.html", "a")

#Wri.write("<p>no bro</p> \n")
#Wri.write("<p>ki khbors </p>")

#deleTE or file remove what i have been created
#import os

#os.remove("bro.html")
#os.rmdir("folder name")
    
#import mymodule
#import module as kaku
#mymodule.te()

#constructor and module

#class parentInfo::
 #        def __init__(self,name,age): #constructor  
         
   #def PrakashHome(self,name,age):   #module
  #            print(f"my name is {name},my age is {age}")

#xr1=parentInfo("arindam",23)    #constructor formula

#xr1.PrakashHome("arindam",11)      #module

class className:
    def InstanceMethod(self):
        print("hello instance method called")  #instance method
v1=className()
v1.InstanceMethod()

class ClassName:

 @classmethod
 def ClassMethod(cls):     #class method
    print("class is method")

ClassName.ClassMethod()



class Static:
    @staticmethod
    def StaticMethod():
        
        print("static method is method")

v1=Static()
v1.StaticMethod()  #you can call static in two ways
Static.StaticMethod()  

#polymorphism

class polymorph():
  def __init__(self,name,age):
      
         self.name=name
         self.age=age
class new2(polymorph):
     pass
class new3(polymorph):
    pass

p5=new3("arindam",34)    
p4=new2("eshak",23)
print(p4.name,p4.age)
print(p5.name,p5.age)


#encapsulation function are used for protection variables (__abc)  just two lowers dash before the module the code will be not able to accept in public
