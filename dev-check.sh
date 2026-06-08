#!/bin/bash

echo "========================================"
echo "      DEVELOPMENT ENVIRONMENT CHECK     "
echo "========================================"

echo ""

# Git
if command -v git >/dev/null 2>&1; then
    echo "✅ Git : INSTALLED"
    git --version
else
    echo "❌ Git : NOT INSTALLED"
fi

echo ""

# VS Code
if command -v code >/dev/null 2>&1; then
    echo "✅ VS Code : INSTALLED"
    code --version | head -n 1
else
    echo "❌ VS Code : NOT INSTALLED"
fi

echo ""

# Python
if command -v python3 >/dev/null 2>&1; then
    echo "✅ Python3 : INSTALLED"
    python3 --version
else
    echo "❌ Python3 : NOT INSTALLED"
fi

echo ""

# Pip
if command -v pip3 >/dev/null 2>&1; then
    echo "✅ Pip : INSTALLED"
    pip3 --version
else
    echo "❌ Pip : NOT INSTALLED"
fi

echo ""

# UV
if command -v uv >/dev/null 2>&1; then
    echo "✅ UV : INSTALLED"
    uv --version
else
    echo "❌ UV : NOT INSTALLED"
fi

echo ""

# Bun
if command -v bun >/dev/null 2>&1; then
    echo "✅ Bun : INSTALLED"
    bun --version
else
    echo "❌ Bun : NOT INSTALLED"
fi

echo ""

# Docker
if command -v docker >/dev/null 2>&1; then
    echo "✅ Docker : INSTALLED"
    docker --version
else
    echo "❌ Docker : NOT INSTALLED"
fi

echo ""

# Ollama
if command -v ollama >/dev/null 2>&1; then
    echo "✅ Ollama : INSTALLED"
    ollama --version
else
    echo "❌ Ollama : NOT INSTALLED"
fi

echo ""

# Python packages
echo "========================================"
echo "        PYTHON PACKAGES CHECK           "
echo "========================================"

python3 -c "
import numpy, pandas, streamlit
print('numpy: INSTALLED')
print('pandas: INSTALLED')
print('streamlit: INSTALLED')
" 2>/dev/null || echo "Some Python packages are missing"

echo ""

echo "Python Path:"
which python3

echo ""
echo "========================================"
echo "           CHECK COMPLETE               "
echo "========================================"
