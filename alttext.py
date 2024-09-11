import requests
import base64
import os

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_alt_text(image_path):
    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"

    # Encode the image
    base64_image = encode_image(image_path)

    # Prepare the payload
    payload = {
        "model": "benzie/llava-phi-3",
        "prompt": "Describe this image in detail for an alt text:",
        "stream": False,
        "images": [base64_image]
    }

    # Send the request to Ollama
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()['response']
    else:
        return f"Error: {response.status_code} - {response.text}"

def process_image(image_path):
    if os.path.isfile(image_path):
        alt_text = generate_alt_text(image_path)
        print(f"File: {os.path.basename(image_path)}")
        print(f"Alt Text: {alt_text}")
    else:
        print(f"Error: The file '{image_path}' does not exist.")

if __name__ == "__main__":
    image_path = r"D:\123\Me 1.jpg"  # Path to your image
    process_image(image_path)