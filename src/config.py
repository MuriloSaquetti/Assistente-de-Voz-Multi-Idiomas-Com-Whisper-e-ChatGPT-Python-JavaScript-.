
"""Configurações e utilitários do projeto.

Centraliza variáveis de ambiente e defaults.
"""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None = os.environ.get('OPENAI_API_KEY')
    default_language: str = os.environ.get('ASSISTANT_LANG', 'pt')
    whisper_model: str = os.environ.get('WHISPER_MODEL', 'small')
    gpt_model: str = os.environ.get('GPT_MODEL', 'gpt-4')
    response_audio_path: str = os.environ.get('RESPONSE_AUDIO_PATH', 'response_audio.wav')

settings = Settings()

def ensure_api_key() -> str:
    if not settings.openai_api_key:
        raise RuntimeError('Defina a variável de ambiente OPENAI_API_KEY antes de executar.')
    return settings.openai_api_key
