import json
import sys
import csv
import os
from PyQt5.QtWidgets import QApplication, QFileDialog
from tkinter import messagebox


class FileHandler:
    """
    Handle saving and retrieving of JSON objects/files
    """

    @staticmethod
    def save_project(project_info):
        """
        Saves project python dictionary into user-defined directory as a .JSON file.

        Parameters:
                project_info (dict()): Project dictionary

        Returns:
                0 if successful, else -1.
        """
        # Get first key/value pair in the dictionary
        project_name = list(project_info.items())[0][1]

        # Loop directory prompt until success or cancel
        while True:
            try:
                # Prompt user for path
                path = FileHandler.prompt_dir()
                # User cancel or close, exit function
                if not path:
                    break
                # Create project directory and update path with new directory
                path = FileHandler.create_dir(project_name, path)
                # Create config.json file
                FileHandler.create_file(path, ".json", project_info, "CONFIG")
                return 0
            # The user has tried to create an already existing directory
            except FileExistsError:
                messagebox.showerror(title="CAN Bus Visualizer", message="Folder Already Exists!")
        return -1

    @staticmethod
    def export_to_csv(py_dict):
        """
        Exports python dictionary into user-defined directory as a .CSV file.

        Parameters:
                py_dict (dict()): Python dictionary data

        Returns:
                0 if successful, else -1.
        """
        # Get file information
        file_info = FileHandler.prompt_file_save()
        # If file saved
        if file_info:
            # Create CSV file
            FileHandler.create_file(file_info[0], file_info[2], py_dict, file_name=file_info[1])
            return 0
        return -1

    @staticmethod
    def create_file(path, file_type, file_contents, file_name="place_holder"):
        """
        File creator

        Parameters:
                path String: path
                file_type String: file extension, Ex. (.json)
                file_contents dict: data to be exported
                file_name String: optional file name
        """
        # Create .json file
        if file_type == ".json":
            FileHandler.create_json_file(path, file_name, file_contents)
        # Create .csv file
        if file_type == ".csv":
            FileHandler.create_csv_file(path, file_name, file_contents)

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
    def create_json_file(path, file_name, py_dict):
        with FileHandler.file_opener(path, file_name, ".json") as json_file:
            json_object = json.dumps(py_dict, indent=2)
            json_file.write(json_object)
            json_file.close()

    @staticmethod
    def create_csv_file(path, file_name, py_dict):
        with FileHandler.file_opener(path, file_name, ".csv") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FileHandler.create_field_names(py_dict))
            writer.writeheader()
            writer.writerow(py_dict)

    @staticmethod
    def prompt_file_open():
        app = QApplication(sys.argv)
        path = QFileDialog.getOpenFileName()[0]
        return FileHandler.parse_file_info(path)

    @staticmethod
    def prompt_file_save():
        app = QApplication(sys.argv)
        path = QFileDialog.getSaveFileName(filter="CSV files (*.csv);; XML files (*.xml)")[0]
        return FileHandler.parse_file_info(path)

    @staticmethod
    def prompt_dir():
        app = QApplication(sys.argv)
        return QFileDialog.getExistingDirectory()

    @staticmethod
    def file_opener(path, file_name, file_type, flag="w"):
        return open(path + "/" + file_name + file_type, flag)

    @staticmethod
    def parse_file_info(path):
        if not path:
            return []
        file_name_split = FileHandler.get_path_last(path, "/").split(".")
        path = FileHandler.remove_path_last(path, 1)
        file_name = file_name_split[0]
        file_type = "." + file_name_split[1]
        return [path, file_name, file_type]

    @staticmethod
    def get_path_last(path, delimiter="/"):
        return path.split(delimiter)[-1]

    @staticmethod
    def remove_path_last(path, remove_count):
        return "/".join(path.split("/")[:-remove_count])

    @staticmethod
    def create_field_names(py_dict):
        key_list = []
        for key in py_dict:
            key_list.append(key)
        return key_list
