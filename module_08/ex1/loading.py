import sys
import importlib #what does this lib do?

dependencies = ["pandas", "numpy", "matplotlib","requests"]
installed = {} #empty dic

print("LOADING SATUS: Loading programs...")
print("Checking dependencies...\n")

for package in dependencies:
    try:
        module = importlib.import_module(package) #what mdule_import do?
        version = getattr(module, "__version__", "unknown")
        installed[package] = module
        print(f"[OK] {package.capitalize()} ({version}) - ready")
    except ImportError:
        print(f"[MISSING] {package.capitalize()} - please install it")

if len(dependencies) > len(installed):
    print("\nPlease install missing dependencies first using:")
    print(" pip install -r requirements.txt")
    print(" or")
    print(" poetry install --no-root")
    sys.exit(1)

print("\nAnalzing Matrix data...")
print("Processing 1000 data points...")

pd = installed["pandas"]
np = installed["numpy"]
plt = importlib.import_module("matplotlib.pyplot")  # FIXED

# create fake matrix data
data = pd.DataFrame({"matrix_code": np.random.randn(1000)})
mean_value = data["matrix_code"].mean()

# Plot
plt.figure()
plt.plot(data["matrix_code"])
plt.title("Matrix Code Stream")
plt.xlabel("Index")
plt.ylabel("Signal Strength")
plt.savefig("matrix_analysis.png")

print("Generating visualization...")
print("Analysis complete!")
print("Results saved to: matrix_analysis.png")

