from setuptools import setup, find_packages

setup(
    name='ToolGPT',
    version='0.0.1',
    url='https://github.com/tehruhn/ToolGPT',
    author='Tarun Raheja',
    author_email='tarunraheja1234@gmail.com',
    description='Package to interface Python functions with ChatGPT',
    packages=find_packages(),    
    install_requires=['openai'],
)
