#  Project 6: Bulk File Re-namer Python Project

import os  # operating system(renaming files)

# Importing all widgets, classes, and functions(button,label,Entry, etc., without needing 'tk.' prefix)
from tkinter import * 

# Function to rename files
def rename():
    folderpath = path.get() # Get the folder path from the user input

    # Path validation: check if the folder path exists
    if not os.path.exists(folderpath):
        result_label.config(text="Invalid Path") # Display an error message if path doesn't exist
        return

    # Initializing counter to 1, for naming files sequentially
    counter = 1

    for filename in os.listdir(folderpath):
          # Get file extension (e.g., .txt, .jpg)
        name, ext = os.path.splitext(filename)
        
        # Rename files only (not folders)
        if os.path.isfile(os.path.join(folderpath, filename)):
             # Rename the file by appending the counter number
            os.rename(os.path.join(folderpath, filename), os.path.join(folderpath, word.get() + str(counter) + ext))

            counter += 1  # Increment the counter for the next file


    result_label.config(text="Files Renamed Successfully!")  # Display success message

    ent.delete(0, END)   # Clear the file path input field
    ent2.delete(0, END)  # Clear the word input field


# Create the main window (root) for the GUI
root = Tk()
root.title('RENAMER')
root.geometry('300x300') # Set the dimensions of the window (300x300 pixels)


# StringVar() is used to store and manage text data in Tkinter widgets like Entry
path = StringVar()

# Labels and entry fields
label = Label(root, text='Paste File Path', font=('Times New Roman', 12)) 
label.pack()  
ent = Entry(root, textvariable=path, font=('Times New Roman', 12))
ent.pack()

word = StringVar()

label = Label(root, text='Give One Word', font=('Times New Roman', 12)) 
label.pack()  
ent2 = Entry(root, textvariable=word, font=('Times New Roman', 12))
ent2.pack()

# Result label to show success or error message
result_label = Label(root, text="", font=('Times New Roman', 12))
result_label.pack()

# Button to trigger renaming
Button(root, text = 'Change', command = rename).pack()


# Run the Tkinter event loop to keep the window open and active
root.mainloop()







