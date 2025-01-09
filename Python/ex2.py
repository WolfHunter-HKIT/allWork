def read():
    with open('data2.txt', 'r') as f:
        txt = f.readlines()
    return txt

total = {}
data = read()
nonUniqueExercise = []
uniqueExercises = []
for exercise in range(len(data)):
    lists = data[exercise].strip('\n').split(' ')
    lists = [lists[0], lists[-1]]
    nonUniqueExercise.append(lists)

for exercise in nonUniqueExercise:
    if len(uniqueExercises) == 0:
        uniqueExercises.append({exercise[0]: exercise[-1]})
    else:
        for unqExercise in uniqueExercises:
            print(next(iter(unqExercise)), exercise)
            if exercise[0] in next(iter(unqExercise)):
                print(unqExercise)
                unqExercise[f'{exercise[0]}'] = int(unqExercise[f'{exercise[0]}']) + int(exercise[-1])
                print(exercise, "not unique") 
                continue
            uniqueExercises.append({exercise[0]: int(exercise[-1])})
            print(exercise, "unique")
        
print(uniqueExercises)