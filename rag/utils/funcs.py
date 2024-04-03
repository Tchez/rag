from rag.lib.database import Database

db = Database(documents_path='teste.txt', tables_path='faiss_index')
db.load_or_create_index()
print(db.query('teste'))