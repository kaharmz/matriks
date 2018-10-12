string = ""

bar = 1

x = int(input("masukan angka  : "))

#loopingbaris

while bar <= x:
    kol = bar

    #looping kolom
    while kol > 0:
        string = string + "*"
        kol = kol -1
    string = string
    bar = bar + 1

    print(string)
