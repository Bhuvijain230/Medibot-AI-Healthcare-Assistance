import imageio_ffmpeg as ffmpeg
print(ffmpeg.get_ffmpeg_version())
import os
from pydub import AudioSegment

# Manually specify the FFmpeg path
os.environ["PATH"] += os.pathsep + r"D:\Medibot Project\ffmpeg-2025-02-20-git-bc1a3bfd2c-full_build\bin"

# Verify FFmpeg is found
print(AudioSegment.ffmpeg)

#step1: Setup Audio recorder(ffmpeg & portaudio)
import logging  # helps us in debugging
import speech_recognition as sr
from  pydub import AudioSegment
from io import BytesIO
logging.basicConfig(level = logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).

    """
    recognizer = sr.Recognizer() # Initializes the speech recognition engine
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_filepath="patient_voice_test_for_patient.mp3"
record_audio(file_path=audio_filepath)

#step2 : Setup speech to text-STT-model for transcription
from groq import Groq
GROQ_API_KEY="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"
stt_model="whisper-large-v3"
def transcribe_with_groq(stt_model,audio_filepath,GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
 
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text


