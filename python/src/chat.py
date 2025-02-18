import openai
from redactor import Redactor

class GPTChat:
    def __init__(self, model="gpt-4"):
        self.model = model
        # Initialize with empty system message
        self.messages = [{"role": "system", "content": ""}]
        self.redactor = Redactor()

    def chat(self, user_input, max_tokens=100):
        """
        Sends a prompt to OpenAI's API while maintaining conversation history.

        :param user_input: Dictionary containing 'system_prompt' and 'prompt' keys
        :param max_tokens: The maximum number of tokens to generate.
        :return: The response from GPT.
        """
        # Update system message with the provided system prompt
        self.messages[0]["content"] = user_input['system_prompt']
        
        self.redactor.clear()
        redacted_input = self.redactor.redact(user_input['prompt'])
        self.messages.append({"role": "user", "content": redacted_input})

        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=self.messages,
                max_tokens=max_tokens,
            )
            assistant_reply = response.choices[0].message.content
            unredacted_reply = self.redactor.unredact(assistant_reply)
            self.messages.append({"role": "assistant", "content": unredacted_reply})
            return unredacted_reply

        except Exception as e:
            return f"Error: {e}" 