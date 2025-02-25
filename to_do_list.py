print("To-Do List Manager")


def print_to_DO_list()->str:
	mark_box =[]
	removing =0
	task =[]
	number =0
	while True:
		print("""
1. Add a task
2. View task
3. Mark task as complete
4. Delete a task
5. Exit
""")
		option = input("Enter your choice: ")
		detail = ["1","2","3","4","5"]
		while option not in detail:
			print("invalid choice")
			option = input("Enter your choice: ")
	
		match option:
			case "1":
				result =input("enter the task: ")
				mark_box.append([])
				
				task.append(result)
				number= number +1
				print(number)
			
			case "2":
				for x in range(number):
					print(f"{x+1}. {mark_box[x]}  {task[x]}")
			
			case "3":
				for x in range(number):
					print(f"{x+1}. {mark_box[x]}  {task[x]}")
				complete = int(input("enter task completed: "))
				while complete > number  :
					print("no task here")
					complete = int(input("enter task completed: "))
				while complete == 0:
					print("no task here")
					complete = int(input("enter task completed: "))
				marking = complete-1
				mark_box[marking]="[x]"
				for x in range(number):
					print(f"{x+1}. {mark_box[x]}  {task[x]}")

				
				
			
			case "4":
				delete = int(input("task you wanna delete: "))
				while delete > number:
					print("no task here")
					delete = int(input("task you wanna delete: "))
				while delete <0:
					print("no task here")
					delete = int(input("task you wanna delete: "))

				deleting =  delete -1
				task.remove(task[deleting])
				number = number -1
				mark_box.pop(deleting)
				
				for x in range(number):
					print(f"{x+1}. {mark_box[x]}  {task[x]}")

			
			case "5":
				print("five")
				break


	return option



print_to_DO_list()
