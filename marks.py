import tkinter as tk

def generate_marksheet():
    # get input values from user
    name = name_entry.get()
    id = id_entry.get()
    english_marks = int(english_marks_entry.get())
    math_marks = int(math_marks_entry.get())
    science_marks = int(science_marks_entry.get())

    # calculate total marks and percentage
    total_marks = english_marks + math_marks + science_marks
    percentage = round((total_marks / 300) * 100, 2)

    # update output labels with calculated values
    total_marks_label.config(text="Total Marks: " + str(total_marks))
    percentage_label.config(text="Percentage: " + str(percentage) + "%")

    # create mark sheet in a new window
    mark_sheet_window = tk.Toplevel(root)
    mark_sheet_window.title("Mark Sheet")

    name_label = tk.Label(mark_sheet_window, text="Name: " + name)
    id_label = tk.Label(mark_sheet_window, text="ID: " + id)
    english_marks_label = tk.Label(mark_sheet_window, text="English: " + str(english_marks))
    math_marks_label = tk.Label(mark_sheet_window, text="Mathematics: " + str(math_marks))
    science_marks_label = tk.Label(mark_sheet_window, text="Science: " + str(science_marks))
    total_marks_label2 = tk.Label(mark_sheet_window, text="Total Marks: " + str(total_marks))
    percentage_label2 = tk.Label(mark_sheet_window, text="Percentage: " + str(percentage) + "%")

    name_label.pack()
    id_label.pack()
    english_marks_label.pack()
    math_marks_label.pack()
    science_marks_label.pack()
    total_marks_label2.pack()
    percentage_label2.pack()

# create main window
root = tk.Tk()
root.title("Automatic Mark Sheet Generator")

# create input labels and entry fields
name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

id_label = tk.Label(root, text="ID")
id_label.grid(row=1, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

english_marks_label = tk.Label(root, text="English Marks")
english_marks_label.grid(row=2, column=0)
english_marks_entry = tk.Entry(root)
english_marks_entry.grid(row=2, column=1)

math_marks_label = tk.Label(root, text="Mathematics Marks")
math_marks_label.grid(row=3, column=0)
math_marks_entry = tk.Entry(root)
math_marks_entry.grid(row=3, column=1)

science_marks_label = tk.Label(root, text="Science Marks")
science_marks_label.grid(row=4, column=0)
science_marks_entry = tk.Entry(root)
science_marks_entry.grid(row=4, column=1)

# create button to generate mark sheet
generate_marksheet_button = tk.Button(root, text="Generate Mark Sheet", command=generate_marksheet)
generate_marksheet_button.grid(row=5, column=0, columnspan=2)

# create output labels
total_marks_label = tk.Label(root, text="")
total_marks_label.grid(row=6, column=0, columnspan=2)

percentage_label = tk.Label(root, text="")
percentage_label.grid(row=7, column=0, columnspan=2)

root.mainloop()