## initial imports
import pandas as pd
from pathlib import Path


# set the file path
csvpath=Path('OneDrive/Desktop/FinTech/FinTech Classwork/Unit3/amd_stock_data.csv')

# create a Pandas dataframe from a csv file
sales_df=pd.read_csv(csvpath)
