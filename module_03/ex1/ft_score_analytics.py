#!/usr/bin/python3.10

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===\n")
    argc = len(sys.argv)

    if argc < 2:
        print(f"No scores provided. usage: " 
              f"python2 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []
        try:
            i = 1
            while i < argc:
                 scores += [int(sys.argv[i])]
                 i += 1
        except:
            print(f"oops, I typed {sys.argv[i]} instead of an int_value")
    
        print("Scores processed:", scores)
        print("Total players:", argc -1)
        print("Total score:", sum(scores))
        print("Average score:", sum(scores) / (argc - 1))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
