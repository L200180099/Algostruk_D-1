def formatRupiah(x):
    a = '{:,}'.format(x).replace(',', '.')
    return "Rp " + a
