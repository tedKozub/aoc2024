def getColFromLine(line: str, col_index: int) -> str:
    return int(line.split("   ")[col_index].strip())


def getAllNumbers(col_index):
    all_numbers = []
    with open("day1/input.txt", "r") as f:
        for line in f.readlines():
            all_numbers.append(getColFromLine(line, col_index))
    return all_numbers

def getOccurencesInList(list):
    occurences = {}
    for num in list:
        if num not in occurences:
            occurences[num] = 1
        else:
            occurences[num] += 1
    return occurences

similarity_score = 0
leftList = sorted(getAllNumbers(0))
rightList = sorted(getAllNumbers(1))
location_id_occurences = getOccurencesInList(rightList)

for location_id in leftList:
    if location_id not in location_id_occurences:
        continue
    similarity_score += location_id * location_id_occurences[location_id]


print(similarity_score)