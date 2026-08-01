# SIADS 699: Capstone Project for the MADS degree

*Analysing Complaints from the Consumer Financial Protection Bureau*

- Alex Yoon 
- Po-Wen "Barry" Lai 
- Zhou "Jo" Jiang
- John Papazian

---

**Predictive Model Implementation:**

Please click on Streamlit web app below to predict the likelihood of a respectful closure of a financial complaint using our Classifier models.

[Streamlit web app](https://mads-capstone-consumer-financial-complaint.streamlit.app/)

---

**Data used in our Capstone Project:**

Below is our function to obtain the CFPB complaints data, which was downloaded from the CFPB website and saved in our AWS S3 bucket on June 16, 2026:

`from Supervised_Learning.data_utils import obtain_CFPB_complaints_data`

Below is the function call to obtain just the 2025 data with non-null narratives. This data frame of 1,221,970 complaints was used for Natural Language Processing, Unsupervised Learning, and Supervised Learning:

`df = obtain_CFPB_complaints_data(start_year=2025, end_year=2025, exclude_null_narratives=True, sampling=False)`

Below is the function call obtain the sampled data over the full time frame. This data frame of 3,974,124 complaints was used for Time Series analysis:

`df = obtain_CFPB_complaints_data(start_year=2011, end_year=2026, exclude_null_narratives=False, sampling=True, sample_fraction=0.25)`

---

**Original CFPB Data Source:**

[CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)

[Data Dictionary](https://cfpb.github.io/api/ccdb/fields.html)