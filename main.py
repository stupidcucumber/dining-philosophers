import argparse
from models import ClassicDiningTable, DijkstraDiningTable


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
        choices=['classic', 'dijkstra'],
        default='classic',
        help='The solution to the Dining problem.'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.solution == 'classic':
        table = ClassicDiningTable(number=args.num_philosophers)
    else:
        table = DijkstraDiningTable(number=args.num_philosophers)
    table.start()