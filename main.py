from ollama import Client

# Initialize the client pointing to your remote LAN host
client = Client(host='http://192.168.50.50:11434')

def weather(city: str) -> str:
    """
    Get weather for a city name.

    Args:
        city: Name of a city (e.g. "New York")
    """

    return "22°C"
    

# Use the client object exactly like the global functions
response = client.chat(
    model='gemma4:12b',
    messages=[{'role': 'user', 'content': 'What is the weather like in New York?'}]
    tools=[weather],
)

print(response.message.content)
