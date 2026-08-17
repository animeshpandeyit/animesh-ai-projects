import os
from pathlib import Path

from dotenv import load_dotenv
from groq  import Groq


load_dotenv() 

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")


client = Groq(api_key=my_api_key)

# model = "llama-3.3-70b-versatile"
# Groq deprecated llama-3.3-70b-versatile and the shutdown date was August 16, 2026. Today is August 18, 2026, which is why you're getting the 404. Groq recommends openai/gpt-oss-120b or qwen/qwen3.6-27b as replacements.
model = "openai/gpt-oss-120b"

role= "user"
# prompt = "I love you, my baby."
prompt = "suggest me a name for my new food company. "


# message_system = {"role": "system", "content": "you are my loving girlfriend"}
# message_system = {"role": "system", "content": "you are my strict office colleague who is also my manager."}
message_system = {"role": "system", "content": "you are a brand manager. who suggests name for my food brands. Suggest one name only.  "}


message = {"role": role, "content": prompt}

messages = [message_system, message]
# messages = [message]

response = client.chat.completions.create(model=model, messages=messages , temperature=1)
# print(response)
answer = response.choices[0].message.content
print("Answer:", answer)