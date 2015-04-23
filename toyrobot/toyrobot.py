from .robot import *
from .point import *
from .table import *


def main():
    dirs=["NORTH", "EAST", "SOUTH", "WEST"]
    table = Table(Point(0,0),Point(4,4))
    robot = Robot(table = table, dirs = dirs)
    robot.report()
