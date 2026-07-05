
task = []
try:
    file = open("tasks.txt","r")
    for line in file:
        task.append(line.strip())

    file.close
except FileNotFoundError:
    pass
while True:
    print("=======TO-DO-LIST=======")
    print("1.Add task")
    print("2.View tasks")
    print("3.remove tasks")
    print("4.exit")
    
   
    choice = int(input("Please tell your choice :- "))

    if choice == 1:
        Add = input("Add the task:")
       
        task.append(Add)
        print(f"{Add} added sucessfully !")
        continue

    elif choice == 2:
        if len(task) == 0:
            print("No tasks found.")
        else:
            for number, i in enumerate(task,start=1):
                print(f"{number}.{i}")
        continue

    elif choice == 3 :
        if len(task) == 0:
            print("No tasks to remove.")
        else:
            for number, i in enumerate(task,start=1):
                print(f"{number}.{i}")
        delete = int( input("Tell which choice do you want to remove : "))
        delete = delete - 1

        if delete>=0 and delete < len(task):
            removed=task.pop(delete)
            print(f"{removed} removed sucessfully!")
        else:
            print("Invalid task number.")
            

    elif choice == 4:
        file=open("tatsks.txt","w")
        for i in task:
            file.write(i + "\n")

        file.close()
        
        print("Exiting the programme. Thank you for using :) ")
        break
   



