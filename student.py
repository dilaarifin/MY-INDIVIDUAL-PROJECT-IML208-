import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# DEFINITIONS
def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT, student_age INTEGER, student_mykad TEXT, student_birthday TEXT, student_address TEXT, student_phone TEXT, student_gender TEXT, student_races TEXT, guardian TEXT, guardian_name TEXT, guardian_mykad TEXT, guardian_job TEXT, guardian_salary INTEGER, guardian_phone TEXT)")
    conn.commit()
    conn.close()

def insert_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        student_name = entry_studentname.get()
        student_age = entry_studentage.get()
        student_mykad = entry_studentmykad.get()
        student_birthday = entry_studentbday.get()
        student_address = entry_studentaddress.get()
        student_phone = entry_studentphone.get()
        student_gender = entry_studentgender.get()
        student_races = entry_studentraces.get()
        guardian = entry_guardian.get()
        guardian_name = entry_guardianname.get()
        guardian_mykad = entry_guardianmykad.get()
        guardian_job = entry_guardianjob.get()
        guardian_salary = entry_guardiansalary.get()
        guardian_phone = entry_guardianphone.get()
        
        if student_name and student_age and student_mykad and student_birthday and student_address and student_phone and student_gender and student_races and guardian and guardian_name and guardian_mykad and guardian_job and guardian_salary and guardian_phone:
            
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (student_name,student_age,student_mykad,student_birthday,student_address,student_phone,student_gender,student_races,guardian,guardian_name,guardian_mykad,guardian_job,guardian_salary,guardian_phone) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (student_name,student_age,student_mykad,student_birthday,student_address,student_phone,student_gender,student_races,guardian,guardian_name,guardian_mykad,guardian_job,guardian_salary,guardian_phone))    
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully added to database",icon='info')
            
            entry_studentname.delete(0, tk.END)
            entry_studentage.delete(0, tk.END)
            entry_studentmykad.delete(0, tk.END)
            entry_studentbday.delete(0, tk.END)
            entry_studentaddress.delete(0, tk.END)
            entry_studentphone.delete(0, tk.END)
            entry_studentgender.delete(0, tk.END)
            entry_studentraces.delete(0, tk.END)
            entry_guardianname.delete(0, tk.END)
            entry_guardianmykad.delete(0, tk.END)
            entry_guardianjob.delete(0, tk.END)
            entry_guardiansalary.delete(0, tk.END)
            entry_guardianphone.delete(0, tk.END)
            entry_guardian.delete(0, tk.END)
        else:
            tkinter.messagebox.showwarning(title="Error", message="Fields cannot be empty", icon="warning")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms", icon="warning")   

def display_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]}")
        listbox.insert(tk.END, f"Name: {row[1]}")
        listbox.insert(tk.END, f"Age: {row[2]}")
        listbox.insert(tk.END, f"My Kad: {row[3]}")
        listbox.insert(tk.END, f"Birthday: {row[4]}")
        listbox.insert(tk.END, f"Address: {row[5]}")
        listbox.insert(tk.END, f"No.Phone: {row[6]}")
        listbox.insert(tk.END, f"Gender: {row[7]}")
        listbox.insert(tk.END, f"Races: {row[8]}")
        listbox.insert(tk.END, f"Guardian: {row[9]}")
        listbox.insert(tk.END, f"Guardian Name: {row[10]}")
        listbox.insert(tk.END, f"Guardian MyKad: {row[11]}")
        listbox.insert(tk.END, f"Guardian Job: {row[12]}")
        listbox.insert(tk.END, f"Guardian Salary: {row[13]}")
        listbox.insert(tk.END, f"Guardian No.Phone: {row[14]}")
        listbox.insert(tk.END, "") 
    
def update_data():
    selected_item = listbox.curselection()
    if not selected_item:
        return

    new_name = entry_studentname.get()
    new_age = entry_studentage.get()
    new_mykad = entry_studentmykad.get()
    new_birthday = entry_studentbday.get()
    new_address = entry_studentaddress.get()
    new_phone = entry_studentphone.get()
    new_gender = entry_studentgender.get()
    new_races = entry_studentraces.get()
    new_guardian = entry_guardian.get()
    new_guardianname = entry_guardianname.get()
    new_guardianmykad = entry_guardianmykad.get()
    new_guardianjob = entry_guardianjob.get()
    new_guardiansalary = entry_guardiansalary.get()
    new_guardianphone = entry_guardianphone.get()
    
    selected_id = listbox.get(selected_item).split(",")[0].split(":")[1].strip()        
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET student_name=?, student_age=?, student_mykad=?, student_birthday=?, student_address=?, student_phone=?, student_gender=?, student_races=?, guardian=?, guardian_name=?, guardian_mykad=?, guardian_job=?, guardian_salary=?,guardian_phone=? WHERE id=?", (new_name, new_age, new_mykad, new_birthday, new_address, new_phone, new_gender, new_races, new_guardian, new_guardianname, new_guardianmykad, new_guardianjob, new_guardiansalary, new_guardianphone, selected_id))
    conn.commit()
    conn.close()

    entry_studentname.delete(0, tk.END)
    entry_studentname.delete(0, tk.END)
    entry_studentage.delete(0, tk.END)
    entry_studentmykad.delete(0, tk.END)
    entry_studentbday.delete(0, tk.END)
    entry_studentaddress.delete(0, tk.END)
    entry_studentphone.delete(0, tk.END)
    entry_studentgender.delete(0, tk.END)
    entry_studentraces.delete(0, tk.END)
    entry_guardian.delete(0, tk.END)
    entry_guardianname.delete(0, tk.END)
    entry_guardianmykad.delete(0, tk.END)
    entry_guardianjob.delete(0, tk.END)
    entry_guardiansalary.delete(0, tk.END)
    entry_guardianphone.delete(0, tk.END)
    display_data() 
    
def delete_data():
    selected_item = listbox.curselection()
    if not selected_item:
        return

    selected_id = listbox.get(selected_item).split(",")[0].split(":")[1].strip()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (selected_id,))
    conn.commit()
    conn.close()

    display_data()    

# Main Window        
window = tk.Tk()
window.title("Welcome to Gotham School: Student Management System")
window.geometry("1070x570")
window.iconbitmap("icons/student.ico")
window.resizable(False,False)

# Set the window size
window_width = 1070
window_height = 570

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main Frame
frame = tkinter.Frame(window,bg="cornsilk4",relief='sunken',borderwidth=4)
frame.pack()

# STUDENT FRAME INFORMATIONS
student_frame = tkinter.LabelFrame(frame, text="Student Information", font="arial 10 bold", bg="cornsilk3",relief='groove', borderwidth=3)
student_frame.grid(row=0, column=0, padx=20, pady=10, sticky="news")

lbl_studentname = tkinter.Label(student_frame, text="Full Name:", bg="cornsilk3")
lbl_studentname.grid(row=0, column=0, sticky="w")
entry_studentname = tkinter.Entry(student_frame, width=30)
entry_studentname.grid(row=1, column=0, sticky="w")

lbl_student_age = tkinter.Label(student_frame, text="Age:", bg="cornsilk3")
lbl_student_age.grid(row=0, column=1, sticky="w")
entry_studentage = tkinter.Spinbox(student_frame, from_=13, to=17)
entry_studentage.grid(row=1, column=1, sticky="w")

lbl_student_mykad = tkinter.Label(student_frame, text="My Kad:", bg="cornsilk3")
lbl_student_mykad.grid(row=0, column=2, sticky="w")
entry_studentmykad = tkinter.Entry(student_frame, width=23)
entry_studentmykad.grid(row=1, column=2, sticky="w")

lbl_studentbday = tkinter.Label(student_frame, text="Birth Date:", bg="cornsilk3")
lbl_studentbday.grid(row=3, column=0, sticky="w")
entry_studentbday = tkinter.Entry(student_frame)
entry_studentbday.grid(row=4, column=0, sticky="w")

lbl_studentphone = tkinter.Label(student_frame, text="Phone:", bg="cornsilk3")
lbl_studentphone.grid(row=3, column=1, sticky="w")
entry_studentphone = tkinter.Entry(student_frame, width=22)
entry_studentphone.grid(row=4, column=1, sticky="w")

lbl_studentgender = tkinter.Label(student_frame, text="Gender:", bg="cornsilk3")
lbl_studentgender.grid(row=3, column=2, sticky="w")
entry_studentgender = ttk.Combobox(student_frame, values=["Male", "Female"])
entry_studentgender.grid(row=4, column=2, sticky="w")

lbl_studentraces = tkinter.Label(student_frame, text="Races:", bg="cornsilk3")
lbl_studentraces.grid(row=5, column=0, sticky="w")
entry_studentraces = ttk.Combobox(student_frame, values=["Malay", "Chinese", "Indian", "Bumiputera", "Other"])
entry_studentraces.grid(row=6, column=0, sticky="w")

lbl_studentaddress = tkinter.Label(student_frame, text="Address:", bg="cornsilk3")
lbl_studentaddress.grid(row=5, column=1, sticky="w")
entry_studentaddress = tkinter.Entry(student_frame, width=30)
entry_studentaddress.grid(row=6, column=1, sticky="w")

for widget in student_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# GUARDIAN INFORMATIONS FRAME (FATHER/MOTHER/OTHER GUARDIAN)
guardian_frame = tkinter.LabelFrame(frame, text="Father/Mother/Other Guardian", font="arial 10 bold", bg="cornsilk3", relief='groove', borderwidth=3)
guardian_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

lbl_guardian = tkinter.Label(guardian_frame, text="Guardian:", bg="cornsilk3")
lbl_guardian.grid(row=0,column=0, sticky="w")
entry_guardian = ttk.Combobox(guardian_frame, values=["Father", "Mother", "Other"])
entry_guardian.grid(row=1,column=0, sticky="w")

lbl_guardianname = tkinter.Label(guardian_frame, text="Full Name:", bg="cornsilk3")
lbl_guardianname.grid(row=0, column=1, sticky="w")
entry_guardianname = tkinter.Entry(guardian_frame, width=30)
entry_guardianname.grid(row=1, column=1, sticky="w")

lbl_guardianmykad = tkinter.Label(guardian_frame, text="MyKad:", bg="cornsilk3")
lbl_guardianmykad.grid(row=0, column=2, sticky="w")
entry_guardianmykad = tkinter.Entry(guardian_frame)
entry_guardianmykad.grid(row=1, column=2, sticky="w")

lbl_guardianjob = tkinter.Label(guardian_frame, text="Job:", bg="cornsilk3")
lbl_guardianjob.grid(row=3, column=0, sticky="w")
entry_guardianjob = ttk.Combobox(guardian_frame, values=["Government","Private","Police","Business","Housewife","Type Other..."])
entry_guardianjob.grid(row=4, column=0, sticky="w")

lbl_guardiansalary = tkinter.Label(guardian_frame, text="Salary (RM):", bg="cornsilk3")
lbl_guardiansalary.grid(row=3, column=1, sticky="w")
entry_guardiansalary = tkinter.Entry(guardian_frame)
entry_guardiansalary.grid(row=4, column=1, sticky="w")

lbl_guardianphone = tkinter.Label(guardian_frame, text="Phone:", bg="cornsilk3")
lbl_guardianphone.grid(row=3, column=2, sticky="w")
entry_guardianphone = tkinter.Entry(guardian_frame)
entry_guardianphone.grid(row=4, column=2, sticky="w")

for widget in guardian_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# DISPLAY FRAME
display_frame = tkinter.LabelFrame(frame, text="Display", font="arial 10 bold", bg="cornsilk3", relief='groove', borderwidth=3)
display_frame.grid(row=0, column=1, sticky="news", padx=20, pady=10)

listbox = tkinter.Listbox(display_frame, width=70, height=13)
listbox.grid(row=0, column=0)


for widget in display_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Buttons Display/Update/Delete
buttons_frame = tkinter.LabelFrame(frame, text="Buttons", font="arial 10 bold", bg="cornsilk3", relief='groove', borderwidth=3)
buttons_frame.grid(row=1, column=1, padx=20, pady=10, sticky="N")

button_display = tkinter.Button(buttons_frame, text="View Record", bg="lightblue", command=display_data)
button_display.grid(row=0, column=0)

button_update = tkinter.Button(buttons_frame, text="Update Record", bg="greenyellow", command=update_data)
button_update.grid(row=0, column=2)

button_delete = tkinter.Button(buttons_frame, text="Delete Record", bg="indianred1", command=delete_data)
button_delete.grid(row=0, column=3)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# ACCEPT TERMS FRAME
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", font="arial 10 bold", bg="cornsilk3", relief='groove', borderwidth=3)
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg="cornsilk3")
terms_check.grid(row=0, column=0)

# Button Enter Data
button = tkinter.Button(frame, text="Submit and Add Record",font='arial 11 bold', bg="cornsilk3", command=insert_data)
button.grid(row=3, column=0, sticky="news",padx=20, pady=10)

# Note
note = tkinter.LabelFrame(frame, text="Notes", font="arial 10 bold", bg="cornsilk3", relief='groove', borderwidth=3)
note.grid(row=2,column=1, sticky="news",padx=20,pady=10)

note1 = tkinter.Label(note, text="Made By: NUR FADHILAH BT ARIFIN (2022764227)", bg="cornsilk3")
note1.grid(row=0, column=0, sticky="w")

note2 = tkinter.Label(note, text="Class: KIM144 3A | Course: IML208 (PROGRAMMING FOR LIBRARIES)", bg="cornsilk3")
note2.grid(row=1, column=0, sticky="w")

# Create the database table (if not already exists)
create_table()

window.mainloop()
