class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Метод для строкового представления стека"""
        items = []
        current = self.top
        while current is not None:
            items.append(current.data)
            current = current.next_node
        return f"Stack: {', '.join(map(str, items))}"

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """Метод для удаления и возврата элемента с вершины стека"""
        if not self.is_empty():
            popped_data = self.top.data
            self.top = self.top.next_node
            return popped_data
        else:
            raise ValueError("Стек пуст")

    def is_empty(self):
        """Метод для проверки, пуст ли стек"""
        return self.top is None