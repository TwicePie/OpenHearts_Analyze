from pymongo import MongoClient
import pandas as pd

# Koneksi ke MongoDB
client = MongoClient("mongodb+srv://Ocharu:pablo123@cluster.hg4wl.mongodb.net/") # Untuk lokal, gunakan localhost
db = client["openhearts_data"]  # Nama database
collection = db["song_comments"]  # Nama collection

# Ambil data dari MongoDB dan simpan ke DataFrame
comments = [doc["comment"] for doc in collection.find()]
df = pd.DataFrame({"comment": comments})

print(f"Berhasil mengambil {len(df)} komentar dari MongoDB!")