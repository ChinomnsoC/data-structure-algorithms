class SocketHandler:
    def __init__(self, data: str):
        self.data = data
        self.position = 0

    def get_next_char(self) -> str:
        """Returns a single character and moves the handler pointer forward"""
        if self.position >= len(self.data):
            return ""
        else:
            char = self.data[self.position]
            self.position += 1

        return char

    def is_eof(self) -> bool:
        """Returns True if reached the end of the stream"""
        return self.position >= len(self.data)


def search(socket_handler: SocketHandler, search_key: str) -> None:
    """
    Implement a streaming JSON parser that searches for a specific key.

    Args:
        socket_handler: Handler that provides character-by-character stream access
        search_key: The JSON key to search for

    Should output the value associated with search_key to stdout if found.

    Example:
        Input stream: {"k1": 1, "k2": {"k3": ["a", "b", "c"]}, "lookup_key": {"a": 1, "b": [2]}}
        search_key: "lookup_key"
        Expected output: {"a": 1, "b": [2]}

    Constraints:
        - Data size may exceed available RAM, so cannot read entire stream into memory
        - Stream contains a sequence of valid JSON documents
        - Must handle unbounded data size
    """
    def skip_whitespaces():
        while not socket_handler.is_eof():
            char = socket_handler.get_next_char()
            if char not in (' ', '\n', '\t', '\r'):
                return char
        return ""

    def get_key():
        key = ""
        char = skip_whitespaces()
        if char == '"':
            while not socket_handler.is_eof():
                char = socket_handler.get_next_char()
                if char == '"':
                    break
                key += char
        
        return key
            
    
    def get_value():
        value = ""
        char = skip_whitespaces()
        # value could start with " or { or [
        if char in ('{', '['):
            depth = 1
            value += char
            while not socket_handler.is_eof() and depth > 0:
                char = socket_handler.get_next_char()
                value += char
                if char in ('{', '['):
                    depth += 1
                elif char in ('}', ']'):
                    depth -= 1
                    
        else:
            while not socket_handler.is_eof():  
                char = socket_handler.get_next_char()
                if char in (',', '}'):
                    break
                if char not in (' ', '\n', '\t'):
                    value += char   
        return value
    
    while not socket_handler.is_eof():
        char = socket_handler.get_next_char()
        
        if char == "{":
            key = get_key()
            
            if key == search_key:
                char = skip_whitespaces()
                if char == ":":
                    value = get_value()
                    print(value)
                    return
            else:
                char = skip_whitespaces()
                if char == ":":
                    get_value()            
        
# Usage example:
# socket_handler = open_handler(...)
# search(socket_handler, 'lookup_key')
# json_data = '{"k1": 1, "k2": {"k3": ["a", "b", "c"]}, "lookup_key": {"a": 1, "b": [2]}}'
# handler = SocketHandler(json_data)

# # Test reading characters
# while not handler.is_eof():
#     char = handler.get_next_char()
#     print(char, end='')  # Should print your JSON string character by character
