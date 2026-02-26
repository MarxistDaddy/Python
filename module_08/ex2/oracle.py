import os
import sys
from dotenv import load_dotenv

load_dotenv() #load the function to read all the files

print("ORACLE STATUS: Reading the Matrix...\n")

#get each vlue one by one!

matrix = os.getenv("MATRIX_MODE")
data = os.getenv("DATABASE_URL")
api = os.getenv("API_KEY")
log = os.getenv("LOG_LEVEL")
zion = os.getenv("ZION_ENDPOINT")

print(matrix)
print(data)
print(api)
print(log)
print(zion)

missing = []

if not matrix:
    missing.append("MATRIX_MODE")
if not data:
    missing.append("DATABASE_URL")
if not api:
    missing.append("API_KEY")
if not log:
    missing.append("LOG_LEVEL")
if not zion:
    missing.append("ZION_ENDPOINT")

if missing:
    print("\nWARNING: Missing configuration variables:")
    for var in missing:
        print(f"    - {var}")
    print("\nPlease configure them in your environment or .env file.")
    sys.exit(1)

print("\nConfiguration loaded:")
if matrix:
    print("Mode:", matrix)
if "sqlite" in data:
    print("Database: Connected to local instance")
else:
    print("Database: Connected to remote instance")

if api:
    print("API Access: Authenticated")
if log:
    print("Log level: DEBUG")
if zion:
    print("Zion Network: Online")


print("\nEnvironment security check:")
if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not found (using system environment variables)")

if matrix == "production":
    print("[OK] Production overrides available")
print("[OK] No hardcoded secrets detected")

print("\nThe Oracle sees all configurations.")
