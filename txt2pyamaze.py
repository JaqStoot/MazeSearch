from pyamaze import maze

def create_maze_from_file(filename):
    # Open the file
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        
        # Split the contents into rows
        rows = contents.strip().split('\n')
        
        # Create the maze object
        m = maze(len(rows[0]), len(rows))
        
        # Loop through each row
        for y, row in enumerate(rows):
            # Loop through each cell in the row
            for x, cell in enumerate(row):
                # If the cell is a wall, set the corresponding maze cell to a wall
                if cell == '%':
                    m.set_wall(x, y)
        
        # Return the maze object
        return m

# Example usage
m = create_maze_from_file('maze_files/smallMaze.txt')
m.run()