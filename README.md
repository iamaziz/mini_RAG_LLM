# Toy RAG example

A minimal example for (in memory) RAG with Ollama LLM.

Using `Mixtral:8x7` LLM (via Ollama), `LangChain` (to load the model), and `ChromaDB` (to build and search the RAG index). More details in [What is RAG anyway?](https://altowayan.notion.site/altowayan/What-is-RAG-anyway-6a945b7b4e784eda8a707249a078937e)


To run this example, the following is required:

- Install [Ollama.ai](https://ollama.ai)
- download a local LLM: `ollama run mixtral` (requires at least ~50GB of RAM, smaller LLMs may work but I didn't test)
- `pip install -r requirements.txt` (venv recommended)

Then run:

```bash
python mini_rag.py
```

#### Example

https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/ee7d12a4-1acd-4a0d-8d46-a90a20a98b5a


#### Simplified sequence

<img width="1469" alt="Untitled" src="https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/6ed53abd-89a2-443a-b3bf-437c17af2ba7">

> <sub>[source](https://chat.openai.com/share/35ddfd24-f719-436f-9109-f735940957c7)</sub>

<!--
sequenceDiagram
    participant User as "User Input"
    participant RAG as "Query RAG System"
    participant LLM_Prompt as "Build LLM's Prompt"
    participant LLM as "Ask the LLM"
    participant Response as "Return LLM Response"
    User->>RAG: Provide input
    RAG->>LLM_Prompt: Provide relevant context
    LLM_Prompt->>LLM: Provide prompt using RAG result
    LLM->>Response: Generate response based on prompt
    Response->>User: Display LLM response
-->
