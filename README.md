# pyrate

- To get an REPL interacting with open-ai models, use `python pyrate.py`

In this mode, you can have conversations with the model.

- To get whatever replied by the model to be automatically run, use `python pyrate.py --run`

In this mode, you can have conversations, in case the output from the model includes code blocks, the code blocks will be run and the output stdout will be as part of the output of the model in the same conversation with you, the files will be written in your file system.

*Motivation*: You don't need to read the output from the model to get the results of suggested project codes.
