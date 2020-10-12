class TaskController:
    def __init__(self, tasks):
        self.tasks = tasks

    def get_tasks(self):
        return self.tasks

    def set_tasks(self, tasks):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def clear_tasks(self):
        self.tasks = []

    def delete_index(self, index):
        del self.tasks[int(index)]
