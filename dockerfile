# Bắt đầu từ image Python mới nhất
FROM python:latest

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép tất cả file từ thư mục hiện tại (từ thư mục chứa Dockerfile) vào container
COPY . /app

# Cài đặt các thư viện phụ thuộc từ requirements.txt
RUN python3 -m pip install -r requirements.txt

