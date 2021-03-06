import argparse
import sys

# build thhe parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename',  help='the file to read') # positional argument
parser.add_argument('--limit', '-l', type=int, help='the number of  lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args  = parser.parse_args()

try:
    f = open(args.filename)
    limit =  args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
else:
    with f:
        lines = f.readlines()
        lines.reverse() # reverse the lines, first line is now last line
        
        if args.limit:
            lines = lines[:limit]
        
        for line in  lines:
            print(line.strip()[::-1]) # reverse the conent of each line with a '-1' step
finally:
    print("---")