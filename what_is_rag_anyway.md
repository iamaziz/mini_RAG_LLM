# What is RAG anyway?

**What is RAG anyway?**

> *RAG == ’Asking Informed Questions’*
> 

In essence, it involves asking Large Language Models (LLMs) "informed questions". This means we include more context, or contextual knowledge, in the questions we ask the LLMs. For example, if the user question is “*How many **days** did it take team X to complete the project Y?*”; the contextual knowledge might be something like: “*X project was delivered in **four months**.*”. When this context is augmented into the question as a prior knowledge to the LLM, the LLM will - often - be able to conclude that “*Team X has spent **120 days** working on project Y.*” Contextual knowledge typically comes from local or private data that the LLM has likely not encountered during its pre-training phase. This is known as Retrieval Augmented Generation or RAG.

There are several methods to implement RAG, from highly sophisticated to more straightforward approaches. It is still experimental space. However, at its core, it is about extracting contextual knowledge, a process akin to a database search. In this scenario, the database is vector-based, and the search is based on similarity, often using the cosine similarity metric.

# Minimal RAG Example

So, in a simplified concept, the sequence of RAG processes might look something like this:

<img width="1469" alt="Untitled" src="https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/6ed53abd-89a2-443a-b3bf-437c17af2ba7">

> [source](https://chat.openai.com/share/35ddfd24-f719-436f-9109-f735940957c7)
> 

The following basic code example demonstrates the simple concept and sequence of processes.

ℹ️ **Jan 12, 2024** | [a minimal example for a toy RAG with `Mixtral` LLM](https://github.com/iamaziz/mini_RAG_LLM)

<img width="1185" alt="Untitled 1" src="https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/227b468d-2cd1-4795-b95f-b82e01d1d05b">

Creating the RAG system


```python
from typing import List

from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

def build_rag(docs: List[str]):
    docs = [Document(page_content=doc) for doc in docs]
    return Chroma.from_documents(documents=docs, embedding=OllamaEmbeddings())

def search_rag(rag, query: str, k=1, **kwargs):
    result = rag.similarity_search_with_score(query, k=k, **kwargs)
    return result[0][0].page_content # NOTE: use a threshold to filter results on the score (i.e. result[0][1] cosine distance)

def create_prompt(context: str, question: str):
    return f"Given the following context: \n\t{context} \n\nAnswer this question: \n\t{question}"

def get_llm(name: str = "mixtral", **kwargs):
    return Ollama(model=name, **kwargs)

def ask_llm(prompt: str):
    llm = get_llm()
    return llm.invoke(prompt)
```

Given the following hypothetical local data “documents”

```python
# -- example usage

# local documents for RAG
docs = [
    "Aziz Alto has lived in NYC for 10 years.",
    "aziz alto is an imaginery LLM engineer in the movive 'The Matrix'.", # intentional typo
    "New York City's subway system is the oldest in the world.",
]
```

Using RAG with sample local data

```python
# Create a RAG instance using the provided local data
rag = build_rag(docs)

# user prompt as question to LLM
while True:
    question = input("\n\nEnter a question:\n> ")
    print(f"\n\nUSER QUESTION>>>\n\t{question}")

    # search RAG for context based on question
    context = search_rag(rag, question, k=1)
    print(f"FOUND RAG CONTEXT>>>\n\t{context}")

    # build prompt for LLM with the found context and the question
    prompt = create_prompt(context, question)
    print(f"LLM PROMPT>>> \n\n```\n{prompt}\n```\n\n")

    # ask LLM with the RAG result as context
    answer = ask_llm(prompt)
    print(f"LLM RESPONSE:\n\n{answer}")
```

<aside>
⚛️ Keep in mind, the RAG system is only as good as the documents it has access to. This means the quality of the answers it provides is directly related to the comprehensiveness and accuracy of the information in the documents.

</aside>

Example **user questions** to the LLM (with intentional typos)

```markdown
# sample user questions
1. in one sentence, how many days did aziz alot live in new york?
2. which subway is the oldest ever?
3. which movie was aziz featured in?
```

After executing the code, the complete sequence of processes is displayed, starting with the user's question, the identified RAG context, the prepared LLM prompt, and finally, the returned LLM response.

***Question 1***

```markdown
# Enter a question:
> in one sentence, how many days did aziz alot live in new york?

# USER QUESTION>>>
	in one sentence, how many days did aziz alot live in new york?
# FOUND RAG CONTEXT>>>
	Aziz Alto has lived in NYC for 10 years.
# LLM PROMPT>>>


Given the following context:
	Aziz Alto has lived in NYC for 10 years.

Answer this question:
	in one sentence, how many days did aziz alot live in new york?


# LLM RESPONSE:

 Aziz Alto has lived in NYC for approximately 3,650 days (10 years x 365 days/year).
```

***Question 2***

```markdown
# Enter a question:
> which subway is the oldest ever?

# USER QUESTION>>>
	which subway is the oldest ever?
# FOUND RAG CONTEXT>>>
	New York City's subway system is the oldest in the world.
# LLM PROMPT>>>


Given the following context:
	New York City's subway system is the oldest in the world.

Answer this question:
	which subway is the oldest ever?


# LLM RESPONSE:

Based on the information provided, New York City's subway system is the oldest in the world. 
It was one of the first cities to build a subway system, which opened in 1904. 
Therefore, New York City's subway would be the answer to your question.
```

***Question 3***

```markdown
# Enter a question:
> which movie was aziz featured in?

# USER QUESTION>>>
	which movie was aziz featured in?
# FOUND RAG CONTEXT>>>
	aziz alto is an imaginery LLM engineer in the movive 'The Matrix'.
# LLM PROMPT>>>


Given the following context:
	aziz alto is an imaginery LLM engineer in the movive 'The Matrix'.

Answer this question:
	which movie was aziz featured in?


# LLM RESPONSE:

Aziz Alto, who is an imaginary LLM engineer, was featured in the movie "The Matrix." 
In the movie, LLM stands for "Logic and Reasoning Machine," and these characters play a crucial role in the plot of the film. 
However, I couldn't find any specific character named Aziz Alto in the original Matrix trilogy or in any of its spin-offs. 
It is possible that this character was invented for the purpose of your question. 
Nonetheless, based on the information provided, Aziz Alto was featured in the movie "The Matrix."
```

---


# Real-world RAG example: Disease Detector

> WIP
![search_flow_diagram](https://github.com/iamaziz/mini_RAG_LLM/assets/3298308/1958c664-0ec0-4c94-807d-1695746e2dbd)