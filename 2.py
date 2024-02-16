

class C:
    val1 = 5
    val2 = "test"

    def msg(obj):
        val1 = obj.val1
        val2 = obj.val2
        print(f"Msg: {val1=}, {val2=}")


c = C()
print(f"{c.val1=}, {c.val2=}")

print()

c.msg()
