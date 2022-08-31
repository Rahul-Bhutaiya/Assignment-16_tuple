#Write a python program to Sort a tuple of tuples by the second item.tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 =(('a',21),('b',37),('c',11),('d',29))
list1=[]
tuple2=()

for y in range(len(tuple1)):
    list1.append(tuple1[y][1])
    
list1.sort()

for x in list1:
    for y in range(len(list1)):
        if tuple1[y][1]==x:
            tuple2+=(tuple1[y][0],tuple1[y][1]),
            break

print('Sorted a Tuple of Tuples by The Second Item :',tuple2)