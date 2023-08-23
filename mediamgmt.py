import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
from tkinter.tix import FileEntry
from tkinter import filedialog, messagebox
import subprocess


metadata = []
source_directory = 'D:\SIXTH SEM\FS lab\FS mini proj\sample output'  # Replace with your source directory
directory_path = 'D:\SIXTH SEM\FS lab\FS mini proj\sample output'

# sorting files
def media_management(source_directory):
    media_types = {
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.mp4': 'Video',
        '.avi': 'Video',
        '.jpg': 'Images',
        '.png': 'Images',
        '.pdf': 'pdf files',
        '.docx':'text files',
        '.txt':'text files'
    }

    for file in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, file)):
            
            if file_extension in media_types:
                media_directory = media_types[file_extension]
                media_path = os.path.join(source_directory, media_directory)
                if not os.path.exists(media_path):
                    os.makedirs(media_path)
                shutil.move(os.path.join(source_directory, file), os.path.join(media_path, file))

#generating metadata
def generate_metadata(directory):
    metadata = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.relpath(file_path, directory)
            file_size = os.path.getsize(file_path)
            file_extension = os.path.splitext(file)[1]
            file_metadata = {
                'filename': file_name,
                'size': file_size,
                'extension': file_extension
            }
            metadata.append(file_metadata)
    return metadata

#adding a file

destination_entry =None
status_label = None  # Declare the global variable
file_entry = None # Declare the global variable

def select_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def add_file():
    global destination_entry
    global status_label
    global file_entry
    
    if file_entry.get() == "":
        messagebox.showinfo("error","file is not defined")
        return

    file_path = file_entry.get()

    if destination_entry.get() == "":
        messagebox.showinfo("error","destination is not defined")
        return

    destination_folder = destination_entry.get()

    try:
        # Copy the file to the destination folder
        shutil.copy(file_path, destination_folder)
        messagebox.showinfo("success","file added successfully")
    except Exception as e:
        messagebox.showinfo("error",str(e))


def create_gui():
    global file_entry  # Declare file_entry as a global variable
    global destination_entry
    global status_label
    # Create the main window
    window = tk.Tk()
    window.title("Add File to Destination")

    # Set the window size and position
    window.geometry("400x200")
    window.resizable(False, False)

    # Create a label and entry for selecting a file
    file_entry = tk.Entry(window, width=40)
    file_entry.pack()

    file_button = tk.Button(window, text="Browse", command=select_file)
    file_button.pack()

    # Create a label and entry for entering the destination folder
    destination_label = tk.Label(window, text="Destination Folder:")
    destination_label.pack()

    destination_entry = tk.Entry(window, width=40)
    destination_entry.pack()

    # Create a button to add the file
    add_button = tk.Button(window, text="Add File", command=add_file)
    add_button.pack()

    # Create a label for displaying the status
    status_label = tk.Label(window, text="")
    status_label.pack()

#deleting a file
destination_entry = None
status_label = None
file_entry = None

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def delete_file():
    global destination_entry
    global status_label

    if destination_entry is None:
        messagebox.showinfo("Error", "Destination is not defined")
        return

    if file_entry is None:
        messagebox.showinfo("Error", "File is not defined")
        return

    file_path = file_entry.get()
    destination_folder = destination_entry.get()

    if not file_path:
        messagebox.showinfo("Error", "File path is empty")
        return

    if not destination_folder:
        messagebox.showinfo("Error", "Destination folder is empty")
        return

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Success", "File deleted successfully")
        else:
            messagebox.showinfo("Error", "File not found")
    except Exception as e:
        messagebox.showinfo("Error", str(e))

def create_gui1():
    global file_entry
    global destination_entry
    global status_label

    window = tk.Tk()
    window.title("Search and Delete File")

    window.geometry("400x200")
    window.resizable(False, False)

    file_label = tk.Label(window, text="File:")
    file_label.pack()

    file_entry = tk.Entry(window, width=40)
    file_entry.pack()

    file_button = tk.Button(window, text="Browse", command=select_file)
    file_button.pack()

    destination_label = tk.Label(window, text="Destination Folder:")
    destination_label.pack()

    destination_entry = tk.Entry(window, width=40)
    destination_entry.pack()

    delete_button = tk.Button(window, text="Delete File", command=delete_file)
    delete_button.pack()

    status_label = tk.Label(window, text="")
    status_label.pack()

#thumbnail
file_entry = None  # Declare the global variable
output_entry = None  # Declare the global variable
width_entry = None  # Declare the global variable
height_entry = None  # Declare the global variable

def generate_thumbnail():
    global file_entry, output_entry, width_entry, height_entry
    input_file = file_entry.get()
    output_file = output_entry.get()
    width = int(width_entry.get())
    height = int(height_entry.get())

    if not input_file:
        messagebox.showinfo("Error", "Input file not selected")
        return

    if not output_file:
        messagebox.showinfo("Error", "Output file not specified")
        return

    if not width or not height:
        messagebox.showinfo("Error", "Width and height must be specified")
        return

    try:
        # Run the ffmpeg command to generate the thumbnail
        subprocess.run([
            "ffmpeg",
            "-i", input_file,
            "-vf", f"scale={width}:{height}",
            "-vframes", "1",
            output_file
        ], check=True)
        messagebox.showinfo("Success", "Thumbnail generated successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showinfo("Error", f"Error generating thumbnail: {e}")

def select_input_file():
    global file_entry
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def select_output_file():
    global output_entry
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def create_gui3():
  global file_entry, output_entry, width_entry, height_entry
  window = tk.Tk()
  window.title("Thumbnail Generator")

# Create and position the necessary widgets
  file_label = tk.Label(window, text="Input File:")
  file_label.grid(row=0, column=0)

  file_entry = tk.Entry(window, width=40)
  file_entry.grid(row=0, column=1)

  file_button = tk.Button(window, text="Browse", command=select_input_file)
  file_button.grid(row=0, column=2)

  output_label = tk.Label(window, text="Output File:")
  output_label.grid(row=1, column=0)

  output_entry = tk.Entry(window, width=40)
  output_entry.grid(row=1, column=1)

  output_button = tk.Button(window, text="Browse", command=select_output_file)
  output_button.grid(row=1, column=2)

  width_label = tk.Label(window, text="Width:")
  width_label.grid(row=2, column=0)

  width_entry = tk.Entry(window, width=10)
  width_entry.grid(row=2, column=1)

  height_label = tk.Label(window, text="Height:")
  height_label.grid(row=2, column=2)

  height_entry = tk.Entry(window, width=10)
  height_entry.grid(row=2, column=3)

  generate_button = tk.Button(window, text="Generate Thumbnail", command=generate_thumbnail)
  generate_button.grid(row=3, column=1, pady=10)



 #button defs
def button1_click():
    media_management(source_directory)
    messagebox.showinfo("sorted","The files are sorted based on the file types!")

def button2_click():
    global metadata
    metadata = generate_metadata(directory_path)
    with open ("metadata.txt",'w') as f:
        for file_metadata in metadata:
         f.write(str(file_metadata)+'\n')
    messagebox.showinfo("metadata", "The metadata has been generated!")

    
def button3_click():
    create_gui()

def button4_click():
    create_gui1()

def button5_click():
    create_gui3()

# Create the main window
window = tk.Tk()
window.title("fs project")

# Set the window size and position
window.geometry("400x200")
window.resizable(False, False)
destination_label = tk.Label(window, text="MEDIA ORGANIZATION & MANAGEMENT", font=40)
destination_label.pack()

# Create and configure the buttons
button1 = tk.Button(window, text="Sort Files", command=button1_click)
button2 = tk.Button(window, text=" Metadata", command=button2_click)
button3 = tk.Button(window, text="Add a file", command=button3_click)
button4= tk.Button(window,text="Delete file",command=button4_click)
button5=tk.Button(window,text="Thumbnail",command=button5_click)
# Add the buttons to the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

# Start the main event loop
window.mainloop()
