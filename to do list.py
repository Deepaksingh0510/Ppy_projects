def task():
    task_list=[]
    
    print("------WELCOME TO TO DO LIST------")
    total_task=int(input("Enter the no of task you want to  add to your task list: "))
    for i in range(1,total_task+1):
        task_name=input(f"{i} :- ")
        
        task_list.append(task_name)
    print(f"Today task  are:-{task_list} ")

    while True:
        try:
            operation=int(input(f"You can Enter\n1:-ADD\n2:-UPDATE\n3:-DELETE\n4:-VIEW\n5:-EXIT\n"))
            
            if operation == 1:
                new_task=input("Enter the task you want to add:- ")
                task_list.append(new_task)
                print(f"{new_task} has been added to the task list sucessfully...")
            
            elif operation == 2:
                updated_val=input("Enter the Task name you want to update: ") 
                if updated_val in task_list:
                    up=input("Enter  new task : ")
                    ind = task_list.index(updated_val) 
                    task_list[ind]=up
                    print(f"'{updated_val}' is been updated with '{up}'")
                    
            elif operation == 3:
                rem=input("Which task you want to Delete from the list: ")
                # if rem in task_list:
                #     no=task_list.index(rem)
                #     del task_list[no]
                #     print(f"{rem} is been removed successfully....")
                                #   OR
                if rem in task_list:
                    task_list.remove(rem)
                    print(f"{rem} is been removed successfully....")
                
                else:  
                    print(f"'{rem}' is not present in the list")
                
                    
            elif operation== 4:
                print(task_list)
                
            elif operation==5:
                break
   
        except:
            
            print("Invalid input")
task()