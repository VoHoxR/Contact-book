import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import os

def create_new_contact_book():
    # Get the number of existing contact books
    existing_files = [f for f in os.listdir() if f.startswith("contactbook") and f.endswith(".csv")]
    new_file_number = len(existing_files) + 1
    new_file_name = f"contactbook{new_file_number}.csv"
    
    # Create the new CSV file
    with open(new_file_name, 'w') as file:
        file.write("Name,Phone\n")  # Add headers to the CSV file
    
    messagebox.showinfo("Success", f"Created new contact book: {new_file_name}")
    add_new_contact(new_file_name)

def add_new_contact(file_name=None):
    if not file_name:
        existing_files = [f for f in os.listdir() if f.startswith("contactbook") and f.endswith(".csv")]
        if not existing_files:
            messagebox.showinfo("Info", "No contact books available.")
            return
        
        selected_file = simpledialog.askstring("Input", f"Enter the contact book number (1-{len(existing_files)}):")
        if selected_file and selected_file.isdigit() and 1 <= int(selected_file) <= len(existing_files):
            file_name = f"contactbook{selected_file}.csv"
        else:
            messagebox.showwarning("Warning", "Invalid contact book number.")
            return
    
    name = simpledialog.askstring("Input", "Enter contact name:")
    phone = simpledialog.askstring("Input", "Enter contact phone number:")
    
    if name and phone:
        with open(file_name, 'a') as file:
            file.write(f"{name},{phone}\n")
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and phone number cannot be empty.")

def view_contact_books():
    existing_files = [f for f in os.listdir() if f.startswith("contactbook") and f.endswith(".csv")]
    if not existing_files:
        messagebox.showinfo("Info", "No contact books available.")
        return
    
    selected_file = simpledialog.askstring("Input", f"Enter the contact book number (1-{len(existing_files)}):")
    if selected_file and selected_file.isdigit() and 1 <= int(selected_file) <= len(existing_files):
        file_name = f"contactbook{selected_file}.csv"
        show_file_content(file_name)
    else:
        messagebox.showwarning("Warning", "Invalid contact book number.")

def show_file_content(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    
    view_window = tk.Toplevel()
    view_window.title(f"Viewing {file_name}")
    
    text_area = scrolledtext.ScrolledText(view_window, wrap=tk.WORD, width=50, height=20)
    text_area.insert(tk.INSERT, content)
    text_area.config(state=tk.DISABLED)
    text_area.pack(pady=10, padx=10)

def main():
    root = tk.Tk()
    root.title("Contact Book Creator")
    
    create_button = tk.Button(root, text="Create New Contact Book", command=create_new_contact_book)
    create_button.pack(pady=20)
    
    view_button = tk.Button(root, text="View Contact Books", command=view_contact_books)
    view_button.pack(pady=20)
    
    add_contact_button = tk.Button(root, text="Add New Contact", command=add_new_contact)
    add_contact_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
