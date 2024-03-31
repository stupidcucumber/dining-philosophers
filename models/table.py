from . import Philosopher, Fork


class DiningTable:
    def __init__(self, number: int) -> None:
        self.forks = [Fork() for _ in range(number)]
        self.philosophers = [Philosopher(index=index, forks=self.forks)
                             for index in range(number)]

    def start(self) -> None:
        print('Dining session has started.')
        for philosopher in self.philosophers:
            philosopher.start()

        for philosopher in self.philosophers:
            philosopher.join()