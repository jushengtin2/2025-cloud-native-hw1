#!/bin/bash

# 遇到錯誤時立即停止執行
set -e

echo "Starting CloudShop CLI..."

# 確保 Python 存在
if ! command -v python3 &> /dev/null
then
    echo "Error: Python3 is not installed."
    exit 1  
fi

# 確保程式碼存在
if [ ! -f "presentation.py" ]; then
    echo "Error: presentation.py not found!"
    exit 1
fi

# 執行 CLI 程式
python3 presentation.py