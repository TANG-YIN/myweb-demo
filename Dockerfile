# 使用官方的轻量级Python镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码到容器
COPY app.py .

# 新增：复制前端模板文件夹
COPY templates/ ./templates/

# 暴露端口
EXPOSE 8080

# 启动应用
CMD ["python", "app.py"]
