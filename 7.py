

class C:
    val3 = None

    def __init__(self, val1, val2) -> None:
        self.val1 = val1
        self.val2 = val2
        self.val3 = self.__sum(val1, val2)
    
    @staticmethod
    def __sum(a, b):
        return a + b
    
    @classmethod
    def set_global_val3(cls, new_val3):
        cls.val3 = new_val3


c = C(3, 4)
print(c.__dict__)

print()

c.set_global_val3(1)
print(f"{c.val3=}")
print(f"{C.val3=}")

