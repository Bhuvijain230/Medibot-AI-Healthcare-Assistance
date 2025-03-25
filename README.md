# 🩺 Medibot - AI Healthcare Assistant

**Medibot** is an intelligent, voice-enabled healthcare assistant that uses advanced AI models to analyze medical images, understand patient voice input, and respond with human-like medical advice — all in one seamless Gradio interface.

> 💡 Built for learning and experimentation. Not a replacement for real medical professionals.

---

## 🎯 Features

- 🎙️ **Speech-to-Text**: Converts patient voice input to text using Whisper/Groq models.
- 🧠 **Medical Image Analysis**: Accepts image input and analyzes it using multi-modal LLMs like LLaMA.
- 🗣️ **AI Doctor Response**: Returns a detailed yet concise voice reply using ElevenLabs or gTTS.
- 🖼️ **Gradio Interface**: Intuitive UI for uploading images and recording voice inputs.
- 🔊 **Voice Output**: Doctor’s reply is automatically played back as realistic speech.

---

## 🚀 Tech Stack

| Feature | Technology |
|--------|------------|
| Voice Input | Gradio + Microphone |
| Transcription | Whisper / Groq API |
| Image Encoding | CLIP + LLaMA 3.2 Vision |
| AI Response | LLaMA (Vision-Language Model) |
| Text-to-Speech | gTTS / ElevenLabs |
| Interface | Gradio |
| Audio Playback | playsound / pydub (platform dependent) |

---
## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Bhuvijain230/Medibot-AI-Healthcare-Assistance.git
cd Medibot-AI-Healthcare-Assistance

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your .env file with API keys
cp .env.example .env
# Add your GROQ_API_KEY, ELEVENLABS_API_KEY, etc.

# 5. Run the app
python gradio_app.py
