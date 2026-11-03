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

    def delete_last(self):
    # Check if linked list is empty
        if self.head is None:
            print("Linked list is empty")
            return

    # If there is only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the last node
        temp = self.head
    
        while temp.next is not None:
            prev = temp
            temp = temp.next

    # Remove the last node
        prev.next = None

   
    

# Main program

obj = Operations()

obj.create()

obj.display()