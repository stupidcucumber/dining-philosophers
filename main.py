import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', '--num-philosophers',
        type=int,
        default=5,
        help='Number of philosophers at dining'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()