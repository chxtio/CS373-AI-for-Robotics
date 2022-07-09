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
    print('\n')
    print('{} x {} grid: '.format(len(grid), len(grid[0])))
    print(grid)
    closed_list = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    g, x, y = 0, init[0], init[1]
    closed_list[x][y] = 1
    open_list = [[g, x, y]]
    print('closed_list: ', closed_list)
    print('open_list: ', open_list)
    
    found = False
    resign = False
    
    while not found and not resign:
        # check if still have elements in open list
        if len(open_list) == 0:
            resign = True
            path = 'fail'
            print('open list empty- path: ', path)
        else:
            # remove node from list
            open_list.sort()
            open_list.reverse()
            print('sorted open list: ', open_list)
            
            # pop element w/ smallest g value
            next_node = open_list.pop()
            g, x, y = next_node[0], next_node[1], next_node[2]
            print('next_node: ', next_node)
            
            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                path = next_node
                print('final path: ', path)
                break
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
                print('open_list: ', open_list, '\n')
    
    return path


# 2 x 2 grid: 
# [[0, 1], [0, 0]]
# closed_list:  [[1, 0], [0, 0]]
# open_list:  [[0, 0, 0]]
# sorted open list:  [[0, 0, 0]]
# next_node:  [0, 0, 0]
# open_list:  [[1, 1, 0]] 

# sorted open list:  [[1, 1, 0]]
# next_node:  [1, 1, 0]
# open_list:  [[2, 1, 1]] 

# sorted open list:  [[2, 1, 1]]
# next_node:  [2, 1, 1]
# final path:  [2, 1, 1]


# 5 x 6 grid: 
# [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0]]
# closed_list:  [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# open_list:  [[0, 0, 0]]
# sorted open list:  [[0, 0, 0]]
# next_node:  [0, 0, 0]
# open_list:  [[1, 1, 0], [1, 0, 1]] 

# sorted open list:  [[1, 1, 0], [1, 0, 1]]
# next_node:  [1, 0, 1]
# open_list:  [[1, 1, 0], [2, 1, 1]] 

# sorted open list:  [[2, 1, 1], [1, 1, 0]]
# next_node:  [1, 1, 0]
# open_list:  [[2, 1, 1], [2, 2, 0]] 

# sorted open list:  [[2, 2, 0], [2, 1, 1]]
# next_node:  [2, 1, 1]
# open_list:  [[2, 2, 0], [3, 2, 1]] 

# sorted open list:  [[3, 2, 1], [2, 2, 0]]
# next_node:  [2, 2, 0]
# open_list:  [[3, 2, 1], [3, 3, 0]] 

# sorted open list:  [[3, 3, 0], [3, 2, 1]]
# next_node:  [3, 2, 1]
# open_list:  [[3, 3, 0], [4, 3, 1], [4, 2, 2]] 

# sorted open list:  [[4, 3, 1], [4, 2, 2], [3, 3, 0]]
# next_node:  [3, 3, 0]
# open_list:  [[4, 3, 1], [4, 2, 2], [4, 4, 0]] 

# sorted open list:  [[4, 4, 0], [4, 3, 1], [4, 2, 2]]
# next_node:  [4, 2, 2]
# open_list:  [[4, 4, 0], [4, 3, 1], [5, 2, 3]] 

# sorted open list:  [[5, 2, 3], [4, 4, 0], [4, 3, 1]]
# next_node:  [4, 3, 1]
# open_list:  [[5, 2, 3], [4, 4, 0], [5, 4, 1]] 

# sorted open list:  [[5, 4, 1], [5, 2, 3], [4, 4, 0]]
# next_node:  [4, 4, 0]
# open_list:  [[5, 4, 1], [5, 2, 3]] 

# sorted open list:  [[5, 4, 1], [5, 2, 3]]
# next_node:  [5, 2, 3]
# open_list:  [[5, 4, 1], [6, 1, 3]] 

# sorted open list:  [[6, 1, 3], [5, 4, 1]]
# next_node:  [5, 4, 1]
# open_list:  [[6, 1, 3], [6, 4, 2]] 

# sorted open list:  [[6, 4, 2], [6, 1, 3]]
# next_node:  [6, 1, 3]
# open_list:  [[6, 4, 2], [7, 0, 3], [7, 1, 4]] 

# sorted open list:  [[7, 1, 4], [7, 0, 3], [6, 4, 2]]
# next_node:  [6, 4, 2]
# open_list:  [[7, 1, 4], [7, 0, 3], [7, 4, 3]] 

# sorted open list:  [[7, 4, 3], [7, 1, 4], [7, 0, 3]]
# next_node:  [7, 0, 3]
# open_list:  [[7, 4, 3], [7, 1, 4], [8, 0, 4]] 

# sorted open list:  [[8, 0, 4], [7, 4, 3], [7, 1, 4]]
# next_node:  [7, 1, 4]
# open_list:  [[8, 0, 4], [7, 4, 3], [8, 1, 5]] 

# sorted open list:  [[8, 1, 5], [8, 0, 4], [7, 4, 3]]
# next_node:  [7, 4, 3]
# open_list:  [[8, 1, 5], [8, 0, 4]] 

# sorted open list:  [[8, 1, 5], [8, 0, 4]]
# next_node:  [8, 0, 4]
# open_list:  [[8, 1, 5], [9, 0, 5]] 

# sorted open list:  [[9, 0, 5], [8, 1, 5]]
# next_node:  [8, 1, 5]
# open_list:  [[9, 0, 5], [9, 2, 5]] 

# sorted open list:  [[9, 2, 5], [9, 0, 5]]
# next_node:  [9, 0, 5]
# open_list:  [[9, 2, 5]] 

# sorted open list:  [[9, 2, 5]]
# next_node:  [9, 2, 5]
# open_list:  [[10, 3, 5]] 

# sorted open list:  [[10, 3, 5]]
# next_node:  [10, 3, 5]
# open_list:  [[11, 4, 5]] 

# sorted open list:  [[11, 4, 5]]
# next_node:  [11, 4, 5]
# final path:  [11, 4, 5]


# 5 x 6 grid: 
# [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
# closed_list:  [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# open_list:  [[0, 0, 0]]
# sorted open list:  [[0, 0, 0]]
# next_node:  [0, 0, 0]
# open_list:  [[1, 1, 0]] 

# sorted open list:  [[1, 1, 0]]
# next_node:  [1, 1, 0]
# open_list:  [[2, 2, 0]] 

# sorted open list:  [[2, 2, 0]]
# next_node:  [2, 2, 0]
# open_list:  [[3, 3, 0]] 

# sorted open list:  [[3, 3, 0]]
# next_node:  [3, 3, 0]
# open_list:  [[4, 4, 0]] 

# sorted open list:  [[4, 4, 0]]
# next_node:  [4, 4, 0]
# open_list:  [[5, 4, 1]] 

# sorted open list:  [[5, 4, 1]]
# next_node:  [5, 4, 1]
# open_list:  [[6, 4, 2]] 

# sorted open list:  [[6, 4, 2]]
# next_node:  [6, 4, 2]
# open_list:  [[7, 3, 2]] 

# sorted open list:  [[7, 3, 2]]
# next_node:  [7, 3, 2]
# open_list:  [[8, 2, 2]] 

# sorted open list:  [[8, 2, 2]]
# next_node:  [8, 2, 2]
# open_list:  [[9, 1, 2]] 

# sorted open list:  [[9, 1, 2]]
# next_node:  [9, 1, 2]
# open_list:  [[10, 0, 2]] 

# sorted open list:  [[10, 0, 2]]
# next_node:  [10, 0, 2]
# open_list:  [[11, 0, 3]] 

# sorted open list:  [[11, 0, 3]]
# next_node:  [11, 0, 3]
# open_list:  [[12, 0, 4]] 

# sorted open list:  [[12, 0, 4]]
# next_node:  [12, 0, 4]
# open_list:  [[13, 1, 4], [13, 0, 5]] 

# sorted open list:  [[13, 1, 4], [13, 0, 5]]
# next_node:  [13, 0, 5]
# open_list:  [[13, 1, 4], [14, 1, 5]] 

# sorted open list:  [[14, 1, 5], [13, 1, 4]]
# next_node:  [13, 1, 4]
# open_list:  [[14, 1, 5], [14, 2, 4]] 

# sorted open list:  [[14, 2, 4], [14, 1, 5]]
# next_node:  [14, 1, 5]
# open_list:  [[14, 2, 4], [15, 2, 5]] 

# sorted open list:  [[15, 2, 5], [14, 2, 4]]
# next_node:  [14, 2, 4]
# open_list:  [[15, 2, 5], [15, 3, 4]] 

# sorted open list:  [[15, 3, 4], [15, 2, 5]]
# next_node:  [15, 2, 5]
# open_list:  [[15, 3, 4], [16, 3, 5]] 

# sorted open list:  [[16, 3, 5], [15, 3, 4]]
# next_node:  [15, 3, 4]
# open_list:  [[16, 3, 5], [16, 4, 4]] 

# sorted open list:  [[16, 4, 4], [16, 3, 5]]
# next_node:  [16, 3, 5]
# open_list:  [[16, 4, 4], [17, 4, 5]] 

# sorted open list:  [[17, 4, 5], [16, 4, 4]]
# next_node:  [16, 4, 4]
# open_list:  [[17, 4, 5]] 

# sorted open list:  [[17, 4, 5]]
# next_node:  [17, 4, 5]
# final path:  [17, 4, 5]


# 5 x 7 grid: 
# [[0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
# closed_list:  [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# open_list:  [[0, 0, 0]]
# sorted open list:  [[0, 0, 0]]
# next_node:  [0, 0, 0]
# open_list:  [[1, 1, 0]] 

# sorted open list:  [[1, 1, 0]]
# next_node:  [1, 1, 0]
# open_list:  [[2, 2, 0]] 

# sorted open list:  [[2, 2, 0]]
# next_node:  [2, 2, 0]
# open_list:  [[3, 3, 0]] 

# sorted open list:  [[3, 3, 0]]
# next_node:  [3, 3, 0]
# open_list:  [[4, 4, 0]] 

# sorted open list:  [[4, 4, 0]]
# next_node:  [4, 4, 0]
# open_list:  [[5, 4, 1]] 

# sorted open list:  [[5, 4, 1]]
# next_node:  [5, 4, 1]
# open_list:  [[6, 4, 2]] 

# sorted open list:  [[6, 4, 2]]
# next_node:  [6, 4, 2]
# open_list:  [[7, 3, 2]] 

# sorted open list:  [[7, 3, 2]]
# next_node:  [7, 3, 2]
# open_list:  [[8, 2, 2]] 

# sorted open list:  [[8, 2, 2]]
# next_node:  [8, 2, 2]
# open_list:  [[9, 1, 2]] 

# sorted open list:  [[9, 1, 2]]
# next_node:  [9, 1, 2]
# open_list:  [[10, 0, 2]] 

# sorted open list:  [[10, 0, 2]]
# next_node:  [10, 0, 2]
# open_list:  [] 

# open list empty- path:  fail
# Correct! 
