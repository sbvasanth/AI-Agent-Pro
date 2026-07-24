from src.llm import get_llm

from src.rag.retriever import retriever

llm = get_llm()


def ask_pdf(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
        You are an AI assistant.

        Answer ONLY from the context below.

        Context:

        {context}

        Question:

        {question}
    """

    response = llm.invoke(prompt)

    return response.content
