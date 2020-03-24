class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us

c0 = MhsTIF('rohmad', "L200180101", 'Riau', 150000)
c1 = MhsTIF('amron', "L200180105", 'Klaten', 125000)
c2 = MhsTIF('dimas', "L200180102", 'Palembang', 20500)
c3 = MhsTIF('dika', "L200180097", 'Bekasi', 350000)
c4 = MhsTIF('Bayu', "L200180096", 'Sragen', 500000)
c5 = MhsTIF('nayu', "L200180099", 'Lampung', 430000)
c6 = MhsTIF('wulan', "L200180091", 'Surakarta', 450000)
c7 = MhsTIF('Rama', "L200180065", 'Sragen', 430000)
c8 = MhsTIF('fandit', "L200180118", 'Sragen', 235000)
c9 = MhsTIF('dhim', "L200180148", 'Sragen', 350000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
        
#######################################nomer1
def swap(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp
    
def ceknim(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.tinggal)

def urutnim(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                swap(a,y,y+1)
##############################################nomer 2
a = [13, 18, 25, 44, 66, 78, 89, 107]
b = [2, 4, 5, 10, 13, 18, 23, 29]

#versi1
def urutC(a,b):
    c = a +b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]=c[pos-1]
            pos -=1
        c[pos]=nilai
    print(c)

#versi2
def urutc(a,b):
    pan1=len(a)
    pan2 = len(b)
    x= 0
    y=0
    c = []
    while x< pan1 and y<pan2:
        if a[x]<b[y]:
            c.append(a[x])
            x+=1
        else:
            c.append(b[y])
            y+=1
    while x<pan1:
        c.append(a[x])
        x+=1
    while y<pan2:
        c.append(b[y])
        y+=1
    return c

###################################################nomer 3
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));

