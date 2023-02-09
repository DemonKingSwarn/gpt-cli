#!/usr/bin/env python3

import openai

import time
import itertools
import sys
import os

spinner = itertools.cycle(['-', '/', '|', '\\'])

# Initialize the OpenAI API client with your API key
openai.api_key = f"{os.getenv('OPENAI_API_KEY')}"


# Define a function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

def loading():
    i=0
    while i<10:
        sys.stdout.write(next(spinner))  # write the next character
        sys.stdout.flush()  # flush the output buffer
        sys.stdout.write('\b') # erase the last written character
        i += 1
        time.sleep(0.1)  # wait for a bit

# Continuously prompt the user for input and generate responses
def __start__():
    while True:
        try:
            try:
                prompt = input("\033[1;35m You: \033[0m")
                response = generate_response(prompt)
                loading()
                print(f"\033[1;32m ChatGPT:\033[0m \033[1;36m{response}\033[0m")
            except KeyboardInterrupt:
                exit(0)
        except Exception as e:
            print("\033[1;31m [!] Invalid Error Occured \033[0m")
            exit(1)

if __name__ == "__main__":
    __start__()
