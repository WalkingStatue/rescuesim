def visualize_grid(grid):

    # Print the legend
    print("Legend:")
    print("  : Open terrain")
    print("#: Building")
    print(".: Rubble")
    print("X: Fallen tree")
    print("A: Agent")
    print("S: Survivor")
    print()  # Add a blank line for separation

    for row in grid:
        for cell in row:
            if cell == 0:
                print(' ', end=' ') 
            elif cell == 2: 
                print('A', end=' ') 
            elif cell == -1: 
                print('S', end=' ')
            elif cell == 3:
                print('#', end=' ')
            elif cell == 5:
                print('.', end=' ') 
            elif cell == 10:
                print('X', end=' ') 
        print()  # Move to the next line after each row