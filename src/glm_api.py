import os
from dotenv import load_dotenv
from zai import ZhipuAiClient
import sys
# ../.env
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

# Load API key from environment variable
ZHIPU_KEY = os.getenv("ZHIPU_KEY")

# Initialize Zhipu AI client
client = ZhipuAiClient(api_key=ZHIPU_KEY)

MODEL_NAME = "glm-4.5"

# Utils
def send_messages(messages, model=MODEL_NAME, stream=False, thinking_enabled=False, max_tokens=4096, temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        thinking={"type": "enabled" if thinking_enabled else "disabled"},
        stream=stream,
        max_tokens=max_tokens,
        temperature=temperature
    )

    if stream:
        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='', flush=True)
                full_response += content
        print()
        return full_response.strip()
    else:
        return response.choices[0].message.content.strip()

# Usage example
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "介绍一下数学建模的学习路径。"}
    ]
    response = send_messages(messages, stream=True)
    # print(response)