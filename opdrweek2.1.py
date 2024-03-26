#1.2.1
def hms(sec):
    uur = sec // 3600
    sec %= 3600
    minuut = sec // 60
    sec %= 60
    print(uur,':',minuut,':',sec)

hms(100000)
#1.2.2
def is_schrikkeljaar(jaar):
    #jaar % 4
    if(jaar%4 == 0):
        print(True)
        if(jaar%100 == 1):
            print(True)
    else:
        print(False)
#1.2.4
