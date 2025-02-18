import re

class Redactor:
    def __init__(self):
        # This could be dynamically generated or configured:
        self.entity_patterns = {
            'US_SSN': r'\b\d{3}-\d{2}-\d{4}\b',
            'PHONE_NUMBER': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'EMAIL_ADDRESS': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }
        self.mappings = {}

    def redact(self, text):
        # This should loop over each entity and replace multiple matches with a sequential placeholder.
        for entity, pattern in self.entity_patterns.items():
            matches = re.findall(pattern, text)
            for i, match in enumerate(matches, start=1):
                placeholder = f"{entity}_{str(i).zfill(4)}"  # e.g., US_SSN_0001
                self.mappings[placeholder] = match
                text = text.replace(match, placeholder)
        return text

    def unredact(self, text):
        # Replace placeholders with original sensitive data
        for placeholder, original in self.mappings.items():
            text = text.replace(placeholder, original)
        return text
    
    def clear(self):
        self.mappings.clear() 