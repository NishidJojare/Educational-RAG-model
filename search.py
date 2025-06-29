from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_groq import ChatGroq
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


def get_search_object():
    try:
        embedder = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
        vectors = FAISS.load_local('local_vectors', embeddings=embedder, allow_dangerous_deserialization=True)

        # Set up the search tool
        searcher = vectors.as_retriever(search_type="similarity", search_kwargs={"k": 3})

        return searcher
    
    except Exception as e: 
        print(f"something went wrong : {e}")




def get_retrieval_chain():
    try:
        
        # Start the AI model
        answer_maker = ChatGroq(api_key=os.environ["GROQ_API_KEY"], model_name="llama3-70b-8192")

        # Write instructions for the AI
        instructions = ChatPromptTemplate.from_template("""You are a helpful assistant.
        Use only the context below to answer the question.

        Always format your answer using raw **Markdown** syntax:
        - Use `**bold**` for important terms.
        - Use `-` or `*` for bullet points.
        - Do not return HTML. Only return raw markdown.

        If the answer is not in the context, say:
        "Hey there! I couldn't find that information right now, but I’m evolving day by day — stay tuned!"

        <context>
        {context}
        </context>

        Question: {input}

        Answer:"""
        )


        # Link the chunks to the AI
        doc_chain = create_stuff_documents_chain(answer_maker, instructions)

        searcher = get_search_object()

        # Build the chain
        chain = create_retrieval_chain(searcher, doc_chain)

        return chain

    except Exception as e: 
        print(f"Something went wrong while getting retrieval chain : {e}")





def ask_question(query,chain):
    try:
        # chain = get_retrieval_chain()
        result = chain.invoke({"input": query})
        return result['answer']

    except Exception as e: 
        print(f"Oops, something went wrong : {e}")

