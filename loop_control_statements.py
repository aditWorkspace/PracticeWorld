b = 5
while b<100:
    if b==8:
        break
    print(b)
    b = b +1
#That was break function
b = 5
while b<100:
    if b==8:
        break
    else:
        pass
    print(b)
    b = b +1
#Pass is a good term to use when you don't want anything. A filler-upper
for i in "Python":
    if i == "h":
        continue
    print(i)
#continue skips a term. If you don't want a code but it still prints, continue removes that. In this case "h".
for i in range(0,5):
    if i<2:
        continue
    print(i)
#continue can also be used like this. 