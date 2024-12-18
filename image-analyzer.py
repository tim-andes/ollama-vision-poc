from ollama import chat
# from pathlib import Path

# Pass in the path to the image
image_name = input('Please enter the path to the image (.jpg): ')
path = "images/" + image_name

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = chat(
  model='phi3',
  messages=[
    {
      'role': 'user',
      'content': 'What is in this image? Be concise.',
      'images': [path],
    }
  ],
)

print(response.message.content)