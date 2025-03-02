from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Koneksi ke MongoDB
client = MongoClient(os.getenv('MONGODB_URI'))
db = client["openhearts_data"]  # Nama database
collection = db["song_comments"]  # Nama collection

# Ambil data dari MongoDB dan simpan ke DataFrame
comments = [doc["comment"] for doc in collection.find()]
df = pd.DataFrame({"comment": comments})

print(f"Berhasil mengambil {len(df)} komentar dari MongoDB!")