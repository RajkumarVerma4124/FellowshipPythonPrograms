class SetDifference:
    def difference(self,firstSetValue,SecondSetValue):
        diffSet = firstSetValue - SecondSetValue
        print("Difference in Set : ",diffSet)

firstSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(1, rangeVal + 1):
    valAddFirst = input("Enter The String Or Value : ")
    firstSetValue.add(valAddFirst)

SecondSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(1, rangeVal + 1):
    valAddSecond = input("Enter The String Or Value : ")
    SecondSetValue.add(valAddSecond)

print("Data Set First: ",firstSetValue)
print("Data Set Second: ",SecondSetValue)

setMembers = SetDifference()
setMembers.difference(firstSetValue,SecondSetValue)