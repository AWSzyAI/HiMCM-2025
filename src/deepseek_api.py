import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

# (0) Official
Deepseek_KEY = os.getenv('Deepseek_KEY')
Deepseek_URL = "https://api.deepseek.com"
client = OpenAI(api_key=Deepseek_KEY, base_url=Deepseek_URL)
MODEL_NAME = "deepseek-chat"

# (1)
# LUCHENTECH_KEY = os.getenv('LUCHENTECH_KEY')
# LUCHENTECH_URL = 'https://cloud.luchentech.com/api/maas/'
# client = OpenAI(api_key=LUCHENTECH_KEY, base_url=LUCHENTECH_URL)
# MODEL_NAME = "deepseek-ai/DeepSeek-R1"

# import requests

# url = 'https://cloud.luchentech.com/api/maas/chat/completions'

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer <your_api_key>'
# }
# payload = {
#     "model": "deepseek-ai/DeepSeek-R1",
#     "messages": [
#       {
#         "role": "user",
#         "content": "写一首描绘春天的诗？"
#       }
#     ],
#     "stream": False, 
#     "max_tokens": 512
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.json())

# (2) Tencent
# tencent_KEY = os.getenv('tencent_KEY')
# tencent_KEY_wzj  = os.getenv('tencent_KEY_wzj')
# tencent_URL = "https://api.lkeap.cloud.tencent.com/v1"
# # tencent_URL = "https://api.lkeap.cloud.tencent.com/"
# client = OpenAI(api_key=tencent_KEY_wzj, base_url=tencent_URL)
# MODEL_NAME = "deepseek-r1"


# (3) 星河社区


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
    

