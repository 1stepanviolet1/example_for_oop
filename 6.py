

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance


class C(Singleton):
    def __init__(self, val1, val2) -> None:
        self.val1 = val1
        self.val2 = val2


c1 = C(1, 2)
c2 = C(3, 4)

print(c1 is c2)
print(c1.__dict__)
print(c2.__dict__)
