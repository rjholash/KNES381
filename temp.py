# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# sample
df = pd.DataFrame({'Time': ['00.08', '10.04', '30.05']})
print(df)
print(type(df.Time[0]))
df['Time'] = pd.to_datetime(df['Time'], format='%S.%f').dt.time
#df['Time'] = pd.to_datetime(df['Time'], format='%S.$f').dt.time
print(type(df.Time[0]))
print(df)

