# Односвязный список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get(self, index):
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next
        raise ValueError('Index out of range')

    def remove(self, index):
        current_node = self.head
        current_index = 0
        if index == 0:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_index != index:
            previous_node = current_node
            current_node = current_node.next
            current_index += 1
        if current_node is None:
            raise ValueError('Index out of range')
        previous_node.next = current_node.next
        current_node = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __str__(self):
        return '[' + ' '.join(str(item) for item in self) + ']'

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)