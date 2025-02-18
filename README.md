# takehome-pii-redaction

## Demo

<video src="https://github.com/user-attachments/assets/9d3753aa-ffbf-42e4-a0e0-a917d0df06aa"></video>


## Overview
The program will:
1. Load requests from `requests.csv`
2. Automatically redact sensitive information before sending to GPT
3. Process each request through GPT-4
4. Unredact and print the response by chunk to the end-user

## Project Structure

- `python/src/`
  - `main.py`: Entry point and program orchestration
  - `chat.py`: GPT chat interaction logic
  - `redactor.py`: PII redaction/unredaction functionality
  - `utils.py`: Utility functions for data loading

## How To Run:
- clone repo
- `cd credal-ai-takehome`
- use a venv: `python -m venv venv && source venv/bin/activate`
- install packages: `pip install -r python/requirements.txt`
- run from root folder: `python python/src/main.py`

## Further Improvements:
- max_tokens is hard-coded for now, but it should be dynamically adjusted according to prompts
- handle more PII types in `redactor.py` like credit card info, physical address, DOB, etc.
- make user-facing API also answer in stream by handling edge cases like split redacted string in two streams
- implement robust error handling for rate limit or user input type error
- for extra security, encrypt sensitive data in memory
