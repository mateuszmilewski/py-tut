class Mapping:
    def __init__(self, iterable):
        self.items = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items.append(item)

    __update = update # interesting priv copy

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items.append(item)


ms = MappingSubclass([1,2])
ms.update([1,2,3],[22,33,44])
print(ms.items)