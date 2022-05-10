class Subscriber:
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f'{self.name} got message: "{message}"')


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who: Subscriber) -> None:
        self.subscribers.add(who)

    def unregister(self, who: Subscriber) -> None:
        self.subscribers.discard(who)

    def dispatch(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message)


pub = Publisher()

bob = Subscriber(name="Bob")
alice = Subscriber(name="Alice")
john = Subscriber(name="John")

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch(message="It's lunchtime!")

pub.unregister(bob)
pub.dispatch(message="Time for dinner!")
