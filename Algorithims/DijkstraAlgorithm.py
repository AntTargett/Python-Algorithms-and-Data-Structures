import heapq
import sys
class priority_queue:
    def __init__(self):
        self.pq=[]
        self.length=0
    def push(self,item):
        heapq.heappush(self.pq,item)
        self.length+=1
    def pop(self):
        self.length-=1
        return heapq.heappop(self.pq)
    def empty(self):
        return len(self.pq)==0
    def __len__(self):
        return self.length
class DijkstraGraph:
    def __init__(self,n):
        self.n=n
        self.adj=[[] for _ in range(n)]
    def add_edge(self,u,v,w):
        self.adj[u].append((v,w))
        self.adj[v].append((u,w))
    def dijkstra(self,s,t):
        dist=[sys.maxsize]*self.n
        pred=[-1]*self.n
        visited=[False]*self.n
        remaining=priority_queue()
        dist[s]=0
        remaining.push((0,s))
        path=str(t)
        while not remaining.empty():
            d,u=remaining.pop()
            if visited[u]:continue
            visited[u]=True
            for v,w in self.adj[u]:
                new_dist=d+w
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    pred[v]=u
                    remaining.push((new_dist,v))

        while pred[t]!=s:
            path=str(pred[t])+'-->'+path
            t=pred[t]
        path=str(s)+'-->'+path
        return dist,pred,path
def WriteInputForFileName():
    # Two Error catches around one part of codea
    while True:
        try:
            file_n = input('Please input your file to begin program: ')
            print('')
            opened_file = open(file_n)
            return opened_file
        except FileNotFoundError:
            print('?')
            print('Your file was not found')
        else:
            break
G=DijkstraGraph(6105)
def readInFile():
    openF=open('customers.txt')
    customerlist=[]
    for line in openF:
        while len(line)!=0:
            line=line.strip('\n')
            line2=line.split(" ")
            line2=int(line2[0])
            customerlist.append(line2)
            line = openF.readline()
    openF=open('edges.txt')
    for line in openF:
        while len(line) != 0:
            line = line.strip('\n')
            line2 = line.split(" ")
            line2[0],line2[1],line2[2]=int(line2[0]),int(line2[1]),int(line2[2])
            G.add_edge(line2[0],line2[1],line2[2])
            line = openF.readline()
    return customerlist
def FindShortPath(s,t,customerlist):
    dist,preds,path=G.dijkstra(s,t)
    dist2,preds2,path2=G.dijkstra(t,s)
    print('Minimum Path and Distance: ')
    paths = str(t)
    current=t
    checklong=True
    checkshort=True
    if s in customerlist:
        checklong=False
    if dist[t]!=0:
      while preds[current]!=s:
        if preds[current] in customerlist:
            checklong=False
            checkshort=False
        if checkshort:
            paths=str(preds[current])+'-->'+paths
        else:
            paths=str(preds[current])+'(C)-->'+paths
            checkshort=True
        current=preds[current]
      paths=str(s)+'-->'+paths
    else:
        paths=str(s)
    print(paths)
    print('Total route distance: '+str(dist[t]))
    if checklong:
        if s==t and s in customerlist:
            finalpath = str(s) + '(C)'
            minval = 0
        else:
            minval = sys.maxsize
            for i in range(len(customerlist)):
                if (dist[customerlist[i]] + dist2[customerlist[i]]) <= minval:
                    minval = (dist[customerlist[i]] + dist2[customerlist[i]])
                    mincust = customerlist[i]
            paths = str(mincust)
            current = mincust
            while preds[current] != s:
                paths = str(preds[current]) + '-->' + paths
                current = preds[current]
            paths = str(s) + '-->' + paths + '(C)-->'
            pathsopp = str(t)
            current = mincust
            while preds2[current] != t:
                pathsopp = str(preds2[current]) + '-->' + pathsopp
                current = preds2[current]
            finalpath = paths + pathsopp
    else:
        finalpath=paths
        minval=dist[t]
    print('Minimum Detour Path and Distance: ')
    print(finalpath)
    print('Total route distance: '+str(minval))
    # minval = int(sys.maxsize)
    # for i in range(len(customerlist)):
    #     dist, preds, path = G.dijkstra(s, customerlist[i][0])
    #     dist2, preds2, path2 = G.dijkstra(customerlist[i][0], t)
    #     dist3 = dist[customerlist[i][0]] + dist2[t]
    #     if dist3 <= minval:
    #         minval = dist3
    #         path3=path+'(C)-->'+path2
    # print('Minimum Detour Path and Distance: ')
    # print(path3)
    # print('Total route distance: '+str(minval))
    return
def userInputSource():
    uinput=int(input("Enter source vertex: "))
    return uinput
def userInputTarget():
    uinput=int(input("Enter target vertex: "))
    return uinput
FindShortPath(userInputSource(),userInputTarget(),readInFile())