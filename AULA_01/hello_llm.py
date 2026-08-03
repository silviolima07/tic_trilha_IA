import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(override=True)

# Cliente da Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Usa o modelo definido no .env ou um valor padrão
modelo = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

print(f"Modelo utilizado: {modelo}")

response = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "user",
            "content": "Qual a capital do Brasil?"
        }
    ]
)

print(response.choices[0].message.content)
