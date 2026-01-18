#!/usr/bin/python3.10

import sys
import math

def main():
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)
    position = (10, 20, 5)

    print(f"position created: {position}")
    distance = math.sqrt(
        (position[0] - origin[0]) ** 2 +
        (position[1] - origin[1]) ** 2 +
        (position[2] - origin[2]) ** 2
    )

    print(f"Distance between {origin} nd {position}: {distance:.2f}\n")

    argc = len(sys.argv)
    if argc > 1:
        cord_str = sys.argv[1]
        print(f'parsing coordinattes: "{cord_str}"')
        try:
            parts = cord_str.split(",")
            x = int(parts[0])        
            y = int(parts[1])        
            z = int(parts[2])

            position2 = (x,y,z)

            print(f"Parsed position: {position2}")
            distance2 = math.sqrt(
               (position2[0] - origin[0]) ** 2 +
               (position2[1] - origin[1]) ** 2 +
               (position2[2] - origin[2]) ** 2 
            )
            print(f"Distance between {origin} and {position2}: "
                  f"{distance2:.2f}\n")

            print("Unpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            X,Y,Z = position2
            print(f"Coordinates: X={X}, Y={Y}, Z={Z}")

        except ValueError as e:
            print(f"Error passing coordinates: {e}")
            print(f"Error details - type: {type(e).__name__}, Args: {e.args}")
            return

main()
