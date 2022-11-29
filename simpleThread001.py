import threading
class Async(threading.Thread):
    def __init__(self, element, nm):
        threading.Thread.__init__(self)
        self.data = []
        self.element = element
        self.nm = nm

    def run(self):
        for i in self.element:
            print(i, self.nm)
            self.data.append( i )

a1 = Async(range(1000), 'async-1')
a2 = Async(range(1000), 'async-2')
a1.start()
a2.start()
a1.join()
a2.join()
# print(a1.data, a2.data)


