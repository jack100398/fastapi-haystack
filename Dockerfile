FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統依賴套件（例如 FAISS 所需的 libgomp1）
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# 複製並安裝 Python 依賴套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製 FastAPI 應用程式代碼
# COPY app.py .

# 開放服務埠
EXPOSE 8000

# 使用 Uvicorn 啟動 FastAPI 應用程式
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
