
import subprocess

class R_sync:
    def __init__(self, from_folderpath, to_folderpath):
        self.from_folderpath = from_folderpath+"/*"
        self.to_folderpath = to_folderpath

    def sync(self):
        #copying everything in the provided folder path
        subprocess.run(f"(rsync {self.from_folderpath} {self.to_folderpath})", shell=True)
