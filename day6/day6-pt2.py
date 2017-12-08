#!/usr/bin/env python

rawInput = '4    1    15    12    0    9    9    5    5    8    7    3    14    5    12    3'

blocks = rawInput.split("    ")
lenBlocks = len(blocks)

saved = str(blocks)
memory = []

while True:
    if saved in memory:
        start = memory.index(saved)
        diff = len(memory) - start
        print(diff)
        break
    memory.append(saved)

    # Find which block has the largest value
    value = 0
    biggestBlock = 0
    for idx in range(lenBlocks):
       if int(blocks[idx]) > value:
            value = int(blocks[idx])
            biggestBlock = idx

    # zero out the biggest block
    blocks[biggestBlock] = 0

    # Set current pos to that of the biggest block
    position = biggestBlock

    # redistribute
    while value != 0:
        # check if we're at the end, incremement and wrap if needed
        if position == lenBlocks - 1:
            position = 0
        else:
            position += 1

        # add 1 to value of block at cur pos.
        blocks[position] = int(blocks[position]) + 1

        # reduce remaining value to distribute
        value -= 1

    # store the current block state into memory to check later
    saved = str(blocks)
