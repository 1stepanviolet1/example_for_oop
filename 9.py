class Integer:
    def __set_name__(self, owner, name):
        print("---set_name---")
        self._name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        print("---get---")
        return getattr(instance, self._name)
    
    def __set__(self, instance, value):
        print("---set---")
        if not isinstance(value, int):
            raise TypeError
        
        setattr(instance, self._name, value)


class C:
    val1 = Integer()
    val2 = Integer()
    val3 = Integer()

    def __init__(self, val1, val2, val3) -> None:
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3


c1 = C(4, 3, 1)

c1.val1

c1.val2 = 4

c1.val3 = 'll'
