import os
from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark

# 从 .env 文件中加载环境变量
load_dotenv()

# 从环境变量中获取 API 密钥
ARK_API_KEY = os.getenv("ARK_API_KEY")

# 初始化 Ark 客户端
client = Ark(api_key=ARK_API_KEY)

# 设置模型名称为 "doubao-1-5-pro-256k-250115"
MODEL_NAME = "doubao-1-5-pro-256k-250115"

# Utils
def send_messages(messages, model=MODEL_NAME, stream=False, tools=None):
    try:
        if stream:
            print("----- streaming request -----")
            # 开启流式响应
            stream_response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True  # 开启流式响应
            )

            # 逐块处理流式响应
            for chunk in stream_response:
                if not chunk.choices:
                    continue
                # 输出流式响应内容
                print(chunk.choices[0].delta.content, end="")
            print()  # 换行
        else:
            # 非流式响应处理
            completion = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            # 处理返回的响应
            response = completion.choices[0].message.content.strip()
            return response
    except Exception as e:
        print(f"Error while sending message: {e}")
        return None

# Usage example for streaming
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"}
    ]
    # send_message(messages, stream=True)  # 启用流式请求
    # send_message(messages)
    print(send_messages(messages))  