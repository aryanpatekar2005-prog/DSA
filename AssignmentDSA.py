class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front == None or self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front
        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def dequeue(self):
        if self.front:
            print("Executed:", self.front.pid, self.front.name, "Priority:", self.front.priority)
            self.front = self.front.next
        else:
            print("Queue is empty")

    def display_next(self):
        if self.front:
            print("Next Process:", self.front.pid, self.front.name, "Priority:", self.front.priority)
        else:
            print("Queue is empty")

    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.pid, temp.name, "(Priority:", temp.priority, ")", end=" -> ")
            temp = temp.next
        print("None")

    def count(self):
        c = 0
        temp = self.front
        while temp:
            c += 1
            temp = temp.next
        print("Total Processes:", c)

pq = PriorityQueue()
pq.enqueue(node(101, "Chrome", 2))
pq.enqueue(node(102, "Backup", 4))
pq.enqueue(node(103, "Antivirus", 3))
pq.enqueue(node(104, "System_Boot", 1))

pq.display_all()
pq.count()
pq.display_next()

pq.dequeue()
pq.dequeue()

pq.display_all()
pq.count()