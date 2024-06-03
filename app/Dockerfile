# 使用官方的 Python 3.9 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到工作目录
COPY requirements.txt /app/

# 安装所需的包
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录内容到工作目录
COPY . /app

# 暴露容器的端口
EXPOSE 5000

# 设置环境变量（根据需要）
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# 运行 Flask 应用
CMD ["flask", "run"]

