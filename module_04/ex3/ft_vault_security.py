def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            file = vault.read()
            print(file)
    except FileNotFoundError:
        print("[CLASSIFIED] No classified data found!")

    print("\nSECURE PRESERVATION:")
    with open("new_protocol", "w"):
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


main()
