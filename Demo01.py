
btnLetter = {"0":"0",
             "1":"1",
             "2":["A", "B", "C"],
             "3":["D", "E", "F"],
             "4":["G", "H", "I"],
             "5":["J", "K", "L"],
             "6":["M", "N", "O"],
             "7":["P", "Q", "R", "S"],
             "8":["T", "U", "V"],
             "9":["W", "X", "Y", "Z"] }
numStr = input("请键入数字\n")
numList = numStr.split(",")
print(numList)
numLen = len(numList)
# 输入的数字列表的长度
outputList = []
n = 0
while n<numLen:
    # outputListLen = len(outputList)
    if n == 0:
        for item in btnLetter[numList[n]]:
            outputList.append(item)
    else:
        tempList, outputList = outputList, []
        i = 0
        while i<len(btnLetter[numList[n]]):
            for item in tempList:
                outputList.append(item + btnLetter[numList[n]][i])
            i += 1
    n += 1
outputList = [item.lower() for item in outputList]
print(outputList)