housechores = "Wash car, clean house, cook dinner, tell Andrew to clean his room"
print(housechores)
housechores2 = ["Wash car", "clean house", "cook dinner", "tell Andrew to clean his room"]
print (housechores2)
print (housechores2[1])
print (housechores[1:9])
#look at the differences between 'housechores' and 'housechores2, then look what printed when I printed both of them. I/You will understand.
housechores2[2]="Buy Tickets to movie"
print (housechores2)
housechores2.append("CRAP")
print(housechores2)

arcade = "spin the wheel", "smash button", "knock the clown", "deal or no deal"
print (arcade)

arcade2 = ["spin the wheel", "smash button", "knock the clown", "deal or no deal"]
print (arcade2)

arcade2[3] = "deal"
print(arcade2[2:])
print(arcade2[:3])
print (arcade2)
del housechores2[2]
print (housechores2)

array1 = [5,5,7,6,6,74]
array2 = [85,85,8,5,585,7]
array3 = array1 + array2
print (array3)
array3.remove(7)
print (array3)
#look at the difference between the two lines above this. I wrote array3.remove.(7).This will remove whatever is in the paranthesis . In this case, it removed the first 7 shown in the array. Array = .remove : list = del")
print (len(housechores2))
#python gave me the length of housechores 2. Python started from 1, not 0, because it was a list.(I deleted one of the
#object in house chores 2(line20)).

numarray = [5,100033,-85,866375368,1]
boy = ['jEFF',"sf",33,55]
print (max(numarray))
print (min(numarray))
housechores2.append("clean the toilets")
print (housechores2)
print (housechores2.count("clean the toilets"))
"""
We learned del, len, max, min, append, and count. del = delete : len = how many tasks or things to do or there is :
 max = biggest number in array : min = smallest number in array : append = add something :
 count = how many times I used, for example, how many times have I added 6
"""
print("hello" + "world")


# ARRAYS AND LISTS ARE THE SAME!!!!
l = ["45"]
l.append("bob")
print(l)
print(l.pop())
#Pop shows you the last object in the list.IT ALSO PERMENANTLY affects your last.
#We just popped of 'bob'. BOD IS NOT IN THE LIS ANYMORE
print(l)
#You can do...
x = l.pop()
print(x)
print(l)
#POP IS A COOL FUNCTION
Grape = ["Bob","Alex","Andrew"]
print(Grape.pop(0))

# 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 1 4 1 5 1 6
