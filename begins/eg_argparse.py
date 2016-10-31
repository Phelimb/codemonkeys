import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('knights',  type=str, nargs='+')
parser.add_argument('--name', default='Arther')
parser.add_argument('--quest', default='Holy Grail')
parser.add_argument('--colour', default='blue')
args = parser.parse_args()
print((args.knights))
