# instead of loading full data in memory 
# one element at a time 
# __iter__()
# __next__()
# it's keep track of each iter variable 
 

price = [1,2,3,4,5,6] # iterables

price_iter = price.__iter__()
print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())

