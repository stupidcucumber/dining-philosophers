import threading
import time
from ..fork import Fork


class DijkstraPhilosopher(threading.Thread):
    def __init__(self, index: int, forks: list[Fork], name: str | None = None) -> None:
        super(DijkstraPhilosopher, self).__init__(name=name)