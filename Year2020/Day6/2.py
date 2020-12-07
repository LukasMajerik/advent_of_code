f = open("data.txt", "r")
data = f.read().strip().split("\n\n")
data = [r.split("\n") for r in data]


print(data)
print(55*"=")
sets = []
for group in data:
    answers = []
    for person in group:
        answers.append(set(person))
    sets.append(answers[0].intersection(*answers))
# print(sets)
group_questions = 0
for s in sets:
    group_questions += len(s)
print(group_questions)
