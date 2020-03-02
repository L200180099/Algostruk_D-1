#1
def cetakSiku(x):
    a = 1
    for i in range(x):
        print("*"*a)
        a+=1
        
#2
def gambarlahPersegiEmpat(tinggi,lebar):
    print ("@"*lebar)
    for i in range (tinggi-2):
        print ("@"+(" "*(lebar - 2))+"@")
    print ("@"*lebar)
#3a
def jumlahHurufVokal(a):
    vokal = ["A","I","U","E","O","a","i","u","e","o"]
    x = 0
    for i in a:
        if i in vokal:
            x+=1
    return(len(a),x)


#3b
def jumlahHurufKonsonan(a):
    x = 0
    vokal = "A,I,U,E,O,a,i,u,e,o"
    hvok = vokal.split(",")
    for i in a:
        if i not in hvok:
            x+=1
    return (len(a),x)

#4
def rerata(x):
    hasil = (sum(x)/len(x))
    return hasil
#5
from math import sqrt as sq

def apakahPrima(n):
    n = int(n)
    assert n>= 0
    primakecil = [2,3,5,7]
    bukanprima = [0,1,2,4,6,8,9,10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n % i == 0:
                return False
                break
            return True
#6
##from math import sqrt as sq
##
##def apakahPrima(n):
##    n = int(n)
##    assert n>= 0
##    primakecil = [2,3,5,7]
##    bukanprima = [0,1,2,4,6,8,9,10]
##    if n in primakecil:
##        return True
##    elif n in bukanprima:
##        return False
##    else:
##        for i in range(2,int(sq(n))+1):
##            if n % i == 0:
##                return False
##                break
##            return True
##for i in range (2,1000):
##    if apakahPrima(i) == True:
##        print(i)

#7
def faktorPrima(n):
    n = int(n)
    data = []
    i=2
    while i <= n:
        if n%i == 0:
            n = n/i
            data.append(i)
        else:
            i += 1
    hasil = tuple(data)
    print (hasil)

#8
def apakahTerkandung(a,b):
    return a in b

#9
##for i in range(1,100):
##    if (i % 3 == 0) and (i % 5 == 0):
##        print ("Python UMS")
##    elif i % 3 == 0:
##        print ("Python")
##    elif i % 5 == 0:
##        print ("UMS")
##    else:
##        print (i)

#10
from math import sqrt as akar

def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = (b**2) - (4*a*c)
    
    if D < 0 :
        return "Determinannya negatif. Persamaan tidak mempunyai akar real."
    else :
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1, x2)
        return hasil

#11
def apakahKabisat(x):
    x = int(x)
    if x%100 == 0 and x%400 != 0:
        return False
    elif x%4 == 0 or x%400 == 0:
        return True
    else:
        return False
    
#12
##import random
##
##print("""permainan tebak angka.
##saya menyimpan sebuah angka bulat antara 1 sampai 100.coba tebak.
##(kesempatan menebak anda 7 kali)
##""")
##jawaban = random.randint(0,100)
##ronde = 1
##benar=0
##salah = 0
##while benar < 1:
##    if salah == 6:
##        inp = int(input("masukan tebakan ke-{}:>".format(ronde)))
##        if inp == jawaban:
##            print("""Ya anda benar.
##            Congratulatulations""")
##            benar+=1
##        elif inp < jawaban:
##            print("itu terlalu kecil.")
##            print("maaf kesempatan anda telah habis")
##            break
##        elif inp > jawaban:
##            print("itu terlalu besar.")
##            print("maaf kesempatan anda telah habis")
##            break
##       
##    elif salah < 6:
##        inp = int(input("masukan tebakan ke-{}:>".format(ronde)))
##        if inp == jawaban:
##            print("Ya anda benar")
##            benar+=1
##        elif inp < jawaban:
##            print("itu terlalu kecil. coba lagi")
##            ronde+=1
##            salah += 1
##        elif inp > jawaban:
##            print("itu terlalu besar. coba lagi")
##            ronde+=1
##            salah+=1
        
    

    
#13
def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])

#14
def formatRupiah(x):
    a = '{:,}'.format(x).replace(',', '.')
    return "Rp " + a

