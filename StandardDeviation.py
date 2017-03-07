from math import sqrt

row1 = input("")
row2 = input("")

row2Split = row2.split(" ")
totalData= 0
for index in range(int(row1)):
    totalData = totalData+int(row2Split[index])

mean = totalData / int(row1)

totalDeviation = 0
for index in range(int(row1)):
    totalDeviation = totalDeviation + pow((int(row2Split[index])-mean),2)

print(round(sqrt(totalDeviation/int(row1)),1))
