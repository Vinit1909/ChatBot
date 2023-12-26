from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter, TextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.chains import RetrievalQA
# from langchain.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
import os

OPENAI_KEY = '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'
os.environ['OPENAI_API_KEY'] = OPENAI_KEY

# Load text files from a directory
loader = DirectoryLoader('chainlit-backend/Artists/', glob='**/*.*')
docs = loader.load() # returns a list
print("Number of docs =", len(docs))

# Shard all the documents
text_splitter = CharacterTextSplitter(chunk_size=5000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)
print("Number of shards =", len(texts))

# Prepare Vector Store
from langchain import vectorstores
from langchain.vectorstores.base import VectorStore
# Convert the document-shards into embeddings
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(texts, embeddings)
qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectordb)

query = "What is the first line of song in Excile written by Taylor Swift?"
qa.run(query)