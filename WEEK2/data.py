my_list=[]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("after appending; ",my_list)

my_list.insert(1,15)
print("after inserting; ",my_list)

my_list.extend([50,60,70])
print("after extending; ",my_list)

my_list.pop()
print("after removing last element; ",my_list)

my_list.sort()
print("after sorting; ",my_list)

print("index of 30; ",my_list.index(30))

print("final list; ",my_list)
