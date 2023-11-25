import sys
import random
import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads"
to_dir = "C:/Users/HP/Downloads/Destination"

dir_tree = {

    "Image_File" : [".jpg",".png",".webp"],
    "Pdf_Files" : [".pdf"]
}

class FileMovementHandler(FileSystemEventHandler) :
    def on_created(self,event) :
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items() :
            time.sleep(1)
            if extension in value :
                file_name = os.path.basename(event.src_path)
                path1 = from_dir+"/"+file_name
                path2 = to_dir+"/"+"Image_Files"
                path3 = to_dir+"/"+"Image_Files"+"/"+file_name


                if os.path.exists(path2) :
                    shutil.move(path1,path3)
                    time.sleep(1)
                else :
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recusive=True)
observer.start()

try :
    while True :
        time.sleep(2)
except KeyboardInterrupt :
    print("STOPPED !")
    observer.stop()