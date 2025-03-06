import ollama 

client = ollama.Client()
model = "DeepSeek-R1"
prompt = "what is the best Ollama model for generating python code related to implementing AI models?"

response = client.generate(model=model, prompt=prompt)

print("Resonse: ")
print(response.response)