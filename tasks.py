task_list=[]
end = False
while end != True:
    task_item = str(input("Task: "))
    if task_item not in ["end", "stop","leave"]:
        task_list.append(task_item)
        print(task_list)
    else:
        end = True
        break