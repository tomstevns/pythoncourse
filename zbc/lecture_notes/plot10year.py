import os
import csv
# import dictionary from py file som data.
from kkdata import STATISTICS as data
import matplotlib.pyplot as plt


""" def find_peeps(year, age):
    # print(kkdata.STATISTICS[1992])
    # Går først over all bydele
    cph_hoods = data[year].keys()

    cph_kids = []
    for hood in cph_hoods:
        for _, value in data[year][hood][age].items():
            cph_kids.append(value)
    return sum(cph_kids)


print(find_peeps(2015, 10))  # 4797 """

# Plot 10 årige i kbh.


def find_peeps(year, age):
    cph_hoods = data[year].keys()
    cph_kids = []
    for hood in cph_hoods:
        try:
            for _, value in data[year][hood][age].items():
                cph_kids.append(value)
        except KeyError:
            cph_kids.append(0)
    return sum(cph_kids)


year_list = data.keys()  # 1992-2015
age_list = [find_peeps(year, 10) for year in year_list]
age_list_12 = [find_peeps(year, 12) for year in year_list]

plt.bar(year_list, age_list)
plt.bar(year_list, age_list_12)
plt.show()
