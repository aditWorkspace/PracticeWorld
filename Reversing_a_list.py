#HINT
a=2
b=3
adit=a
a=b
b=adit
print(a,b)
#or
a=2
b=3
a,b=b,a
print(a,b)
#Real Problem
a = [1,2,3,4,5]
b=len(a)
c=[0]*b
for i in range(b-1,-1,-1):
    c[b-i-1]=a[i]
print(c)
#or
a=[1,2,3,4,5,6,7,7,8,8,7,64,4,5,46,57]
b=len(a)
c=[]


for i in range(b-1,-1,-1):
    c.append(a[i])

print(c)

for i in range(16,14,-1):
    print(i)


