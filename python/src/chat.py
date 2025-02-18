import openai
from redactor import Redactor

class GPTChat:
    def __init__(self, model="gpt-4"):
        self.model = model
        # Initialize with empty system message
        self.messages = [{"role": "system", "content": ""}]
        self.redactor = Redactor()

    def chat(self, user_input, max_tokens=200):
        """
        Sends a prompt to OpenAI's API while maintaining conversation history.
        Streams the response token by token, handling cross-chunk redacted strings.

        :param user_input: Dictionary containing 'system_prompt' and 'prompt' keys
        :param max_tokens: The maximum number of tokens to generate.
        """
        print('\nNew chat! User input: ', user_input)
        self.messages[0]["content"] = user_input['system_prompt']
        
        self.redactor.clear()
        redacted_input = self.redactor.redact(user_input['prompt'])
        # print('\nredacted input sent to GPT: ', redacted_input) # debug
        self.messages.append({"role": "user", "content": redacted_input})

        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=self.messages,
                max_tokens=max_tokens,
                stream=True
            )

            print("\n------------------------Streaming unredacted response-------------------------------\n")
            
            # Buffer for handling cross-chunk redacted strings
            buffer = ""
            complete_response = ""
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    buffer += content
                    complete_response += content
                    
                    # Check if we have any complete redacted strings in buffer
                    unredacted_chunk = ""
                    remaining_buffer = buffer
                    
                    for placeholder in self.redactor.mappings.keys():
                        if placeholder in buffer:
                            # Split buffer at the placeholder
                            parts = buffer.split(placeholder)
                            
                            if len(parts) > 1:
                                # Process all complete parts except the last one
                                for part in parts[:-1]:
                                    unredacted_chunk += part + self.redactor.mappings[placeholder]
                                # Keep the last part in buffer
                                remaining_buffer = parts[-1]
                    
                    if unredacted_chunk:
                        print(unredacted_chunk, end="", flush=True)
                        buffer = remaining_buffer
                    elif len(buffer) > max(len(p) for p in self.redactor.mappings.keys()):
                        # If buffer is longer than longest possible placeholder and no matches,
                        # print the first character and shift buffer
                        print(buffer[0], end="", flush=True)
                        buffer = buffer[1:]
            
            # Process any remaining buffer content
            if buffer:
                final_unredacted = self.redactor.unredact(buffer)
                print(final_unredacted, end="", flush=True)
                
            print("\n--------------------------------------------------------------------------------\n")

        except Exception as e:
            print(f"\nError: {e}\n")
            return f"Error: {e}" 