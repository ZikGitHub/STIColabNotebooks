import nbformat as nbf
import os
import re

notebook_path = r'e:\AIML\GoogleAntigravity_proj\ColabNotebooks\ServiceTickets004.ipynb'

def add_advanced_visualizations():
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)

    # 1. Prepare t-SNE section
    tsne_md = nbf.v4.new_markdown_cell("### 6. Advanced Semantic Mapping (t-SNE)\nWhile PCA is great for noise reduction, **t-SNE** (t-Distributed Stochastic Neighbor Embedding) is much more effective at visualizing high-dimensional clusters in a 2D plane. It preserves local structures, making similar tickets group together into visible 'islands'.")
    tsne_code = nbf.v4.new_code_cell([
        "from sklearn.manifold import TSNE\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Computing t-SNE (using PCA result as input for stability and speed)\n",
        "print(\"Computing t-SNE manifold (this may take a minute)...\")\n",
        "tsne = TSNE(n_components=2, perplexity=30, random_state=42, init='pca', learning_rate='auto')\n",
        "X_tsne = tsne.fit_transform(X) # X is our 10D PCA output\n",
        "\n",
        "# Plotting the Semantic Map\n",
        "plt.figure(figsize=(12, 8))\n",
        "sns.scatterplot(\n",
        "    x=X_tsne[:, 0], y=X_tsne[:, 1], \n",
        "    hue=df_incidents['cluster_label'], \n",
        "    palette='turbo', \n",
        "    legend='full', \n",
        "    alpha=0.6\n",
        ")\n",
        "plt.title(\"2D Semantic Map of Service Tickets (t-SNE projection)\")\n",
        "plt.xlabel(\"t-SNE dimension 1\")\n",
        "plt.ylabel(\"t-SNE dimension 2\")\n",
        "plt.grid(True, alpha=0.3)\n",
        "plt.show()"
    ])

    # 2. Prepare Heatmap section
    heatmap_md = nbf.v4.new_markdown_cell("### 7. Inter-Cluster Semantic Similarity (Heatmap)\nThis heatmap shows the 'Overlap' between clusters. If two clusters have a similarity close to 1.0, it means their semantic meaning is nearly identical, suggesting they might be merged.")
    heatmap_code = nbf.v4.new_code_cell([
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "import numpy as np\n",
        "\n",
        "# 1. Calculate Centroids for each cluster based on raw SBERT embeddings\n",
        "unique_labels = sorted([l for l in df_incidents['cluster_label'].unique() if l != -1])\n",
        "cluster_centroids = []\n",
        "for label in unique_labels:\n",
        "    mask = df_incidents['cluster_label'] == label\n",
        "    centroid = np.mean(embeddings[mask], axis=0)\n",
        "    cluster_centroids.append(centroid)\n",
        "\n",
        "# 2. Compute Similarity Matrix\n",
        "sim_matrix = cosine_similarity(cluster_centroids)\n",
        "\n",
        "# 3. Plot Heatmap\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.heatmap(sim_matrix, annot=True, fmt=\".2f\", cmap='YlGnBu', \n",
        "            xticklabels=[f'C{l}' for l in unique_labels], \n",
        "            yticklabels=[f'C{l}' for l in unique_labels])\n",
        "plt.title(\"Cluster Relationship Heatmap (Cosine Similarity)\")\n",
        "plt.show()"
    ])

    # Find where to insert (Looking for EKG/Graph construction header)
    insert_idx = -1
    for i, cell in enumerate(nb.cells):
        content = "".join(cell.source)
        if 'Knowledge Graph' in content and 'Construction' in content:
            insert_idx = i
            break
        if 'EKG' in content and 'Construction' in content:
            insert_idx = i
            break

    if insert_idx != -1:
        # Check if already exists
        if "Advanced Semantic Mapping" in "".join([str(c.source) for c in nb.cells]):
            print("Visualizations already exist.")
            return

        nb.cells.insert(insert_idx, tsne_md)
        nb.cells.insert(insert_idx + 1, tsne_code)
        nb.cells.insert(insert_idx + 2, heatmap_md)
        nb.cells.insert(insert_idx + 3, heatmap_code)
        
        # Clean metadata IDs
        for cell in nb.cells:
            if 'id' in cell: del cell['id']
            
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)
        print(f"Modified {notebook_path} successfully at index {insert_idx}.")
    else:
        # Fallback to appending if header not found
        nb.cells.append(tsne_md)
        nb.cells.append(tsne_code)
        nb.cells.append(heatmap_md)
        nb.cells.append(heatmap_code)
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)
        print(f"Could not find exact header, appended to the end instead.")

if __name__ == "__main__":
    add_advanced_visualizations()
