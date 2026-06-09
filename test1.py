#Rag test 1
from langchain import OpenAI
from langchain.chains import RetrievalQA    
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings