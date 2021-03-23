
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Jim","Oscar", "Toby"]
friends.insert(1, "Kelly")             #it will insert an elements inside the list at the targeted index
friends.remove("Jim")                  #it will remove the targeted elements
friends.append("Creed")                #it will append to the back of the list
friends.sort()                         #it will sort in acsending order
print(friends)

friends.reverse()                     #it will sort in reverse order
print(friends)

friends2 = friends.copy()              #it will make a copy for the list
print(friends2)

friends.extend(lucky_numbers)          #it will append another list to an another list, friends extend lucky_numbers
friends.pop()                          #it will pop the last elements inside the list
print(friends)
print(friends.index("Kelly"))          #it will return the index of the targeted element
print(friends.count("Jim"))            #it will count how many targeted element
print(friends)

friends.clear()                        #it will clear all the elements inside the list
print(friends)