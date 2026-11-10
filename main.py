import json
from ollama import Client
from pathlib import Path

# Initialize the client pointing to your remote LAN host
client = Client(host='http://192.168.50.50:11434')

systemPrompt = Path("system_prompt.txt").read_text()
print(systemPrompt)


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
    messages=[
        {'role': 'system', 'content': systemPrompt},
        {'role': 'user', 'content': 'What is the weather like in New York?'},
    ],
    tools=[weather],
)

print(response.message)
print("=======================")

functions = {
    'weather': weather,
}
for call in response.message.tool_calls:
    name = call.function.name
    args = call.function.arguments
    resp = functions[name](**args)
    print(resp)
