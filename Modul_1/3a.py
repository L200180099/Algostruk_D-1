def jumlahHurufVokal(a):
    vokal = ["A","I","U","E","O","a","i","u","e","o"]
    x = 0
    for i in a:
        if i in vokal:
            x+=1
    return(len(a),x)


