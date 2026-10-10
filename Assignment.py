class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, data):
        """Helper method to easily populate the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        elements.append("None")
        print(" -> ".join(elements))

    def insert(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        current_pos = 1
        
        while temp and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
            
        if not temp:
            print(f"Error: Position {pos} out of bounds.")
            return
            
        new_node.next = temp.next
        temp.next = new_node

    def find_middle(self):
        if not self.head:
            print("List is empty.")
            return
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        print(f"Middle node value: {slow.data}")

    def delete(self, pos):
        if not self.head:
            print("List is empty.")
            return
            
        if pos == 1:
            self.head = self.head.next
            return
            
        temp = self.head
        current_pos = 1
        
        while temp and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
            
        if not temp or not temp.next:
            print(f"Error: Position {pos} out of bounds.")
            return
            
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current           
            current = next_node       
            
        self.head = prev             

    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sums.")
            return
            
        temp = self.head
        sums = []
        
        while temp and temp.next:
            pair_sum = temp.data + temp.next.data
            sums.append(str(pair_sum))
            temp = temp.next  
            
        print("Consecutive sums: " + ", ".join(sums))


if __name__ == "__main__":
    llist = LinkedList()
    
    print("1. Creating List and Appending Data:")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.display()
    
    print("\n3. Inserting '25' at position 3:")
    llist.insert(25, 3)
    llist.display()
    
    print("\n4. Finding the Middle Node:")
    llist.find_middle()
    
    print("\n5. Deleting node at position 4 (value 30):")
    llist.delete(4)
    llist.display()
    
    print("\n6. Reversing the List:")
    llist.reverse()
    llist.display()
    
    print("\n7. Calculating sum of every two consecutive nodes:")
    llist.sum_consecutive()