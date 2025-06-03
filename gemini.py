import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()





genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain Python decorators with an example")

print(response.text)
