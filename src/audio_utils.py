
"""Funções auxiliares para lidar com áudio e Base64."""
import base64
import re
from pathlib import Path

DATA_URL_PREFIX = re.compile(r'^data:audio/.+;base64,')

def save_base64_audio(data_url: str, out_path: str | Path) -> str:
    """
    Salva um Data URL (base64) de áudio em disco.
    Aceita formatos como "data:audio/x-wav;base64,AAAA...".
    """
    out_path = Path(out_path)
    raw = DATA_URL_PREFIX.sub('', data_url)
    out_path.write_bytes(base64.b64decode(raw))
    return str(out_path)
