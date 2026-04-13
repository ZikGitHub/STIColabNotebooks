# Service Ticket Intelligence (STI) - Semantic NLP & Agentic AIOps Pipeline

This repository contains an end-to-end evolutionary pipeline for intelligently processing, clustering, and visualizing service tickets. It has evolved from keyword-based analysis to an **Agentic Managed Services (AMS)** system powered by local LLMs.

## 🚀 The AIOps Roadmap

The notebooks are organized into two tracks: **Research (ServiceTickets)** and **Agentic MVP (AMS Automation)**.

### 🛠️ Track A: Agentic AIOps (The AMS MVP Series)
This track focuses on autonomous remediation and the "Agentic Brain."

1. **[Agentic_AIOps_AMS_MVP001.ipynb](./Agentic_AIOps_AMS_MVP001.ipynb) - Statistical Baseline**
   - Uses statistical mode analysis to synthesize Knowledge Articles (KAs).
   - Maps IT systems to issue clusters using a heuristic Knowledge Graph.
   - Provides a basic AIOps Orchestrator for incident routing.

2. **[Agentic_AIOps_AMS_MVP002.ipynb](./Agentic_AIOps_AMS_MVP002.ipynb) - LLM-Powered Agent (Llama 3.2)**
   - **Local LLM Integration**: Uses **Ollama** with the `llama3.2:1b` model to generate context-aware Technical Playbooks.
   - **LLM-Enhanced EKG**: An Enterprise Knowledge Graph that color-codes nodes based on whether they require an "Auto-Bot" or an "Expert Human."
   - **Dynamic Orchestration**: Generates real-time execution plans for new incidents using semantic lookup.

---

### 🔬 Track B: Research & Development (ServiceTickets Series)
The foundation of the semantic NLP pipeline.

1. **[ServiceTickets001.ipynb](./ServiceTickets001.ipynb) - Keyword Baseline**
   - Implements **TF-IDF** vectorization and standard **K-Means**.
2. **[ServiceTickets002.ipynb](./ServiceTickets002.ipynb) - Semantic Introduction**
   - Replaces keywords with **SBERT** embeddings and adds **PCA** for visualization.
3. **[ServiceTickets003.ipynb](./ServiceTickets003.ipynb) - Cluster Optimization**
   - Integrates the **Elbow Method** and Auto-Logging to CSV.
4. **[ServiceTickets004.ipynb](./ServiceTickets004.ipynb) - High-Performance Search**
   - Implements **HNSW** indexing for sub-millisecond similarity search.
5. **[ServiceTickets005.ipynb](./ServiceTickets005.ipynb) - Noise Reduction**
   - Uses **HDBSCAN** for high-density clustering to isolate outlier tickets.

---

## 📊 Evaluation & Monitoring

- **[Performance_Dashboard.ipynb](./Performance_Dashboard.ipynb)**: A unified dashboard visualizing model comparisons across all versions.
- **[notebook_evaluations.csv](./notebook_evaluations.csv)**: Central registry for Silhouette and Davies-Bouldin metrics.

---

## ⚙️ Setup & Prerequisites

### 1. Local LLM Setup (For MVP 002)
To run the Agentic LLM features, you must have **Ollama** installed:
1. Download from [ollama.com](https://ollama.com).
2. Open your terminal and run:
   ```bash
   ollama run llama3.2:1b
   ```

### 2. Environment Setup
1. Activate your virtual environment: `.\venv\Scripts\activate`
2. Install dependencies:
   ```bash
   pip install sentence-transformers hdbscan scikit-learn networkx matplotlib pandas numpy ollama
   ```

---

## 🛠️ Technology Stack
- **AI Models**: Llama 3.2 (via Ollama), SBERT (MiniLM-L6)
- **Graphing**: NetworkX (EKG Logic)
- **Vector Search**: HNSWlib
- **Clustering**: HDBSCAN, KMeans

---

## ⚖️ License
Internal Use Only.
