# VoiceBot UI with Gradio
import os
import gradio as gr
from dotenv import load_dotenv

# Load environment variables (from Hugging Face Secrets when deployed)
load_dotenv()

# Import your helper modules
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# System prompt for the doctor model
system_prompt = """You have to act as a professional doctor. I know you are not, but this is for learning purposes.
What's in this image? Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them.
Do not add any numbers or special characters in your response.
Your response should be in one long paragraph. Also provide the medicines or other things the patient can use in points.
Always answer as if you are talking to a real person.
Don't say 'In the image I see' but say 'With what I see, I think you have...'
Don’t respond as an AI model or use markdown — mimic a real doctor.
 No preamble — start your answer directly."""

# Core function: handles audio and image input
def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze."

    # Generate speech from the doctor's response
    voice_of_doctor = text_to_speech_with_elevenlabs(
        input_text=doctor_response,
        output_filepath="final.mp3"
    )

    return speech_to_text_output, doctor_response, voice_of_doctor

# Gradio UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Speak your symptoms"),
        gr.Image(type="filepath", label="Upload affected area image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3", label="Doctor's Voice")
    ],
    title="🩺 MediBot – AI Doctor with Vision and Voice",
    #description="Upload your voice + image to receive a diagnosis-style response from MediBot. Built using Gradio, LLaMA, Whisper, and ElevenLabs."
)

iface.launch()
