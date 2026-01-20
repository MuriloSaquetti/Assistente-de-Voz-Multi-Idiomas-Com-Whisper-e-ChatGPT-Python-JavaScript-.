
"""Pipeline de fim a fim: áudio -> Whisper -> ChatGPT -> gTTS."""
from __future__ import annotations

from pathlib import Path
from .config import settings, ensure_api_key
from .audio_utils import save_base64_audio
from .whisper_transcriber import transcribe_audio
from .chat_gpt_client import ask_chatgpt
from .tts_generator import generate_audio

def run_pipeline(*, audio_b64: str | None = None, audio_path: str | None = None, language: str | None = None, whisper_model: str | None = None) -> dict:
    if not audio_b64 and not audio_path:
        raise ValueError('Forneça `audio_b64` OU `audio_path`.')
    ensure_api_key()

    # 1) Persistir áudio
    tmp_path = Path('request_audio.wav')
    if audio_b64:
        save_base64_audio(audio_b64, tmp_path)
    else:
        tmp_path = Path(audio_path)

    # 2) Transcrição
    lang = language or settings.default_language
    w_model = whisper_model or settings.whisper_model
    transcription = transcribe_audio(str(tmp_path), language=lang, model_size=w_model, fp16=False)

    # 3) ChatGPT
    response_text = ask_chatgpt(transcription, model=settings.gpt_model)

    # 4) TTS
    out_audio = generate_audio(response_text, language=lang, out_path=settings.response_audio_path)

    return {
        'transcription': transcription,
        'response_text': response_text,
        'response_audio_path': out_audio,
    }

if __name__ == '__main__':
    # Exemplo de execução simples por caminho de arquivo
    result = run_pipeline(audio_path='request_audio.wav')
    print('Transcrição:', result['transcription'])
    print('Resposta:', result['response_text'])
    print('Áudio gerado:', result['response_audio_path'])
