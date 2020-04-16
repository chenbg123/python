import os
from collections import defaultdict
from itertools import product
from graph.wordLadder.queue import Queue
from graph.wordLadder.myGraph import *


def build_graph(words):

    backets=defaultdict(list)
    g=Graph()

    for word in words:
        for i in range(len(word)):
            backet='{}_{}'.format(word[:i],word[i+1:])
            backets[backet].append(word)

    for word in backets.values():
        for word1,word2 in product(word,repeat=2):
            if word1 !=word2:
                g.addEge(word1,word2)
    return g


def get_words(vocabulary_file):
    for line in open(vocabulary_file, 'r'):
        yield line[:-1] # remove newline character


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    queue=[]
    queue.append(start)

    while (queue):
        currword=queue.pop(0)
        for neighbor in currword.getConnection():
            if(neighbor.getColor()=='white'):
                neighbor.setColor("gray")
                neighbor.setDistance(currword.getDistance()+1)
                neighbor.setPred(currword)
                queue.append(neighbor)
        currword.setColor('black')



def traverse(x):
    endWord=x
    while(endWord.getPred()):

        print(endWord.getName())

        endWord=endWord.getPred()

    print(endWord.getName())


vocabulary_file = os.path.join(os.path.dirname(__file__), 'vocabulary.txt')

vocabulary=get_words(vocabulary_file)

wordgraph=build_graph(vocabulary)

bfs(wordgraph, wordgraph.getVertex('FOOL'))

traverse(wordgraph.getVertex('SAGE'))






