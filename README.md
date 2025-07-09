
# Smartcli

Smartcli is a Python script that uses Ollama to convert natural language instructions into Bash commands. It can be used as a command-line interface for running tasks on Linux systems.

## Requirements

Smartcli requires having installed [ollama](https://ollama.com/) then download a model to your likings, works really great with `codellama` the `7b` version. 
It's not meant to be used with heavy models that take a long time to generate a response, but by using the `-t` flag the timeout for the  Ollama response can be extended.

## Setup
If is the first use just type `smart-cli` and follow the setup wizard.

Later is possible to list all the models available
```
$ smart-cli --show-models
```
then set the one you like with
```
$ smart-cli --model <model_name>
```
optionally set the timeout for the response
```
$ smart-cli --timeout <integer>
``` 

## Usage

To use Smartcli, simply run it with the desired natural language query as an argument. For example:
```bash
$ smart-cli "how can i see all the files in this directory"
```
The script will ask Ollama to convert the query into a Bash command and then prompt you to confirm whether to run the command. If the confirmation is successful, the command will be executed using `subprocess`.

## Features

Smartcli has several features that make it a powerful tool for automating tasks on Linux systems:

* **Natural Language Support**: Smartcli uses Ollama to convert natural language instructions into Bash commands. This means that users can give their instructions in their own words, rather than having to learn a specific syntax or command structure.
* **Using different models**: Supports every Ollama model that's available.

## To do:
* **Dangerous commands**: If the command suggested can cause serious harm a warning is showed
* **Error Detection**: If the user's input results in an error or a syntax issue with the generated Bash command, Smartcli will notify them of the problem and provide suggestions for correcting the issue.
* **History of the previous generated commands**: the option to see an re use past asked commands
