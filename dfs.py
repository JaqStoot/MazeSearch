def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = {start}
    frontier = [start]
    dfsPath = {}
    dSeacrh = []
    directions = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
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
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return dSeacrh, dfsPath, fwdPath