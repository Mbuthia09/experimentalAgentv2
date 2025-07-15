from llm_axe import OllamaChat, OnlineAgent, PdfReader


llm = OllamaChat(model="llama3.1:8b")

pdfReader = PdfReader(llm)

resp = pdfReader.ask("Using winPE", [
                     "Installation_steps.pdf"])


onlineAgent = OnlineAgent(llm)


prompt = "Can you tell me what the latest update for Unreal Engine 5 is?"
print("Sending request to agent...")
resp = online_agent.search(prompt)
print("Response received:")
print(resp)
