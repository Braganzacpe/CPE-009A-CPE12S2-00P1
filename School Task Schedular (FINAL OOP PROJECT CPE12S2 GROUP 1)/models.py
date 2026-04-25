class Task:
    def __init__(self, name, deadline, owner):
        self.name     = name
        self.deadline = deadline
        self.done_by  = set()
        self.owner    = owner

class Day:
    def __init__(self):
        self.day   = 0
        self.tasks = []
