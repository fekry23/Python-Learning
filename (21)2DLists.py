#This is an example of 2d lists
number_grid = [
    [1,2,3], #[0] , [0][1][3]
    [4,5,6], #[1] , [0][1][3]
    [7,8,9], #[2] , [0][1][3]
    [0]      #[3] , [0][1][3]
]

#Nested Loop
for row in number_grid:
    for col in row:
        print(col)