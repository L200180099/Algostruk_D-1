class Stack():
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)
    
class StackLL():
    def __init__(self):
        self.top = None
        
        self.size=0
    def isEmpty(self):
        return self.top is None
    def __len__(self):
        return self.size
    def peek(self):
        assert not self.isEmpty(),"tidak bisa diintip.stack kosong"
        return self.top.item
    def pop(self):
        assert not self.isEmpty(),"tidak bisa pop dari stack kosong"
        node = self.top 
        self.top = self.top.next
        self.size -=1
        return node.item
    def push(self,data):
        self.top =_stackNode(data,self.top)
        self.size+=1
class _stackNode():
    def __init__(self,data,link):
        self.data = data
        self.link = link
        self.next =None

class queque():
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

class _PriorityQue():
    def __init__(self,data,priority):
        self.item = data
        self.priority= priority

class Priorityqueque():
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

def cetakBinner(d):
    f=Stack()
    if d==0 : f.push(0);
    while d!=0:
        sisa = d%2
        d=d//2
        f.push(sisa)
    st=""
    for i in range(len(f)):
        st = st+str(f.pop())
    return st
prompt = "masukan bilangan positif (<0 untuk mengakhiri):"
mystack = StackLL()
value =int(input(prompt))
while value >0:
    mystack.push(value)
    value =int(input(prompt))
while not mystack.isEmpty():
    value = mystack.pop()
    print(value)
