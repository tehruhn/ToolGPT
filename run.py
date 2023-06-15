import os
import openai
import re
from dotenv import load_dotenv
from presentationMethods import create_presentation, add_slide_with_bullets, get_completion

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#-----------

QUESTION = (
    "Make a 5 page presentation about the political impact of cricket in India. Each page should have a theme and 4 long text points about the theme."
)
messages = [
    {"role": "user", "content": QUESTION},
]

# -----------

while True:
    response = get_completion(messages)
    print(response)

    if response.choices[0]["finish_reason"] == "stop":
        print(response.choices[0]["message"]["content"])
        break

    elif response.choices[0]["finish_reason"] == "function_call":
        fn_name = response.choices[0].message["function_call"].name
        arguments = response.choices[0].message["function_call"].arguments

        function = locals()[fn_name]
        result = function(arguments)

        messages.append(
            {
                "role": "assistant",
                "content": None,
                "function_call": {
                    "name": fn_name,
                    "arguments": arguments,
                },
            }
        )

        messages.append(
            {
                "role": "function", 
                "name": fn_name, 
                "content": f'{{"result": {str(result)} }}'}
        )

        response = get_completion(messages)

