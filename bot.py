import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY_1")

def get_response(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message['content']
prompt = input("enter prompt:>")

if __name__ == "__main__":
    
    response = get_response(prompt)
    print(response)

