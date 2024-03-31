import threading


class Fork(threading.Semaphore):
    def __init__(self, value: int = 1) -> None:
        super(Fork, self).__init__(value)