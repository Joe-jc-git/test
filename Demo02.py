btnLetter = {"0":["S"],
             "1":["Z"],
             "2":["A", "B", "C"],
             "3":["D", "E", "F"],
             "4":["G", "H", "I"],
             "5":["J", "K", "L"],
             "6":["M", "N", "O"],
             "7":["P", "Q", "R"],
             "8":["T", "U", "V"],
             "9":["W", "X", "Y"]}
# 把s跟z拆给了0和1，然后0-99，输入99的话就是拆成9,9 这种思路
# 这种方法没去考虑会不会输入99,99的情况
numStr = input("请键入数字\n")
numList = list(numStr)
# 把输入的数字拆成数组
print(numList)
numLen = len(numList)
# 输入的数字列表的长度
outputList = []
n = 0
while n<numLen:

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