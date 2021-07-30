import numpy as np
# numpi er hurtigt fordi det er i c.

filename = 'befkbhalderstatkode.csv'

# np.int16 betyder assigned.
# np.uint16 afhænig af det største tal.
d = np.genfromtxt(filename, delimiter=',', dtype=np.uint16, skip_header=1)
# print(d)

# Antal af alle 10 årige danskere i 2015
# d[:,0] første kolone
np.sum(d[(d[:, 0] == 2015) & (d[:,2] == 10) & (d[:, 3] == 5100)][:,-1])


# Sumer franskmænd
german_mask = (d[(d[:, 0] == 2015) & (d[:,2] == 10) & (d[:, 3] == 5180)]
french_mask= (d[(d[:, 0] == 2015) & (d[:,2] == 10) & (d[:, 3] == 5130)]

np.unique(d[:,1]) 

french = np.sum[d[french_mask & (d[:,1] == n)][:4] for n in neighb.keys()]
neighb[neighb.keys()](np.argmax(french))

antal = d[:1, 1:]
print(antal)
