from sklearn import preprocessing
import pandas as pd
AR = pd.read_csv("artists1.csv")
painting=AR.columns
d = preprocessing.normalize(AR, axis=1)
scaled_df = pd.DataFrame(d, columns=painting)
scaled_df.head()
print(scaled_df)
