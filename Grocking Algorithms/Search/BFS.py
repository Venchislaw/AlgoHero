from collections import deque

# build graph:

relations = {}
relations['Walter'] = ['Walter jr.', 'Hank']
relations['Walter jr.'] = ['Hank', 'Skyler']
relations['Skyler'] = ['Mary']
relations['Hank'] = ['Mary', 'Walter', 'Walter jr.']

# build BFS

queue = deque(relations['Walter'])
checked = []

while queue:
    person = queue.popleft()
    if not person in checked:
        if person == 'Skyler':
            print("You let that sink in")
            break
        else:
            queue += relations[person]
            checked.append(person)
