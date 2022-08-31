#Write a python program to Swap two tuples in Python.

tuple_1=11,22,33,44
tuple_2='ab','cd','ef','gh'
print('Elements in Tuple 1 :',tuple_1,'\nElements in Tuple 2 :',tuple_2)

tuple_1,tuple_2=tuple_2,tuple_1
print('\nAfter Swapping...\nElements in Tuple 1 :',tuple_1,'\nElements in Tuple 2 :',tuple_2)