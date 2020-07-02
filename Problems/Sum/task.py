# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    print(sum(int(x) for x in line.split()))
file.close()
