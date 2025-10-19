# -----------------------------
# Imports
# -----------------------------
import streamlit as st

# -----------------------------
# Sidebar - View Mode Selection
# -----------------------------
st.sidebar.header("👥 View Mode")
view_mode = st.sidebar.radio("Select your role:", ["Patient View", "Doctor View"])



# -----------------------------
# Mock Planner and Tool Classes
# -----------------------------

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

class PatientMemory:
    def __init__(self):
        self.store = {}

    def add_summary(self, patient_id, summary):
        if patient_id not in self.store:
            self.store[patient_id] = []
        self.store[patient_id].append(summary)

    def retrieve_summary(self, query):
        # For demo, return all summaries for PAT123
        # Note: query parameter is currently unused in this demo implementation
        return self.store.get("PAT123", [])
# -----------------------------
# Tool Functions
# -----------------------------

def identify_patient(query):
    """Mock function to identify patient from query"""
    return {
        "patient_id": "PAT123",
        "age": 70,
        "condition": "chronic kidney disease"
    }

def book_appointment(patient_id, specialty):
    """Mock function to book appointment"""
    return {
        "appointment": f"Appointment booked for {patient_id} with {specialty} on 2024-01-15 at 2:00 PM"
    }

def search_treatment_info(condition):
    """Mock function to search treatment information"""
    return {
        "summary": f"Latest treatment options for {condition} include lifestyle modifications, medication management, and regular monitoring."
    }
    st.write("**Output:**", entry["output"])


# -----------------------------
# Streamlit UI
# -----------------------------

# Initialize planner and memory
planner = HealthcarePlanner()
memory = PatientMemory()

# Sidebar input
st.sidebar.header("🗣️ Ask the Assistant")
user_input = st.sidebar.text_input(
    "Enter a healthcare query:",
    value="My 70-year-old father has chronic kidney disease. I want to book a nephrologist for him. Also, can you summarize latest treatment methods?"
)



# Agent execution
if user_input:
    goals = planner.plan(user_input)

    st.sidebar.header("🧩 Agent Planning Breakdown")
    for i, goal in enumerate(goals, 1):
        st.sidebar.write(f"Step {i}: {goal}")

    # Initialize tool log
    tool_log = []

    patient_info = identify_patient(goals[0])
    tool_log.append({
        "tool": "identify_patient",
        "input": goals[0],
        "output": patient_info
    })

    patient_id = patient_info["patient_id"]

    # Add multiple memory entries
    memory.add_summary(patient_id, "Diagnosed with CKD Stage 3 in 2022. On ACE inhibitors.")
    memory.add_summary(patient_id, "Had elevated creatinine levels in 2021.")
    memory.add_summary(patient_id, "Referred to nephrologist in 2023 for worsening kidney function.")

    retrieved = memory.retrieve_summary("kidney disease treatment history")
    medical_history = retrieved[0] if retrieved else "No history found."

    appointment = book_appointment(patient_id, "nephrologist")
    tool_log.append({
        "tool": "book_appointment",
        "input": {"patient_id": patient_id, "specialty": "nephrologist"},
        "output": appointment
    })

    treatment = search_treatment_info(patient_info["condition"])
    tool_log.append({
        "tool": "search_treatment_info",
        "input": patient_info["condition"],
        "output": treatment
    })



    # Main layout
    # -----------------------------
    # Streamlit UI
    # -----------------------------

    st.title("Agentic Healthcare Assistant")

    st.header("👤 Patient Information")
    st.write(f"Patient ID: {patient_info['patient_id']}")
    st.write(f"Age: {patient_info['age']}")
    st.write(f"Condition: {patient_info['condition']}")

    st.header("📅 Appointment Status")
    st.success(appointment['appointment'])

    # st.header("🧠 Medical History")
    # st.info(medical_history)

    st.header("💊 Treatment Summary")
    st.warning(treatment['summary'])

if view_mode == "Doctor View":
    st.header("🧠 Medical History")
    st.info(medical_history)


    # search_link = f"https://www.bing.com/search?q={patient_info['condition']}+latest+treatment+site:medlineplus.gov+OR+site:who.int"
    # st.markdown(f"[🔍 View Latest Treatments]({search_link})", unsafe_allow_html=True)

    # Tool Execution Log
    st.header("🛠️ Tool Execution Log")
    for entry in tool_log:
        st.subheader(f"🔧 {entry['tool']}")
        st.write("**Input:**", entry["input"])
        st.write("**Output:**", entry["output"])


    st.header("🧠 Memory Trace Viewer")
    for i, summary in enumerate(retrieved, 1):
        st.write(f"{i}. {summary}")
