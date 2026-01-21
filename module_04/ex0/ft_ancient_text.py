def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        vault = open("ancient_fragment.txt")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Accessing Storage Vault:", vault.name)
    print("Connection established...\n")

    print("RECOVERED DATA:")
    file = vault.read()
    print(file)

    vault.close()
    print("\nData recovery complete. Storage unit disconnected.")


main()
