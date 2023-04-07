'''
DETAILS: This program is an A* search algorithm that uses the Mangattan distance 
as it's heuristic function and automatically searches a maze and displays:
    a. The solution and its path cost;
    b. Number of nodes expanded;
    c. Maximum tree depth searched;
    d. Maximum size of the fringe.
    
AUTHOR: Jack Stout
'''


from pyamaze import maze,agent,textLabel
from queue import PriorityQueue

# Define the Manhattan distance heuristic function h
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)

# Define the A* search algorithm function
def aStar(m):
    # Set the start and goal nodes
    start = (m.rows, m.cols)
    goal = (1, 1)

    # Initialize the dictionaries to store g and f scores for each cell
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)

    # Create a priority queue to store open nodes
    open = PriorityQueue()
    # Add the start node to the priority queue
    open.put((h(start, goal), h(start, goal), start))

    # Initialize a dictionary to store the path
    aPath = {}

     # Initialize counters for the number of nodes expanded, the maximum tree depth searched, and the maximum fringe size
    visited = set()
    max_depth = 0
    max_fringe = 1

    # Loop until the priority queue is empty or the goal is found
    while not open.empty():
        # Get the node with the lowest f score
        currCell = open.get()[2]
        # Check if the goal has been reached
        if currCell == goal:
            break
        visited.add(currCell)
        # Loop through all neighboring cells
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                # Compute the child cell
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])

                # Compute the g and f scores for the child cell
                if childCell not in visited:
                    temp_g_score = g_score[currCell] + 1
                    temp_f_score = temp_g_score + h(childCell, goal)

                    # Update the g and f scores and add the child cell to the priority queue if it has a lower f score
                    if temp_f_score < f_score[childCell]:
                        g_score[childCell] = temp_g_score
                        f_score[childCell] = temp_f_score
                        open.put((temp_f_score, h(childCell, goal), childCell))
                        aPath[childCell] = currCell
                        if temp_g_score > max_depth:
                            max_depth = temp_g_score
                    max_fringe = max(max_fringe, open.qsize())

    # calculate solution path and path cost
    path = [goal]
    cost = 0
    cell = goal
    while cell != start:
        cost += 1
        path.append(aPath[cell])
        cell = aPath[cell]
    path.reverse()

    return path, cost, len(visited), max_depth, max_fringe

#Create Maze and Run Algorithm
if __name__ == '__main__':
    #Create maze by dimensions below, can be adjusted to anything
    m = maze(10,10) #changeable to any dimensions for the maze
    m.CreateMaze()

    # run A* search and get results
    path, cost, nodes_expanded, max_depth, max_fringe = aStar(m)

    # display maze and solution path
    a = agent(m, footprints=True)
    m.tracePath({a: path})
    l1 = textLabel(m, 'A* Path Cost:', cost)
    l2 = textLabel(m, 'Nodes Expanded:', nodes_expanded)
    l3 = textLabel(m, 'Max Depth:', max_depth)
    l4 = textLabel(m, 'Max Fringe:', max_fringe)

    m.run()