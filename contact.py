import tkinter as tk
from tkinter import ttk, messagebox
import re  # Regular expressions for validation

# A simple dictionary to store contacts
contacts = {}

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to validate phone number (basic validation)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10  # Assuming a 10-digit phone number

# Function to add a new contact with validation
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or name == "Enter name...":
        messagebox.showwarning("Input Error", "Name is required!")
        return
    
    if not phone or phone == "Enter phone number...":
        messagebox.showwarning("Input Error", "Phone number is required!")
        return

    if not is_valid_phone(phone):
        messagebox.showwarning("Input Error", "Invalid phone number! Must be 10 digits.")
        return

    if email and email != "Enter email..." and not is_valid_email(email):
        messagebox.showwarning("Input Error", "Invalid email address!")
        return

    contacts[name] = {'phone': phone, 'email': email if email != "Enter email..." else "", 'address': address if address != "Enter address..." else ""}
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    display_contacts()

# Function to display the contact list
def display_contacts():
    for item in contact_tree.get_children():
        contact_tree.delete(item)
    for name, details in contacts.items():
        contact_tree.insert("", tk.END, values=(name, details['address'], details['email'], details['phone']))

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    for item in contact_tree.get_children():
        contact_tree.delete(item)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            contact_tree.insert("", tk.END, values=(name, details['address'], details['email'], details['phone']))
            return
    messagebox.showinfo("Not Found", "No contact found!")

# Function to clear the entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "Enter name...")
    name_entry.config(fg="grey")
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, "Enter phone number...")
    phone_entry.config(fg="grey")
    email_entry.delete(0, tk.END)
    email_entry.insert(0, "Enter email...")
    email_entry.config(fg="grey")
    address_entry.delete(0, tk.END)
    address_entry.insert(0, "Enter address...")
    address_entry.config(fg="grey")

# Function to handle placeholders in entry fields
def on_entry_click(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black")

def on_focusout(event, placeholder):
    if event.widget.get() == "":
        event.widget.insert(0, placeholder)
        event.widget.config(fg="grey")

# Function to exit the application
def exit_application():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
style.configure("TButton.TButton", font=("Arial", 12), background="#007ACC", foreground="black", padding=6)  # Set text color to black
style.configure("TEntry", font=("Arial", 12), foreground="black")  # Set entry text color to black

# Create a frame for the form fields and buttons
form_frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
form_frame.pack(pady=10, padx=10, fill="x")

# Labels and entry fields for contact details
ttk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
name_entry = tk.Entry(form_frame, font=("Arial", 12), fg="grey")
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.insert(0, "Enter name...")
name_entry.bind('<FocusIn>', lambda event: on_entry_click(event, "Enter name..."))
name_entry.bind('<FocusOut>', lambda event: on_focusout(event, "Enter name..."))

ttk.Label(form_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="W")
phone_entry = tk.Entry(form_frame, font=("Arial", 12), fg="grey")
phone_entry.grid(row=1, column=1, padx=5, pady=5)
phone_entry.insert(0, "Enter phone number...")
phone_entry.bind('<FocusIn>', lambda event: on_entry_click(event, "Enter phone number..."))
phone_entry.bind('<FocusOut>', lambda event: on_focusout(event, "Enter phone number..."))

ttk.Label(form_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="W")
email_entry = tk.Entry(form_frame, font=("Arial", 12), fg="grey")
email_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.insert(0, "Enter email...")
email_entry.bind('<FocusIn>', lambda event: on_entry_click(event, "Enter email..."))
email_entry.bind('<FocusOut>', lambda event: on_focusout(event, "Enter email..."))

ttk.Label(form_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="W")
address_entry = tk.Entry(form_frame, font=("Arial", 12), fg="grey")
address_entry.grid(row=3, column=1, padx=5, pady=5)
address_entry.insert(0, "Enter address...")
address_entry.bind('<FocusIn>', lambda event: on_entry_click(event, "Enter address..."))
address_entry.bind('<FocusOut>', lambda event: on_focusout(event, "Enter address..."))

# Buttons for adding, searching, and clearing contacts
add_button = ttk.Button(form_frame, text="Add Contact", command=add_contact, style="TButton")
add_button.grid(row=4, column=0, padx=5, pady=10, sticky="W")

search_button = ttk.Button(form_frame, text="Search", command=search_contact, style="TButton")
search_button.grid(row=4, column=1, padx=5, pady=10, sticky="E")

# Search field
search_entry = tk.Entry(form_frame, font=("Arial", 12), fg="grey")
search_entry.grid(row=5, column=1, padx=5, pady=5)
search_entry.insert(0, "Search by name or phone...")
search_entry.bind('<FocusIn>', lambda event: on_entry_click(event, "Search by name or phone..."))
search_entry.bind('<FocusOut>', lambda event: on_focusout(event, "Search by name or phone..."))

# Create a Treeview widget to display the contacts
columns = ("Name", "Address", "Email", "Phone")
contact_tree = ttk.Treeview(root, columns=columns, show="headings")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Address", text="Address")
contact_tree.heading("Email", text="Email")
contact_tree.heading("Phone", text="Phone")
contact_tree.pack(pady=20, padx=10, fill="both", expand=True)

# Add an Exit button at the bottom of the window
exit_button = ttk.Button(root, text="Exit", command=exit_application, style="TButton")
exit_button.pack(pady=10)

# Run the application
root.mainloop()
