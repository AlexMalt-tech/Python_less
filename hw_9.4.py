class Singleton(type):
    data_cls = None

    def __new__(data_cls, *args):
        if data_cls == None:
            data_cls = super(Singleton).__new__(*args)
        return data_cls


class UserClass(metaclass=Singleton):

    def method_1(self):
        pass


obj_1 = UserClass()
obj_2 = UserClass()

print(obj_1 is obj_2)
