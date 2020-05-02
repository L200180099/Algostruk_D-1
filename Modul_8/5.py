class Priorityqueue():
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,item,priority):
        entry = _PriorityQue(item,priority)
        self.qlist.append(entry)
    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]

class _PriorityQue():
    def __init__(self,data,priority):
        self.item = data
        self.priority= priority

q = Priorityqueue()
q.enqueue("rohmad", 5)
q.enqueue("khoir", 2)
q.enqueue("udin", 11)
q.enqueue("khoirudin", 6)
print("dequeue 1==>")
q.dequeue()











