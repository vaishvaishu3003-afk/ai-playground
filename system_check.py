import sys
import subprocess

print("🔍 AI SYSTEM CHECK STARTING...\n")

# Python version
print("1️⃣ Python Version:")
print(sys.version, "\n")

# Check packages
print("2️⃣ Checking Python packages:")

packages = ["numpy", "pandas", "streamlit", "requests"]

for pkg in packages:
    try:
        __import__(pkg)
        print(f"   ✅ {pkg} installed")
    except:
        print(f"   ❌ {pkg} missing")

print("\n3️⃣ Checking Ollama connection:")

try:
    import requests

    res = requests.get("http://localhost:11434/api/tags")
    if res.status_code == 200:
        print("   ✅ Ollama is running")
    else:
        print("   ⚠️ Ollama responded but not OK")
except:
    print("   ❌ Ollama NOT running or not installed")

print("\n4️⃣ Checking uv environment:")

try:
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
    print("   ✅ uv installed:", result.stdout.strip())
except:
    print("   ❌ uv not found")

print("\n5️⃣ Checking Streamlit:")

try:
    result = subprocess.run(["streamlit", "--version"], capture_output=True, text=True)
    print("   ✅ Streamlit:", result.stdout.strip())
except:
    print("   ❌ Streamlit not found")

print("\n🚀 SYSTEM CHECK COMPLETE")
