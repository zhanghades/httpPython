from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "status": "success",
        "message": "Hello! 这是一个运行在云端容器里的接口",
        "env": "Production"
    }

if __name__ == '__main__':
    # 重点：Render 等平台通常要求监听 0.0.0.0
    # 端口通过环境变量获取，默认 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)