import matplotlib.pyplot as plt
import pandas as pd
import csv, io
from pprint import pprint

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# data = pd.read_csv('../../Empirical/source/Evolve/miniphylotrees/GenTrees/OrgDiversityGenotypePercentiles.csv', sep=',', header=None, index_col=0)
#
# data.plot(kind='hist')
# plt.ylabel('Frequency')
# plt.xlabel('Phylogenetic Diversity')
# plt.title('Percentile Data For Phylogenetic Diversity (10000 runs)')
#
#
# plt.show()


data = pd.read_csv('../../Empirical/source/Evolve/miniphylotrees/GenTrees/OrgDiversityGenotypePercentiles.csv', sep=',', header=None, index_col=0)



