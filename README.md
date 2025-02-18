# takehome-pii-redaction

## Demo
### with detailed redaction-unredaction process:
<video src="https://github.com/user-attachments/assets/72e02ddd-c632-4173-980b-29d1446235ef"></video>

### user-facing "black-boxed" API:
<video src="https://github.com/user-attachments/assets/6c153787-1c3c-47a4-9470-465666aa59d1"></video>


## Overview
The program will:
1. Load requests from `requests.csv`
2. Automatically redact sensitive information before sending to GPT
3. Process each request through GPT-4
4. Unredact the information in the response
5. Print each response

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
- handle more PII types in `redactor.py`
- make user-facing API also answer in stream by handling edge cases like split redacted string in two streams
