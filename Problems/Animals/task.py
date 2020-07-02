# read animals.txt
# and write animals_new.txt
file_old = open('animals.txt', 'r')
file_new = open('animals_new.txt', 'w')
for line in file_old:
    file_new.write(line.replace('\n', ' '))
file_old.close()
file_new.close()
