from ToolGPT import ChatGPTWithFunctions

import os
import openai
from dotenv import load_dotenv
from powerpointMethods import create_presentation, add_slide_with_bullets

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "Make a 5 page presentation about bananas."
wrapper = ChatGPTWithFunctions()
ans = wrapper.prompt_with_functions(prompt, [create_presentation, add_slide_with_bullets])
print(ans)