
class MixinLogger:
    __id = 0

    def __init__(self) -> None:
        self._id = self.__get_id()
    
    @classmethod
    def __get_id(cls):
        cls.__id += 1
        return cls.__id


class User(MixinLogger):
    def __init__(self, username, pwd) -> None:
        super().__init__()

        self.username = username
        self.pwd = pwd

    def get_id(self):
        return self._id


user1 = User("user1", "test1")
user2 = User("user2", "test2")

user123 = User("user123", "test123")

print(user1.__dict__)
print(user2.__dict__)
print(user123.__dict__)
