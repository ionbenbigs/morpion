grille = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def print_grid(grid):
    """
        Print grid in the console
        @param grid (list): grid
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(f"[{grid[i][j]}]", end=" ")
        print("")

print_grid(grille)