#Syntax : for VARIABLE(can be anything) in ARGUMENTS
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

#Syntax range : range(start,last)
for index in range(len(friends)):               #len to count the length
    print(friends[index])