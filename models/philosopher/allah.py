import threading
import time
from ..fork import Fork


class AllahPhilosopher(threading.Thread):
    def __init__(self, index: int, forks: list[Fork], name: str | None = None) -> None:
        super(AllahPhilosopher, self).__init__(name=name)
        self.forks = forks
        self.index = index

    def run(self) -> None:
        left_fork_index = (self.index + 1) % len(self.forks)
        right_fork_index = self.index 
        while True:
            print('Philosopher under number %d is thinking...' % self.index)
            time.sleep(3)
            self.forks[right_fork_index].acquire()
            acquired = self.forks[left_fork_index].acquire(False)
            if not acquired:
                time.sleep(3)
                print('Philosopher under number %d is hungry...' % self.index)
                self.forks[left_fork_index].release()
            print('Philosopher under number %d is eating...' % self.index)
            time.sleep(3)