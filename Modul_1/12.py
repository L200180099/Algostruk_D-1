import random

print("""permainan tebak angka.
saya menyimpan sebuah angka bulat antara 1 sampai 100.coba tebak.
(kesempatan menebak anda 7 kali)
""")
jawaban = random.randint(0,100)
ronde = 1
benar=0
salah = 0
while benar < 1:
    if salah == 6:
        inp = int(input("masukan tebakan ke-{}:>".format(ronde)))
        if inp == jawaban:
            print("""Ya anda benar.
            Congratulatulations""")
            benar+=1
        elif inp < jawaban:
            print("itu terlalu kecil.")
            print("maaf kesempatan anda telah habis")
            break
        elif inp > jawaban:
            print("itu terlalu besar.")
            print("maaf kesempatan anda telah habis")
            break
       
    elif salah < 6:
        inp = int(input("masukan tebakan ke-{}:>".format(ronde)))
        if inp == jawaban:
            print("Ya anda benar")
            benar+=1
        elif inp < jawaban:
            print("itu terlalu kecil. coba lagi")
            ronde+=1
            salah += 1
        elif inp > jawaban:
            print("itu terlalu besar. coba lagi")
            ronde+=1
            salah+=1
        
    

    
