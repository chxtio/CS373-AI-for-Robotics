# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed_list = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    print(closed_list)
    closed_list[init[0]][init[1]] = 1
    x =init[0]
    y = init[1]
    g = 0
    
    open_list = [[g, x, y]]
    
    found = False
    resign = False
    
    while not found and not resign:
        # check if still have elements in open list
        if len(open_list) == 0:
            resign = True
            path = 'fail'
            print('path: ', path)
        else:
            # remove node from list
            open_list.sort()
            open_list.reverse()
            
            # pop element w/ smallest g value
            next_node = open_list.pop()
            g, x, y = next_node[0], next_node[1], next_node[2]
            
            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                path = next_node
                print('path: ', path)
            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if grid[x2][y2] != 1 and closed_list[x2][y2] != 1:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            closed_list[x2][y2] = 1
    
    return path