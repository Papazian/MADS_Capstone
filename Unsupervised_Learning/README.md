# CFPB Credit Reporting Complaint Clustering

This folder contains the unsupervised-learning playbook for the CFPB capstone project.

The analysis uses sentence embeddings, UMAP, and HDBSCAN to identify common themes in 2025 credit-reporting complaint narratives.

## Main Files

- `credit_clustering_final_notebook.ipynb`  
  Final clustering analysis, model selection, topic interpretation, and export process.

- `clean_rebuild_outputs/credit_complaint_cluster_assignments.csv`  
  Final complaint-level cluster assignments for use by the other capstone playbooks.

- `requirements.txt`  
  Python packages used for the analysis.

## Final Results

The final model identified 13 complaint clusters.

HDBSCAN also classified some complaints as outliers. These complaints have:

- `cluster_id = -1`
- `cluster_name = Outlier`
- `is_outlier = True`

The final export contains 2,902 complaints, including 1,064 outliers.

## Cluster Assignment File

The final complaint-level results are available here:

`clean_rebuild_outputs/credit_complaint_cluster_assignments.csv`

The file contains one row per complaint with these columns:

- `Complaint ID`
- `cluster_id`
- `cluster_name`
- `cluster_membership_strength`
- `is_outlier`

`cluster_membership_strength` is the HDBSCAN membership strength for the assigned cluster. It is not a conventional prediction probability.

The CSV can be merged with the supervised-learning and NLP results using `Complaint ID`. This allows the team to compare outcomes, sentiment, severity, and other measures across the complaint clusters.

The CSV is already generated, so teammates do not need to rerun the clustering notebook just to use the results. The notebook only needs to be rerun if the clustering analysis is being reproduced or updated.

