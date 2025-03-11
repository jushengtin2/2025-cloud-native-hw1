#!/bin/bash

# 遇到錯誤時立即停止執行
set -e

echo "Building CloudShop CLI application..."

# # 打包專案（可選）
# tar -czf build/cloudshop.tar.gz presentation.py application.py persistence.py README.md build.sh run.sh

echo "Build completed successfully!"