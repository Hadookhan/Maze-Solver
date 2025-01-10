from Window import window
from Maze import maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = window(screen_x, screen_y)

    maze1 = maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 15)
    print("maze created")
    is_solvable = maze1.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()
