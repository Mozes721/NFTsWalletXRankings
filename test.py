import argparse
parser = argparse.ArgumentParser()


parser.add_argument(
    '-c',
    '--compare',
    nargs=2,
    metavar=('newfile', 'oldfile'),
    help='Compares previous run results in oldfile with actual run results in newfile.',
    )

args = parser.parse_args()

newfile, oldfile = args.compare
print(newfile)
print("*"*8)
print(oldfile)