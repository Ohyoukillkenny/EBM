# Calculate the item degree and vertex weight distributions for Audioscrobbler dataset
import numpy as np
import matplotlib.pyplot as plt
degree = [0]*10000000
item = [0]*10000000
weight = [0]*10000000
files = 'user_artist_data.txt'
csvf = open(files)
data = []
cnt =0
print 'Start reading from '+files
for line in csvf:
    cnt = cnt + 1
    if cnt ==1:
        continue
    if cnt % 1000000 == 0:
        print cnt
    line = line.strip().split()
    user = hash(line[0])%10000000
    book = hash(line[1])%10000000
    rate = float(line[2])
    if rate<2:
        rate = 1
    elif rate<5:
        rate = 2
    elif rate<10:
        rate = 3
    elif rate<20:
        rate = 4
    else:
        rate = 5
    degree[book] = degree[book] + 1
    weight[book] = weight[book] + rate
deg = np.array(degree)
bins = np.bincount(deg)
np.set_printoptions(threshold=np.inf)
degseq = bins[:20000]
xind = np.arange(degseq.shape[0])
plt.plot(xind[1:100],degseq[1:100],'bo')
plt.title('Item Degree Distributions')
plt.xlabel('Degree')
plt.ylabel('Number')
plt.show()
plt.plot(np.log(xind[1:100]),np.log(degseq[1:100]),'bo')
plt.title('Item Degree Distributions (Logarithm)')
plt.xlabel('Degree')
plt.ylabel('Number')
plt.show()
wei = np.array(weight)
binw = np.bincount(wei.astype('int'))
weiseq = binw[:20000]
plt.plot(xind[1:100],weiseq[1:100],'ro')
plt.title('Item Vertex Weight Distributions')
plt.xlabel('Vertex weight')
plt.ylabel('Number')
plt.show()
plt.plot(np.log(xind[1:100]),np.log(weiseq[1:100]),'ro')
plt.title('Item Vertex Weight Distributions (Logarithm)')
plt.xlabel('Vertex weight')
plt.ylabel('Number')
plt.show()

