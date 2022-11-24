file1 = open("input.txt", "r")
top = 0
counter = 0
buyuk = -999
kucuk = 999

for each in file1:
    top = top + int(each)
    counter += 1
    if int(each) > buyuk:
        buyuk = int(each)
    if int(each) < kucuk:
        kucuk = int(each)

file2 = open("output.txt", "w")
file2.write("ortalama: ")
file2.write(str(top / counter))
file2.write(" en buyuk sayi: ")
file2.write(str(buyuk))
file2.write(" en kucuk sayi: ")
file2.write(str(kucuk))

file1.close()
file2.close()

print("4:01")
