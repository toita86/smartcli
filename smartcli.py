import subprocess
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "codellama:latest"


def ask_ollama(nl_query):
    """
    Ask Ollama to perform a task based on a natural language query.

    Parameters:
        nl_query (str): The natural language query to be processed.

    Returns:
        str: The output of the task performed by Ollama.
    """
    prompt = f"You are a helpful Linux shell assistant. \
        Convert the following natural language instruction \
        into a single bash command, it must not be given nothing more than the command \
        :\n\nInstruction: {nl_query}\n\nCommand:"
    response = requests.post(
        OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=10
    )
    return response.json()["response"].strip()


def main():
    """
    The main entry point for the smartcli program.

    Parameters:
        sys (module): The Python sys module.

    Returns:
        None
    """
    if len(sys.argv) < 2:
        print("Usage: python smartcli.py 'Your natural language query here'")
        return

    nl_query = " ".join(sys.argv[1:])
    print(f"🧠 Interpreting: {nl_query}")

    bash_cmd = ask_ollama(nl_query)
    print(f"💡 Suggested command:\n{bash_cmd}")
    bash_cmd = bash_cmd.strip("`").strip('"').strip("'")

    confirm = input("Run this command? [y/N]: ").strip().lower()
    if confirm == "y":
        subprocess.run(bash_cmd, shell=True, check=True)
    else:
        print("❌ Cancelled.")


if __name__ == "__main__":
    main()
