# def book_load_split ():
from langchain_community.document_loaders import PyPDFLoader
# loading the doc 
loader = PyPDFLoader(r"C:\Users\lenovo\Downloads\pre.pdf")
pages = loader.load_and_split()


from langchain.text_splitter import RecursiveCharacterTextSplitter
#splitting the doc based on chunk
text_splitter  = RecursiveCharacterTextSplitter(
    chunk_size = 1000,chunk_overlap = 200,add_start_index =True
)
all_splits = text_splitter.split_documents(pages)


from langchain_community.embeddings import HuggingFaceEmbeddings
#loading the embedding
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


from langchain_community.vectorstores import Chroma
#storing the embedding in the vector store
db = Chroma.from_documents(all_splits, embeddings, persist_directory="./book_db")
