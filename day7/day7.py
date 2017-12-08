#!/usr/bin/env python

import re

discDirectory = {}

info = open("input.txt").read().splitlines()

def parseNameWeight(nameWeight):
    name, weight = nameWeight.split(" ")
    p = re.compile('\d+')
    weight = p.findall(weight)[0]
    return name, weight

# parse data
for line in info:
    if "->" in line:
        nameWeight, childDiscs = line.split(" -> ")
        name, weight = parseNameWeight(nameWeight)
        children = childDiscs.split(", ")

        for child in children:
            discDirectory[child] = name


def iterDict(parent):
    if parent in discDirectory:
        iterDict(discDirectory[parent])
    else:
        print(parent)


first = list(discDirectory.keys())[0]
iterDict(first)


