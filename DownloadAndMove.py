import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/Deetya/Downloads"
to_dir = "C:/Users/Deetya/Desktop/downloadedFiles"

dir_tree = {
    "image_files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif','.webp'],
    "video_files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "pdf_files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "zipped_files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,extenction=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extenction in value:
                file_name=os.path.basename(event.src_path)
                print("downloaded")
                path1=from_dir+'/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir+'/'+key+'/'+file_name


                if os.path.exists(path2):
                    print("directory exists")
                    time.sleep(1)
                    if os.path.exists(path3):
                    
                        print(" file already exists in "+key+"....")
                        print("renaming file"+file_name+"....")
                        new_file_name=os.path.splitext(file_name)[0]+str(random.randint(0,999))+os.path.splitext(file_name)[1]
                        path4=to_dir+'/'+key+'/'+new_file_name
                        print("moving...")
                        shutil.move(path1,path4)
                        time.sleep(1)
                else :
                    print("making directory")
                    os.makedirs(path2)
                    print("moving...")
                    shutil.move(path1,path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:
        while True:
            time.sleep(2)
            print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()

    