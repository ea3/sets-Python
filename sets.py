#You can't add repeated items to a set. It won't throw an error, but it won't be added. 
# sets are unordered collections of unique elements. 
myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3]
print(mylist)
print(set(mylist))
string = 'Mississippi'
print(set(string))
