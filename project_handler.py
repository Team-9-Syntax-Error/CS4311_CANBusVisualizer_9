import json
import tkinter as tk
from tkinter import filedialog


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
        """

        # Dump dictionary into json object
        json_object = json.dumps(project_info, indent=2)
        # Prompt user for directory and create blank json file
        json_file = open(FileHandler.prompt_dir() + "/" + project_info['project_name'] + ".json", "w")
        # Write json contents to file
        json_file.write(json_object)

    @staticmethod
    def retrieve_project():
        """
        Retrieves JSON contents from user-selected file

        Returns:
                Project dictionary
        """
        # Prompt user file and load into dictionary
        return json.load(FileHandler.prompt_file())


    @staticmethod
    def prompt_dir():
        """
        Prompt user for directory using Tkinter GUI

        Returns:
                Directory string
        """

        # Create root
        root = tk.Tk()
        # Prompt directory
        file_path = filedialog.askdirectory()
        # Kill window
        root.destroy()
        return file_path

    @staticmethod
    def prompt_file():
        """
        Prompt user for file using Tkinter GUI

        Returns:
                File object
        """

        root = tk.Tk()
        # Prompt user file
        file = filedialog.askopenfile()
        root.destroy()
        return file
