def read():
    with open('data1.txt', 'r') as f:
        txt = f.readlines()
    return txt

rezGroups = 1
def append(group):
    with open('rez1.txt', 'a') as f:
        f.write(f'Group {rezGroups}\n')
        for i in range(len(group)):
            f.write(f'{group[i-1]}')

data = read()

groupNr =  int(data[0])
currGroup = 1

groupList = {}

for groups in range(groupNr):
    groupMems = []
    toFastest = []
    print(f'Group {groups}; Member Count: {int(data[currGroup])}')
    # Makes a member list for current group
    for member in range(int(data[currGroup])):
        currGroup += 1
        groupMems.append(data[currGroup])
    for member in groupMems:
        memToList = member.strip('\n').split(' ')
        timeSec = int(memToList[len(memToList)-1]) + (int(memToList[len(memToList)-2]) * 60)
        # print(memToList[0], memToList[1])
        # print(timeSec)
        toFastest.append([memToList[0], memToList[1], timeSec])
        # print(toFastest)
    for memberNr in range(len(toFastest)):
        for member in range(len(toFastest)):
            if toFastest[member][-1] > toFastest[member-1][-1]:
                print(f"{toFastest[member][-1]} > {toFastest[member-1][-1]}\nSWAPPED")
                toFastest[member], toFastest[member-1] = toFastest[member-1], toFastest[member]
                # print(toFastest)
            else:
                print(f"{toFastest[member][-1]} < {toFastest[member-1][-1]}\nNOTHING CHANGED")
    currGroup += 1
    print(toFastest)
    # append(groupMems)
    rezGroups += 1
        
        