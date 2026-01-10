#!/usr/bin/python3.10

import sys
import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coord = sys.argv[1]
    try:
        parts = coord.split(',')
        x, y, z = parts
        parts2 = (int(x), int(y), int(z))
        print(f'Parsing coordinates: "{coord}"')
        print(f'Parsing position: "{parts2}"')
        
    except Exception as e:
        print(f'Parsing invalid coordinates "{coord}"')
        print(f'Error parsing coordinates: {e}')
        print(f'Error details - Type: {e}, Args: {e.args}')



