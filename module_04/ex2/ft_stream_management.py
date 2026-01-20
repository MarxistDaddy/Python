import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    user = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n{{[}}STANDARD{{]}} Archive status from {user}: {status}\n")
    sys.stderr.write("{[}ALERT{]} System diagnostic: Communication channels verified\n")
    sys.stdout.write(f"{{[}}STANDARD{{]}} Data transmission complete\n\n")

    print("Three-channel communication test successful")

main()
