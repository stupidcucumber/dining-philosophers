import threading
import time
from ..fork import Fork


class DijkstraPhilosopher(threading.Thread):
    def __init__(self, index: int, mutex: threading.Lock, forks: list[Fork], name: str | None = None) -> None:
        super(DijkstraPhilosopher, self).__init__(name=name)
        self.forks = forks
        self.mutex = mutex
        self.index = index

    def run(self) -> None:
        left_fork_index = (self.index + 1) % len(self.forks)
        right_fork_index = self.index 
        while True:
            print('Philosopher under number %d is thinking...' % self.index)
            self.mutex.acquire()
            time.sleep(3)
            self.forks[right_fork_index].acquire()
            self.forks[left_fork_index].acquire()
            print('Philosopher under number %d is eating...' % self.index)
            time.sleep(3)
            self.forks[left_fork_index].release()
            self.forks[right_fork_index].release()
            self.mutex.release()