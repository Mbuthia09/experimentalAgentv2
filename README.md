# experimentalAgentv2

OllamaV2

# Local LLM Project: Exploring Ollama and AI Agents

This repository demonstrates how to use **locally hosted language models** (via [Ollama](https://ollama.com)) to perform intelligent tasks like reading PDFs, searching the web, and generating responses without relying on cloud APIs.

I use the `llm_axe` library to attempt to build an agent that combines reasoning, document analysis, and internet research using the model `llama3.1:8b`, that I pulled from Ollama.

---

## Scripts Overview

### 1. `internetmodel.py` – Combining PDF Insights with Web Search

**Purpose**:  
Extract information from a local PDF, then use that insight to perform a contextual internet search.

**How It Works**:

- Uses `PdfReader` to analyze `Installation_steps.pdf` and answer a question about "Drivers download".
- Takes the LLM-generated response and appends a follow-up query: _"What is on the website?"_
- The `OnlineAgent` performs a web search based on the inferred URL or context.
- Returns a summary of what’s found online.

**Key Tools Used**:

- `PdfReader`: Reads and interprets PDF content using the LLM.
- `OnlineAgent`: Searches the web and summarizes results intelligently.

**Lesson Learned**:

> You can chain **document understanding** with **real-time internet research** to create powerful, context-aware assistants, to mimic how humans read a manual and then look up related resources online.

---

### 2. `internetSearch.py` – Direct Internet Research Agent

**Purpose**:  
Answer factual questions by directly searching the web using an AI agent.

**How It Works**:

- Asks: _"What does the International Livestock Research Institute do?"_
- The `OnlineAgent` conducts a search, retrieves relevant pages, and uses the LLM to summarize the findings.

**Lesson Learned**:

> Local LLMs can be improved with **up-to-date internet access** to overcome their training data limitations. This turns a static model into a dynamic knowledge explorer.

---

### 3. `model.py` – Combining Document & Web Queries (With a Bug!)

**Purpose**:  
Demonstrate combining PDF analysis and internet search in one workflow.

**What Goes Wrong**:

- Correctly reads the PDF for info on "Using winPE".
- Attempts to search for the latest Unreal Engine 5 update — but fails due to a **naming bug**:
  ```python
  resp = online_agent.search(prompt)  # I had not defined 'online_agent'
  ```
- I noticed the bug and fixed it by changing it to 'onlineAgent':
  ```python
  resp = onlineAgent.search(prompt)  # I had not defined 'online_agent'
  ```

**Lesson Learned**:

- typos can break the workflow. Always counter check variable names.

### 4. `package.py` - Barebones Ollama Interaction

**Purpose**:
The most basic way to interact with Ollama using the official python client.

**How it works**:

- Uses ollama.Client() to connect to the local Ollama server.
- Sends a simple prompt: "What is python?"
- Prints raw response directly from the model

**Lesson Learned**:
It is possible to run inference locally with a few lines of code.

## Requirements:

To run these scripts,

- install and run (via [Ollama](https://ollama.com))
- A local model, like llama3.1:8b
  ```bash
      ollama pull llama3.1:8b
  ```
- Python packages
  ```bash
    pip install ollama llm-axe
  ```

## Key Takeaways

- Start simple: Begin with direct Ollama calls before adding layers.
- Augment Local Models: Local LLMs lack real time data, so use agents to give them internet access.
- Chain Actions: Combine document parsing with web search for deeper insights.
- Document Parsing: Use LLMs to extract meaning from PDFs, not just text.
- Debugging: A typo can and will mess up the flow and crash your agent.

## Next Steps

- Add dynamic user input
- Build a user interface... I'm thinking streamlit
- Experiment wih other models.
- Write more README files
