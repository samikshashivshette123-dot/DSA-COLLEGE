x=10
print("Type of x==>",type(x))
y="ADYPSOE"
print("Type of y==>",type(y))
a,b,c=10,20,30
print("Value of b==>",b)
a=input("Enter the value of a==>")
print("Value of a==>",a)
print("Type of variable a==>",type(a))
print("Value of a==>",a)
b=int(input("Enter the value of b==>"))
print("Type of variable a==>",type(b))
print("Demonstration fo Comma in print fumnction")
x=10
y="Atharav"
print("x==",x,"y =",y)
print("Demonstration fo + operator  in print fumnction")
y="Ashish"
print("x=="+y)
print("Demonstration of % foramt  in print fumnction")
t=9
print("t==%d"%t)
print("t ==%d , y==%s"%(t,y))
y="vaishali"
print("Demonstration of  .foramt  in print fumnction")
print("t =={}, y=={}".format(t,y))
y="vaishanvi"
print("Demonstration of   printf fumnction")
print(f"t =={t} y=={y}")
age=int(input("Enter the value of age==>"))
if (age>=18):
    print("Yes voting possible")
else:
    print("Not elegible for  voting")
sum=0
for i in range(0,21,2):
    sum=sum+i;
print(sum)

def HelloPrint():
    print("Hello We learn Basics of python programming using function")
HelloPrint()

def Display(Array):
    print(f"Array elements ==> {Array}")

def Inseretion(Array):
    element=int(input("Enter the element which you want to insert==>"))
    position=int(input("Enter the position where you want to insert==>"))
    Array.insert(position,element)
    Display(Array)
    
def Deletion(Array):
    element=int(input("Enter the element which you want to delete==>"))
    if element in Array:
         Array.remove(element)
         Display(Array)
    else:
         print("The element which you wnat to delete is not present")
def Search(Array):
    Search=int(input("Enter the element which you want to Search==>"))
    if Search in Array:
         i=Array.index(Search)
         print(f"The lement is present at {i}")
    else:
         print("The element which you wnat to Search is not present")
Array=[10,20,30,40,50]
Display(Array)
Inseretion(Array)
Deletion(Array)
Search(Array)