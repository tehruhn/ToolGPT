from ToolGPT import ChatGPTWithFunctions

import os
import openai
from dotenv import load_dotenv
from sqlMethods import get_max_sale, get_top_rows, setup_database

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# # Uncomment this to make the table
# setup_database()
prompt = "What is the Max Sale? My table is sales_data.db"
wrapper = ChatGPTWithFunctions()
ans = wrapper.prompt_with_functions(prompt, [get_max_sale, get_top_rows])
print(ans)