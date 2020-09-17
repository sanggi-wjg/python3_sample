import pandas as pd
import numpy as np

dates = pd.date_range('20200901', periods = 10)
print(dates)

df = pd.DataFrame(np.random.rand(10, 4), index = dates, columns = list('ABCD'))
print(df)
