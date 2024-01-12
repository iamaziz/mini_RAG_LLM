# Toy RAG example

A minimal example for (in memory) RAG with Ollama LLM.

Using `Mixtral:8x7` LLM (via Ollama), `LangChain` (to load the model), and `ChromaDB` (to build and search the RAG index).


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


<img width="1377" alt="image" src="https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/6390aa47-bac7-4868-837b-ea99dd466d59">

