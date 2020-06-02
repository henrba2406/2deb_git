import mathplotlib.pyplot as plt
f = open("input.log","r") #åpner fila vi skal telle vokaler i teksten med
f_out  = open("output.txt","w") #åpne utskriftsfil fo å lage data
file_content = f.read() #lagre innhold i fila til file_content

vokal_array = ['a', 'e', 'i', 'o', 'u', 'y']
n = len(vokal_array)
telle_array = [0]*n

for i in file_content:
    index = 0
    for k in vokal_array:
        if (i.lower() == k):
            telle_array[index] = telle_array[index] + 1
        index = index + 1

index = 0
for k in vokal_array:
    f_out.write(k)
    f_out.write(": ")
    f_out.write(str(telle_array[index]))
    f_out.write("\n")
    index = index + 1

f.close() #alltid lukk fila etter bruk 
f_out.close()

plt.plot(vokal_array,telle_array)