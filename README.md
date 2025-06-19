# Policy QA Assistant – RAG-Based Question Answering System

This assistant helps extract relevant answers from company policy documents using Retrieval-Augmented Generation (RAG). Users can type natural-language questions and get responses grounded in actual content.

---

## Use Case

Designed for internal HR/Compliance teams to quickly extract policy-based answers without manually searching through long PDF documents.

Example:
> Q: What is the refund policy for cancellations?  
> A: Approved amounts for reimbursements are processed on the next payroll cycle. Non-reimbursable items are not refunded.

---

## Tech Stack

- Python 3.11  
- OpenAI API (GPT-3.5-turbo + Embeddings)  
- Streamlit for UI  
- scikit-learn for cosine similarity  
- python-dotenv for managing API keys  

---

## Folder Structure

```
.
├── app.py              # Streamlit UI
├── retrieval_engine.py      # Core logic for chunking, embedding and retrieval
├── policies/           # .txt files extracted from original PDFs
├── requirements.txt
├── .env                # Contains your OpenAI API key
└── README.md
```

---

##  How It Works

1. Document Ingestion: 
   `.txt` policy documents are loaded from the `policies/` folder.

2. Chunking:  
   Each document is split into manageable 500-character text chunks.

3. Embedding & Retrieval: 
   All chunks are embedded using `text-embedding-ada-002`, and the top relevant ones are retrieved using cosine similarity to the user's question.

4. Answer Generation:  
   The retrieved chunks and the original question are sent to `gpt-3.5-turbo` for answer generation.

5. Display:
   The answer is shown through an interactive Streamlit interface.

---

## How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key

Create a `.env` file in the root directory and add your key:

```
OPENAI_API_KEY=your-api-key-here
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Live Demo
[Try the App](https://6df63fa3-085c-487d-a4f0-5145a083bbfc-00-tmi8knx8ff2t.pike.replit.dev/)

## GitHub Repository
[view on GitHub](https://github.com/Yiscab/policy-qa-assistant)

---

## Author

Built by **Yisca Biton** – Automation & AI Developer  

---