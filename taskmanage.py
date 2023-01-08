from datetime import datetime
import uuid


class Task:
    tasks = []

    def __init__(self, name) -> None:
        self.name = name
        self.created_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.updated_time = "NA"
        self.completed_time = "NA"
        self.task_done = False
        self.id = uuid.uuid4()
        Task.tasks.append(self)

    def __repr__(self):
        return f"ID = {self.id} \nTask = {self.name} \nCreated Time = {self.created_time} \nUpdated Time = {self.updated_time} \nCompleted = {self.task_done} \nCompleted Time = {self.completed_time}"

    def updateTask(self, id):
        z = False
        for task in Task.tasks:
            if id == task.id:
                newName = input("Enter Updated Task Name : ")
                task.name = newName
                task.updated_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                z = True
        if z:
            print("\nTask Updated Successfully.\n")

    def completeTask(self, id):
        for task in Task.tasks:
            if id == task.id:
                task.task_done = True
                task.completed_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def showAllTask(self):
        if len(Task.tasks):
            for task in Task.tasks:
                print(task)
                print('\n')
        else:
            print("Thare is No task.\n")

    def showIncompleteTask(self):
        y = False
        for task in Task.tasks:
            if task.task_done == False:
                print(task)
                print()
                y = True
        if y == False:
            print("Thare is No Incomplete Task.\n")

    def showCompletedTask(self):
        y = False
        for task in Task.tasks:
            if task.task_done == True:
                print(task)
                print()
                y = True
        if y == False:
            print("Thare is No Completed Task.\n")


instruction = "1. Add New Task\n2. Show All Task\n3. Show Incomplete Tasks\n4. Show Complete Tasks\n5. Update Task\n6. Make A Task Completed\n7. Exit"

while True:
    print(instruction)
    option = int(input("Enter Option : "))
    if option == 1:
        name = input("Enter New Task Name : ")
        a = Task(name)
        print("\nTask Created Successfully.\n")
    elif option == 2:
        print("")
        a.showAllTask()
    elif option == 3:
        print("")
        a.showIncompleteTask()
    elif option == 4:
        print('')
        a.showCompletedTask()
    elif option == 5:
        print("Select Which Task to Update\n\n")
        incompletes = []
        count = 1
        for task in a.tasks:
            if task.task_done == False:
                print(f"Task No = {count}")
                count = count + 1
                print(task)
                incompletes.append(task.id)
                print("\n")
        select = int(input("Enter Task Number : "))
        a.updateTask(incompletes[select-1])

    elif option == 6:
        print("Select Which Task You Want to Complete\n\n")
        completes = []
        number = 1
        isUncomplete = False
        for task in a.tasks:
            if task.task_done == False:
                isUncomplete = True
                print(f"Task No = {number}")
                number = number + 1
                print(task)
                completes.append(task.id)
                print("\n")

        if isUncomplete:
            elect = int(input("Enter Task Number : "))
            a.completeTask(completes[elect-1])
        else:
            print("\nThere are no Task to Complete\n")
    else:
        break
