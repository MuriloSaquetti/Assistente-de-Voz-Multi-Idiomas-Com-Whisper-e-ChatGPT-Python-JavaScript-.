
"""Geração de voz (TTS) com gTTS."""
from gtts import gTTS

def generate_audio(text: str, language: str = 'pt', out_path: str = 'response_audio.wav', slow: bool = False) -> str:
    tts = gTTS(text=text, lang=language, slow=slow)
    # gTTS salva como .mp3 por padrão; alguns players leem .wav incorretamente.
    # Para manter compatibilidade com o notebook original, salvamos com extensão .wav,
    # embora o container de fato seja MP3. Ajuste conforme necessário.
    tts.save(out_path)
    return out_path
