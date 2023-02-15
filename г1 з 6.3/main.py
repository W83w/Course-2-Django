# ковер ░▒▓
def carpet(width, height):
    border_line = "▓" + '░' * (width - 2) + '▓'
    midle_line = "▓"+'░'+'▒' * (width - 4) + '░' + '▓'


    print(border_line)
    for i in range(height - 2):
        print(midle_line)
    print(border_line)

carpet(12, 4)


