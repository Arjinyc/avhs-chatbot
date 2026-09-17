import os

from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def load_school_data():
    with open("school_data.txt", "r", encoding="utf-8") as file:
        data = file.read()
    return data[:32000]


def build_system_prompt():
    school_data = load_school_data()
    return f"""You are the Amador Valley High School virtual assistant.
You help students, parents, and staff find information about AVHS.

Here is the official information from the AVHS website:

{school_data}

RULES:
1. Only answer questions about Amador Valley High School.
2. If you don't know, say "I'm not sure — please contact the main office or visit https://amador.pleasantonusd.net"
3. Never make up information. Only use what's in the data above.
4. Keep answers short and friendly — 2 to 3 sentences.
5. If asked something off-topic, politely say you can only help with AVHS questions.
"""


SYSTEM_PROMPT = build_system_prompt()


def get_response(conversation_history):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history,
    )
    return response.choices[0].message.content
