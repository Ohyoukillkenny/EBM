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

filenames = ['AI','Algorithm','ProgrammingLanguage']
for filename in filenames:
    print 'Topic:', filename
    degree_file = 'L1-layers/'+filename+'/Author_Topic_'+filename+'.txt'
    myfile = open(degree_file, 'r')
    cnt =0
    author = {}
    topic = {}
    print 'Start reading from '+ degree_file
    for line in myfile:
        cnt = cnt + 1
        if (cnt % 2) == 1:
            authorid = line.split()[0]
            if authorid in author:
                author[authorid] += 1
            else:
                author[authorid] = 1
        else:
            topicid = line.split()[0]
            if topicid in topic:
                topic[topicid] += 1
            else:
                topic[topicid] = 1
    print 'read done, author length, topic length', len(author), len(topic)

    paper_author = {}
    paper_topic = {}

    author_weight_file = 'L1-layers/'+filename+'/Paper_Author_'+filename+'.txt'
    myfile = open(author_weight_file, 'r')
    print 'Start reading from '+ author_weight_file
    for line in myfile:
        paperid = line.split('\t')[0]
        authorid = line.split('\t')[1].split()[0]
        if authorid not in author:
    #         print 'error', authorid
            continue
        if paperid in paper_author:
            paper_author[paperid].add(authorid)
        else:
            paper_author[paperid] = set()
            paper_author[paperid].add(authorid)
            
    topic_weight_file = 'L1-layers/'+filename+'/Paper_Topic_'+filename+'.txt'
    myfile = open(topic_weight_file, 'r')
    print 'Start reading from '+ topic_weight_file
    for line in myfile:
        paperid = line.split('\t')[0]
    #     PaperSet.update(paperid)
        topicid = line.split('\t')[1].split()[0]
        if topicid not in topic:
            continue
        if paperid in paper_topic:
            paper_topic[paperid].add(topicid)
        else:
            paper_topic[paperid] = set()
            paper_topic[paperid].add(topicid)
    print 'Author Number:', len(paper_author), 'Topic Number:', len(paper_topic)

    author_topic = {}
    for k, v in paper_author.iteritems():
        if k not in paper_topic:
            continue
        for a in v:
            for t in paper_topic[k]:
                if (a,t) in author_topic:
                    author_topic[(a,t)] += 1
                else:
                    author_topic[(a,t)] = 1

    myMap = MapWeightRate()
    author_weight = {}
    topic_weight = {}
    for k,v in author_topic.iteritems():
        rate = myMap.mappingFunc(v)
        a = k[0]
        t = k[1]
        if a in author_weight:
            author_weight[a] += rate
        else:
            author_weight[a] = rate
        if t in topic_weight:
            topic_weight[t] += rate
        else:
            topic_weight[t] = rate

    print filename, 'weight_scale:', myMap.seeRatingScale()
