def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        storage = open("new_discovery.txt", "w")
    except FileExistsError:
        print("Discovery already exists")
        return
    print(f"{storage.name}: storage unit created successfully...")

    print("Inscribing preservation data...")
    storage.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
    storage.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
    storage.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")

    storage.close()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")



main()
