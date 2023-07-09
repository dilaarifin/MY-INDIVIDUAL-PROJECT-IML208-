from tkinter import *
from tkinter import messagebox

def login_success():
    messagebox.showinfo("Login Successful", "Welcome, Admin!")
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    window.destroy()  # Close the login window

def login():
    user = username.get()
    code = password.get()

    if user == "Admin" and code == "Password":
        login_success()
        import student
        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        prompt_try_again()
        
def prompt_try_again():
    result = messagebox.askretrycancel("Try Again", "Do you want to try again?")
    if result == True:
        username_entry.focus_set()  # Set focus back to username entry field
    else:
        window.destroy()  # Close the login window

# Create the main window
window = Tk()
window.title("Welcome to Gotham School: Student Management System")
window.iconbitmap("icons/student.ico")
window.geometry("490x230")
window.resizable(False,False)
window.configure(bg="cornsilk4",relief='sunken', borderwidth=4)  

# Set the window size
window_width = 490
window_height = 230

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the username label and entry field
login_label = Label(window, text="LOG IN", font=("Times", 30, "bold"), bg="cornsilk3")
login_label.pack(padx=20,pady=10)

username_label = Label(window, text="Username:", font=(10), bg="cornsilk3")
username_label.pack(padx=5,pady=2)
username = StringVar()  # Create a StringVar for the username
username_entry = Entry(window, textvariable=username)
username_entry.pack(padx=5,pady=2)

# Create the password label and entry field
password_label = Label(window, text="Password:", font=(5), bg="cornsilk3")
password_label.pack(padx=5,pady=2)
password = StringVar()  # Create a StringVar for the password
password_entry = Entry(window, show="*", textvariable=password)
password_entry.pack(padx=5,pady=2)

# Create the login button
login_button = Button(window, text="Log In", bg="lightblue", font=(5), command=login)
login_button.pack(ipadx=30,padx=20,pady=10) 


# Start the main event loop
window.mainloop()
