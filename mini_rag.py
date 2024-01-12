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


def get_ollama_llm(name: str = "mixtral", **kwargs):
    return Ollama(model=name, **kwargs)


def ask_llm(prompt: str):
    llm = get_ollama_llm()
    return llm.invoke(prompt)


if __name__ == "__main__":

    # -- example usage

    # local documents for RAG
    docs = [
        "Aziz Alto has lived in NYC for 10 years.",
        "aziz alto is an imaginery LLM engineer in the movive 'The Matrix'.", # intentional typo
        "New York City's subway system is the oldest in the world.",
    ]

    # create RAG
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












# sample user questions (intentional typos)
#   in one sentence, how many days did aziz alot live in new york?
#   which subway is the oldest ever?
#   which movie was aziz featured in?