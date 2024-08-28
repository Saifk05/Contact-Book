This Python code implements a contact book application using the Tkinter library to create a graphical user interface (GUI). The contact book allows users to add, search, and display contacts, with basic validation for phone numbers and email addresses. The contacts are stored in a simple dictionary, and the GUI provides a user-friendly interface to interact with the data. Here's a detailed breakdown of the code:

1. Importing Libraries:
tkinter and ttk: Tkinter is used for creating the GUI components, and ttk is used for themed widgets.
re: Regular expressions are used to validate email addresses.
2. Contact Storage:
contacts: A dictionary is used to store contact details, where the keys are contact names, and the values are dictionaries containing phone numbers, emails, and addresses.
3. Validation Functions:
is_valid_email(email): This function checks if the entered email address matches a basic email pattern using regular expressions.
is_valid_phone(phone): This function checks if the phone number contains only digits and is 10 digits long.
4. Adding a Contact - add_contact():
This function retrieves user input from the entry fields (name, phone, email, and address).
It performs validation checks on the inputs:
Name and phone number are required.
The phone number must be valid (10 digits).
If provided, the email address must be valid.
If the input passes validation, the contact is added to the contacts dictionary.
The function then clears the entry fields and updates the displayed contact list using display_contacts().
5. Displaying Contacts - display_contacts():
This function clears the existing rows in the Treeview widget and then iterates through the contacts dictionary to insert each contact's details into the Treeview for display.
6. Searching for a Contact - search_contact():
This function searches the contacts by name or phone number based on the user's input in the search field.
If a match is found, it displays the contact details in the Treeview.
If no match is found, a messagebox informs the user.
7. Clearing Entry Fields - clear_entries():
This function clears the content of the entry fields and resets the placeholder text with greyed-out text to guide the user.
8. Handling Entry Field Placeholders:
on_entry_click(event, placeholder): This function removes the placeholder text when the user clicks on an entry field.
on_focusout(event, placeholder): This function restores the placeholder text if the entry field is left empty after losing focus.
9. Exiting the Application - exit_application():
This function closes the application by calling root.quit().
10. Creating the Main Window:
root = tk.Tk(): Initializes the main application window.
root.title("Contact Book"): Sets the window title.
root.geometry("500x600"): Sets the window size.
root.configure(bg="#f0f0f0"): Configures the background color of the window.
11. Styling the GUI:
ttk.Style(): Configures styles for labels, buttons, and entry fields, such as font size, padding, and background colors.
12. Form Fields and Buttons:
Form Fields: Entry fields for the user's input (name, phone, email, and address) are created with placeholder text. Labels are added next to each entry field.
Buttons:
Add Contact: Calls add_contact() to add a new contact.
Search: Calls search_contact() to search for a contact by name or phone number.
Exit: Closes the application.
13. Displaying Contacts - Treeview:
A Treeview widget is used to display the list of contacts in a tabular format with columns for name, address, email, and phone.
14. Running the Application:
root.mainloop(): This line starts the Tkinter event loop, making the application responsive to user actions.
15. User Interaction:
Users can add contacts by filling in the form fields and clicking the "Add Contact" button.
Users can search for specific contacts by entering a name or phone number in the search field and clicking the "Search" button.
The contact list is displayed in a tabular format, and users can exit the application by clicking the "Exit" button.
