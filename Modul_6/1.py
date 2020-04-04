from mhstif import *
c0 = MhsTIF('rohmad', 101, 'Riau', 150000)
c1 = MhsTIF('amron', 105, 'Klaten', 125000)
c2 = MhsTIF('dimas', 102, 'Palembang', 20500)
c3 = MhsTIF('dika', 97, 'Bekasi', 350000)
c4 = MhsTIF('Bayu', 96, 'Sragen', 500000)
c5 = MhsTIF('nayu', 99, 'Lampung', 430000)
c6 = MhsTIF('wulan', 91, 'Surakarta', 450000)
c7 = MhsTIF('Rama', 65, 'Sragen', 430000)
c8 = MhsTIF('fandit', 118, 'Sragen', 235000)
c9 = MhsTIF('dhim', 148, 'Sragen', 350000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

def cek(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.tinggal)
#nomer 1
    #mergesort
def mergesort(A) :
    if len (A) > 1 :
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergesort(separuhkiri)
        mergesort(separuhkanan)

        i=0;j=0;k=0
        while i < len (separuhkiri)and j < len (separuhkanan) :
            if separuhkiri[i].nim < separuhkanan[j].nim :
                A[k] = separuhkiri[i]
                i = i+1
            else :
                A[k] = separuhkanan[j]
                j = j+1
            k = k+1

        while i < len (separuhkiri) :
            A[k] = separuhkiri[i]
            i = i+1
            k = k+1
        while j < len (separuhkanan) :
            A[k] = separuhkanan[j]
            j = j+1
            k = k+1
    #quicksort
def quicksort(A):
    quicksortbantu(A,0,len(A)-1)

def quicksortbantu(A,awal,akhir):
    if awal < akhir:
        titikbelah = partisi(A,awal,akhir)
        quicksortbantu(A,awal,titikbelah -1)
        quicksortbantu(A,titikbelah+1,akhir)

def partisi(A,awal,akhir):
    nilaipivot = A[awal].nim
    penandakiri = awal + 1
    penandakanan = akhir
    selesai = False

    while not selesai:
        while penandakiri <= penandakanan and A[penandakiri].nim <= nilaipivot:
            penandakiri +=1
        while A[penandakanan].nim >= nilaipivot and penandakanan >= penandakiri :
            penandakanan -=1
        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp
    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

cek(Daftar)
print("=====================================")
print("mergesortnya")
print("=====================================")
mergesort(Daftar)
cek(Daftar)
print("=====================================")
print("quicksortnya")
quicksort(Daftar)
print("=====================================")
cek(Daftar)

        
