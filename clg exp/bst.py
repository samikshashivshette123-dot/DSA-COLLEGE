class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Searching
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Find minimum value
    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    # Deletion
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Display (Inorder Traversal)
    def display(self, root):
        if root:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)


# Main Program
tree = BST()

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        tree.root = tree.insert(tree.root, data)
        print("Node inserted successfully.")

    elif choice == 2:
        data = int(input("Enter value to delete: "))
        tree.root = tree.delete(tree.root, data)
        print("Node deleted successfully.")

    elif choice == 3:
        data = int(input("Enter value to search: "))
        result = tree.search(tree.root, data)

        if result:
            print("Element found.")
        else:
            print("Element not found.")

    elif choice == 4:
        print("BST elements (Inorder): ", end="")
        tree.display(tree.root)

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")