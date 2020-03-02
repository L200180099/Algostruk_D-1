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
