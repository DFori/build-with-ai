import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = ""
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

vision_model = genai.GenerativeModel('gemini-1.5-flash-latest')

import PIL.Image
image = PIL.Image.open('download.jpeg')

response = vision_model.generate_content(["Explain this image", image])
print(response.text)
