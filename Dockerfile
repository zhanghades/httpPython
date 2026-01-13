FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# 使用 gunicorn 运行生产环境服务
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]