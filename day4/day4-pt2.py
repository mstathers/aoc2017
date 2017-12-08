#!/usr/bin/env python

import re

numberOfGoodPhrases = 0
with open("input.txt") as file:
    lines = [line.split(",") for line in file.read().splitlines()]
    for line in lines:
        badLine = 0

        words = line[0].split(" ")
        for word in range(len(words)):
            for match in range(len(words)):
                # we don't want it to match itself
                if word == match:
                    continue

                # check if length is the same length
                if len(words[word]) != len(words[match]):
                    continue

                srcLetters = list(words[word])
                dstLetters = list(words[match])
                srcUsed = []
                for letter in srcLetters:
                    x = letter
                    if x in dstLetters:
                        dstLetters.remove(x)
                        srcUsed.append(letter)

                if (len(dstLetters) == 0) and (srcLetters.sort() == srcUsed.sort()):
                    badLine = 1
                    break

        if badLine == 0:
            numberOfGoodPhrases += 1

print("The number of good passphrases: {}".format(numberOfGoodPhrases))
