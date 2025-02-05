from openai import OpenAI
import os
import sys
import random
import string
import colorama
import shutil
import argparse
import readline
from colorama import Fore, Back, Style
from src import codeblock
from src import run
import logging

"""
Pirate: pirating openai using openai-python
"""

def main():
    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )
    def parse_args():
        parser = argparse.ArgumentParser(description="Pyrate: take from ChatGPT")
        parser.add_argument(
            "--model",
            default="gpt-4o-mini", ## gpt-4o-mini is so cheap
            choices=["gpt-4", "code-davinci-002", "text-davinci-003", "o3-mini", "gpt-4o-mini"],
            help="Choose the API model to use",
        )
        parser.add_argument(
            "--temperature",
            default=0.7,
            type=float,
            help="Control the randomness of the response (default: 0.7)",
        )
        parser.add_argument(
            "question", nargs="*", help="Optional question for non-interactive mode"
        )
        ## -[] parse the python environment
        # parser.add_argument(
        #     "--python", action="store_true", help="Run the code in python environment"
        # )
        parser.add_argument(
            "--logging", action="store_true", help="logging file path"
        )
        parser.add_argument(
            "--run", action="store_true", help="Run the code after generating it"
        )
        return parser.parse_args()

    def initial_promt():
        term_width = shutil.get_terminal_size((80, 20)).columns

        print(
            Fore.RED
            + "Ask a question, or 'q' to quit:"
            + "\n"
        )

    def get_user_input(prompt):
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            return "q"

    args = parse_args()

    messages = []


    if args.question:
        prompt = " ".join(args.question).rstrip(string.punctuation)
    else:
        initial_promt()
        prompt = get_user_input(Fore.BLUE + "You: ")
    if args.logging:
            logging.basicConfig(filename=args.logging, level=logging.DEBUG, format='%(asctime)s - %(message)s')

    while True:
        if prompt.lower() in ["quit", "q", "bye"]:
            break
        messages.append({"role": "user", "content": prompt})
        ## to do, with prompt_tookit, add the role of the ai
        response = client.chat.completions.create(
            model=args.model, messages=messages, temperature=args.temperature
        )
        reply = response.choices[0].message.content
        if args.run:
            cbs = codeblock.create_code_block(reply)
            ## logging the len of cbs
            logging.info(f"Codeblocks: {len(cbs)}")
            run.run_code_permutations(cbs)
        messages.append({"role": "assistant", "content": reply})
        print(Fore.RED + "\nPyrate: " + reply + "\n")

        if args.question:
            break
        else:
            prompt = get_user_input(Fore.BLUE + "You: ")


if __name__ == "__main__":
    main()
