import os
import json
import tkinter as tk
from tkinter import filedialog


class ProjectHandler:
    json_object = ""
    json_dict = []

    def __init__(self, project_info):
        self.json_object = json.dumps(project_info, indent=2)
        self.json_dict = project_info

    def save_project(self):
        json_file = open(ProjectHandler.prompt_dir()+"/"+self.json_dict['project_name']+".json", "w")
        json_file.write(self.json_object)

    @staticmethod
    def prompt_dir():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        root.destroy()
        return file_path


