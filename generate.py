from ollama import generate

response = generate('deepseek-r1', 'Why is the sky blue?')
print(response['response'])