#1.2.1
def hms(sec):
    uur = sec // 3600
    sec %= 3600
    minuut = sec // 60
    sec %= 60
    print(uur,':',minuut,':',sec)

hms(100000)
#1.2.2
