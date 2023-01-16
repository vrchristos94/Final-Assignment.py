import pandas as pd
import pandas
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('2016-2019.csv')
pandas.set_option('display.max_rows', df.shape[0]+1)

df.drop_duplicates(subset='zip_code', inplace=True, keep='last')

cnz = df.groupby(['zip_code','bottles_sold'])

print(cnz.first())

df.arr1 = np.array('bottles_sold')
print(df.sum())

ab = np.array([288,4,108,48,24,84,72,90,60,48,24,72,102,18,30,108,4,8,2,768,24,60,5,240,5,6,48,12,4,2,4,5,
              2,1,60,48,900,90,216,36,6,48,36,24,4,3,2])/ 3853*100
print(ab)



x = np.array([50010,50022,50111,50131,50158,50263,50265,50266,50314,50316,50317,50320,50327,50401,50461,50501,
              50588,50662,50701,50702,50703,50707,50801,51106,51246,51247,51360,51401,51501,51555,52001,52003,52136,
             52172,52240,52241,52314,52338,52402,52411,52556,52601,52627,52732,52761,52803,52804])

y = np.array([288,4,108,48,24,84,72,90,60,48,24,72,102,18,30,108,4,8,2,768,24,60,5,240,5,6,48,12,4,2,4,5,
              2,1,60,48,900,90,216,36,6,48,36,24,4,3,2])

plt.xlabel('zip_code')
plt.ylabel('bottles_sold')

plt.scatter(x,y)

plt.show()







