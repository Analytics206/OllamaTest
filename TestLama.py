import ollama 

client = ollama.Client()
model = "DeepSeek-R1"
prompt = "What is the capital of France?"

response = client.generate(model=model, prompt=prompt)

print("Resonse: ")
print(response.response)