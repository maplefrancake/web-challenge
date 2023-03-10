import pandas as pd

#read in the provided csv file
df = pd.read_csv('Resources/cities.csv')

#save to html
df.to_html('data.html', index=False)

table = df.to_html()
print(table)