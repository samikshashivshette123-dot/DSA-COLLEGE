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

    def sort(self):
       temp = self.head
       while temp is not None and temp.next is not None:
            np = temp.next
            while np is not None:
                if temp.data > np.data:
                    t = temp.data
                    temp.data = np.data
                    np.data = t
                np = np.next
            temp = temp.next



    


   
    

# Main program

obj = Operations()

obj.create()

obj.display()
obj.sort()
obj.display()