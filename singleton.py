from threading import Lock


class SingletonBaseClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonBaseClass, cls).\
                    __call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = "Singleton"
        self.value_a = 3
        self.value_b = 5

    def add_a_b(self) -> int:
        return self.value_a+self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


my_singleton1 = MySingleton()
my_singleton2 = MySingleton()
print("Singleton1 name: " + my_singleton1.get_name())
my_singleton1.set_name("New Singleton")
print("Singleton2 name: " + my_singleton2.get_name())
print(my_singleton1)
print(my_singleton2)
print(id(my_singleton1) == id(my_singleton2))
