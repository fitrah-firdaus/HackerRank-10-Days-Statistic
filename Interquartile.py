from math import floor


def calculateMedian( data ):
    median = 0
    if len(data) % 2 == 0:
        median = float((data[int(len(data) / 2)] + data[(int(len(data) / 2) - 1)]) / 2)
    else:
        median = float(data[floor(len(data) / 2)])
    return median

def calculateQ1( data ):
    dataQ1 = []
    if len(data) % 2 == 0:
        for index in range(0, ((int)(len(data) / 2))):
            dataQ1 = dataQ1 + [data[index]]
    else:
        for index in range(0, floor(len(data) / 2)):
            dataQ1 = dataQ1 + [data[index]]
    #print("DataQ1=",dataQ1)
    return calculateMedian(dataQ1)

def calculateQ3( data ):
    dataQ3 = []
    if len(data) % 2 == 0:
        for index in range(floor(len(data) / 2), len(data)):
            dataQ3 = dataQ3 + [data[index]]
    else:
        for index in range(floor(len(data) / 2)+1, len(data)):
            dataQ3 = dataQ3 + [data[index]]
    #print("DataQ3=",dataQ3)
    return calculateMedian(dataQ3)

row1 = input("")
row2 = input("")
row3 = input("")
row2Split = row2.split(" ")
row3Split = row3.split(" ")

data = []
freq = [int(j) for j in row3Split]
seq = 0
for i in row2Split:
    for k in range(freq[seq]):
        data.append(int(i))
    seq=seq+1
data.sort()
#print(data)
print(calculateQ3(data)-calculateQ1(data))

