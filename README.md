# Dining Philosophers Problem
Five philosophers dine together at the same table. Each philosopher has his own plate at the table. There is a fork between each plate. The dish served is a kind of spaghetti which has to be eaten with two forks. Each philosopher can only alternately think and eat. Moreover, a philosopher can only eat his spaghetti when he has both a left and right fork. Thus two forks will only be available when his two nearest neighbors are thinking, not eating. After an individual philosopher finishes eating, he will put down both forks. The problem is how to design a regimen (a concurrent algorithm) such that any philosopher will not starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think (an issue of incomplete information).

# Usage
For using this repository Python3.10> is required.

```
usage: main.py [-h] [-n NUM_PHILOSOPHERS] [--solution {classic,dijkstra}]

options:
  -h, --help            show this help message and exit
  -n NUM_PHILOSOPHERS, --num-philosophers NUM_PHILOSOPHERS
                        Number of philosophers at dining
  --solution {classic,dijkstra}
                        The solution to the Dining problem.
```

## Solutions

I have implemented two solutions: Classic (resource hierarchy) and Dijkstra (involving mutex for synchronization).