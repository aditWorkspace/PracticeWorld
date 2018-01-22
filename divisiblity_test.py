#2aa6%3 == 0


a="3aa1"

first=a[0]
last=a[-1]

for i in range(10):
    if int(first + str(i) + str(i) + last )%9==0:
        print(first+2*str(i)+last)

