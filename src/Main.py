from Window import window, Point, Line

def main():
    win = window(800,600)
    line = Line(Point(200,100), Point(400,400))
    win.draw_line(line,"black")
    win.wait_for_close()

main()