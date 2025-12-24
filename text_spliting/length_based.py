from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, # charcters overlap that is similar info between the chunks
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)