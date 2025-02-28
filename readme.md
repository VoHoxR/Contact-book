
# Contact Book Application

## Overview
This application allows users to create and manage contact books using a graphical user interface built with Tkinter. Users can create new contact books, add contacts, and view existing contact books.

## Features
### 1. Create New Contact Book
- Users can create a new contact book.
- The new contact book is saved as a CSV file named `contactbook[num].csv`, where `[num]` is the next available number.
- The CSV file includes headers: `Name` and `Phone`.

### 2. Add New Contact
- Users can add new contacts to an existing contact book.
- Contacts are labeled as "contact 1", "contact 2", etc.
- The user is prompted to enter the contact's name and phone number.
- The new contact is appended to the selected contact book.

### 3. View Contact Books
- Users can view the contents of existing contact books.
- The user is prompted to select a contact book by entering its number.
- The selected contact book is displayed in a new window with a scrolled text area.

## Usage
1. Run the application.
2. Use the buttons to create a new contact book, add new contacts, or view existing contact books.
3. Follow the prompts to enter the required information.

## Code Summary
- `create_new_contact_book()`: Creates a new contact book CSV file.
- `add_new_contact(file_name=None)`: Adds a new contact to the specified or selected contact book.
- `view_contact_books()`: Prompts the user to select a contact book to view.
- `show_file_content(file_name)`: Displays the content of the selected contact book in a new window.
- `main()`: Sets up the main application window and buttons, and starts the Tkinter event loop.

# NOTE: AI DID EVERYTHING!!!!! <--(except for this)