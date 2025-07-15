import ollama

client = ollama.Client()

model = "llama3.1:8b"
prompt = "What is python?"

response = client.generate(model=model, prompt=prompt)

print("Response from Ollama:")
print(response.response)
