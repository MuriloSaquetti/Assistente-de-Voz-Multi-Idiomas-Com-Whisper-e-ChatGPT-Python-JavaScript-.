# 🎤 Assistente de Voz Multilíngue com Whisper + ChatGPT + gTTS  
### Um assistente virtual completo com Reconhecimento de Fala, IA e Síntese de Voz

Este projeto implementa um **assistente de voz inteligente multilíngue**, capaz de:

✅ Gravar áudio do usuário diretamente pelo navegador  
✅ Converter fala em texto usando **Whisper** (OpenAI)  
✅ Interpretar e responder usando **ChatGPT**  
✅ Converter a resposta da IA em áudio usando **gTTS**  
✅ Funcionar de forma simples e amigável em **Python + JavaScript + Jupyter Notebook**  

---

## 🧠 Tecnologias Utilizadas

| Tecnologia | Função |
|----------|--------|
| **Python 3** | Lógica principal do assistente |
| **JavaScript (MediaRecorder API)** | Captura de áudio via navegador |
| **Whisper (OpenAI)** | Speech-to-Text |
| **OpenAI GPT‑4 / GPT‑3.5 turbo** | Geração de respostas |
| **gTTS** | Text‑to‑Speech |
| **Jupyter Notebook** | Ambiente de execução |

---

## 📂 Estrutura do Repositório

```
assistente-voz-ia/
├── notebook/
│   └── Assistente_de_Voz_Multi_Idiomas_Com_Whisper_e_ChatGPT.ipynb
├── src/
│   ├── recorder.js
│   ├── whisper_transcriber.py
│   ├── chat_gpt_client.py
│   ├── tts_generator.py
├── examples/
│   ├── exemplo_entrada.wav
│   ├── exemplo_resposta.wav
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Como Executar o Projeto

### **1️⃣ Clone o repositório**
```bash
git clone https://github.com/seu-usuario/assistente-voz-ia.git
cd assistente-voz-ia
```

### **2️⃣ Instale as dependências**
```bash
pip install -r requirements.txt
```

---

## 🎙 1. Captura de Áudio (JavaScript)
O projeto usa a API nativa do navegador:

```javascript
navigator.mediaDevices.getUserMedia({ audio: true })
```

O JS grava o áudio, converte para base64 e envia ao Python dentro do notebook.

---

## 🗣 2. Transcrição de Voz com Whisper

```python
import whisper
model = whisper.load_model("small")
result = model.transcribe("request_audio.wav", fp16=False, language="pt")
```

---

## 💬 3. Integração com ChatGPT

```python
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": transcription}]
)
```

---

## 🔊 4. Síntese da Resposta (Text‑to‑Speech)

```python
from gtts import gTTS
gtts_object = gTTS(text=chatgpt_response, lang=language)
gtts_object.save("response_audio.wav")
```

---

## 🌎 Idiomas Suportados

O assistente suporta qualquer idioma reconhecido pelo Whisper e sintetizado pelo gTTS, incluindo:

- Português  
- Inglês  
- Espanhol  
- Francês  
- Alemão  
- Italiano  
- Japonês  
- Coreano  
- E muitos outros

---

## 📘 Requisitos

Conteúdo do arquivo `requirements.txt` recomendado:

```
openai
whisper
gTTS
torch
numpy
soundfile
```

---

## 🛡 Licença

Distribuído sob a licença **MIT**.  
Sinta‑se livre para usar, modificar e melhorar!

---

## 🙋🏻 Autor

**Murilo Gonçalves Saquetti dos Santos**  
Assistente de Voz com Inteligência Artificial  
Jacareí – São Paulo, Brasil
