import sys

def main():
   av = sys.argv
   try:
       tt = (a for a in int(av.split()))
       a, b, c = tt
       print(f"a = {a}, b = {b}, c = {c}")
   except Exception:
       print("error")

main()
