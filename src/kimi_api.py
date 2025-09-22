import os
from dotenv import load_dotenv
from openai import OpenAI

# 从 .env 文件中加载环境变量
load_dotenv()

KIMI_API_KEY = os.getenv("KIMI_API_KEY")
BASE_URL = "https://api.moonshot.cn/v1"
# BASE_URL = "http://127.0.0.1:11434/v1/"
client = OpenAI(api_key=KIMI_API_KEY, base_url=BASE_URL)
MODEL_NAME = "moonshot-v1-auto"
# MODEL_NAME = "kimi-latest"
# MODEL_NAME = "deepseek-r1:14b"




# Utils
def send_messages(messages, model=MODEL_NAME, tools=None):
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages = messages,
        # temperature=1.3, #deepseek
        temperature=1, #kimi
        response_format={"type": "json_object"},  # 确保返回 JSON 格式
        n=1  # 请求返回1个结果
    )
    response = completion.choices[0].message.content.strip()
    return response

# Usage example
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
    response = send_messages(messages)
    print(response)