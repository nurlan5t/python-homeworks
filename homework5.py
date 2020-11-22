from datetime import date

class Task:
    def __init__(self, name, status):
        self.date = date.today()
        self.name = name
        self.status = status

    def __str__(self):
        return f'{self.name} | {self.status} | {self.date}'

tasks = []

while True:
    print('1) + New task')
    print('2) Complete task')
    option = int(input('Select an option: '))
    if option == 1:
        name = input('Task name: ')
        status = 'not done'
        tasks.append(Task(name, status))

        for i in range(len(tasks)):
            print(i+1 ,tasks[i])

    if option == 2:
        number = int(input('Enter the number of the completed task: '))
        tasks[number-1][1] = "Done"

        for i in range(len(task+s)):
            print(i+1 ,tasks[i])