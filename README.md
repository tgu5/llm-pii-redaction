# takehome-pii-redaction

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
