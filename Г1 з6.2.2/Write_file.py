with open('Write_data_file.txt', 'wt') as file: # запись в файл модификатор записи создает постоянно новый файл
    file.write('Hello\n')   # спец символ для переноса строки расшифровывается как Newline
    file.write("World\n")
    file.write("newLine text ")