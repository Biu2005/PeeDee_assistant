#!/bin/bash

# Thiết lập môi trường
PROJECT_DIR="/home/peedee/PeeDee"
cd "$PROJECT_DIR"

# ĐIỂM QUAN TRỌNG: Kích hoạt môi trường ảo
source PeeDee_venv/bin/activate

# Chạy chương trình chính
# Khi môi trường ảo đã được kích hoạt, hệ thống sẽ sử dụng Python và các thư viện trong venv.
/home/peedee/PeeDee/PeeDee_venv/bin/python main.py

# Nếu chương trình của bạn là một vòng lặp vô hạn, lệnh này sẽ giữ terminal bận.
