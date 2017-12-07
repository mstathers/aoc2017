#!/usr/bin/env python

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

                if words[word] == words[match]:
                    badLine = 1
                    break


        if badLine == 0:
            numberOfGoodPhrases += 1

print("The number of good passphrases: {}".format(numberOfGoodPhrases))
