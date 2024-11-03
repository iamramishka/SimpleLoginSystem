import tkinter as tk
from tkinter import messagebox
user_db = {}

def center_window(window, width=400, height=350):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Making the Login Window Panel
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Making the SignUp Window Panel
def signup():
    name = name_entry.get()
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not name or not new_username or not new_password:
        messagebox.showerror("Signup Failed", "Please enter all fields")
        return
    if new_username in user_db:
        messagebox.showerror("Signup Failed", "Username already exists")
        return
    if new_password != confirm_password:
        messagebox.showerror("Signup Failed", "Passwords do not match")
        return

    user_db[new_username] = new_password
    messagebox.showinfo("Signup Successful", f"Account Created! Welcome, {name}")
    signup_window.destroy()

def toggle_password(entry, toggle_button):
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text='Hide')
    else:
        entry.config(show='*')
        toggle_button.config(text='Show')

def open_signup_window():
    global signup_window, name_entry, new_username_entry, new_password_entry, confirm_password_entry

    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    center_window(signup_window, 400, 350)
 
    tk.Label(signup_window, text="Create a New Account", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=(10, 20))

    tk.Label(signup_window, text="Name").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    name_entry = tk.Entry(signup_window, width=25)
    name_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")

    tk.Label(signup_window, text="New Username").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    new_username_entry = tk.Entry(signup_window, width=25)
    new_username_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")

    tk.Label(signup_window, text="New Password").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    new_password_entry = tk.Entry(signup_window, show="*", width=22)  
    new_password_entry.grid(row=3, column=1, pady=5, sticky="w")
    toggle_button = tk.Button(signup_window, text="Show", command=lambda: toggle_password(new_password_entry, toggle_button))
    toggle_button.grid(row=3, column=2, padx=5)

    tk.Label(signup_window, text="Confirm Password").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    confirm_password_entry = tk.Entry(signup_window, show="*", width=22)  
    confirm_password_entry.grid(row=4, column=1, pady=5, sticky="w")
    confirm_toggle_button = tk.Button(signup_window, text="Show", command=lambda: toggle_password(confirm_password_entry, confirm_toggle_button))
    confirm_toggle_button.grid(row=4, column=2, padx=5)

    # Signup button
    signup_button = tk.Button(signup_window, text="Signup", command=signup)
    signup_button.grid(row=5, column=0, columnspan=3, pady=(20, 10))

root = tk.Tk()
root.title("Login System")
center_window(root, 400, 250)

tk.Label(root, text="Login", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=(10, 20))

tk.Label(root, text="Username").grid(row=1, column=0, sticky="e", padx=10, pady=5)
username_entry = tk.Entry(root, width=25)
username_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Password").grid(row=2, column=0, sticky="e", padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=22)  # Adjust width for alignment with button
password_entry.grid(row=2, column=1, pady=5, sticky="w")
toggle_button_login = tk.Button(root, text="Show", command=lambda: toggle_password(password_entry, toggle_button_login))
toggle_button_login.grid(row=2, column=2, padx=5)


button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=(10, 5))

signup_button = tk.Button(button_frame, text="Create Account", command=open_signup_window)
signup_button.pack(side="left", padx=5)

login_button = tk.Button(button_frame, text="Login", command=login)
login_button.pack(side="left", padx=5)

root.mainloop()
