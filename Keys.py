import math
import music

def Convert(z):
    z = int(z)
    print(f'\n{z} Hz = {z} cycles/s')
    Note2BPM = z * 60
    print(f'x60 = {Note2BPM} cycles/m')
    return Note2BPM


def Me(x):
    BPM = int(x)
    Count = 0
    while BPM > 100:
        BPM = BPM/2
        Count +=1
        print(f'x/2 = {BPM}')
    else:
        #print(f'BPM is {BPM}')
        return BPM

def Make(y):
    y = float(y)
    while y < 70:
        y = y*2
    else:
        Final = round(y)
        return Final


def Main(): 
    Letter, Hz = (music.Main())
    Final = Make(Me(Convert(Hz)))
    print(f'\n{Letter} = {Final} bpm\n')

    return Letter, Final
    
Main()

