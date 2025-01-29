from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="full-stack-agent",
    version="0.2.0",
    author="Gopal Mathur",
    author_email="mathurgopal1001@gmail.com",
    description="A CLI tool for initializing full-stack projects with best practices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GM-11/full-stack-agent",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "langchain-groq",
        "langchain",
        "langchain-community",
        "inquirer",
        "python-dotenv",
        "tavily-python",
    ],
    entry_points={
        "console_scripts": [
            "full-stack-agent=main:main",
        ],
    },
)
