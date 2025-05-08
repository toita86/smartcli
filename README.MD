
# Smartcli

Smartcli is a Python script that uses Ollama to convert natural language instructions into Bash commands. It can be used as a command-line interface for running tasks on Linux systems.

## Usage

To use Smartcli, simply run it with the desired natural language query as an argument. For example:
```bash
python smartcli.py "List all the files"
```
The script will ask Ollama to convert the query into a Bash command and then prompt you to confirm whether to run the command. If the confirmation is successful, the command will be executed using `subprocess`.

## Features

Smartcli has several features that make it a powerful tool for automating tasks on Linux systems:

* **Natural Language Support**: Smartcli uses Ollama to convert natural language instructions into Bash commands. This means that users can give their instructions in their own words, rather than having to learn a specific syntax or command structure.
* **Command Auto-Completion**: When users are prompted to confirm the command they want to run, Smartcli will suggest possible completions for the command based on their input. This makes it easier to find and run the desired command.
* **Error Detection**: If the user's input results in an error or a syntax issue with the generated Bash command, Smartcli will notify them of the problem and provide suggestions for correcting the issue.

## Requirements

Smartcli requires Python 3.x and the `requests` library to function properly. It also uses Ollama's API to convert natural language instructions into Bash commands. To use Smartcli, users must have an internet connection and a functional installation of Ollama on their system.a functional installation of Ollama on their system.