# PII Redaction and Reconstruction LLM

This project implements a simple redaction pipeline that detects and redacts personally identifiable information (PII) from user-submitted requests before sending them to a Large Language Model (LLM). After receiving a response from the LLM, the system reconstructs the original content by unredacting the placeholders back into their original values. This was originally built as part of a take-home engineering assignment.

## Problem Overview

Many enterprises want to avoid exposing sensitive data (e.g. SSNs, phone numbers, email addresses) to external LLM providers. This project simulates a middleware service that:

1. **Redacts** sensitive data from user inputs before forwarding to the LLM.
2. **Invokes the LLM API** (OpenAI or compatible).
3. **Unredacts** the LLM responses before returning them to the user.

The system ensures users receive seamless responses, as if no redaction ever occurred behind the scenes.

## Redacted Entities

The following types of PII are detected and redacted:

- US Social Security Numbers (`US_SSN`)
- Phone Numbers (`PHONE_NUMBER`)
- Email Addresses (`EMAIL_ADDRESS`)

## The program will:
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
- `cd llm-pii-redaction`
- use a venv: `python -m venv venv && source venv/bin/activate`
- install packages: `pip install -r python/requirements.txt`
- run from root folder: `python python/src/main.py`
