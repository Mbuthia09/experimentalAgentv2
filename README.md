# experimentalAgentv2

OllamaV2

# Local LLM Project: Exploring Ollama and AI Agents

This repository demonstrates how to use **locally hosted language models** (via [Ollama](https://ollama.com)) to perform intelligent tasks like reading PDFs, searching the web, and generating responses — all without relying on cloud APIs.

We use the `llm_axe` library to build AI agents that combine reasoning, document analysis, and internet research using models like `llama3.1:8b`.

---

## Scripts Overview

### 1. `internetmodel.py` – Chaining PDF Insights with Web Search

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

> You can chain **document understanding** with **real-time internet research** to create powerful, context-aware assistants. This mimics how humans read a manual and then look up related resources online.

---

### 2. `internetSearch.py` – Direct Internet Research Agent

**Purpose**:  
Answer factual questions by directly searching the web using an AI agent.

**How It Works**:

- Asks: _"What does the International Livestock Research Institute do?"_
- The `OnlineAgent` conducts a search, retrieves relevant pages, and uses the LLM to summarize the findings.

**Lesson Learned**:

> Local LLMs can be augmented with **up-to-date internet access** to overcome their training data limitations. This turns a static model into a dynamic knowledge explorer.

---

### 3. `model.py` – Combining Document & Web Queries (With a Bug!)

**Purpose**:  
Demonstrate combining PDF analysis and internet search in one workflow.

**What Goes Wrong**:

- Correctly reads the PDF for info on "Using winPE".
- Attempts to search for the latest Unreal Engine 5 update — but fails due to a **naming bug**:
  ```python
  resp = online_agent.search(prompt)  # 'online_agent' not defined
  ```
