class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash(self, key):      # Hash function
        return key % self.size
    def insert(self, key):     # Insert a key
        index = self.hash(key)
        while self.table[index] is not None:  # Linear probing
            index = (index + 1) % self.size
        self.table[index] = key
        print("Key inserted successfully.")
    def search(self, key):  # Search a key
        index = self.hash(key)
        for i in range(self.size):
            if self.table[index] == key:
                print("Key found.")
                return
            index = (index + 1) % self.size
        print("Key not found.")
    def delete(self, key): # Search a key
        index = self.hash(key)
        for i in range(self.size):
            if self.table[index] == key:
                self.table[index] = "DELETED"
                print("Key deleted.")
                return
            index = (index + 1) % self.size
        print("Key not found.")
    def display(self):# Display hash table
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])
# Main program
size = int(input("Enter size of hash table: "))
h = HashTable(size)
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = int(input("Enter key: "))
        h.insert(key)
    elif choice == 2:
        key = int(input("Enter key: "))
        h.search(key)
    elif choice == 3:
        key = int(input("Enter key: "))
        h.delete(key)
    elif choice == 4:
        h.display()
    elif choice == 5:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")