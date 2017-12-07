#!/usr/bin/env python

import math

target = 325489

coord = {"0,0": 1}
orientation = "right"

def sumSurrounding(position):
    x,y = position.split(",")
    thisSum = 0
    # check 0
    if "{},{}".format(x,int(y)+1) in coord:
        thisSum += coord["{},{}".format(x,int(y)+1)]
    # check 45
    if "{},{}".format(int(x)+1,int(y)+1) in coord:
        thisSum += coord["{},{}".format(int(x)+1,int(y)+1)]
    # check 90
    if "{},{}".format(int(x)+1,y) in coord:
        thisSum += coord["{},{}".format(int(x)+1,y)]
    # check 135
    if "{},{}".format(int(x)+1,int(y)-1) in coord:
        thisSum += coord["{},{}".format(int(x)+1,int(y)-1)]
    # check 180
    if "{},{}".format(x,int(y)-1) in coord:
        thisSum += coord["{},{}".format(x,int(y)-1)]
    # check 225
    if "{},{}".format(int(x)-1,int(y)-1) in coord:
        thisSum += coord["{},{}".format(int(x)-1,int(y)-1)]
    # check 270
    if "{},{}".format(int(x)-1,y) in coord:
        thisSum += coord["{},{}".format(int(x)-1,y)]
    # check 315
    if "{},{}".format(int(x)-1,int(y)+1) in coord:
        thisSum += coord["{},{}".format(int(x)-1,int(y)+1)]

    return thisSum


def goingRight(position):
    x,y = position.split(",")
    global orientation
    # check if position above the next position is open
    if "{},{}".format(int(x)+1,int(y)+1) not in coord:
        orientation = "right"
    # shift position right
    return "{},{}".format(int(x)+1,y)


def goingUp(position):
    x,y = position.split(",")
    global orientation
    # check if position to left of the next position is open
    if "{},{}".format(int(x)-1,int(y)+1) not in coord:
        orientation = "top"
    # shift position up
    return "{},{}".format(x,int(y)+1)

def goingLeft(position):
    x,y = position.split(",")
    global orientation
    # check if position below next position is open
    if "{},{}".format(int(x)-1,int(y)-1) not in coord:
        orientation = "left"
    # shift position left
    return "{},{}".format(int(x)-1,y)

def goingDown(position):
    x,y = position.split(",")
    global orientation
    # check if position to right of next position is open
    if "{},{}".format(int(x)+1,int(y)-1) not in coord:
        orientation = "bottom"
    # shift position down
    return "{},{}".format(x,int(y)-1)

orientDict = {
    "bottom": goingRight,
    "right": goingUp,
    "top": goingLeft,
    "left": goingDown,
}

valueOfSquare = 0
curPosition = "1,0"
while valueOfSquare < target:
    valueOfSquare = int(sumSurrounding(curPosition))
    coord[curPosition] = valueOfSquare

    print("{} {} {}".format(orientation, curPosition, valueOfSquare))
    curPosition = orientDict[orientation](curPosition)

