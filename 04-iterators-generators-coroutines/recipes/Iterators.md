# Iterator
In Python Iterators consist of two different parts. The `Iterable` needs to implement the `__iter__` method returning the second part - the `Iterator` which needs to implement the `__next__` method.
The following code shall depict an exampe iterator which takes a sentence and adds a random number to every word:

```python
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
```

Based on the classes the following output can be generated:

```python 
iterable = RandomIntIterable("This is a nice sentence")
for i in iterable:
	print(i)

>> This 8
>> is 4
>> a 9
>> nice 8
>> sentence 1	
```
