
"""Cliente para a API da OpenAI (ChatGPT)."""
import os
import openai
from typing import Optional

# Suporta SDK v0.x
openai.api_key = os.environ.get('OPENAI_API_KEY')

def ask_chatgpt(prompt: str, model: str = None, max_tokens: int = 500, temperature: float = 0.7) -> str:
    """Envia um prompt ao ChatGPT e retorna o texto de resposta."""
    if not openai.api_key:
        raise RuntimeError('Defina a variável de ambiente OPENAI_API_KEY.')
    model = model or os.environ.get('GPT_MODEL', 'gpt-4')
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content
