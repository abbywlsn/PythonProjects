import numpy as np
import csv
from pprint import pprint

# treedata_array = np.genfromtxt("../../Empirical/source/Evolve/miniphylotrees/GenTrees/ChooseOrgGenotype.csv", delimiter=",")
# print(treedata_array)
#
# with open('../../Empirical/source/Evolve/miniphylotrees/GenTrees/OrgGenotypePercentiles.csv', 'w') as tree_percentiles:
#     for i in range(101):
#         print(i, np.percentile(treedata_array, i))
#
#         tree_percentiles.write(str(i) + "," + " " + str(np.percentile(treedata_array, i)) + '\n')

MyList=[]
with open('../../Empirical/source/Evolve/miniphylotrees/GenTrees/ChooseOrgGenotype.csv', 'r', newline='') as csv_file:
    reader = csv.reader(line.replace('  ', ',') for line in csv_file)
    for row in reader:
        MyList.append(row)

        # print(MyList)

    MyList.sort()

    print(MyList)
    # my_list = list(reader)
    # # x = my_list
    # data_array = []
    #
    # for a_list in my_list:
    #     print(a_list)
    #     floatlist = []
    #     floatlist = np.array(a_list)
    #     try:
    #         floatlist = floatlist.astype(np.float)
    #     except:
    #         print('that didnt work')
    #     #floatlist = [float(i) for i in a_list]
    #     floatlist = np.sort(floatlist)

        #data_array.append(floatlist)

        # every_10th_element = floatlist[::10]
        # data_array.append(every_10th_element)

    # print(data_array)

    # with open('../../Empirical/source/Evolve/miniphylotrees/GenTrees/SortedChooseOrgGenotype.csv',
    #           'w') as tree_percentiles:
    #     for index, line in enumerate(data_array):
    #         stringlist = [str(i) for i in line]
    #         fileline = ",".join(stringlist)
    #
    #         # tree_percentiles.write(str(index) + "," + fileline + '\n')
    #         tree_percentiles.write(fileline + '\n')

    # type(data_array[0])
    #
    # data_array = data_array.astype(np.float)
    #
    # print(data_array)  # multidimensional array

# for lists in data_array:
#     for num in lists:
#             print(num, np.percentile(lists, num))
