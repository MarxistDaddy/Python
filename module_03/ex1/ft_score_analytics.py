#!/usr/bin/python3.10

class ScoreError(Exception):
    pass

if __name__ == "__main__":
    print("=== Player Score Analytics ===\n")
    try:
        argc = len(sys.argv)
        if argc == 1:
            raise ScoreError("No scores provided.")
        else:
            list = []
            for i in (range(1, argc)):
                list += int(sys.argv[i])
            
        
