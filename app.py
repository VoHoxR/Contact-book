import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=20)

        self.create_button = tk.Button(self.menu_frame, text="Create a new contact book", command=self.create_contact_book)
        self.create_button.pack(fill='x')

        self.view_button = tk.Button(self.menu_frame, text="View current contact book", command=self.view_contact_book)
        self.view_button.pack(fill='x')

        self.edit_button = tk.Button(self.menu_frame, text="Edit current contact book", command=self.edit_contact_book)
        self.edit_button.pack(fill='x')

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=root.quit)
        self.exit_button.pack(fill='x')

    def create_contact_book(self):
        self.contacts = []
        while True:
            name = simpledialog.askstring("Input", "Enter contact name (or 'done' to finish):")
            if name is None or name.lower() == 'done':
                break
            phone = simpledialog.askstring("Input", "Enter contact phone number:")
            if phone is not None:
                self.contacts.append({'name': name, 'phone': phone})

    def view_contact_book(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contacts_str = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact Book", contacts_str)

    def edit_contact_book(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to edit.")
            return
        name_to_edit = simpledialog.askstring("Input", "Enter the name of the contact to edit:")
        for contact in self.contacts:
            if contact['name'] == name_to_edit:
                new_phone = simpledialog.askstring("Input", f"Enter new phone number for {name_to_edit}:")
                if new_phone is not None:
                    contact['phone'] = new_phone
                    messagebox.showinfo("Info", "Contact updated.")
                    return
        messagebox.showinfo("Info", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
