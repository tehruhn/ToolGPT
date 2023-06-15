import inspect
import re
import openai
import json

class ChatGPTWithFunctions:
    """
    A class that encapsulates the interaction with OpenAI GPT-3 with functions 
    """
    def __init__(self, model="gpt-3.5-turbo-0613"):
        """
        Constructor for ChatGPTWithFunctions class
        
        Parameters
        ----------
        model : str, optional
            The OpenAI GPT model to use. Defaults to "gpt-3.5-turbo-0613".
        """
        self.model = model

    @staticmethod
    def parse_docstring(function):
        """
        Parse the docstring of a function to extract function name, description and parameters.
        
        Parameters
        ----------
        function : Callable
            The function whose docstring is to be parsed.

        Returns
        -------
        dict
            A dictionary with the function's name, description, and parameters.
        """
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

    @staticmethod
    def get_role_message_dict(role, content=None, fn_name=None, arguments=None, result=None):
        """
        Get message dicts for different roles.
        
        Parameters
        ----------
        role : str
            The role of the user.
        content : str, optional
            The content of the message. Defaults to None.
        fn_name : str, optional
            The name of the function. Defaults to None.
        arguments : dict, optional
            The arguments for the function. Defaults to None.
        result : Any, optional
            The result of the function. Defaults to None.

        Returns
        -------
        dict
            The dictionary with the role, content, function name, arguments, and result.
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

    def run_with_functions(self, messages, function_dicts):
        """
        Gets the ChatGPT completion based on list of given function_dicts.
        
        Parameters
        ----------
        messages : list
            List of message dictionaries.
        function_dicts : list
            List of function dictionaries.
        
        Returns
        -------
        OpenAI.ChatCompletion
            The response from ChatCompletion API.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            functions=function_dicts,
            temperature=0,
        )
        return response

    def prompt_with_functions(self, prompt, functions):
        """
        Runs the prompt with given functions.
        
        Parameters
        ----------
        prompt : str
            The prompt to be used with the GPT model.
        functions : list
            List of functions to be used with the GPT model.
        """
        print(prompt)
        fn_names_dict = {}
        for fn in functions:
            fn_names_dict[fn.__name__] = fn
        function_dicts = [self.parse_docstring(fun) for fun in functions]
        messages = [self.get_role_message_dict("user", content=(prompt))]

        while True:
            response = self.run_with_functions(messages, function_dicts)

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
                function = fn_names_dict[fn_name]
                result = function(**json_arguments)
                messages.append(self.get_role_message_dict("assistant", fn_name=fn_name, arguments=arguments))
                messages.append(self.get_role_message_dict("function", fn_name=fn_name, result=result))
                response = self.run_with_functions(messages, function_dicts)
