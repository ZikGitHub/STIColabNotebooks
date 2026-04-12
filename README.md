# Service Ticket Intelligence (STI) - Semantic NLP Pipeline

This repository contains an end-to-end evolutionary pipeline for intelligently processing, clustering, and visualizing service tickets. The project moves from traditional keyword-based analysis to state-of-the-art **Semantic Embeddings** and **High-Performance Vector Indexing**.

## 🚀 Project Evolution (The Notebook Roadmap)

The analysis is structured across four primary stages, representing the progression of semantic complexity:

1. **[ServiceTickets001.ipynb](./ServiceTickets001.ipynb) - The Baseline**
   - Implements traditional **TF-IDF** vectorization.
   - Uses standard **K-Means** clustering.
   - Provides the "keyword count" perspective of the data.

2. **[ServiceTickets002.ipynb](./ServiceTickets002.ipynb) - Semantic Introduction**
   - Replaces TF-IDF with **SBERT (Sentence-BERT)** dense embeddings using the `all-MiniLM-L6-v2` model.
   - Introduces **PCA (Principal Component Analysis)** for dimensionality reduction (from 384 dimensions to 10).

3. **[ServiceTickets003.ipynb](./ServiceTickets003.ipynb) - Cluster Optimization**
   - Integrates the **Elbow Method** to programmatically and visually identify the optimal number of clusters (`k`).
   - Implements **Auto-Logging** to register metrics for every run.

4. **[ServiceTickets004.ipynb](./ServiceTickets004.ipynb) - Advanced EKG & HNSW**
   - Implements **HNSW (Hierarchical Navigable Small World)** for approximate nearest neighbor search.
   - Constructs a dual-layer **Enterprise Knowledge Graph (EKG)**:
     - **Incident -> Cluster** links for hierarchical grouping.
     - **Incident -> Incident** "Similarity Mesh" for direct sematic relationships.
   - Adds an interactive **Fast Search** cell for real-time ticket discovery.

---

## 📊 Evaluation & Monitoring

Model performance is tracked centrally to ensure quality and reproducibility:

- **[notebook_evaluations.csv](./notebook_evaluations.csv)**: A central registry storing Silhouette scores, Davies-Bouldin indices, and cluster counts for every experiment.
- **[Performance_Dashboard.ipynb](./Performance_Dashboard.ipynb)**: A unified dashboard that visualizes model comparisons across all notebook versions.

---

## 🛠️ Technology Stack

- **NLP**: `sentence-transformers` (SBERT)
- **Vector Search**: `hnswlib` (HNSW)
- **Clustering**: `scikit-learn` (KMeans, PCA), `hdbscan`
- **Graphing**: `NetworkX`, `Matplotlib`
- **Data**: `Pandas`, `Numpy`

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- A virtual environment (recommended)

### Installation
1. Activate your virtual environment:
   ```bash
   # Windows
   .\venv\Scripts\activate
   ```
2. Install the core dependencies:
   ```bash
   pip install sentence-transformers hnswlib hdbscan scikit-learn networkx matplotlib pandas numpy nbformat
   ```

### Running the Pipeline
Open any notebook and run all cells. Ensure `all_tickets_processed_improved_v3.csv` is present in the root directory. After running an analysis notebook, check the **Performance Dashboard** to see how your new metrics compare to historical runs.

---

## ⚖️ License
Internal Use Only.
