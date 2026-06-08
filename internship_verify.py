import sys
import importlib
import subprocess

print("\n=== SUMMER OF AI INTERNSHIP CHECK ===\n")

# Python version
print("Python Version:", sys.version.split()[0])

# Required packages
required = ["numpy", "pandas", "streamlit"]

print("\nPython Packages:")
for pkg in required:
    try:
        importlib.import_module(pkg)
        print(f"✔ {pkg}")
    except ImportError:
        print(f"✘ {pkg}")

# uv check
print("\nuv check:")
try:
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
    print("✔ uv installed")
except:
    print("✘ uv not found")

# streamlit check
print("\nStreamlit check:")
try:
    result = subprocess.run(["streamlit", "--version"], capture_output=True, text=True)
    print("✔ streamlit installed")
except:
    print("✘ streamlit not found")

print("\n=== CHECK COMPLETE ===\n")
