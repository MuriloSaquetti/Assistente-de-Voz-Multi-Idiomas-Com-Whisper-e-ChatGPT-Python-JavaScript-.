
"""Módulo de transcrição usando Whisper."""
from typing import Optional
import whisper

def transcribe_audio(audio_path: str, language: Optional[str] = None, model_size: str = 'small', fp16: bool = False, verbose: bool = False) -> str:
    """
    Transcreve o áudio em `audio_path` usando Whisper.
    - language: código do idioma (ex.: 'pt'). Se None, o Whisper tenta detectar.
    - model_size: tiny | base | small | medium | large
    - fp16: em CPU normalmente deve ser False.
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, fp16=fp16, language=language, verbose=verbose)
    return result.get('text', '').strip()
