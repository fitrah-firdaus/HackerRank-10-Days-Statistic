row1 = input("")
row2 = input("")
row3 = input("")

row2Split = row2.split(" ")
row3Split = row3.split(" ")
# print("row 1", row1)
if int(row1) >= 5 & int(row1) <= 500:
    topResult = 0
    bottomResult = 0
    for index in range(int(row1)):
        topResult = topResult + (int(row2Split[index]) * int(row3Split[index]))
        bottomResult = bottomResult + int(row3Split[index])

    print(round(topResult / bottomResult,1))
