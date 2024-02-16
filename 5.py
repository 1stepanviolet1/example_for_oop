

class C:
    def __new__(cls, val1, val2):
        print("---new---")
        return object.__new__(cls)
    
    def __init__(self, val1, val2) -> None:
        print("---init---")
        self.val1 = val1
        self.val2 = val2


c = C(1, 2)
