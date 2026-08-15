# SIADS 699: Capstone Project for the MADS Degree

*Analyzing Complaints from the Consumer Financial Protection Bureau (CFPB)*

- Alex Yoon
- Po-Wen "Barry" Lai
- Zhou "Jo" Jiang
- John Papazian

## Project Structure

This repository contains four analysis components:

- `Geospatial_and_Time_Series_Analysis/` – Geospatial and time series analysis
- `Natural_Language_Processing/` – Natural language processing analysis
- `Supervised_Learning/` – Supervised learning analysis
- `Unsupervised_Learning/` – Unsupervised learning analysis

Each folder contains the code used to generate the corresponding analysis, results, and figures presented in the final report.

## Running the Project

1. Clone the repository:

```bash
git clone https://github.com/Papazian/MADS_Capstone.git
cd MADS_Capstone
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

The requirements file includes Jupyter and all Python libraries needed for the analyses.

3. Start Jupyter Notebook:

```bash
jupyter notebook
```

This will open Jupyter in your web browser.

4. Run the analyses.

Open the corresponding `.ipynb` notebook in Jupyter and select **Run All** to execute the notebook and reproduce the analysis, results, and figures.

The unsupervised topic modeling analysis uses the df_filtered dataset created by the NLP analysis notebook. Therefore, run the NLP notebook first to generate the filtered dataset before running the unsupervised learning notebook.

## Predictive Model Implementation

In addition to the analysis notebooks, we also created a Streamlit web application based on our supervised learning models.

Please click on the Streamlit web app below to predict the likelihood of a respectful closure of your CFPB financial complaint using our classifier models.

[Streamlit web app](https://mads-capstone-consumer-financial-complaint.streamlit.app/)

To run the application locally, use:

```bash
streamlit run predict_using_streamlit.py
```

## Data Used in Our Capstone Project

All data used for our project is publicly available on the CFPB website.

Below is our custom-built function to obtain the CFPB complaints data, which was downloaded from the CFPB website and saved in our AWS S3 bucket on June 16, 2026:

```python
from Supervised_Learning.data_utils import obtain_CFPB_complaints_data
```

Below is the function call to obtain the 2025 data with non-null narratives. This Pandas DataFrame of 1,221,970 complaints was used for Natural Language Processing, Unsupervised Learning, and Supervised Learning:

```python
df = obtain_CFPB_complaints_data(
    start_year=2025,
    end_year=2025,
    exclude_null_narratives=True,
    sampling=False
)
```

Below is the function call to obtain the sampled data over the full time frame. This Pandas DataFrame of 3,974,124 complaints was used for Time Series analysis:

```python
df = obtain_CFPB_complaints_data(
    start_year=2011,
    end_year=2026,
    exclude_null_narratives=False,
    sampling=True,
    sample_fraction=0.25
)
```

## Original Source of CFPB Data

[CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)

[Data Dictionary](https://cfpb.github.io/api/ccdb/fields.html)
