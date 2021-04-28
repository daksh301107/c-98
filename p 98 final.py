f = open('pari.txt', 'r+')
e = open('daksh.txt', 'r+')
file1Lines = f.readline()
e.write(file1Lines)
print(file1Lines)
file2Lines = f.readline()


f.write(file2Lines)
