try:
    if name < 5:
        print("Hi")
except:
    print("ERROR")
#name is obviously not defined so it will go to the except statement and print "ERROR".
try:
    for i in range(6,0,-21):
        print(i)
except:
    print(5)
