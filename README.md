# pyrate

## Before usage

export OPENAI_API_KEY= #Your openai api key

## Usage

### Conversation mode

`python pyrate.py`  

In this mode, you can have conversations with the model.  

### Executive mode

`python pyrate.py --run`. 

In this mode, you can have conversations, in case the output from the model includes code blocks, the code blocks will be run automatically  

- Output
  - the stdout will be as part of the output of the model in the same conversation with you
  - the files will be written in your file system.  
- Executive order
  - It will first try to run the code blocks in the order of being generated, if it fails, then will permutate the code block orders to try and execute.  
  - Therefore, could be good if the prompt set to generate the code block in executive order.
- Motivation
  - You don't need to read the output from the model to get the results of suggested project codes.  

### To choose models

With `--model` parameter  

Example: `python pyrate.py --model gpt-4o-mini`
