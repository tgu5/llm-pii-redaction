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
        Streams the response token by token while accumulating the full response.

        :param user_input: Dictionary containing 'system_prompt' and 'prompt' keys
        :param max_tokens: The maximum number of tokens to generate.
        :return: The complete unredacted response from GPT.
        """
        print('New chat! User input: ', user_input)
        # Update system message with the provided system prompt
        self.messages[0]["content"] = user_input['system_prompt']
        
        self.redactor.clear()
        redacted_input = self.redactor.redact(user_input['prompt'])
        print('\nredacted input sent to GPT: ', redacted_input) # comment out for black-boxing
        self.messages.append({"role": "user", "content": redacted_input})

        try:
            # Initialize stream response
            response = openai.chat.completions.create(
                model=self.model,
                messages=self.messages,
                max_tokens=max_tokens,
                stream=True
            )

            # Accumulate the complete response while streaming
            complete_response = ""
            
            # comment out for black-boxing
            print("\n------------------------Redacted response stream-------------------------------\n", end="", flush=True) 
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    complete_response += content
                    print(content, end="", flush=True) # comment out for black-boxing
            print("------------------------------------------------------------------------------------------------\n")  # New line after response is complete
            
            # Unredact the complete response and update conversation history
            unredacted_reply = self.redactor.unredact(complete_response)
            self.messages.append({"role": "assistant", "content": unredacted_reply})
            
            return "\n------------------------Unredacted response stream-------------------------------\n" + unredacted_reply + ("\n-----------------------------------------\n")

        except Exception as e:
            print(f"\nError: {e}\n")
            return f"Error: {e}" 