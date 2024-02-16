
def msg(self):
    val1 = self.val1
    val2 = self.val2
    print(f"Msg: {val1=}, {val2=}")

class C:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def msg(self):
        val1 = self.val1
        val2 = self.val2
        print(f"Msg: {val1=}, {val2=}")


c = C(3, 4)
print(f"{c.val1=}, {c.val2=}")
print(c.__dict__)

print()

c.msg()
