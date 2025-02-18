import openai
from chat import GPTChat
from utils import load_requests

openai.api_key = "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"

if __name__ == "__main__":
    chat_session = GPTChat()

    print("Start chatting!\n")
    requests = load_requests('requests.csv')
    for r in requests:
        response = chat_session.chat(r)
        print(f"\nResponse: {response}")

