import os
import tkinter as tk
from tkinter import filedialog

# Set the default folder paths
BASE_PATH = "C:/Users/lucas/Desktop/languages"
OTHER_FILES_PATH = "C:/Users/lucas/Desktop/other_files"

# Check if the folder paths exist, prompt the user to select a folder if they don't
if not os.path.isdir(BASE_PATH):
    root = tk.Tk()
    root.withdraw()
    BASE_PATH = filedialog.askdirectory(title="Select base path folder")

if not os.path.isdir(OTHER_FILES_PATH):
    root = tk.Tk()
    root.withdraw()
    OTHER_FILES_PATH = filedialog.askdirectory(title="Select other files path folder")

# Initialize a set to keep track of all file names
all_files = set()

# Get a list of all the language folders in the base path
language_folders = [folder for folder in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, folder))]

# Loop over each language folder
for language_folder in language_folders:
    # Get a list of all the mp3 files in the language folder
    mp3_files = [file for file in os.listdir(os.path.join(BASE_PATH, language_folder)) if file.endswith(".mp3")]
    # Get a list of all the zip files in the language folder
    zip_files = [file for file in os.listdir(os.path.join(BASE_PATH, language_folder)) if file.endswith(".zip")]
    # Loop over each zip file
    for zip_file in zip_files:
        # Unzip the zip file in the same folder
        with zipfile.ZipFile(os.path.join(BASE_PATH, language_folder, zip_file), "r") as zip_ref:
            zip_ref.extractall(os.path.join(BASE_PATH, language_folder))
        # Delete the zip file
        os.remove(os.path.join(BASE_PATH, language_folder, zip_file))
    # Check if the folder contains any subfolders
    subfolders = [folder for folder in os.listdir(os.path.join(BASE_PATH, language_folder)) if os.path.isdir(os.path.join(BASE_PATH, language_folder, folder))]
    if subfolders:
        # Loop over each subfolder and move its contents to the language folder
        for subfolder in subfolders:
            for file in os.listdir(os.path.join(BASE_PATH, language_folder, subfolder)):
                # Check if the file already exists
                if file in all_files:
                    shutil.move(os.path.join(BASE_PATH, language_folder, subfolder, file), OTHER_FILES_PATH)
                else:
                    shutil.move(os.path.join(BASE_PATH, language_folder, subfolder, file), os.path.join(BASE_PATH, language_folder))
                    all_files.add(file)
            # Remove the empty subfolder
            os.rmdir(os.path.join(BASE_PATH, language_folder, subfolder))
    # Move any non-mp3 files to the "other files" folder
    for file in os.listdir(os.path.join(BASE_PATH, language_folder)):
        if file not in mp3_files and file not in zip_files:
            # Check if the file already exists
            if file in all_files:
                shutil.move(os.path.join(BASE_PATH, language_folder, file), OTHER_FILES_PATH)
            else:
                shutil.move(os.path.join(BASE_PATH, language_folder, file), os.path.join(BASE_PATH, language_folder))
                all_files.add(file)
    # Loop over each mp3 file
    for mp3_file in mp3_files:
        # Rename the mp3 file to replace spaces with underscores
        new_filename = mp3_file.replace(" ", "_")
        # Check if the file already exists
        if new_filename in all_files:
            shutil.move(os.path.join(BASE_PATH, language_folder, mp3_file), OTHER_FILES_PATH)
        else:
            os.rename(os.path.join(BASE_PATH, language_folder, mp3_file), os.path.join(BASE_PATH, language_folder, new_filename))
            all_files.add(new_filename)