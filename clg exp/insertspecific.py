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

    def insert_Specific(self):
        val = int(input("Enter data for new node: "))
        key = int(input("Enter data of node after which to insert: "))

        new_node = Node(val)

        if self.head is None:  # If linked list is empty
            print("Linked list is empty")
            return

        temp = self.head

    # Find the node containing key
        while temp is not None and temp.data != key:
            temp = temp.next

    # Key not found
            if temp is None:
                print("Node not found")
                return

    # Insert new node after temp
        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted successfully")

     
    

# Main program

obj = Operations()

obj.create()

obj.display()

obj.insert_Specific()
obj.display()