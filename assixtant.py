import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss

class PatientMemory:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)
        self.memory_store = []
        self.id_map = {}

    def add_summary(self, patient_id, text):
        embedding = self.model.encode([text])
        self.index.add(embedding)
        self.memory_store.append(text)
        self.id_map[len(self.memory_store) - 1] = patient_id

    def retrieve_summary(self, query, top_k=1):
        embedding = self.model.encode([query])
        D, I = self.index.search(embedding, top_k)
        results = [self.memory_store[i] for i in I[0]]
        return results

class HealthcarePlanner:
    def __init__(self):
        pass

    def plan(self, user_input):
        sub_goals = []
        if "father" in user_input and "kidney disease" in user_input:
            sub_goals.append("Identify patient: 70-year-old male with chronic kidney disease")
            sub_goals.append("Retrieve medical history from EHR DB")
            sub_goals.append("Book nephrologist appointment via Doctor Schedule API")
            sub_goals.append("Search and summarize latest CKD treatments via RAG")
        return sub_goals

def identify_patient(context):
    print(f"[Tool] Identifying patient context: {context}")
    return {"patient_id": "PAT123", "age": 70, "condition": "Chronic Kidney Disease"}

def book_appointment(patient_id, specialty):
    print(f"[Tool] Booking appointment with {specialty} for patient {patient_id}")
    return {"appointment": "Confirmed with Dr. Rivera on Oct 20 at 10:30 AM"}

def search_treatment_info(condition):
    print(f"[Tool] Searching treatment info for {condition}")
    query = f"{condition} latest treatment site:medlineplus.gov OR site:who.int"
    url = f"https://www.bing.com/search?q={query}"
    print(f"[Search] You can explore results here:\n{url}")
    return {"summary": "Visit the link above to view current treatment options from trusted sources."}