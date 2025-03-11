#!/bin/bash

# 遇到錯誤時立即停止執行
set -e

echo "Building CloudShop CLI application..."

# 確保 Python 存在
if ! command -v python3 &> /dev/null
then
    echo "Error: Python3 is not installed."
    exit 1
fi

# 確保所有必要的 Python 檔案存在
FILES=("presentation.py" "application.py" "persistence.py")
for file in "${FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Error: $file not found!"
        exit 1
    fi
done

# 確保 build 目錄存在
mkdir -p build

# # 打包專案（可選）
# tar -czf build/cloudshop.tar.gz presentation.py application.py persistence.py README.md build.sh run.sh

echo "Build completed successfully!"