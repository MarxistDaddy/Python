from abc import ABC, abstractmethod



class aa(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    def multi(self, a, b):
        return a * b

class bb(aa):
    def add(self, a, b):
        return a + b

a = bb()


l = dir(bb)

for i in l:
    if not i.startswith("_"):
        print(i)

