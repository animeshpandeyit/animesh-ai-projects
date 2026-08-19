import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

role = "user"

prompt1 = "Hi!"
prompt2 = "Explain time travel in detail."
prompt3 = "Write a 1000 word essay on machine learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:

    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=50
    )

    usage = response.usage

    print(
        f"Prompt: {prompt} --> "
        f"Tokens used: {usage.prompt_tokens}, "
        f"Completion tokens used: {usage.completion_tokens}, "
        f"Total tokens used: {usage.total_tokens}",
        f"Finish reason: {response.choices[0].finish_reason}"
    )