import string
from collections import deque

wordList = ["hot","dot","dog","lot","log","cog"]

def ladderLength(beginWord, endWord, wordList):
    queue=deque([(beginWord, 1)])
    visited = set()
    alph=string.ascii_lowercase

    while queue:
        word, dist = queue.popleft()
        if word == endWord:
            return dist
        for i in range(len(word)):
            for a in alph:
                tmp = word[:i] + a + word[i + 1:]
                if tmp not in visited and tmp in wordList:
                    queue.append((tmp, dist + 1))
                    visited.add(tmp)
    return 0

list=ladderLength('hot','cog',wordList)
print(list)



