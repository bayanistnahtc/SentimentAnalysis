import pandas as pd
f = pd.read_csv('training.1600000.processed.noemoticon.csv',encoding='ISO-8859-1')
print(set(f['0']))