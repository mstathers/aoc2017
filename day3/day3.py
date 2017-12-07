#!/usr/bin/env python

import math

target = 325489

## This part is clever.
squareroot = int(math.sqrt(target))
squareroot += 1 # we need a box that contains our number, so we go bigger.
if squareroot % 2 == 0: # need an odd squareroot. Again, go bigger.
    squareroot += 1
fromCenter = squareroot / 2
box = int(math.pow(squareroot, 2))

## HOT TRASH
centers = []
for edges in range(4):
    centers.append(box - fromCenter - (squareroot - 1) * edges)

stepsOnEdge = None
for center in centers:
    distance = math.fabs(int(target) - int(center))

    if (not stepsOnEdge) or (int(distance) < int(stepsOnEdge)):
        stepsOnEdge = int(distance)

    if int(stepsOnEdge) == 0:
        break


## Output
totalSteps = int(fromCenter) + int(stepsOnEdge)

print("Target: {}\n\
Squareroot: {}\n\
Steps from Center: {}\n\
Box Size: {}\n\
Centers: {}\n\
Steps On Edge: {}\n\
\n\
Total Steps: {}\n".format(\
target,\
squareroot,\
fromCenter,\
box,\
centers,\
stepsOnEdge,\
totalSteps))
