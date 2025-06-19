import os
from openai import OpenAI
import numpy as np
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_documents(folder_path="policies"):
    texts = []
    for file in Path(folder_path).glob("*.txt"):
        with open(file, encoding="utf-8") as f:
            texts.append(f.read())
    return texts


def split_into_chunks(text, chunk_size=500):
    paragraphs = text.split("\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current += para + " "
        else:
            chunks.append(current.strip())
            current = para + " "
    if current:
        chunks.append(current.strip())
    return chunks


def generate_embeddings(texts):
    clean_texts = [
        str(t).strip() for t in texts
        if isinstance(t, str) and 1 <= len(t.strip()) <= 8192
    ]
    if not clean_texts:
        raise ValueError("No valid input texts for embedding.")
    response = client.embeddings.create(input=clean_texts,
                                        model="text-embedding-ada-002")
    return [r.embedding for r in response.data]


def retrieve_relevant_chunks(question, chunks, chunk_embeddings, top_k=3):
    question_embedding = generate_embeddings([question])[0]
    similarities = cosine_similarity([question_embedding], chunk_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]


def ask_gpt(question, context):
    prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {question}"
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[{
                                                  "role": "user",
                                                  "content": prompt
                                              }])
    return response.choices[0].message.content.strip()
