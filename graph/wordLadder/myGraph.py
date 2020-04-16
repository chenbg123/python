class Vertex:
    def __init__(self,name):
        self.name=name
        self.connectTo={}
        self.distance=0
        self.color="white"
        self.pred=None

    def addNeighbor(self,neighbor,weight=0):
        self.connectTo[neighbor]=weight

    def getName(self):
        return self.name

    def getWeight(self,neighbor):
        return self.connectTo[neighbor]

    def getConnection(self):
        return self.connectTo.keys()

    def setDistance(self,dis):
        self.distance=dis

    def getDistance(self):
        return self.distance

    def setColor(self,color):
        self.color=color

    def getColor(self):
        return self.color

    def setPred(self,pred):
        self.pred=pred

    def getPred(self):
        return self.pred


    def __str__(self):
        return str(self.name) + ":color " + self.color + ":distance " + str(self.distance) + ":pred \n\t[" + str(self.pred)+ "]\n"


class Graph:
    def __init__(self):
        self.vertexList={}

    def addVertex(self,v):
        self.vertexList[v]=Vertex(v)


    def getVertex(self,v):
        if v not in self.vertexList:
            return None
        else:
            return self.vertexList[v]

    def getVertices(self):
        return self.vertexList.keys()


    def addEge(self,f,t,cost=0):

        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)

        self.vertexList[f].addNeighbor(self.vertexList[t],cost)

    def __iter__(self):
        return iter(self.vertexList.values())


"""""
if __name__ == '__main__':
    g=Graph()

    for i in range(6):
       g.addVertex(i)

    g.addEge(1,2,0)
    g.addEge(2,3,1)
    g.addEge(1,3,9)

    for i in g:
        for k in i.getConnection():
            print('(%s,%s)'%(i.getName(),k.getName()))

"""









