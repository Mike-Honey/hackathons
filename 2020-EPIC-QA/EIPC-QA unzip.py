# EPIC-QA unzip.py
# Unpacks the input .gz file

import json
import os
import pandas
import shutil
PATH = "C:/Dev/EPIC-QA/"
# uncomment lines below to delete the target directory
# try:
#     shutil.rmtree(PATH + "coronawhy-sciSpacy")
# except:
#     p = ""

for p in os.listdir(PATH):
    if p.endswith(".gz")  :
        gz_file = PATH + p
        print("found gz file: " + gz_file)
        shutil.unpack_archive(PATH + p, PATH + str.replace(p,".gz",""))
        # os.remove(gz_file)
        # print ('deleted file:' + gz_file)


# uncomment below to delete input files (once processed and written to an output_file)
        # os.remove(input_file)
        # print ('deleted file:' + input_file)
        
        # break

