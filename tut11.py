my_list1 = [0,1,2,3,4,5,6,6,7,8,9]

#list[start:end:end]


#sample_url  ='https://coreymas.com'
#print sample_url


num =[0,1,2,3,4,5,6,6,7,8,9]
my_list= []


# I want 'n' for each 'n' in num
#or n in num:
#   my_list.append(n)
#rint (my_list)

# I want 'n+n' for each 'n' in num
#my_list =[]
#for n in num:
#    my_list.append(n+n)
#print(my_list)


#my_list = [n+n for n in num]
#print(my_list)


# Using a map + lambda
#my_list= map (lambda n: n+n,num)
#
#print(my_list)

# I want 'n' for each  'n' nums if 'n' is even
#my_list =[]
#for n  in num:
# if  n%2==0:
#  my_list.append(n)
#print(my_list)

# using a filter +lambda

#my_list =filter[lambda n: n%2==0  ,num]
#print my_list

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

#for letter in 'abcd':
#     for num in '0123':
#          my_list.append((letter,num))
#print (my_list)

#my_list=[(letter,num) for letter in 'abcd' for num in (4)]
#print (my_list)

names = ['Bruce','Clark','peter','Logan','wade']
heroes = ['Batman','superman','spidermen','Wolverine','Deadpool']
#print  zip(names,heroes)

# I want a dict{'name': 'hero} for each name, hero in zip (name, heros)
#my_dict= {}
#for name, hero in zip(names,heroes):
#    my_dict[name] =hero
#print (my_dict)

#my_dict ={name: hero for name, hero in zip (names,heroes) if name != 'Peter'}
#print (my_dict)

# set comprehensions
#nums =[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set =set()
#for n in nums:
#    my_set.add(n)
#print  (my_set)

