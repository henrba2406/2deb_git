f = open("input.log","r") #åpner fila vi skal telle vokaler i teksten med

f_out = open("output.txt","w") #åpne utskriftsfil fo å lage data

file_content = f.read() #lagre innhold i fila til file_content

count = 0

for i in file_content:
    if (i == 'a') or (i == 'A') or (i == 'e') or (i == 'E') or (i == 'i') or (i == 'I') or (i == 'o') or (i == 'O') or (i == 'u') or (i == 'U') or (i == 'y') or (i == 'Y'):
        count = count + 1

print(count)

f_out.write("A or a: ") #skriv til output.tex om
f_out.write(str(count)) #hvor mange store og små A'er vi fant

f.close() #alltid lukk fila etter bruk 
f_out.close()