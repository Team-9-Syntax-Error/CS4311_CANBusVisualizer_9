import json
import os
from tkinter import filedialog
from tkinter import messagebox
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class FileHandler:
    """
    Handle saving and retrieving of JSON objects/files
    """

    @staticmethod
    def save_project(project_info):
        """
        Saves project dictionary into user-defined directory as a .JSON file.

        Parameters:
                project_info (dict()): Project dictionary

        Returns:
                1 if successful, else 0.
        """

        # Dump dictionary into json object
        json_object = json.dumps(project_info, indent=2)
        # Get first key/value in the dictionary
        file_name = list(project_info.items())[0][1]
        while True:
            try:
                # Prompt user for path
                path = FileHandler.prompt_dir()
                # Create project directory and update path with new directory
                path = FileHandler.create_dir(file_name, path)
                print(path)
                # Create config file
                FileHandler.create_file("config", ".json", path, json_object)
                return 1
            # Tkinter 'cancel' has returned an error tuple to path, resulting in a type error
            except TypeError:
                break
            # The user has tried to create an already existing directory
            except FileExistsError:
                messagebox.showerror(title="CAN Bus Visualizer", message="Folder Already Exists!")
        return 0

    @staticmethod
    def load_file():
        """
        Loads JSON contents from user-selected file

        Returns:
                Project dictionary
        """
        # Prompt user file and load into dictionary
        return json.load(FileHandler.prompt_file())

    @staticmethod
    def create_dir(dir_name, path):
        """
        Provide simple API for creating a directory.

        Parameters:
                dir_name str: Name of the directory
                path str: Path of the directory
        """
        path = path + "/" + dir_name
        os.mkdir(path)
        return path

    @staticmethod
    def create_file(file_name, file_type, path, contents):
        """
        Provide simple API for creating a file.

        Parameters:
                file_name str: Name of the file
                file_type str: File extension
                path str: Directory path
                contents str: Contents to write
        """
        # Open file in writing mode
        json_file = open(path + "/" + file_name + file_type, "w")
        # Write and close file
        json_file.write(contents)
        json_file.close()

    @staticmethod
    def prompt_dir():
        """
        Prompt user for directory using Tkinter GUI

        Returns:
                Directory string
        """

        # Create PyQt application
        app = QApplication(sys.argv)
        # Create the main window
        win = QMainWindow()
        # Prompt for directory
        file_path = QtWidgets.QFileDialog.getExistingDirectory(win, 'Select Folder')
        # Exit application
        app.quit()

        return file_path

    @staticmethod
    def prompt_file():
        """
        Prompt user for file using Tkinter GUI

        Returns:
                File object
        """
        file = filedialog.askopenfile()
        return file
