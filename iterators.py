class OddIterator:
    # constuctor accepts iterable 'it'
    # only return integers from 'it' that are odd
    # use __init__, __iter__, __next__ since iterator
    # DO NOT USE ITERTOOLS**
    def __init__(self, it):
        self.iterable = it
        self.iterator = iter(it)

    def __iter__(self):
        return self

    def __next__(self):
        while True: # return the odd valued result
            result = next(self.iterator)
            if result % 2 != 0:
                return result

class Last:
    def __init__(self, it, count):
        self.iterator = iter(it)
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        # Iterate over the iterable
        last_count = [] # store last values here
        for element in self.iterator:
            last_count.append(element) # append the values to the list
            if len(last_count) > self.count:
                last_count.pop(0) # if the length of the mutable list is larger than count, pop

        return last_count


