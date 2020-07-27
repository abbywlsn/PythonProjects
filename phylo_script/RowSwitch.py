import pandas as pd

df = pd.read_csv('../../Empirical/source/Evolve/miniphylotrees/CladeMultiGenPercentiles.csv', header=None, delimiter=',')

dft = df.T

print(dft)

dft.to_csv('../../Empirical/source/Evolve/miniphylotrees/SortedMultiGenPercentiles.csv')