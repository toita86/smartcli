"""
This module contains functions to interact with Ollama 
for converting natural language instructions into Bash commands.
"""

import subprocess
import os
import json
import argparse
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(model, nl_query):
    """
    Ask Ollama to perform a task based on a natural language query.

    Parameters:
        nl_query (str): The natural language query to be processed.

    Returns:
        str: The output of the task performed by Ollama.
    """
    prompt = f"""You are a Linux shell assistant. 
        Your only task is to convert natural language instructions into a single bash command. 
        Do not provide any explanation or context. 
        Only respond with a single line in the format: cmd:<command>

        Instruction: {nl_query}
        cmd:"""

    response = requests.post(
        OLLAMA_URL, json={"model": model, "prompt": prompt, "stream": False}, timeout=10
    )
    raw = response.json()["response"].strip()

    # Extract the command after 'cmd:'
    if raw.lower().startswith("cmd:"):
        cmd = raw[4:].strip()
    else:
        cmd = raw.strip()

    # Clean up possible formatting
    # Remove backticks, quotes, and extract only the first line (the actual bash command)
    cmd = cmd.strip("`\"'\n ").split("\n")[0]
    return cmd


def show_available_models():
    """Display available models"""
    subprocess.run("ollama list", shell=True)


def set_default_model(model_name):
    """Set the default model in the config file."""
    config_dir = os.path.expanduser("~/.config/smartcli")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    config_file = os.path.join(config_dir, "config.json")
    try:
        with open(config_file, "w") as f:
            json.dump({"model": model_name}, f, indent=2)
        print(f"Default model set to {model_name}")
    except Exception as e:
        print(f"Error setting default model: {e}")


def cli():
    """
    The main entry point for the smartcli program.

    Parameters:
        sys (module): The Python sys module.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Smart CLI tool powered by Ollama")
    parser.add_argument("query", nargs="?", help="Your natural language query")
    parser.add_argument("-m", "--model", help="Sets the LLM model to use")
    parser.add_argument(
        "-sm",
        "--show-models",
        action="store_true",
        help="Show available models and exit",
    )
    args = parser.parse_args()

    if args.show_models:
        show_available_models()
        return

    if args.model:
        set_default_model(args.model)
        return

    # Check for existing model configuration
    config_file = os.path.expanduser("~/.config/smartcli/config.json")
    selected_model = None

    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                config = json.load(f)
                selected_model = config.get("model", None)
        except Exception as e:
            print(f"Error reading config file: {e}")

    if not selected_model:
        print("There is no Model defined to use smart-cli. Use --set-model to set one.")
        model_choice = input(
            "Would you like to:\n"
            "[1] Set a default model\n"
            "[2] Show available models\n"
            "[3] Cancel\n"
            "Choose option: "
        )

        if model_choice == "1":
            new_model = input("Enter the model name (e.g., codellama:latest): ")
            set_default_model(new_model)
            return
        elif model_choice == "2":
            show_available_models()
        else:
            print("Exiting...")
            return
    elif not args.query:
        print("Usage: smart-cli 'your natural language query'")
        return
    else:
        print(f"🧠 Interpreting: {args.query}")

        bash_cmd = ask_ollama(selected_model, args.query)
        print(f"💡 Suggested command:\n{bash_cmd}")

        confirm = input("Run this command? [y/N]: ").strip().lower()
        if confirm == "y":
            subprocess.run(bash_cmd, shell=True)
        else:
            print("❌ Cancelled.")
