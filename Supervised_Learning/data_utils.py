import pandas as pd

def obtain_CFPB_complaints_data(start_year: int, end_year: int, exclude_null_narratives: bool, sampling: bool, sample_fraction: float = 0.25):
    """
    Obtain a subset of the CFPB complaints data that was downloaded and saved in our AWS S3 bucket on June 16, 2026
    https://aletheia-public.s3.us-east-2.amazonaws.com/complaints_16Jun2026.csv

    This CSV data was originally downloaded from the CFPB website on June 16, 2026
    https://www.consumerfinance.gov/data-research/consumer-complaints/#get-the-data

    This function will also convert the date columns from a string object format to a datetime format with just a date (i.e. YYYY-MM-DD)

    Parameters:
        start_year (int): start year of the complaints desired (2011 to 2026) where start_year <= end_year
        end_year (int): end year of the complaints desired (2011 to 2026) where end_year >= start_year
        exclude_null_narratives (bool): flag to exclude complaints with null consumer complaint narratives
        sampling (bool): flag to activate sampling of the complaints
        sample_fraction (float): percentage of complaints to sample

    Returns:
        pandas data frame: subset of the CFPB complaints
    """
    # Retrieve the full data of CFPB complaints from our AWS S3 bucket that was downloaded on June 16, 2026
    url = "https://aletheia-public.s3.us-east-2.amazonaws.com/complaints_16Jun2026.csv" 
    df = pd.read_csv(url)

    # Convert the date columns from a string object format to a datetime format with just a date (i.e. YYYY-MM-DD)
    df['Date received'] = pd.to_datetime(df['Date received'].str[:10]).dt.normalize()
    df['Date sent to company'] = pd.to_datetime(df['Date sent to company'].str[:10]).dt.normalize()

    # Filter the complaints by start year and end year
    if ((start_year < 2011) or (end_year > 2026) or (start_year > end_year)):
        raise ValueError("Invalid years!")
    df = df[(df['Date received'].dt.year >= start_year) & (df['Date received'].dt.year <= end_year)]

    # If desired, then filter complaints with non-null values in the complaint narrative
    if exclude_null_narratives:
        df = df[df['Consumer complaint narrative'].notna()]

    # If desired, then sample complaints at the specified sample fraction percentage
    if sampling:
        df = df.sample(frac=sample_fraction, random_state=42)

    return df