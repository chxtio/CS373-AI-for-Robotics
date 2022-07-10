# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
##                print('current: ({},{})'.format(x,y))
                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        print('change @ {},{} to 0'.format(x,y))
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
##                        print('next: ({},{})'.format(x2,y2))

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) \
                               and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost
##                            print('v2: ', v2)

                            if v2 < value[x][y]:
                                print('change @ {},{} to v2 = {}'.format(x,y, v2))
                                change = True
                                value[x][y] = v2

        
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 

value = compute_value(grid,goal,cost)
for i in range(len(value)):
    print(value[i])

##change @ 4,5 to 0
##change @ 3,5 to v2 = 1
##change @ 2,5 to v2 = 2
##change @ 3,4 to v2 = 2
##change @ 1,5 to v2 = 3
##change @ 2,4 to v2 = 3
##change @ 3,3 to v2 = 3
##change @ 4,3 to v2 = 4
##change @ 0,5 to v2 = 4
##change @ 1,4 to v2 = 4
##change @ 2,3 to v2 = 4
##change @ 3,2 to v2 = 4
##change @ 4,2 to v2 = 5
##change @ 0,4 to v2 = 5
##change @ 1,3 to v2 = 5
##change @ 2,2 to v2 = 5
##change @ 4,1 to v2 = 6
##change @ 0,3 to v2 = 6
##change @ 1,2 to v2 = 6
##change @ 4,0 to v2 = 7
##change @ 0,2 to v2 = 7
##change @ 3,0 to v2 = 8
##change @ 2,0 to v2 = 9
##change @ 1,0 to v2 = 10
##change @ 0,0 to v2 = 11
##
##[11, 99, 7, 6, 5, 4]
##[10, 99, 6, 5, 4, 3]
##[9, 99, 5, 4, 3, 2]
##[8, 99, 4, 3, 2, 1]
##[7, 6, 5, 4, 99, 0]
