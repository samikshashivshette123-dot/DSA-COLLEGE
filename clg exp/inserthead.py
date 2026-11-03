class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Operations:
    def __init__(self):
        self.head = None

   
    def create(self):
        temp = None
        while True:
            val = int(input("Enter the Node data: "))
            new_node = Node(val)   # Create a new node
            if self.head is None:  	# First node
                self.head = new_node
                temp = self.head
            else:				# Other nodes
                temp.next = new_node
                temp = new_node
            ans = input("Do you want to enter more elements? (y/n): ")
            if ans != 'y' and ans != 'Y':
                break

    def display(self):
         temp = self.head
         if temp is None:
            print("Linked list is empty")
         else:
            while temp is not None:
                print("|", temp.data, "| --> ", end="")
                temp = temp.next
            print("None")
            
    def insert_head(self):
        val = int(input("Enter data in first node: "))
        new_node = Node(val) # Create a new node
        if self.head is None:    # If linked list is empty
            self.head = new_node
        else:        # If linked list already contains nodes
            new_node.next = self.head
            self.head = new_node

# Main program

obj = Operations()

obj.create()

obj.display()
obj.insert_head()
obj.display()