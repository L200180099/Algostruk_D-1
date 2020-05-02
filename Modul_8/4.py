####################1
import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self,data,priority):
        heapq.heappush(self.qlist, (priority,data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFrontMost(self):
        return self.qlist[-1]
    def getRearMost(self):
        return self.qlist[0]
    
a = PriorityQueue()
a.enqueue("rohmad", 5)
a.enqueue("khoir", 2)
a.enqueue("udin", 11)
a.enqueue("khoirudin", 6)
print("ProrityQueue Front==>",a.getFrontMost())
print("PriorityQueue Rear",a.getRearMost())

################################# bisa juga pake ini
##class _PriorityQue():
##    def __init__(self,data,priority):
##        self.item = data
##        self.priority= priority
##
##class Priorityqueue():
##    def __init__(self):
##        self.qlist=[]
##    def isEmpty(self):
##        return len(self)==0
##    def __len__(self):
##        return len(self.qlist)
##    def enqueue(self,item,priority):
##        _PriorityQue(self.qlist,(item,priority))
##        self.qlist.append(entry)
##    def dequeue(self):
##        n = []
##        for i in self.qlist:
##            n.append(i.priority)
##        print (self.qlist.pop(n.index(min(n))).item)
##    def getFrontMost(self):
##        return self.qlist[0]
##    def getRearMost(self):
##        return self.qlist[len(self.qlist)-1]

#############################queue
class Queue():
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(),"Antria sedang kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]


q = Queue()
q.enqueue(7)
q.enqueue(11)
q.enqueue(12)
q.enqueue(18)
print("queue front==>",q.getFrontMost())
print("queue rear==>",q.getRearMost())





















    
    
