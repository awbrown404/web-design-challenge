import pandas as pd

df = pd.read_csv("data/cities.csv")

df = pd.DataFrame(df)

df.to_html(class="table-striped", coloumns=10, header=True, index=false)