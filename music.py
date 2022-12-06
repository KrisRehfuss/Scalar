music = ({

    'A': 440,
    'B': 494,
    'C': 261,
    'D': 293,
    'E': 330,
    'F': 350,
    'G': 392

})


def Me():
    me = input("What note? ")
    if me.isdigit:
        me = me.capitalize()
        if me in music:

            return me

        else:
            print("Must be a music note.")
    else:
        print("Must be a letter. ")

    return me


def Check(z):
    for x, y in music.items():
        if x == z:
            print(f'\n{x} = {y} Hz ')

            return x, y


def Main():
    let, hz = Check(Me())
    return let, hz
