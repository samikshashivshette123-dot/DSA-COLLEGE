class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Operations:
    def __init__(self):
        self.head = None
        self.head1 = None

    # Create a linked list
    def create(self):
        head = None
        temp = None

        while True:
            val = int(input("Enter the Node data: "))
            new_node = Node(val)

            # First node
            if head is None:
                head = new_node
                temp = head
            else:
                # Other nodes
                temp.next = new_node
                temp = new_node

            ans = input("Do you want to enter more elements? (y/n): ")

            if ans != 'y' and ans != 'Y':
                break

        return head

    # Display a linked list
    def display(self, head):
        temp = head

        if temp is None:
            print("Linked list is empty")
        else:
            while temp is not None:
                print("|", temp.data, "| --> ", end="")
                temp = temp.next
            print("None")

    # Concatenate two linked lists
    def concatenate(self, head1, head2):
        if head1 is None:
            return head2

        temp = head1

        # Go to the last node of first list
        while temp.next is not None:
            temp = temp.next

        # Connect first list to second list
        temp.next = head2

        print("The lists are concatenated")
        return head1


# Main program

obj = Operations()

# Create first linked list
print("Enter elements for First Linked List:")
head = obj.create()

# Create second linked list
print("\nEnter elements for Second Linked List:")
head1 = obj.create()

# Display first list
print("\nFirst Linked List:")
obj.display(head)

# Display second list
print("Second Linked List:")
obj.display(head1)

# Concatenate both lists
head = obj.concatenate(head, head1)

# Display concatenated list
print("\nAfter Concatenation:")
obj.display(head)