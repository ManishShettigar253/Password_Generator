import tkinter as tk
from tkinter import messagebox
import random
from pymongo import MongoClient
import tkinter.font as tkFont

# Function to generate a password
def generate_password():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specialchars = "~@#$%^&*()_+-,./;'[]\\|<>:?"

    length = 8
    use_for = lowercase + uppercase + numbers + specialchars

    password = "".join(random.sample(use_for, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to submit details to MongoDB
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty")
        return
    
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Users"]
    collection = db["User"]
    
    # Insert data into MongoDB
    user_data = {
        "username": username,
        "password": password
    }
    
    collection.insert_one(user_data)
    messagebox.showinfo("Success", "Form Submitted Successfully")
    client.close()

# Function to toggle the visibility of the password
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

# Setting up the GUI window
root = tk.Tk()
root.title("User Registration")
root.geometry("400x300")

# Setting custom fonts
heading_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=12)

# Adding a heading
heading = tk.Label(root, text="USER REGISTRATION", font=heading_font)
heading.pack(pady=10)

# Adding username label and entry on the same line
username_frame = tk.Frame(root)
username_frame.pack(pady=5)
lblUsername = tk.Label(username_frame, text="Username:", font=label_font)
lblUsername.pack(side=tk.LEFT)
username_entry = tk.Entry(username_frame, width=30)
username_entry.pack(side=tk.LEFT, padx=5)

# Adding password label, entry, generate button, and show/hide button on the same line
password_frame = tk.Frame(root)
password_frame.pack(pady=5)
lblPassword = tk.Label(password_frame, text="Password:", font=label_font)
lblPassword.pack(side=tk.LEFT)
password_entry = tk.Entry(password_frame, width=30, show="*")
password_entry.pack(side=tk.LEFT, padx=5)
generate_button = tk.Button(password_frame, text="Generate Password", font=label_font, command=generate_password)
generate_button.pack(side=tk.LEFT, padx=5)
show_password = tk.Checkbutton(password_frame, text="Show", command=toggle_password)
show_password.pack(side=tk.LEFT, padx=5)

# Adding a button to submit the form
register_button = tk.Button(root, text="Register", font=heading_font, command=register_user)
register_button.pack(pady=20)

# Running the GUI application
root.mainloop()
