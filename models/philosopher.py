import threading


class Philosopher(threading.Thread):
    def __init__(self, name: str) -> None:
        super(Philosopher, self).__init__(name=name)
