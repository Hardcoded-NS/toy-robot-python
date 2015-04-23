from robot import Robot
from point import Point
from table import Table
from re import compile,X
from sys import exit,argv

def main(file):
    dirs = ["NORTH", "EAST", "SOUTH", "WEST"]
    pattern = compile(r"""(?<=^)                                    # start
                          (?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
                          (?=\s?                                    # space
                          (?P<x>\d+),                               # x co-ord
                          (?P<y>\d+),                               # y co-ord
                          (?P<dir>NORTH|EAST|SOUTH|WEST)            # direction
                          $))                                       # EOL
                          """, X)

    table = Table(Point(0,0),Point(4,4))
    robot = Robot(dirs = dirs)

    with open(file) as f:
        for line in f:
            m = pattern.match(line.rstrip('\n'))
            if m is not None and m.group("cmd") == "PLACE":
                robot = robot.place(Point(float(m.group("x")),
                                          float(m.group("y"))),
                                          dirs.index(m.group("dir"))/2.0,
                                          table)
            elif m is not None and hasattr(robot,m.group("cmd").lower()):
                robot = getattr(robot,m.group("cmd").lower())()


if __name__ == '__main__':
    if len(argv) == 2:
        exit(main(argv[1]))
    else:
        print("usage: ")
