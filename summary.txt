# Capstone Project Summary

**Title:** Agentic Healthcare Assistant for Medical Task Automation  
**Student:** J  
**Specialization:** Applied Generative AI  
**Submission Date:** October 2025

## Problem Statement

Modern healthcare systems often rely on fragmented tools for scheduling, recordkeeping, and disease information retrieval. These silos create inefficiencies and limit patient-centered automation. This project addresses that gap by building an Agentic Healthcare Assistant that autonomously coordinates medical tasks using planning, memory, and retrieval-augmented generation (RAG).

## Project Objectives

The assistant was designed to:

- Interpret multi-step patient queries using agentic planning
- Automate appointment booking based on patient intent
- Retrieve and summarize medical history using memory modules
- Search and summarize disease treatment information from trusted sources

## System Architecture

**Planner:**

- Decomposes complex queries into sequential sub-goals
- Maps each sub-goal to a tool or API

**Tools:**

- `identify_patient`: Extracts patient context
- `book_appointment`: Simulates scheduling via Doctor Schedule API
- `search_treatment_info`: Retrieves treatment summaries using Bing/Medline/WHO

**Memory Module:**

- FAISS-based vector store using SentenceTransformer embeddings
- Stores and retrieves patient summaries for long-term context

**Execution Flow:**

- Agent plans and executes sub-goals in order
- Each tool logs its input/output for traceability
- Memory is updated and queried dynamically

## Streamlit Dashboard Features

- Sidebar query input
- Agent Planning Breakdown
- Patient and Doctor View toggle
- Appointment status and treatment summary
- Tool execution log
- Memory trace viewer
- External search link to MedlinePlus and WHO

## Completed Capstone Requirements

| Requirement                           | Status |
| ------------------------------------- | ------ |
| Agent planning and goal decomposition | ✅     |
| Tool and memory setup                 | ✅     |
| Prompt chaining and execution         | ✅     |
| Sample scenario implementation        | ✅     |
| Streamlit UI with role-based views    | ✅     |
| Tool logs and memory trace display    | ✅     |
| External search integration           | ✅     |
