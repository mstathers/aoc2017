#!/usr/bin/env python


instructions = open("input.txt").read().splitlines()

curPos = 0
totalSteps = 0


while True:
    try:
        jump = int(instructions[curPos])
        if jump >= 3:
            instructions[curPos] = jump - 1
        else:
            instructions[curPos] = jump + 1
        curPos += jump
        totalSteps += 1

    except IndexError:
        break

print(totalSteps)
