import subprocess
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma:latest"


def ask_ollama(nl_query):
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
        OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=10
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


def cli():
    """
    The main entry point for the smartcli program.

    Parameters:
        sys (module): The Python sys module.

    Returns:
        None
    """
    if len(sys.argv) < 2:
        print("Usage: smart-cli 'your natural language query'")
        return

    nl_query = " ".join(sys.argv[1:])
    print(f"🧠 Interpreting: {nl_query}")

    bash_cmd = ask_ollama(nl_query)
    print(f"💡 Suggested command:\n{bash_cmd}")

    confirm = input("Run this command? [y/N]: ").strip().lower()
    if confirm == "y":
        subprocess.run(bash_cmd, shell=True)
    else:
        print("❌ Cancelled.")
