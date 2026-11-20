class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      new_node.next = self.head  # Points to itself
      return

    temp = self.head
    while temp.next != self.head:
      temp = temp.next
    temp.next = new_node
    new_node.next = self.head  # Connects last node back to head

  def display(self):
    if not self.head:
      print("List is empty.")
      return

    temp = self.head
    elements = []
    while True:
      elements.append(str(temp.data))
      temp = temp.next
      if temp == self.head:
        break
    print(" -> ".join(elements) + " -> (back to head)")

  def insert(self, data, pos):
    new_node = Node(data)
    if pos == 1:
      if not self.head:
        self.head = new_node
        new_node.next = self.head
        return

      # Find last node to update its pointer
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      new_node.next = self.head
      temp.next = new_node
      self.head = new_node
      return

    temp = self.head
    current_pos = 1

    while current_pos < pos - 1:
      temp = temp.next
      current_pos += 1
      if temp == self.head:
        print(f"Error: Position {pos} out of bounds.")
        return

    new_node.next = temp.next
    temp.next = new_node

  def find_middle(self):
    if not self.head:
      print("List is empty.")
      return

    # Count total nodes safely in a circular list
    temp = self.head
    count = 0
    while True:
      count += 1
      temp = temp.next
      if temp == self.head:
        break

    # Find the middle node
    mid_index = count // 2
    temp = self.head
    for _ in range(mid_index):
      temp = temp.next

    print(f"Middle node value: {temp.data}")

  def delete(self, pos):
    if not self.head:
      print("List is empty.")
      return

    if pos == 1:
      # If only one node exists
      if self.head.next == self.head:
        self.head = None
        return

      # Find the last node to update its pointer
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = self.head.next
      self.head = self.head.next
      return

    temp = self.head
    current_pos = 1

    while current_pos < pos - 1:
      temp = temp.next
      current_pos += 1
      if temp == self.head:
        print(f"Error: Position {pos} out of bounds.")
        return

    if temp.next == self.head:
      print(f"Error: Position {pos} out of bounds.")
      return

    temp.next = temp.next.next


if __name__ == "__main__":
  llist = LinkedList()

  print("Creating List and Appending Data:\n")
  llist.append(10)
  llist.append(20)
  llist.append(30)
  llist.append(40)

  llist.display()
  llist.delete(2)
  llist.display()

  llist.find_middle()
  llist.display()