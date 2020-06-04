class Stack:

    def __init__(self):
        self.current_index = -1
        self.elements = []

    def push(self, element):
        self.current_index += 1
        self.elements.insert(self.current_index, element)

    def pop(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        self.current_index -= 1
        return self.elements[self.current_index + 1]

    def peek(self):
        if self.is_empty():
            print('Stack is empty!')
            return None
        return self.elements[self.current_index]

    def is_empty(self):
        return self.current_index == -1
