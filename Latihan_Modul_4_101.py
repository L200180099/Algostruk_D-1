 #1
def linser(a,target):
    if target in a:
        print("targetnya terdapat diaray tersebut")
    else:
        print("targetnya tidak terdapat diarray tersebut")
        
a = [10,51,2,18,4,31,13,5,23,64,29]
print("a =",a)
linser(a,31)
linser(a,8)

##2
def cariLurus(wadah,target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False
a = [10,51,2,18,4,31,13,5,23,64,29]
cariLurus(a,31)
cariLurus(a,8)

#3
class MhsTIF(object):
    def __init__(self,nama,umur,tinggal,us):
        self.nama = nama
        self.umur = umur
        self.tinggal = tinggal
        self.us = us

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
target ='Klaten'
for i in Daftar:
    if i.tinggal == target:
        print(i.nama + ' tinggal di '+ target)
        

#latihan4
def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range(1,n):
        if kumpulan[i]<terkecil:
            terkecil = kumpulan[i]
    return terkecil
print("data terkecil dari data a adalah ", cariTerkecil(a))

#tantangan 1
def cariUSTerkecil():
    terkecil = Daftar[0].us
    for i in range (len(Daftar)):
        if terkecil > Daftar[i].us:
            terkecil = Daftar[i].us
    return terkecil
print("uang saku terkecil adalah ",cariUSTerkecil())

#tantangan2
def cariUSTerbesar():
    a= len(Daftar)
    terbesar = Daftar[10].us
    for i in range (len(Daftar)):
        if Daftar[i].us> terbesar:
            terbesar = Daftar[i].us
    return terbesar
print("uang saku terbesar adalah ",cariUSTerbesar())

#tantangan3
def carikurang25():
    a = 250000
    x = []
    for i in range(len(Daftar)):
        if Daftar[i].us < a:
            x.append(Daftar[i].nama)
    return x
print("uang sakunya yang kurang dari 250000 adalah",carikurang25())

#tantangan4
def carilebih25():
    a = 250000
    x = []
    for i in range(len(Daftar)):
        if Daftar[i].us > a:
            x.append(Daftar[i].nama)
    return x
print("uang sakunya yang lebih dari 250000 adalah",carilebih25())

#latihan5
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return True
        elif target <= kumpulan[mid]:
            high=mid-1
        else:
            low = mid +1
    return False

a = [10,51,2,18,4,31,13,5,23,64,29]
target = 31
print(binSe(a,target))

#tantangan5
def binSe2(kumpulan,target):
    low = 0
    high = len(kumpulan)
    while low < high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return "Target pada indeks " + str(mid)
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
a = [10,51,2,18,4,31,13,5,23,64,29]
target = 31
print(binSe2(a,target))

