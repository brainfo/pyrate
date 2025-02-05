import code
from code import InteractiveInterpreter 
## using exec
import os
import itertools  # Import itertools for permutations
import logging
## compile the code

def run_python_code(codeblock):
    language = codeblock.language
    assert language in ["python", ""]
    source = codeblock.code
    ## print with all the special characters
    # ##what if just exec
    # exec(source)
    compile_code = code.compile_command(source, '<string>', 'exec')
    ## logging the compile code
    logging.info(f"Compiled code: {compile_code}")
    InteractiveInterpreter().runcode(compile_code)

def run_shell_code(codeblock):
    language = codeblock.language
    assert language == "bash"
    source = codeblock.code
    os.system(source)

def run_code_single(codeblock):
    language = codeblock.language
    if language in ["python", ""]:
        run_python_code(codeblock)

    elif language == "bash":
        run_shell_code(codeblock)

def run_code_orderded(codeblocks):
    for cb in codeblocks:
        logging.info(f"Running {cb.language} codeblock: {cb.code}")
        try:
            run_code_single(cb)
        except Exception as e:
            logging.error(f"Error running codeblock: {e}")

def run_code_permutations(codeblocks, retry_count=0, max_retries=3):
    # Generate all permutations of the codeblocks
    for perm in itertools.permutations(codeblocks):
        logging.info(f"Trying permutation: {[cb.language for cb in perm]}")
        run_code_orderded(perm)  # Run the code blocks in this permutation
        if retry_count < max_retries:
            retry_count += 1
        else:
            logging.error("Max retries reached. Stopping execution.")
            break

