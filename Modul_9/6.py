##Rohmad Khoirudin
##L200180101
class simpulbiner(object):
    def __init__(self, data):
        self.data=data
        self.kiri=None
        self.kanan=None

    def __str__(self):
        return str(self.data)

A=simpulbiner('Ambarawa')
B=simpulbiner('Bantul')
C=simpulbiner('Cimahi')
D=simpulbiner('Denpasar')
E=simpulbiner('Enrekang')
H=simpulbiner('Halmahera Timur')


A.kiri=B; A.kanan=C
B.kiri=D; B.kanan=E
D.kiri=H; 

#nomer 6
def size(node):
    if node is None: 
        return 0
    else: 
        return (size(node.kiri)+ 1 + size(node.kanan)) 

print('Ukuran dari Binary Tree ini adalah', size(A))

