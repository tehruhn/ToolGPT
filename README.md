# 🛠️ ToolGPT 🤖

Welcome to ToolGPT! This package is a powerful, user-friendly wrapper for OpenAI's GPT models that enables you to easily incorporate advanced AI-powered functionalities into your chatbots or virtual assistants.

ToolGPT gives you the ability to leverage the power of OpenAI's cutting-edge GPT models to perform tasks that require understanding and generating human-like text. 

With ToolGPT, you can get your chatbot or virtual assistant to not only chat like a human, but also execute functions based on chat commands! 🚀🚀

## 📥 Installation

ToolGPT is as easy to install as any other Python package. Just run the following command:

```
pip install ToolGPT
```

## 🏃‍♀️ Quickstart

Once you have ToolGPT installed, you can use it as follows:

```
from ToolGPT import ChatGPTWithFunctions

# Define your functions
def add(x, y):
    """Add two numbers."""
    return x + y

def sub(x, y):
    """Subtract two numbers."""
    return x - y

# Create a functions dictionary
functions_dict = {
    "add": add,
    "sub": sub
}

# Instantiate the class
wrapper = ChatGPTWithFunctions(functions_dict)

# Define a prompt
prompt = "The user says: 'What is 5 plus 3?'"

# Use the chatbot
ans = wrapper.prompt_with_functions(prompt, [add, sub])
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
