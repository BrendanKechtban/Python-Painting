import sys
from graphics import *


def main():
    class RoadLines:
        def __init__(self, p1x: int, p1y: int, p2x: int, p2y: int, width: int, color: str, window):
            self.p1x = p1x
            self.p1y = p1y
            self.p2x = p2x
            self.p2y = p2y
            self.width = width
            self.color = color

            line = self
            print(line)
            line = Line(Point(p1x, p1y), Point(p2x, p2y))
            line.setWidth(width)
            line.setFill(color)
            line.draw(window)
            print(line.getP1(), line.getP2())

    win = GraphWin("Art by Brendan", 800, 600)

    sky = Rectangle(Point(0, 0), Point(800, 600))
    sky.setFill("skyblue")
    sky.draw(win)

    sun = Circle(Point(110, 105), 100)
    sun.setFill("yellow")
    sun.draw(win)

    grass = Rectangle(Point(0, 400), Point(800, 600))
    grass.setFill("green")
    grass.draw(win)

    road = Rectangle(Point(425, 600), Point(325, 400))
    road.setFill("grey")
    road.setOutline("grey")
    road.draw(win)

    road2 = Rectangle(Point(0, 450), Point(325, 540))
    road2.setFill("grey")
    road2.setOutline("grey")
    road2.draw(win)

    road3 = Rectangle(Point(425, 450), Point(800, 540))
    road3.setFill("grey")
    road3.setOutline("grey")
    road3.draw(win)

    road3_line1 = RoadLines(20, 490, 40, 490, 5, "yellow", win)
    road3_line2 = RoadLines(70, 490, 90, 490, 5, "yellow", win)
    road3_line3 = RoadLines(120, 490, 140, 490, 5, "yellow", win)
    road3_line4 = RoadLines(170, 490, 190, 490, 5, "yellow", win)
    road3_line5 = RoadLines(220, 490, 240, 490, 5, "yellow", win)
    road3_line6 = RoadLines(270, 490, 290, 490, 5, "yellow", win)
    road3_line7 = RoadLines(440, 490, 460, 490, 5, "yellow", win)
    road3_line8 = RoadLines(490, 490, 510, 490, 5, "yellow", win)
    road3_line9 = RoadLines(540, 490, 560, 490, 5, "yellow", win)
    road3_line10 = RoadLines(590, 490, 610, 490, 5, "yellow", win)
    road3_line11 = RoadLines(640, 490, 660, 490, 5, "yellow", win)
    road3_line12 = RoadLines(690, 490, 710, 490, 5, "yellow", win)
    road3_line13 = RoadLines(740, 490, 760, 490, 5, "yellow", win)

    is_day = False

    animation_start = False
    if road3_line13.color == "yellow":
        animation_start = True
    else:
        animation_start = False

    def day_handler(day_state, movey, animationstart):
        import time
        while animationstart:
            if sun.getCenter().y + 100 < win.getHeight():
                day_state = True
            else:
                day_state = False

            while day_state:
                print(day_state)
                # print(sun.getCenter())
                time.sleep(0.2)
                car.move(car_move, 0)
                print(car.getAnchor().x)
                if car.getAnchor().x > 800:
                    car.move(car_move*-70, 0)
                time.sleep(0.13)
                sun.move(0, movey)
                if sun.getCenter().y + 100 > win.getHeight():
                    sky.setFill('black')
                    print(f"Sunrise in 9 seconds")
                    time.sleep(5)
                if sun.getCenter().y + 100 > win.getHeight() or sun.getCenter().y - 100 < 0:
                    time.sleep(4)
                    movey *= -1
                    if sun.getCenter().y + 100 > win.getHeight() or sun.getCenter().y < 0:
                        sky.setFill("skyblue")
                if not day_state:
                    break

    road_line_width = 5
    road_line_color = "yellow"
    road_line1 = RoadLines(375, 595, 375, 575, road_line_width, road_line_color, win)
    print("Line 1 instantiated")
    road_line2 = RoadLines(375, 560, 375, 540, road_line_width, road_line_color, win)
    print("Line 2 instantiated")
    road_line4 = RoadLines(375, 440, 375, 420, road_line_width, road_line_color, win)
    print("Line 4 instantiated")

    car = Image(Point(50, 470), "car.gif")
    car.draw(win)



    # lol = RoadLines(150, 200, 150, 300, 5, "green", win)
    # sun_movex = 0
    sun_movey = 5
    car_move = 15

    day_handler(is_day, sun_movey,  animation_start)


if __name__ == '__main__':
    main()