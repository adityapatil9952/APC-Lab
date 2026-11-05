# Tkinter (simple GUI example)
#
# Problem Statement:
# Create a small Student Registration window. The user enters a name and age,
# clicks "Add" to store the student in a list shown on screen, and can
# "Clear" the fields or "Delete" a selected student.
#
# Run:  python Tkinter_Practical.py

import tkinter as tk
from tkinter import messagebox


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("350x400")

        # Heading
        tk.Label(root, text="Student Registration",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # Input fields
        frame = tk.Frame(root)
        frame.pack(pady=5)

        tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(frame, width=25)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add", width=8,
                  command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Clear", width=8,
                  command=self.clear_fields).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=8,
                  command=self.delete_student).grid(row=0, column=2, padx=5)

        # List of students
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)

        # Status label
        self.status = tk.Label(root, text="Total students: 0")
        self.status.pack()

    def add_student(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if name == "" or age == "":
            messagebox.showwarning("Missing Data", "Please enter name and age.")
            return
        if not age.isdigit():
            messagebox.showerror("Invalid Age", "Age must be a number.")
            return

        self.listbox.insert(tk.END, f"{name} - {age} years")
        self.clear_fields()
        self.update_status()

    def delete_student(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Select", "Select a student to delete.")
            return
        self.listbox.delete(selected[0])
        self.update_status()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.name_entry.focus()

    def update_status(self):
        self.status.config(text=f"Total students: {self.listbox.size()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
