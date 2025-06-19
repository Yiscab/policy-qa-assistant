DECISIONS.md – Build Summary and Trade-offs

**Time Spent**

The project was completed in approximately 3 hours, including implementation, testing, and deployment.

**What Was Built**

A lightweight RAG-based question answering system was developed using Python, Streamlit, and OpenAI’s API. It allows users to query internal policy documents via a simple web interface.

Key features:

User-friendly Streamlit UI

Embedding of document chunks using text-embedding-ada-002

Cosine similarity search with scikit-learn

OpenAI’s gpt-3.5-turbo used for contextual answer generation

Deployed live via Replit

**Key Design Decisions**

1. No Database

All embeddings and document chunks are kept in memory for simplicity, as per the exercise guidelines.

2. PDF to Text Conversion

PDFs were converted manually to .txt format using a script outside of the app (to save dev time within the 3-hour limit). This ensured better control over chunking and encoding.

3. Chunk Size

Chunks were split at 500 characters each. This balances semantic relevance with performance and avoids token overflows in the prompt.

4. Minimal UI

Streamlit was chosen for rapid development and clean layout, allowing a single question input and real-time response display.

5. Security

API keys were handled via .env file and excluded from version control. Replit secrets were also used.

**Trade-offs**

No vector DB: While a vector store like FAISS or Pinecone could scale better, in-memory storage was sufficient here.

Basic text processing: No advanced cleaning/tokenization was added, to stay within the time frame.

Limited source highlighting: The system returns contextual snippets but not full document citations or streaming.

**Next Steps (Day 2 Production Plan)**

If taken further, here’s what I would improve:

Integrate a vector database for efficient and scalable storage

Add multi-question history or chat window

Improve chunking with sentence-boundary logic

Support more file formats (e.g. DOCX)

Add basic authentication layer for secured access

Add Dockerfile for easier containerized deployment
