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

    def insert_last(self):
        val = int(input("Enter data in last node: "))
        new_node = Node(val) # Create a new node
        new_node.next = None
        if self.head is None: # If linked list is empty
            self.head = new_node
        else: # If linked list already contains nodes
            temp = self.head
            while temp.next is not None:# Traverse to the last node
               	temp = temp.next
            temp.next = new_node  # Attach new node at the end
     
    

# Main program

obj = Operations()

obj.create()

obj.display()

obj.insert_last()
obj.display()