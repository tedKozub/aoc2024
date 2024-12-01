def getColFromLine(line: str, col_index: int) -> str:
    return int(line.split("   ")[col_index].strip())


def getAllNumbers(col_index):
    all_numbers = []
    with open("day1/input.txt", "r") as f:
        for line in f.readlines():
            all_numbers.append(getColFromLine(line, col_index))
    return all_numbers


total_distances = 0
firstNumbers = sorted(getAllNumbers(0))
secondNums = sorted(getAllNumbers(1))

for index, num in enumerate(firstNumbers):
    total_distances += abs(num - secondNums[index])

print(total_distances)
