# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    print('\n')
    print('{} x {} grid: '.format(len(grid), len(grid[0])))
    for i in range(len(grid)):
        print(grid[i])
    
    count = 0
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
        
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
            expand[x][y] = count
            count += 1
            
            
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
                            action[x2][y2] = i
                print('open_list: ', open_list, '\n')
        
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    x, y = goal[0], goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2

    print('\naction:')
    print(delta)
    print(delta_name, '\n')
    for i in range(len(action)):
        print(action[i])
    print('\nexpand: ')
    for i in range(len(expand)):
        print(expand[i])
    print('\npolicy: ')
    for i in range(len(policy)):
        print(policy[i])
        
    return path, expand, policy  # make sure you return the shortest path
  
#   2 x 2 grid: 
# [0, 1]
# [0, 0]
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

# action:
# [[-1, 0], [0, -1], [1, 0], [0, 1]]
# ['^', '<', 'v', '>'] 

# [-1, -1]
# [2, 3]

# expand: 
# [0, -1]
# [1, 2]

# policy: 
# ['v', ' ']
# ['>', '*']


# 5 x 5 grid: 
# [0, 1, 1, 1, 1]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 1, 0]
# [1, 1, 1, 1, 0]
# [0, 0, 0, 1, 0]
# closed_list:  [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# open_list:  [[0, 0, 0]]
# sorted open list:  [[0, 0, 0]]
# next_node:  [0, 0, 0]
# open_list:  [[1, 1, 0]] 

# sorted open list:  [[1, 1, 0]]
# next_node:  [1, 1, 0]
# open_list:  [[2, 2, 0]] 

# sorted open list:  [[2, 2, 0]]
# next_node:  [2, 2, 0]
# open_list:  [[3, 2, 1]] 

# sorted open list:  [[3, 2, 1]]
# next_node:  [3, 2, 1]
# open_list:  [[4, 2, 2]] 

# sorted open list:  [[4, 2, 2]]
# next_node:  [4, 2, 2]
# open_list:  [[5, 1, 2]] 

# sorted open list:  [[5, 1, 2]]
# next_node:  [5, 1, 2]
# open_list:  [[6, 1, 3]] 

# sorted open list:  [[6, 1, 3]]
# next_node:  [6, 1, 3]
# open_list:  [[7, 1, 4]] 

# sorted open list:  [[7, 1, 4]]
# next_node:  [7, 1, 4]
# open_list:  [[8, 2, 4]] 

# sorted open list:  [[8, 2, 4]]
# next_node:  [8, 2, 4]
# open_list:  [[9, 3, 4]] 

# sorted open list:  [[9, 3, 4]]
# next_node:  [9, 3, 4]
# open_list:  [[10, 4, 4]] 

# sorted open list:  [[10, 4, 4]]
# next_node:  [10, 4, 4]
# final path:  [10, 4, 4]

# action:
# [[-1, 0], [0, -1], [1, 0], [0, 1]]
# ['^', '<', 'v', '>'] 

# [-1, -1, -1, -1, -1]
# [2, -1, 0, 3, 3]
# [2, 3, 3, -1, 2]
# [-1, -1, -1, -1, 2]
# [-1, -1, -1, -1, 2]

# expand: 
# [0, -1, -1, -1, -1]
# [1, -1, 5, 6, 7]
# [2, 3, 4, -1, 8]
# [-1, -1, -1, -1, 9]
# [-1, -1, -1, -1, 10]

# policy: 
# ['v', ' ', ' ', ' ', ' ']
# ['v', ' ', '>', '>', 'v']
# ['>', '>', '^', ' ', 'v']
# [' ', ' ', ' ', ' ', 'v']
# [' ', ' ', ' ', ' ', '*']


# 5 x 7 grid: 
# [0, 1, 0, 0, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 0]
# [0, 1, 0, 1, 0, 1, 1]
# [0, 0, 0, 1, 0, 0, 0]
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
# open_list:  [[11, 0, 3]] 

# sorted open list:  [[11, 0, 3]]
# next_node:  [11, 0, 3]
# open_list:  [[12, 0, 4]] 

# sorted open list:  [[12, 0, 4]]
# next_node:  [12, 0, 4]
# open_list:  [[13, 1, 4]] 

# sorted open list:  [[13, 1, 4]]
# next_node:  [13, 1, 4]
# open_list:  [[14, 2, 4]] 

# sorted open list:  [[14, 2, 4]]
# next_node:  [14, 2, 4]
# open_list:  [[15, 3, 4]] 

# sorted open list:  [[15, 3, 4]]
# next_node:  [15, 3, 4]
# open_list:  [[16, 4, 4]] 

# sorted open list:  [[16, 4, 4]]
# next_node:  [16, 4, 4]
# open_list:  [[17, 4, 5]] 

# sorted open list:  [[17, 4, 5]]
# next_node:  [17, 4, 5]
# open_list:  [[18, 4, 6]] 

# sorted open list:  [[18, 4, 6]]
# next_node:  [18, 4, 6]
# final path:  [18, 4, 6]

# action:
# [[-1, 0], [0, -1], [1, 0], [0, 1]]
# ['^', '<', 'v', '>'] 

# [-1, -1, 0, 3, 3, -1, -1]
# [2, -1, 0, -1, 2, -1, -1]
# [2, -1, 0, -1, 2, -1, -1]
# [2, -1, 0, -1, 2, -1, -1]
# [2, 3, 3, -1, 2, 3, 3]

# expand: 
# [0, -1, 10, 11, 12, -1, -1]
# [1, -1, 9, -1, 13, -1, -1]
# [2, -1, 8, -1, 14, -1, -1]
# [3, -1, 7, -1, 15, -1, -1]
# [4, 5, 6, -1, 16, 17, 18]

# policy: 
# ['v', ' ', '>', '>', 'v', ' ', ' ']
# ['v', ' ', '^', ' ', 'v', ' ', ' ']
# ['v', ' ', '^', ' ', 'v', ' ', ' ']
# ['v', ' ', '^', ' ', 'v', ' ', ' ']
# ['>', '>', '^', ' ', '>', '>', '*']


# 5 x 6 grid: 
# [0, 0, 1, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 1, 0]
# [0, 0, 1, 0, 1, 0]
# [0, 0, 1, 0, 1, 0]
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
# open_list:  [[2, 2, 0], [3, 2, 1], [3, 1, 2]] 

# sorted open list:  [[3, 2, 1], [3, 1, 2], [2, 2, 0]]
# next_node:  [2, 2, 0]
# open_list:  [[3, 2, 1], [3, 1, 2], [3, 3, 0]] 

# sorted open list:  [[3, 3, 0], [3, 2, 1], [3, 1, 2]]
# next_node:  [3, 1, 2]
# open_list:  [[3, 3, 0], [3, 2, 1], [4, 1, 3]] 

# sorted open list:  [[4, 1, 3], [3, 3, 0], [3, 2, 1]]
# next_node:  [3, 2, 1]
# open_list:  [[4, 1, 3], [3, 3, 0], [4, 3, 1]] 

# sorted open list:  [[4, 3, 1], [4, 1, 3], [3, 3, 0]]
# next_node:  [3, 3, 0]
# open_list:  [[4, 3, 1], [4, 1, 3], [4, 4, 0]] 

# sorted open list:  [[4, 4, 0], [4, 3, 1], [4, 1, 3]]
# next_node:  [4, 1, 3]
# open_list:  [[4, 4, 0], [4, 3, 1], [5, 0, 3], [5, 2, 3], [5, 1, 4]] 

# sorted open list:  [[5, 2, 3], [5, 1, 4], [5, 0, 3], [4, 4, 0], [4, 3, 1]]
# next_node:  [4, 3, 1]
# open_list:  [[5, 2, 3], [5, 1, 4], [5, 0, 3], [4, 4, 0], [5, 4, 1]] 

# sorted open list:  [[5, 4, 1], [5, 2, 3], [5, 1, 4], [5, 0, 3], [4, 4, 0]]
# next_node:  [4, 4, 0]
# open_list:  [[5, 4, 1], [5, 2, 3], [5, 1, 4], [5, 0, 3]] 

# sorted open list:  [[5, 4, 1], [5, 2, 3], [5, 1, 4], [5, 0, 3]]
# next_node:  [5, 0, 3]
# open_list:  [[5, 4, 1], [5, 2, 3], [5, 1, 4], [6, 0, 4]] 

# sorted open list:  [[6, 0, 4], [5, 4, 1], [5, 2, 3], [5, 1, 4]]
# next_node:  [5, 1, 4]
# open_list:  [[6, 0, 4], [5, 4, 1], [5, 2, 3], [6, 1, 5]] 

# sorted open list:  [[6, 1, 5], [6, 0, 4], [5, 4, 1], [5, 2, 3]]
# next_node:  [5, 2, 3]
# open_list:  [[6, 1, 5], [6, 0, 4], [5, 4, 1], [6, 3, 3]] 

# sorted open list:  [[6, 3, 3], [6, 1, 5], [6, 0, 4], [5, 4, 1]]
# next_node:  [5, 4, 1]
# open_list:  [[6, 3, 3], [6, 1, 5], [6, 0, 4]] 

# sorted open list:  [[6, 3, 3], [6, 1, 5], [6, 0, 4]]
# next_node:  [6, 0, 4]
# open_list:  [[6, 3, 3], [6, 1, 5], [7, 0, 5]] 

# sorted open list:  [[7, 0, 5], [6, 3, 3], [6, 1, 5]]
# next_node:  [6, 1, 5]
# open_list:  [[7, 0, 5], [6, 3, 3], [7, 2, 5]] 

# sorted open list:  [[7, 2, 5], [7, 0, 5], [6, 3, 3]]
# next_node:  [6, 3, 3]
# open_list:  [[7, 2, 5], [7, 0, 5], [7, 4, 3]] 

# sorted open list:  [[7, 4, 3], [7, 2, 5], [7, 0, 5]]
# next_node:  [7, 0, 5]
# open_list:  [[7, 4, 3], [7, 2, 5]] 

# sorted open list:  [[7, 4, 3], [7, 2, 5]]
# next_node:  [7, 2, 5]
# open_list:  [[7, 4, 3], [8, 3, 5]] 

# sorted open list:  [[8, 3, 5], [7, 4, 3]]
# next_node:  [7, 4, 3]
# open_list:  [[8, 3, 5]] 

# sorted open list:  [[8, 3, 5]]
# next_node:  [8, 3, 5]
# open_list:  [[9, 4, 5]] 

# sorted open list:  [[9, 4, 5]]
# next_node:  [9, 4, 5]
# final path:  [9, 4, 5]

# action:
# [[-1, 0], [0, -1], [1, 0], [0, 1]]
# ['^', '<', 'v', '>'] 

# [-1, 3, -1, 0, 3, 3]
# [2, 2, 3, 3, 3, 3]
# [2, 2, -1, 2, -1, 2]
# [2, 2, -1, 2, -1, 2]
# [2, 2, -1, 2, -1, 2]

# expand: 
# [0, 1, -1, 11, 15, 18]
# [2, 3, 5, 8, 12, 16]
# [4, 6, -1, 13, -1, 19]
# [7, 9, -1, 17, -1, 21]
# [10, 14, -1, 20, -1, 22]

# policy: 
# ['>', 'v', ' ', ' ', ' ', ' ']
# [' ', '>', '>', '>', '>', 'v']
# [' ', ' ', ' ', ' ', ' ', 'v']
# [' ', ' ', ' ', ' ', ' ', 'v']
# [' ', ' ', ' ', ' ', ' ', '*']
# Correct! 
