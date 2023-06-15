# 🛠️ ToolGPT 🤖

Introducing ToolGPT, your power tool to tap into the groundbreaking function-calling abilities of OpenAI's GPT-4-0613 and GPT-3.5-turbo-0613 models! 🚀

With ToolGPT, developers now have the capability to describe Python functions to the model, enabling the model to intelligently output a JSON object containing arguments to call those functions. This revolutionary feature seamlessly integrates GPT's powerful capabilities with external tools and APIs in a whole new way, offering a highly reliable method to extract structured data.

What's even more exciting? The GPT models have been expertly fine-tuned to not only detect when a function needs to be called based on user's input, but also to respond with a JSON that conforms to the function's signature. This groundbreaking function calling ability makes it possible for developers to interact with the model in a structured way, effectively transforming natural language queries into executable function calls. 

From creating chatbots that can call external tools to answer questions, converting natural language into API calls or database queries, to extracting structured data from text - the possibilities with ToolGPT are limitless.

And the icing on the cake? All of this can be done with ANY custom Python function that you define, simply by writing a good docstring. Yes, you heard it right! You can define any Python function and run it LOCALLY on your machine without the need to share your data with OpenAI. ToolGPT is like having an intelligent system that decides when and where to call APIs, all while ensuring the privacy and security of your data. 🛡️ 

Welcome to the future of AI interaction with ToolGPT! 🚀🚀


## 📥 Installation

ToolGPT is as easy to install as any other Python package. Just run the following command:

```
pip install ToolGPT
```

## 🏃‍♀️ Quickstart

Once you have ToolGPT installed, you can use it as follows:

```
from ToolGPT import ChatGPTWithFunctions

# Define your functions with good docstrings in NumpyCode format
def add(a, b):
    """
    Adds Two Numbers

    Parameters
    ----------
    a : integer
        number to be added
    b : integer
        number to be added

    Returns
    -------
    integer
        sum
    """
    return a + b


# Instantiate the class
wrapper = ChatGPTWithFunctions()

# Define a prompt
prompt = "What is five plus ten?"

# Use the chatbot
ans = wrapper.prompt_with_functions(prompt, [add])
print(ans)
```

## 📚 Documentation

You can find more detailed documentation in the code itself!

## 🌐 Contribute

We welcome contributions from the community! If you'd like to contribute, please fork the repository and submit a pull request.

## 📄 License

ToolGPT is licensed under the MIT license. For more details, see [LICENSE](./LICENSE).

## ⭐ Star us on GitHub

If you find this package useful, please consider starring us on GitHub!

Happy coding! 🚀🚀
