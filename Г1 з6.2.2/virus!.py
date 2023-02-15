virus_code = 'print("Я вирус!!!!!")'

with open('write_file_task.py', 'a') as file: # вирус будет дописывать
    file.write(f"\n{virus_code}\n")

