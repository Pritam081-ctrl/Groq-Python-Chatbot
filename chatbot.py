import os
from dotenv import load_dotenv

from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found in .env file")

client = Groq(api_key=api_key)

print("chatbot(Groq streaming):Type 'quit'.'exit',or 'bye' to stop\n")

while True:
    user_input=input("You:")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("\nChatbot:Goodbye!")
        break

    print("chatbot:",end="",flush=True)

    stream=client.chat.completions.create(model="openai/gpt-oss-20b",
    messages=[{"role":"system",        "content":"You are a helpful chatbot."},{"role":"user","content":user_input}
    ],
    stream=True #Enable streaming
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="",flush=True)

    print() #new line after response
                              