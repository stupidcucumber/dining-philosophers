import argparse
from models import ClassicDiningTable, DijkstraDiningTable, AllahTable


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', '--num-philosophers',
        type=int,
        default=5,
        help='Number of philosophers at dining'
    )
    parser.add_argument(
        '--solution',
        type=str,
        choices=['classic', 'dijkstra', 'allah'],
        default='classic',
        help='The solution to the Dining problem.'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.num_philosophers <= 0:
        print('Number must be positive non-zero!')
        exit(1)
    
    if args.solution == 'classic':
        table = ClassicDiningTable(number=args.num_philosophers)
    elif args.solution == 'allah':
        table = AllahTable(number=args.num_philosophers)
    else:
        table = DijkstraDiningTable(number=args.num_philosophers)
    table.start()