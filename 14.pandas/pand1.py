import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('/path/train.csv', sep=',')
# Take a look
print(train.head())

# Subset
part_train = train[train.matches > sum(train.matches)/len(train.matches)]
part_train = part_train[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]

part_train.to_csv("/path/part_train.csv", sep=',')

# filling NAs in A, C, G, T
train.A = train.iloc[:,6].fillna(train.iloc[:,1] - train.iloc[:,7] - train.iloc[:,8] - train.iloc[:,9])
train.C = train.iloc[:,7].fillna(train.iloc[:,1] - train.iloc[:,6] - train.iloc[:,8] - train.iloc[:,9])
train.T = train.iloc[:,8].fillna(train.iloc[:,1] - train.iloc[:,7] - train.iloc[:,6] - train.iloc[:,9])
train.G = train.iloc[:,9].fillna(train.iloc[:,1] - train.iloc[:,7] - train.iloc[:,8] - train.iloc[:,6])

# making a plot
nucl = train.iloc[:,6:10]
nucl.plot.bar()
plt.show()

