import pandas as pd
import numpy as np


exam_results = {'name' :['David', 'Samantha', 'Emil', 'David', 'Emily'],
'score':  [56, 25, 59, np.nan, 82],
'attempts':  [1, 2, 1, 1, 5],
 'qualify':  ['yes' ,'no', 'yes', 'no', 'yes', ]}
labels = ['a', 'b', 'c', 'd', 'e' ]
df = pd.DataFrame(exam_results , index=labels)
print("Summary of the baisic information about  this dataframeand its data  : ")
print(df.info)