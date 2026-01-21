import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    user = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {user}: {status}")
    print("[ALERT] System diagnostic:"
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful")


main()
