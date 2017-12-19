import numpy as np
import matplotlib.pyplot as plt
class MapWeightRate(object):
    def __init__(self):
        self._mappinglist = []
        self._default = 10000
        i = 0
        n = 0
        while n <= self._default:
            i = i + 1
            n = i ** 2
            self._mappinglist.append(n)
        self._ratingscale = i
        self._maxwei = 0
    def mappingFunc(self, weight):
        if weight > self._mappinglist[-1]:
            print 'Extending...'
            k = len(self._mappinglist)
            while k**2 < weight:
                k += 1
                self._mappinglist.append(k**2)
        if weight > self._maxwei:
            self._maxwei = weight
        for i in range(len(self._mappinglist)):
            if weight <= self._mappinglist[i]:
                return i + 1
    def seeRatingScale(self):
        return self.mappingFunc(self._maxwei)
    def getMappingList(self):
        return self._mappinglist

users = {}
followers = {}
fr = open('twitter_rv.net', 'r')
cnt = 0
for line in fr:
    user = line.split('\t')[0]
    follower = line.split('\t')[1].split('\n')[0]
    if user in users:
        users[user] += 1
    else:
        users[user] = 1
    if follower in followers:
        followers[follower] += 1
    else:
        followers[follower] = 1
    cnt += 1
    if cnt == 10000000:
        break
print cnt

# degree plotting, black: items degree distribution, gray: users, i.e., cust
degree = []
for k,v in users.iteritems():
    degree.append(v)
deg = np.array(degree)

bins = np.bincount(deg)
np.set_printoptions(threshold=np.inf)
degseq = bins
xind = np.arange(degseq.shape[0])

xaxis = []
yaxis = []
for i in range(1, len(degseq)):
    if degseq[i] == 0 or xind[i] == 0:
        continue
    xaxis.append(xind[i])
    yaxis.append(degseq[i])
X = np.asarray(xaxis)
Y = np.asarray(yaxis)
plt.plot(np.log(X),np.log(Y),'o',
    color = 'gray', alpha = 0.8, markersize=4, markeredgewidth=0.0)

degree = []
for k,v in followers.iteritems():
    degree.append(v)
deg = np.array(degree)

bins = np.bincount(deg)
np.set_printoptions(threshold=np.inf)
degseq = bins
xind = np.arange(degseq.shape[0])

xaxis = []
yaxis = []
for i in range(1, len(degseq)):
    if degseq[i] == 0 or xind[i] == 0:
        continue
    xaxis.append(xind[i])
    yaxis.append(degseq[i])
X = np.asarray(xaxis)
Y = np.asarray(yaxis)
plt.plot(np.log(X),np.log(Y),'o',
    color = 'black', alpha = 0.8, markersize=4, markeredgewidth=0.0)

plt.xlabel('Degree',fontsize = 18)
plt.ylabel('Followee/Follower #',fontsize = 18)
figure = plt.gcf()
figure.set_size_inches(5, 2)
plt.savefig('Degree twitter.pdf', bbox_inches='tight')
plt.close()


# rating map
myMap1 = MapWeightRate()
myMap2 = MapWeightRate()
user_weights = {}
follower_weights = {}
fr = open('twitter_rv.net', 'r')
cnt = 0
for line in fr:
    user = line.split('\t')[0]
    follower = line.split('\t')[1].split('\n')[0]
    if user in user_weights:
        if follower in users:
            user_weights[user] += myMap1.mappingFunc(users[follower])
        else:
            user_weights[user] += 1
    else:
        if follower in users:
            user_weights[user] = myMap1.mappingFunc(users[follower])
        else:
            user_weights[user] = 1
            
    if follower in follower_weights:
        if user in followers:
            follower_weights[follower] += myMap2.mappingFunc(followers[user])
        else:
            follower_weights[follower] += 1
    else:
        if user in followers:
            follower_weights[follower] = myMap2.mappingFunc(followers[user])
        else:
            follower_weights[follower] = 1
    cnt += 1
    if cnt == 10000000:
        break
print cnt
print 'Followee Scale:', myMap1.seeRatingScale()
print 'Follower Scale:', myMap2.seeRatingScale()

# weight map, black: items weight distribution, gray: users, i.e., cust
weight = []
for k,v in user_weights.iteritems():
    weight.append(v)
wei = np.array(weight)

bins = np.bincount(wei)
np.set_printoptions(threshold=np.inf)
weiseq = bins
xind = np.arange(weiseq.shape[0])

xaxis = []
yaxis = []
for i in range(1, len(weiseq)):
    if weiseq[i] == 0 or xind[i] == 0:
        continue
    xaxis.append(xind[i])
    yaxis.append(weiseq[i])
X = np.asarray(xaxis)
Y = np.asarray(yaxis)
plt.plot(np.log(X),np.log(Y),'o',
    color = 'gray', alpha = 0.8, markersize=4, markeredgewidth=0.0)

weight = []
for k,v in follower_weights.iteritems():
    weight.append(v)
wei = np.array(weight)

bins = np.bincount(wei)
np.set_printoptions(threshold=np.inf)
weiseq = bins
xind = np.arange(weiseq.shape[0])

xaxis = []
yaxis = []
for i in range(1, len(weiseq)):
    if weiseq[i] == 0 or xind[i] == 0:
        continue
    xaxis.append(xind[i])
    yaxis.append(weiseq[i])
X = np.asarray(xaxis)
Y = np.asarray(yaxis)
plt.plot(np.log(X),np.log(Y),'o',
    color = 'black', alpha = 0.8, markersize=4, markeredgewidth=0.0)

plt.xlabel('Weight',fontsize = 18)
plt.ylabel('Followee/Follower #',fontsize = 18)
figure = plt.gcf()
figure.set_size_inches(5, 2)
plt.savefig('Weight twitter.pdf', bbox_inches='tight')
plt.close()










