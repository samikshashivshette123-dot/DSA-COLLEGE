class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo = []
        self.redo = []
    def change(self):
        new_text = input("\nEnter text: ")
        self.undo.append(self.text)# Save current text before changing
        self.text =self.text + new_text
        print("Text:", self.text)
    def undo_text(self):
        if len(self.undo) > 0:
            self.redo.append(self.text)
            self.text = self.undo.pop()
            print("Undo successful.")
        else:
            print("Nothing to undo.")
        print("Text:", self.text)
    def redo_text(self):
        if len(self.redo) > 0:
            self.undo.append(self.text)
            self.text = self.redo.pop()
            print("Redo successful.")
        else:
            print("Nothing to redo.")
        print("Text:", self.text)
editor = TextEditor()# Create object
while True:
    print("\n1.Add Text \n2.Undo \n3.Redo \n4.Display \n5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        editor.change()
    elif choice == "2":
        editor.undo_text()
    elif choice == "3":
        editor.redo_text()
    elif choice == "4":
        print("Text:", editor.text)
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice")