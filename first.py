print("this is KASHAF");

a=4.6;
print(a);
a=68.6;
print(type(a));

# OPERATOR

x=4;
y=7;

print(x+y);


a=3;
b=6;
print(a>b);



lisa="i am lisa";
print(lisa);


#STRING
name="kashaf Abdullah"
name='kashaf'
name='''KAshaf'''
print(name)

# Extracting individual characters


print(name[0])
print(name[-1])
print(name[2:5])


#STRING FUNCTION

#Find length of string
print(len(name))
#convert into lower case 
print(name.lower())
#convert into upper case
print(name.upper())

#Replcing a substring
print(name.replace('s','m'))
#Number of occurence string
print(name.count("ka"))

#Finding the index of substring
print(name.find('a'))
#Splitting a string

fruit='This is , an , apple'
print(fruit.split(','))


#DATA STRUCTURES 
tup1=(2,'a',True)
print(tup1[1])


#tup1[2]="apple"  #will give error nbcz tuple is immutable(yoou cannot modify) 

#Findng Length of Tuple
print(len(tup1))
#concatenating tuples

tupl1=(1,2,3)
tupl2=(4,5,6)
print(tupl1+tupl2);

print(min(tupl2))




#List
l1=[1,'ss',False]
print(l1)
print(l1[2])
print(l1[1:2])

#Modify a list
l2=[1,'k',True,'a',5]
l2[1]=50;
print(l2)
#Appending a new element
l2.append("Kashaf")
print(l2)

#Popping the last element
print(l2.pop())

#Reversing elemt of list
l3=[1,"a",4,"d"]

l3.reverse()
print(l3)
#Inserting element of a specified
l3.insert(3,"helo")
print(l3)
#Sorting a list
l4=["mango","banana","guava","apple"]
l4.sort()
print(l4)

#concatenating a list
l6=[1,2,3]
l7=["a","b","c"]
print(l6+l7)
#Repeating element
l8=[1,"a",True]
print(l8*3)




#DICTIONARY

Fruit={"Apple":1,"Orange":40}
print(Fruit.keys())
print(Fruit.values())
#Adding a new value in dictionary
Fruit["Mango"]=50;
print(Fruit)

#Changing an existing element

Fruit["Apple"]=20;
print(Fruit)

#Update one dictionary elemnt with another
Fruit2={"Banana":66,"Strawberry":11};
Fruit.update(Fruit2)
print(Fruit)

#Popping an element
Fruit.pop("Orange")
print(Fruit)



#SET
s1={1,"kashaf",True}
print(s1)

#SET OPERATIONS
#Adding a ew Element
s1.add("Hello")
print(s1)
#Updating multiple elements
s1.update([10,20,30])
print(s1)
#Removing an elements

s1.remove("kashaf")
print(s1)

#SET FUNCTIONS
#Union of two sets
a={1,2,3}
b={"a","b","c"}
print(a.union(b))
#Intersection of two sets
x={1,2,3}
y={2,3,4}
print(x.intersection(y))




#IF STATEMENT
a=70;
b=30;
c=44;
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


if (a>b & a>c):
    print("a is greater ")
elif (b>a & b>c):
    print("a is not greater")
else :
    print("c is greater")
#if wit tuple

tup5=(1,2,3)
if 2 in tup5:
    print("2 is present in tup5")
else:
        print("2 is not present in tup5")


#if with tuple in list

l=[1,2,3,4,5,6]
if l[2]==3:
    print("hello")


    # IF WITH dictionary
    d1={"a":3,"b":1}
    if d1["a"]==3:
        print("yes")



#WHILE LOOPING STATEMENT:
# i=1;
# while i<=10:
#     print(i);
#     i=i+1



#FOR LOOP
# m={"apple","banana","orange"}
# for i in m:
#     print(i)


    #FUNCTIONS

    def hello():
        print("HELLO WORLD")
    
    hello()

    #function with parammeters
    def myfunc(x):
        print("HELLO WORLD",x)
    
    myfunc(4)

#2
    def myfunc2(x):
        return "HELLO WORLD",x;
    
    print( myfunc2(4))

#3

def even_odd(x):
    if x%2==0:
        print("even")
    else :
        print("odd")


even_odd(4)

#Lambda function
g=lambda x:x*x*x # x is parameter
print(g(7))

#lambda function with filters
li=[3,4,5,77,88,42,35,754]
final_list=list(filter(lambda x:(x%2!=0),li))
print(final_list)


#lambda function with map
from functools import reduce
li=[3,4,6,8,22,56,87,5433]
sum= reduce((lambda x,y:x+y),li)
print(sum)

