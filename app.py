from flask import Flask, request, render_template
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Simple TF-IDF based embeddings
class TfidfEmbeddings(Embeddings):
    def __init__(self):
        self.vectorizer = None
    
    def embed_documents(self, texts):
        self.vectorizer = TfidfVectorizer(max_features=300, lowercase=True, stop_words='english').fit(texts)
        vectors = self.vectorizer.transform(texts).toarray()
        return vectors.tolist()
    
    def embed_query(self, text):
        if self.vectorizer is None:
            return [0.0] * 300
        vector = self.vectorizer.transform([text]).toarray()[0]
        return vector.tolist()

# Load environment variables from .env file
load_dotenv()

# Get Groq API key from environment variable
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("Error: GROQ_API_KEY not found in environment variables!")
    print("Please set your Groq API key in the .env file")
    exit(1)

# Initialize Flask app
app = Flask(__name__)

# Load and prepare the data
pdfreader = PdfReader('annavaram.pdf')

# Read text from PDF
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# Split the text into smaller chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Create embeddings using TF-IDF
embeddings = TfidfEmbeddings()

# Create FAISS vector store
document_search = FAISS.from_texts(texts, embeddings)

# Initialize Groq LLM
llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile")

def generate_answer(input_query):
    """Process the input query and return an answer."""
    # Search for relevant documents
    docs = document_search.similarity_search(input_query, k=3)
    
    # Format the context from retrieved documents
    if docs:
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Create a prompt
        prompt = f"""Based on the following context from the Annavaram Temple knowledge base, answer the question concisely.

Context:
{context}

Question: {input_query}

Answer:"""
        
        # Generate answer using Groq
        response = llm.invoke(prompt)
        return response.content
    else:
        return "Sorry, I couldn't find relevant information about that topic in the Annavaram Temple knowledge base."

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = generate_answer(msg)
    return str(response)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8085, debug=False)
