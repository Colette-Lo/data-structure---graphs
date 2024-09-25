class Stack:
  def __init__(self):
    self.stack_array = []

  def push(self, new_item):
      self.stack_array.append(new_item)

  def pop(self):
    if len(self.stack_array) != 0:
      self.stack_array.pop()

  def get_size(self):
      return len(self.stack_array)

