import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('winequality.csv')

report=ProfileReport(df,title='pandas profilling report')
report.to_file('repor