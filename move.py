import os
import shutil

from_dir = r"C:\Users\ASHUTOSH ARYAN\OneDrive\Desktop\coding\module 3\project\C---102[AUTOMATE FILE SEGREGATION]\Download_Files"
to_dir = r"C:\Users\ASHUTOSH ARYAN\OneDrive\Desktop\coding\module 3\project\C---102[AUTOMATE FILE SEGREGATION]\Download_Files\downloads"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for download_files in list_of_files:
    root,ext = os.path.splitext(download_files)
    #print(root,ext)
    if ext == "":
        continue
    if ext in [".docx",".txt","docx",".doc"]:
        if not os.path.exists(to_dir):
            os.mkdir(to_dir)
        source = from_dir + r'\\' + download_files
        #print("Source:", source)
        destination = to_dir + r'\\' + download_files
        #print("Destination:", destination)
        shutil.move(source, destination)

print("task completed")

