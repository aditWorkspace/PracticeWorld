a = "string"
print("Place my variable here: %s" %(a))

a = "123"
print("Place my variable here: %s" %(a))

"""
The %s stands for string.
All it is doing is that is is transforming whatever variable we have, in this case the letter a, turns it in to a string and 
replaces the %s with it.
"""

print("Floating Point number: %1.5f" %(13.344))
#the %1.5f is saying that the number afterward, in this case  13.344, should have at least 1
# digits before the decimal and 5 digits after the decimal. We only have three numbers after the decimal point and
# so python will fill it up with 0s. Print this.
a = "Floating Point number: %15.5f" %(13.344)
print(a)
#print this
#Python fills up the spaces with blank characters so t will be a total of 15 characters before the decimal point.
str = repr
#did you know that?!
print("First: %s, Second: %s, third: %s, ..."%("hi","dsah","aa"))
#You can print many objects. At the end put them in the order you want them to be in.



#WHAT IF YOU WANT THE SAME OBJECT FOR MANY??????
print("first: {s}, second: {s}".format(s=3))
#remember to use: .format immediately.
print("first: {s}, second: {s}, third: {y}".format(s=3,y=5))

print ('First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22))

