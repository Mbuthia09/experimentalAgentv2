from llm_axe import OllamaChat, OnlineAgent, PdfReader


llm = OllamaChat(model="llama3.1:8b")

pdfReader = PdfReader(llm=llm)

resp = pdfReader.ask("Drivers download", [
                     "Installation_steps.pdf"])


onlineAgent = OnlineAgent(llm)
resp = onlineAgent.search(resp + "\n What is on the website?")


print(resp)
