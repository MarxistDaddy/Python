def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as fd:
            file1 = fd.read()
            print(f"SUCCESS: Archive recovered - ``{file1}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as fd2:
            file2 = fd2.read()
            print(f"SUCCESS: Archive recovered - ``{file2}''")
            print("STATUS: Normal operations resumed")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("")
    print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as fd3:
            file3 = fd3.read()
            print(f"SUCCESS: Archive recovered, {file3}"
                  " - ``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system stable")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


main()
