import inspect
import re
import openai
import json
import os

from dotenv import load_dotenv
# from methods import add, mul, sub
from presentationMethods import create_presentation, add_slide_with_bullets

def parse_docstring(function):
    doc = inspect.getdoc(function)

    # Find function description
    function_description = re.search(r'(.*?)Parameters', doc, re.DOTALL).group(1).strip()

    # Find parameter descriptions
    parameters_description = re.findall(r'(\w+)\s*:\s*(\w+)\n(.*?)(?=\n\w+\s*:\s*|\nReturns|$)', doc, re.DOTALL)

    # Get the parameters from the function signature
    signature_params = list(inspect.signature(function).parameters.keys())

    # Construct the parameters dictionary
    properties = {}
    required = []
    for name, type, description in parameters_description:
        name = name.strip()
        type = type.strip()
        description = description.strip()

        required.append(name)
        properties[name] = {
            "type": type,
            "description": description,
        }

    # Check if the number of parameters match
    if len(signature_params) != len(required):
        raise ValueError(f"Number of parameters in function signature ({len(signature_params)}) does not match the number of parameters in docstring ({len(required)})")

    # Check if each parameter in the signature has a docstring
    for param in signature_params:
        if param not in required:
            raise ValueError(f"Parameter '{param}' in function signature is missing in the docstring")

    parameters = {
        "type": "object",
        "properties": properties,
        "required": required,
    }

    # Construct the function dictionary
    function_dict = {
        "name": function.__name__,
        "description": function_description,
        "parameters": parameters,
    }

    return function_dict

def get_role_message_dict(role, content=None, fn_name=None, arguments=None, result=None):
    """
    Get message dicts for different roles
    """
    message_dict = {"role":role}
    if role == "user":
        message_dict["content"] = content
    elif role == "assistant":
        message_dict["content"] = content
        message_dict["function_call"] = {}
        message_dict["function_call"]["name"] = fn_name
        message_dict["function_call"]["arguments"] = arguments
    elif role == "function":
        message_dict["name"] = fn_name
        message_dict["content"] = f'{{"result": {str(result)} }}'
    return message_dict

def run_with_functions(messages, function_dicts, COMPLETION_MODEL = "gpt-3.5-turbo-0613"):
    """
    Gets the ChatGPT completion based on list of given function_dicts
    """
    response = openai.ChatCompletion.create(
        model=COMPLETION_MODEL,
        messages=messages,
        functions=function_dicts,
        temperature=0,
    )
    return response

def prompt_with_functions(prompt, functions, COMPLETION_MODEL="gpt-3.5-turbo-0613"):
    """
    Runs the prompt with given functions
    """
    print(prompt)
    function_dicts = [parse_docstring(fun) for fun in functions]
    messages = [get_role_message_dict("user", content=(prompt))]

    while True:
        response = run_with_functions(messages, function_dicts)

        if response.choices[0]["finish_reason"] == "stop":
            print(response.choices[0]["message"]["content"])
            print("Received STOP signal")
            break

        elif response.choices[0]["finish_reason"] == "function_call":
            print("Received FUNCTION_CALL signal")
            fn_name = response.choices[0].message["function_call"].name
            arguments = response.choices[0].message["function_call"].arguments
            print(arguments)
            json_arguments = json.loads(arguments)
            function = globals()[fn_name]
            result = function(**json_arguments)
            messages.append(get_role_message_dict("assistant", fn_name=fn_name, arguments=arguments))
            messages.append(get_role_message_dict("function", fn_name=fn_name, result=result))
            response = run_with_functions(messages, function_dicts)


if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # prompt = "What is five plus ten minus fifteen times two?"
    # ans = prompt_with_functions(prompt, [add, sub, mul])
    prompt = "Make a 5 page presentation about bananas."
    ans = prompt_with_functions(prompt, [create_presentation, add_slide_with_bullets])
    
    print(ans)
