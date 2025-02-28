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
        # If no file name is provided, prompt the user to select an existing contact book
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
    
    # Get the number of existing contacts in the selected contact book
    with open(file_name, 'r') as file:
        lines = file.readlines()
    new_contact_number = len(lines)
    
    # Prompt the user to enter the contact's name and phone number
    name = simpledialog.askstring("Input", "Enter contact name:")
    phone = simpledialog.askstring("Input", "Enter contact phone number:")
    
    if name and phone:
        # Append the new contact to the selected contact book
        with open(file_name, 'a') as file:
            file.write(f"contact {new_contact_number},{name},{phone}\n")
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and phone number cannot be empty.")

def view_contact_books():
    # Get the list of existing contact books
    existing_files = [f for f in os.listdir() if f.startswith("contactbook") and f.endswith(".csv")]
    if not existing_files:
        messagebox.showinfo("Info", "No contact books available.")
        return
    
    # Prompt the user to select a contact book to view
    selected_file = simpledialog.askstring("Input", f"Enter the contact book number (1-{len(existing_files)}):")
    if selected_file and selected_file.isdigit() and 1 <= int(selected_file) <= len(existing_files):
        file_name = f"contactbook{selected_file}.csv"
        show_file_content(file_name)
    else:
        messagebox.showwarning("Warning", "Invalid contact book number.")

def show_file_content(file_name):
    # Read the content of the selected contact book
    with open(file_name, 'r') as file:
        content = file.read()
    
    # Create a new window to display the content of the contact book
    view_window = tk.Toplevel()
    view_window.title(f"Viewing {file_name}")
    
    # Create a scrolled text area to display the content
    text_area = scrolledtext.ScrolledText(view_window, wrap=tk.WORD, width=50, height=20)
    text_area.insert(tk.INSERT, content)
    text_area.config(state=tk.DISABLED)
    text_area.pack(pady=10, padx=10)

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Contact Book Creator")
    
    # Create a button to create a new contact book
    create_button = tk.Button(root, text="Create New Contact Book", command=create_new_contact_book)
    create_button.pack(pady=20)
    
    # Create a button to view existing contact books
    view_button = tk.Button(root, text="View Contact Books", command=view_contact_books)
    view_button.pack(pady=20)
    
    # Create a button to add a new contact to an existing contact book
    add_contact_button = tk.Button(root, text="Add New Contact", command=add_new_contact)
    add_contact_button.pack(pady=20)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
