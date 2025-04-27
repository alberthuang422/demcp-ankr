FROM python:3.10-slim

WORKDIR /app

# 安装uv
RUN pip install --no-cache-dir uv

# 安装依赖
COPY requirements.txt .
RUN uv pip install --system --no-cache --requirement requirements.txt

# 复制代码
COPY src/ ./src/

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露端口（根据MCP服务需要调整）
EXPOSE 8080

# 启动命令
CMD ["uv", "run", "src/main.py"] 