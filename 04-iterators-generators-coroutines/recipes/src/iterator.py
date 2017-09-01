#!/usr/bin/env python
import random

class RandomIntIterable:

    def __init__(self, sentence):
        self.sentence = sentence

    def __iter__(self):
        return RandomIntIterableIterator(self.sentence)


class RandomIntIterableIterator:

    def __init__(self, sentence):
        self.words = [word + " " + str(random.randint(0, 10)) for word in
                      sentence.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word



if __name__ == "__main__":
    iterable = RandomIntIterable("This is a nice sentence")
    for i in iterable:
        print(i)
