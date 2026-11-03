class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    # Insert a key and value
    def insert(self, key, value):
        index = key % self.size
        self.table[index].append([key, value])
        print("Inserted:", key, value)

    # Search for a key
    def search(self, key):
        index = key % self.size

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return "The key not Found which you want to search"

    # Delete a key
    def delete(self, key):
        index = key % self.size

        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                print("the Key is Deleted:", key)
                return

        print("Key not found")

    # Display the table
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Create hash table
ht = HashTable(10)

# Insert values
ht.insert(15, "Apple")
ht.insert(25, "Banana")
ht.insert(35, "Cherry")

# Display
print("\nHash Table:")
ht.display()

# Search
print("Search 25:", ht.search(25))

# Delete
ht.delete(25)

# Search again
print("Search 25:", ht.search(25))

# Display
print("\nHash Table:")
ht.display()