# 使用官方的轻量级Python镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 让Python日志直接输出，方便k8s收集
ENV PYTHONUBUFFERED=1

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码到容器
COPY . .

# 暴露端口
EXPOSE 8080

# 启动应用
CMD ["python", "run.py"]
