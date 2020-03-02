def jumlahHurufKonsonan(a):
    x = 0
    vokal = "A,I,U,E,O,a,i,u,e,o"
    hvok = vokal.split(",")
    for i in a:
        if i not in hvok:
            x+=1
    return (len(a),x)
