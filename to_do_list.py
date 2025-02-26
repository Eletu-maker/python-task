print("To-Do List Manager")

def add_task(task,mark_box,number):
	result =input("enter the task: ")
	mark_box.append("[]")
	task.append(result)
	number += 1
	print("task added")
	print(number)
	return number

def view_task(number,mark_box,task):
	if number == 0:
		print("no task added yet")
	else:
		for nom in range(number):
			print(f"{nom+1}. {mark_box[nom]}  {task[nom]}")

def mark_task(number,mark_box,task):
	if number == 0:
		print("no task added yet")
	else:
		for nom in range(number):
			print(f"{nom+1}. {mark_box[nom]}  {task[nom]}")
		complete = int(input("enter task completed: "))
		while complete > number  :
			print("no task here")
			complete = int(input("enter task completed: "))
				
		marking = complete-1
		mark_box[marking]="[x]"
		for nom in range(number):
			print(f"{nom+1}. {mark_box[nom]}  {task[nom]}")

def delete_task(number,mark_box,task):
	if number == 0:
		print("no task added yet")
	else:
		delete = int(input("task you wanna delete: "))
		while delete > number:
			print("no task here")
			delete = int(input("task you wanna delete: "))
		deleting =  delete -1
		task.remove(task[deleting])
		number = number -1
		mark_box.pop(deleting)
				
		for nom in range(number):
			print(f"{nom+1}. {mark_box[nom]}  {task[nom]}")
	return number
		


def print_to_DO_list():
	mark_box =[]
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
		detail = [1,2,3,4,5]
		while option not in detail:
			print("invalid choice")
			option = input("Enter your choice: ")
	
		match option:
			case 1:
				number = add_task(task,mark_box,number)			
			case 2:
				view_task(number,mark_box,task)
			
			case 3:
				mark_task(number,mark_box,task)

				
				
			
			case 4:
				number = delete_task(number,mark_box,task)

			
			case 5:
				print("goodBye")
				break


	return option



print_to_DO_list()
