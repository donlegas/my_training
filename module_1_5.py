immutable_var = True, 5, 3, 7, 'horda', 5.2
print(immutable_var)             ## (True, 5, 3, 7, 'horda', 5.2)

# immutable_var[0]= 2            ## TypeError: 'bool' object does not support item assignment

mutable_list = ['machine', 'list', 'koleso']
print(mutable_list)                   ## ['machine', 'list', 'koleso']

mutable_list.extend([3, 'polo'])      ## ['machine', 'list', 'koleso', 3, 'polo']
print(mutable_list)

mutable_list.reverse()
print(mutable_list)                   ## ['polo', 3, 'koleso', 'list', 'machine']

mutable_list[1] = 'good'
print(mutable_list)                   ## ['polo', 'good', 'koleso', 'list', 'machine']