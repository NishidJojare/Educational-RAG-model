from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_all_docs():
    try:
        pdf_folder = "docs"
        loader = DirectoryLoader(pdf_folder, glob="*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        return docs
    
    except Exception as e: 
        print(f"Something went wrong while loading available docs : {e}")


def split_doc_into_chunks(docs,chunk_size,chunk_overlap):
    try:
        # splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(docs)
        print(f"Total created chunks are : {len(chunks)}")
        return chunks
    
    except Exception as e: 
        print(f"Something went wrong while splitting and returning the chunks : {e}")


def create_embeddings_store_into_db():
    try:
        # creating an object of embedding model
        embedder = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

        # getting loaded docs
        docs = load_all_docs()

        # getting text chunks out of docs
        chunks = split_doc_into_chunks(docs,800,200)

        # Creating a searchable local db object
        vector_db = FAISS.from_documents(chunks, embedder)

        # storing all embeddings into local storage
        vector_db.save_local('local_vectors')

    except Exception as e: 
        print(f"Something went wrong while creating embeddings and storing it into vector store : {e}")





# # run this only first time, once you have a local vector store of all the available docs, dont need to call this again. 
# create_embeddings_store_into_db()