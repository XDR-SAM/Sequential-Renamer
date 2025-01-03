import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files_by_creation_time(folder_path):
    try:
        # Get a list of all files in the folder
        folder = Path(folder_path)
        files = [f for f in folder.iterdir() if f.is_file()]

        # Sort files by creation time
        sorted_files = sorted(files, key=lambda f: f.stat().st_ctime)

        # Rename files sequentially
        for idx, file in enumerate(sorted_files, start=1):
            new_name = folder / f"{idx}{file.suffix}"  # Retain the original file extension
            file.rename(new_name)

        messagebox.showinfo("Success", f"Renamed {len(sorted_files)} files successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_folder_and_rename():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:  # Check if a folder was selected
        rename_files_by_creation_time(folder_path)

# GUI setup
root = tk.Tk()
root.title("File Renamer")

# Window size
root.geometry("400x200")

# Instructions
label = tk.Label(root, text="Click the button below to select a folder and rename files:", font=("Arial", 12))
label.pack(pady=20)

# Button to trigger folder selection
rename_button = tk.Button(root, text="Select Folder and Rename", command=select_folder_and_rename, font=("Arial", 12), bg="lightblue")
rename_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
