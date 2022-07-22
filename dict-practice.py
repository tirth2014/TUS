dic = {}

dic.update({'name': 'tirth'})
dic.update({'age': 21})
dic['city'] = 'Ahmedabad'
del dic['city']

print(dic)
heyDic = [('name', 'tirth'), ('city', 'ahmedabad'), ('age', 21)]
print("type of heyDic is: ", type(heyDic))
print(dict(heyDic))

print(list(dic))

# dict comprehension :-
dc = {x: x ** 2 for x in range(2, 8)}
print(dc)
print(dict(name='tirth', age=21, keyword='w/o apostrophe'))

# Looping

for k, v in dic.items():
    print("key: {}  value: {}  ".format(k, v), end=" | ")

print('\n')

for i, v in enumerate(['tirth', 'jay', 'bhavik']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function
lst1 = ['red', 'blue', 'black', 'white']
lst2 = ['c1', 'c2', 'c3', 'c4']

for l1, l2 in zip(lst1, lst2):
    print('color number: {1} is {0}'.format(l1, l2))

for i in reversed(range(1, 10, 2)):
    print(i, end=" ")

flot = 51.2343435436543543543
print('\n')
print('{:.2f}'.format(flot))
print('%.2f' % flot)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i,end=" ")
print('\n')
for f in sorted(set(basket)):
    print(f,end=" ")

lst3 = []
lst3.append(dic)
lst3.append(dc)
print(lst3)
