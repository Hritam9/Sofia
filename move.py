import shutil
import os
import glob
import time
#source = os.listdir("D://Video SONGS/Videos/")
source = "YOUR FILE LOCATION"
destination = "FILE LOCATION"
file_list = glob.glob(source)
for single_file in file_list:
    shutil.move(single_file,destination)
time.sleep(1)
#for files in source:
#    if files.endswith('.pdf'):
#        shutil.move(os.path.join(source, files), os.path.join(destination, files))
#shutil.move(source,destination)
