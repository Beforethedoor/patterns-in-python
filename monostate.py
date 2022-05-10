class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


obj1 = ThreadData()
obj2 = ThreadData()

obj1.id = 3
print(obj1.__dict__)
print(obj2.__dict__)

obj1.attr_new = 'new attr'
print(obj1.__dict__)
print(obj2.__dict__)
