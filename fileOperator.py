class FileOperator:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        file = open(self.name, "r")
        lines = file.readlines()
        for line in lines:
            self.tasks.append(line)

    def clear_file(self):
        file = open(self.name, "w")
        file.write("")

    def save_file(self):
        self.clear_file()
        file = open(self.name, "a")
        for task in self.tasks:
            file.write(task + "\n")

    def get_content(self):
        return self.tasks

    def add_to_file(self, text):
        file = open(self.name, "a")
        file.write(text + "\n")

    def update_file(self, tasks):
        text = ""
        for item in tasks:
            text = text + item + '\n'
        self.clear_file()
        file = open(self.name, "w")
        file.write(text)