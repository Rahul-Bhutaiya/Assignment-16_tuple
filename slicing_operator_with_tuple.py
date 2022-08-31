#Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
tuple2=tuple1[tuple1.index(4):tuple1.index(5)+1:]
print('tuple1 :',tuple1,'\ntuple2 :',tuple2)