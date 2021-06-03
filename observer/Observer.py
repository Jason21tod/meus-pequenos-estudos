
from abc import ABC, abstractmethod
from time import sleep


class Observer(ABC):
    def __init__(self):
        self.subscribers = []

    @abstractmethod
    def subscribe(self, sub):
        ...

    @abstractmethod
    def notify_all(self, state):
        ...


class ConcreteObserver(Observer):
    def __init__(self):
        super().__init__()

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify_all(self, state):
        print('notificando ...', len(self.subscribers))
        for sub in self.subscribers:
            sub.update(state)


observer_1 = ConcreteObserver()


class Subject:
    def __init__(self):
        self.state = True

    def switch_state(self):
        if self.state:
            self.state = False
        else:
            self.state = True
        observer_1.notify_all(self.state)


subject_1 = Subject()


class ObserverObject:
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f'\033[32m {self.name} recebeu {state}\033[m')


ob1 = ObserverObject('roger')
ob2 = ObserverObject('Gian')

observer_1.subscribe(ob1)
observer_1.subscribe(ob2)

for r in range(0, 10):
    subject_1.switch_state()
    sleep(1)
