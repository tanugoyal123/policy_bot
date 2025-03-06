# **Policy Chatbot**
## **Overview**
The Policy Chatbot is an AI-powered assistant designed to answer questions about government policies. It leverages Retrieval-Augmented Generation (RAG) to provide accurate responses based on extracted public data.

## **Features**
1. AI-driven Q&A: Uses RAG to retrieve relevant policy information.
2. Public Data Integration: Extracts and indexes government policies.
3. FastAPI Backend: Efficient API for chatbot interaction.
4. Dockerized Deployment: Easily deploy the chatbot in a containerized environment.

## **Technologies Used**
1. FastAPI - API Framework
2. LangChain - RAG Implementation
3. Vector Database - (FAISS) for policy retrieval
4. Gemini - LLM-based chatbot
5. Docker - Deployment
6. Python 3.10+

## **Installation**

### 1.  Clone the Repository
```bash
git clone https://github.com/your-username/policy-chatbot.git
cd policy-chatbot
```

### 2. Create and Activate Virtual Environment (Optional)
```bash
python -m venv venv
source venv/scripts/activate
```

### 3. install dependencies
```bash
pip install -r requirements.txt
```
### 4. setting the env file
```bash
HF_TOKEN=""
GOOGLE_APPLICATION_CREDENTIALS = ""
```
### 5. Deployment
```bash
uvicorn app.main:app --reload
```


