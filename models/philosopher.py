import threading
import time
from .fork import Fork


class Philosopher(threading.Thread):
    def __init__(self, index: int, forks: list[Fork], name: str | None = None) -> None:
        super(Philosopher, self).__init__(name=name)
        self.index = index
        self.forks = forks

    def isodd(self) -> bool:
        return self.index % 2 == 1
    
    def iseven(self) -> bool:
        return self.index % 2 == 0

    def run(self) -> None:
        left_fork_index = (self.index + 1) % len(self.forks)
        right_fork_index = self.index 
        while True:
            print('Philosopher under number %d is thinking...' % self.index)
            time.sleep(3)
            if self.isodd():
                self.forks[left_fork_index].acquire()
                self.forks[right_fork_index].acquire()
            else:
                self.forks[right_fork_index].acquire()
                self.forks[left_fork_index].acquire()
            print('Philosopher under number %d is eating...' % self.index)
            time.sleep(3)
            self.forks[left_fork_index].release()
            self.forks[right_fork_index].release()
