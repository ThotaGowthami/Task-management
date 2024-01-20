import heapq

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, description, priority=0):
        task = (priority, self.task_counter, description)
        heapq.heappush(self.tasks, task)
        self.task_counter += 1
        print(f'Task added: {description}')

    def remove_task(self, task_id):
        new_tasks = [task for task in self.tasks if task[1] != task_id]
        if len(new_tasks) == len(self.tasks):
            print(f'Task with ID {task_id} not found.')
        else:
            self.tasks = new_tasks
            print(f'Task with ID {task_id} removed.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            for priority, task_id, description in self.tasks:
                print(f'{task_id}. {description} (Priority: {priority})')

    def prioritize_task(self, task_id, new_priority):
        for i, task in enumerate(self.tasks):
            if task[1] == task_id:
                updated_task = (new_priority, task[1], task[2])
                self.tasks[i] = updated_task
                print(f'Task {task_id} prioritized to {new_priority}.')
                return
        print(f'Task with ID {task_id} not found.')

    def recommend_task(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task[2].lower()]
        if not matching_tasks:
            print(f'No tasks found with keyword "{keyword}".')
        else:
            recommended_task = heapq.nlargest(1, matching_tasks)[0]
            print(f'Recommended task: {recommended_task[2]} (Priority: {recommended_task[0]})')

# Example usage:
task_manager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Prioritize Task")
    print("5. Get Task Recommendation")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (default is 0): "))
        task_manager.add_task(description, priority)
    elif choice == '2':
        task_id = int(input("Enter task ID to remove: "))
        task_manager.remove_task(task_id)
    elif choice == '3':
        task_manager.list_tasks()
    elif choice == '4':
        task_id = int(input("Enter task ID to prioritize: "))
        new_priority = int(input("Enter new priority: "))
        task_manager.prioritize_task(task_id, new_priority)
    elif choice == '5':
        keyword = input("Enter keyword for task recommendation: ")
        task_manager.recommend_task(keyword)
    elif choice == '6':
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
