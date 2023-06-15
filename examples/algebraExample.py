from ToolGPT import ChatGPTWithFunctions

import os
import openai
from dotenv import load_dotenv
from algebraMethods import add, mul, sub

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is five plus ten minus fifteen times two?"
wrapper = ChatGPTWithFunctions()
ans = wrapper.prompt_with_functions(prompt, [add, sub, mul])
print(ans)