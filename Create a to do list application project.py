#Create a to do list application
task =["Clean the house", "Wash the Car", "Walk the Dog"]


def main():
    while True:
        try:
         print(""" 
              Welcome to your 'To-do list' Management. 
              Please make a selection: 
              
              1. Add a task
              2. Delete a task 
              3. View tasks
              4. Exit
              """)
         user_option = input("Select an option: ")
         if user_option == "1":
            new_task = input("add a new task: ")
            print("New task successfully added.")
            task.append(new_task)
            print(task)
         elif user_option == "2":
            delete_task = input("Select which task to delete: ")
            if delete_task not in task:
               print("Task not found.")
            else:
               print(task)
               print("Task succefully deleted")
               task.remove(delete_task)
               print(task) 
         elif user_option == "3":
            if len(task) == 0:
             print("No task found")
            else:
               print(task) 
         elif user_option == "4":
           print("Now exiting To-do list")
           break
         else:
          print("Invalid option") 
         if task != 0:
            print("this is gonna run anyway")
        finally:
         print("when ready, select again")


main()