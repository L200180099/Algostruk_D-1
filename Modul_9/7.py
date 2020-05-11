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

#nomer 7
def tinggipohon(a): 
    if a is None: 
        return 0 ;  
  
    else : 
        kirtinggi = tinggipohon(a.kiri) 
        kantinggi = tinggipohon(a.kanan) 
  
        if (kirtinggi > kantinggi): 
            return kirtinggi+1
        else: 
            return kantinggi+1
        
print("Tinggi max Binnary Tree ini adalah",tinggipohon(A))
