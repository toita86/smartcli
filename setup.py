from setuptools import setup, find_packages

setup(
    name="smartcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "smart-cli=smartcli.cli:cli",
        ],
    },
    author="Eduard Brahas",
    description="AI-powered terminal assistant using Ollama",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
)
