# Стек
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def new_task(self, task, priority):
        self.stack.push((task, priority))

    def remove_task(self, task):
        for i in range(len(self.stack.stack)):
            if self.stack.stack[i][0] == task:
                self.stack.stack.pop(i)
                break

    def __str__(self):
        sorted_stack = sorted(self.stack.stack, key=lambda x: x[1])
        result = ""
        for i in range(len(sorted_stack)):
            result += f"{sorted_stack[i][1]} — {sorted_stack[i][0]}\n"
        return result

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)