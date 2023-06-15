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

## 🎉 Cool Examples 🚀

ToolGPT isn't just about chat – it's about supercharging chat with the power of function calls! Let's have a look at two exciting examples that demonstrate ToolGPT's capabilities to a whole new level:

### 🧮 Algebra Capabilities (algebra_example) 🤓

Ever wished your chatbot could solve algebraic equations? Now it can! With ToolGPT, you can make ChatGPT solve math problems by leveraging the power of Python functions. Check out the `algebra_example` directory for an enlightening example:

```
├── algebra_example
│   ├── algebraExample.py
│   └── algebraMethods.py
```

In this example, the `algebraMethods.py` file contains custom Python functions for solving algebraic problems. The `algebraExample.py` file showcases how ToolGPT uses these functions to add algebraic capabilities to a chatbot. Run the `algebraExample.py` to see how ChatGPT can now solve math problems for you!

### 🎙️ PowerPoint Presentation Capabilities (powerpoint_example) 🖥️

Yes, you read that right. ToolGPT can even help in automating the creation of PowerPoint presentations! 🎉

Explore the `powerpoint_example` directory for an example that's worth a thousand slides:

```
├── powerpoint_example
│   ├── powerpointExample.py
│   └── powerpointMethods.py
```

In this example, `powerpointMethods.py` contains Python functions that interact with Microsoft's PowerPoint application. The `powerpointExample.py` file demonstrates how ToolGPT uses these functions to create PowerPoint presentations based on user instructions. With this, creating PowerPoint presentations is as easy as chatting!

With ToolGPT, the possibilities are endless. Create more Python functions, and ToolGPT will help you incorporate them into your chatbot. It's like having a chatbot on steroids, all in the comfort of your Python environment!


## 📚 Documentation

You can find more detailed documentation in the code itself!

## 🌐 Contribute

We welcome contributions from the community! If you'd like to contribute, please fork the repository and submit a pull request.

## 📄 License

ToolGPT is licensed under the MIT license. For more details, see [LICENSE](./LICENSE).

## ⭐ Star us on GitHub

If you find this package useful, please consider starring us on GitHub!

Happy coding! 🚀🚀
