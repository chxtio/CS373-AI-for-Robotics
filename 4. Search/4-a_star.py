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

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost, heuristic):
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
    h = heuristic[x][y]
    f = g + h
    closed_list[x][y] = 1
    open_list = [[f, g, h, x, y]]
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
            g, x, y = next_node[1], next_node[3], next_node[4]
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
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open_list.append([f2, g2, h2, x2, y2])
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

##    print('\naction:')
##    print(delta)
##    print(delta_name, '\n')
##    for i in range(len(action)):
##        print(action[i])
    print('\nexpand: ')
    for i in range(len(expand)):
        print(expand[i])
    print('\npolicy: ')
    for i in range(len(policy)):
        print(policy[i])
    print('\n')
        
    return path, expand, policy  # make sure you return the shortest path

print(search(grid,init,goal,cost, heuristic))



##5 x 6 grid:
##[0, 1, 0, 0, 0, 0]
##[0, 1, 0, 0, 0, 0]
##[0, 1, 0, 0, 0, 0]
##[0, 1, 0, 0, 0, 0]
##[0, 0, 0, 0, 1, 0]
##closed_list:  [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
##open_list:  [[9, 0, 9, 0, 0]]
##sorted open list:  [[9, 0, 9, 0, 0]]
##next_node:  [9, 0, 9, 0, 0]
##open_list:  [[9, 1, 8, 1, 0]]
##
##sorted open list:  [[9, 1, 8, 1, 0]]
##next_node:  [9, 1, 8, 1, 0]
##open_list:  [[9, 2, 7, 2, 0]]
##
##sorted open list:  [[9, 2, 7, 2, 0]]
##next_node:  [9, 2, 7, 2, 0]
##open_list:  [[9, 3, 6, 3, 0]]
##
##sorted open list:  [[9, 3, 6, 3, 0]]
##next_node:  [9, 3, 6, 3, 0]
##open_list:  [[9, 4, 5, 4, 0]]
##
##sorted open list:  [[9, 4, 5, 4, 0]]
##next_node:  [9, 4, 5, 4, 0]
##open_list:  [[9, 5, 4, 4, 1]]
##
##sorted open list:  [[9, 5, 4, 4, 1]]
##next_node:  [9, 5, 4, 4, 1]
##open_list:  [[9, 6, 3, 4, 2]]
##
##sorted open list:  [[9, 6, 3, 4, 2]]
##next_node:  [9, 6, 3, 4, 2]
##open_list:  [[11, 7, 4, 3, 2], [9, 7, 2, 4, 3]]
##
##sorted open list:  [[11, 7, 4, 3, 2], [9, 7, 2, 4, 3]]
##next_node:  [9, 7, 2, 4, 3]
##open_list:  [[11, 7, 4, 3, 2], [11, 8, 3, 3, 3]]
##
##sorted open list:  [[11, 8, 3, 3, 3], [11, 7, 4, 3, 2]]
##next_node:  [11, 7, 4, 3, 2]
##open_list:  [[11, 8, 3, 3, 3], [13, 8, 5, 2, 2]]
##
##sorted open list:  [[13, 8, 5, 2, 2], [11, 8, 3, 3, 3]]
##next_node:  [11, 8, 3, 3, 3]
##open_list:  [[13, 8, 5, 2, 2], [13, 9, 4, 2, 3], [11, 9, 2, 3, 4]]
##
##sorted open list:  [[13, 9, 4, 2, 3], [13, 8, 5, 2, 2], [11, 9, 2, 3, 4]]
##next_node:  [11, 9, 2, 3, 4]
##open_list:  [[13, 9, 4, 2, 3], [13, 8, 5, 2, 2], [13, 10, 3, 2, 4], [11, 10, 1, 3, 5]]
##
##sorted open list:  [[13, 10, 3, 2, 4], [13, 9, 4, 2, 3], [13, 8, 5, 2, 2], [11, 10, 1, 3, 5]]
##next_node:  [11, 10, 1, 3, 5]
##open_list:  [[13, 10, 3, 2, 4], [13, 9, 4, 2, 3], [13, 8, 5, 2, 2], [13, 11, 2, 2, 5], [11, 11, 0, 4, 5]]
##
##sorted open list:  [[13, 11, 2, 2, 5], [13, 10, 3, 2, 4], [13, 9, 4, 2, 3], [13, 8, 5, 2, 2], [11, 11, 0, 4, 5]]
##next_node:  [11, 11, 0, 4, 5]
##final path:  [11, 11, 0, 4, 5]
##
##
##expand (Greedy):
##[0, -1, 14, 18, -1, -1]
##[1, -1, 11, 15, 19, -1]
##[2, -1, 9, 12, 16, 20]
##[3, -1, 7, 10, 13, 17]
##[4, 5, 6, 8, -1, 21]

##expand (A*):
##[0, -1, -1, -1, -1, -1]
##[1, -1, -1, -1, -1, -1]
##[2, -1, -1, -1, -1, -1]
##[3, -1, 8, 9, 10, 11]
##[4, 5, 6, 7, -1, 12]
##
##policy:
##['v', ' ', ' ', ' ', ' ', ' ']
##['v', ' ', ' ', ' ', ' ', ' ']
##['v', ' ', ' ', ' ', ' ', ' ']
##['v', ' ', ' ', '>', '>', 'v']
##['>', '>', '>', '^', ' ', '*']






