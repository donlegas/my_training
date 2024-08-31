my_dict = {'Vasya': 1985, 'Kirill': 1990, 'Polina': 1993}
print(my_dict)                                  ## {'Vasya': 1985, 'Kirill': 1990, 'Polina': 1993}

print(my_dict['Kirill'])                        ## 1990

print(my_dict.get('Samara'))                    ## None

my_dict['Samara'] = 1978
my_dict['Stas'] = 1994
print(my_dict)                                  ## {'Vasya': 1985, 'Kirill': 1990, 'Polina': 1993, 'Samara': 1978, 'Stas': 1994}

b = my_dict.pop("Polina")
print(b)                                        ## 1993
print(my_dict)                                  ## {'Vasya': 1985, 'Kirill': 1990, 'Samara': 1978, 'Stas': 1994}



my_set = {2, 7, 5.2, (1, 2), (1, 2), 5.2, 7, 'cal', 'to', 'cal'}
print(my_set)                                   ## {2, (1, 2), 'to', 5.2, 7, 'cal'}

my_set.add('call')
my_set.add('4.6')
print(my_set)                                   ## {'4.6', 2, (1, 2), 5.2, 'to', 7, 'cal', 'call'}

my_set.discard('to')
print(my_set)                                   ## {2, (1, 2), 7, 5.2, 'call', 'cal', '4.6'}