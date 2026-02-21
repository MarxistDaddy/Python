import sys  
import os
import site

def in_virtualenv():
    return sys.prefix != sys.base_prefix


def main():
    if in_virtualenv():
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix),)
        print("Environment Path:", sys.prefix, "\n")
        print("SUCCESS: You're in an isolated environment!\nSafe to install packages without affecting the global system.\n")
        print("Package installation path:")

        for path in site.getsitepackages():
            if sys.prefix in path:
                print(path)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Vritaul Environment: None detected")
        print("WARNING: You're in the global environment!\nThe machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
    

if __name__ == "__main__":
    main()

