import threading
from . import Fork
from .philosopher import ClassicPhilosopher, DijkstraPhilosopher, AllahPhilosopher


class ClassicDiningTable:
    def __init__(self, number: int) -> None:
        self.forks = [Fork() for _ in range(number)]
        self.philosophers = [ClassicPhilosopher(index=index, forks=self.forks)
                             for index in range(number)]

    def start(self) -> None:
        print('Dining session has started.')
        for philosopher in self.philosophers:
            philosopher.start()

        for philosopher in self.philosophers:
            philosopher.join()


class DijkstraDiningTable:
    def __init__(self, number: int) -> None:
        self.forks = [Fork() for _ in range(number)]
        self.mutex = threading.Lock()
        self.philosophers = [DijkstraPhilosopher(index=index, forks=self.forks, mutex=self.mutex)
                             for index in range(number)]
        
    def start(self) -> None:
        print('Dining session has started.')
        for philosopher in self.philosophers:
            philosopher.start()

        for philosopher in self.philosophers:
            philosopher.join()


class AllahTable:
    def __init__(self, number: int) -> None:
        self.forks = [Fork() for _ in range(number)]
        self.philosophers = [AllahPhilosopher(index=index, forks=self.forks)
                             for index in range(number)]

    def start(self) -> None:
        print('Dining session has started.')
        for philosopher in self.philosophers:
            philosopher.start()

        for philosopher in self.philosophers:
            philosopher.join()