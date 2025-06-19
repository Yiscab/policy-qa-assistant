import streamlit as st
from retrieval_engine import load_documents, split_into_chunks, generate_embeddings, retrieve_relevant_chunks, ask_gpt

st.title("📄 Policy QA Assistant (RAG-based)")
question = st.text_input("Ask a question based on the policies")

if question:
    with st.spinner("Processing..."):
        docs = load_documents()
        chunks = []
        for doc in docs:
            chunks.extend(split_into_chunks(doc))
        chunk_embeddings = generate_embeddings(chunks)
        top_chunks = retrieve_relevant_chunks(question, chunks,
                                              chunk_embeddings)
        context = "\n".join(top_chunks)
        answer = ask_gpt(question, context)
        st.subheader("Answer:")
        st.write(answer)
