class Sentences:

    # Original method.
    def sentence(self):
        new_phrase = ""
        for x in self:
            print(x)
            new_phrase += x
        return new_phrase


class MySentenceIterator(object):

    # Init method.
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter_obj = iter(iterable)
        self.value = object

    # Iterator method.
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                next_obj = next(self.iter_obj)
                return next_obj
            except StopIteration:
                self.iter_obj = iter(self.iterable)

