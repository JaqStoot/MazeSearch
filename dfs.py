'''
DETAILS: This program is a Depth-First search algorithm used to solve a maze
Additionally, it displays:
    a. The solution and its path cost;
    b. Number of nodes expanded;
    c. Maximum tree depth searched;
    d. Maximum size of the fringe.
    
AUTHOR: Josh Butler
'''

from pyamaze import maze, agent, textLabel

# Define the DFS search algorithm function
def DFS(m, start=None):
    # Set the start and goal nodes
    if start is None:
        start = (m.rows, m.cols)
    explored = {start}
    frontier = [start]
    dfsPath = {}
    dSeacrh = []
    directions = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
    # Initialize counters for expanded, max depth, and max fringe
    num_expanded = 0
    max_depth = 0
    max_fringe_size = 1  # start with 1 for the initial node
    while frontier:
        currCell = frontier.pop()
        dSeacrh.append(currCell)
        if currCell == m._goal:
            break
        poss = 0
        for d, (dx, dy) in directions.items():
            x, y = currCell[0] + dx, currCell[1] + dy
            child = (x, y)
            if m.maze_map[currCell][d] and child not in explored:
                poss += 1
                explored.add(child)
                frontier.append(child)
                dfsPath[child] = currCell
        if poss > 1:
            m.markCells.append(currCell)
        num_expanded += 1
        max_depth = max(max_depth, len(dSeacrh))
        max_fringe_size = max(max_fringe_size, len(frontier))
    if currCell == m._goal:
        path_cost = len(dSeacrh) - 1  # subtract 1 to exclude the start node
        fwdPath = {}
        cell = m._goal
        while cell != start:
            fwdPath[dfsPath[cell]] = cell
            cell = dfsPath[cell]
        return dSeacrh, fwdPath, path_cost, num_expanded, max_depth, max_fringe_size
    else:
        return [], {}, float('inf'), num_expanded, max_depth, max_fringe_size

if __name__ == '__main__':
    m = maze(10, 10) #changeable to any dimensions for the maze
    m.CreateMaze()

    dSeacrh, fwdPath, path_cost, num_expanded, max_depth, max_fringe_size = DFS(m) # (5,1) is Start Cell, Change that to any other valid cell

    a = agent(m, footprints=True)
    m.tracePath({a: dSeacrh}, showMarked=True)
    l1= textLabel(m, 'DFS Path Cost:', path_cost)
    l2= textLabel(m, 'Nodes Expanded:', num_expanded)
    l3= textLabel(m, 'Max Depth:', max_depth)
    l4= textLabel(m, 'Max Fringe:', max_fringe_size)   

    m.run()
