#Write a python program to check if all items in the tuple are the same.

tuple_var1=tuple([eval(x) for x in input('Enter Elements Separated by Comma : ').split(',')])

if tuple_var1.count(tuple_var1[0])==len(tuple_var1):
    print('All Items in The Tuple are The Same...')
else:
    print('All Items in The Tuple are Not The Same...')