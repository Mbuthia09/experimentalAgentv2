# This is getting information from the internet
from llm_axe import OllamaChat, OnlineAgent, PdfReader


llm = OllamaChat(model="llama3.1:8b")

onlineAgent = OnlineAgent(llm)
resp = onlineAgent.search(
    "What does the International Livestock Research Institute do?")


print(resp)
