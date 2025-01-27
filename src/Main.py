from Window import window
from Maze import maze
import random


def main():
    num_rows = 10
    num_cols = 10
    margin = 25
    screen_x = 1000
    screen_y = 1000
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = window(screen_x, screen_y)

    maze1 = maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, random.randint(1,9999))
    print("maze created")
    is_solvable = maze1.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()
