from math import floor


def calculateMedian( data ):
    median = 0
    if len(data) % 2 == 0:
        median = int((data[int(len(data) / 2)] + data[(int(len(data) / 2) - 1)]) / 2)
    else:
        median = int(data[floor(len(data) / 2)])
    return median

def calculateQ1( data ):
    dataQ1 = []
    if len(data) % 2 == 0:
        for index in range(0, ((int)(len(data) / 2))):
            dataQ1 = dataQ1 + [data[index]]
    else:
        for index in range(0, floor(len(data) / 2)):
            dataQ1 = dataQ1 + [data[index]]
    print("DataQ1=",dataQ1)
    return calculateMedian(dataQ1)

def calculateQ3( data ):
    dataQ3 = []
    if len(data) % 2 == 0:
        for index in range(floor(len(data) / 2), len(data)):
            dataQ3 = dataQ3 + [data[index]]
    else:
        for index in range(floor(len(data) / 2)+1, len(data)):
            dataQ3 = dataQ3 + [data[index]]
    print("DataQ3=",dataQ3)
    return calculateMedian(dataQ3)

row1 = input("")
row2 = input("")

row2Split = row2.split(" ")

data = [int(i) for i in row2Split]
data.sort()
print(data)
print(calculateQ1(data))
print(calculateMedian(data))
print(calculateQ3(data))

