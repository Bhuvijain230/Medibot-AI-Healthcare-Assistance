# Step 1: Load .env and setup API key
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step 2: Convert image to base64
import base64

#image_path = "cut.jpg"
def encode_image(image_path):
    image_file = open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode("utf-8")
# with open(image_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Step 3: Setup Groq Multimodal LLM
from groq import Groq
query = "What's wrong with me? and provide the solution"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query,model,encoded_image):
    client = Groq(api_key=GROQ_API_KEY)

   
    

    messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": query},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                },
            },
        ],
    }
    ]

    chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
    )

    return chat_completion.choices[0].message.content
