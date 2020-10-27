import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20200917'),
    'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
    'D': np.array([3] * 4, dtype = 'int32'),
    'E': pd.Categorical(['a', 'b', 'a', 'b']),
    'F': 'foo val'
})
print(df)

# for row in df.iterrows():
#     print(row)

print(df.describe())
