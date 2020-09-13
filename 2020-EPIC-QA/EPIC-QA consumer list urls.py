# EIPC-QA consumer list urls.py
# Lists the url tags found in the consumer documents

import json
import os
import pandas
import shutil
PATH = "C:/Dev/EPIC-QA/epic_qa_consumer_2020-06-10_v2.tar/"
# uncomment lines below to delete the target directory
# try:
#     shutil.rmtree(PATH + "coronawhy-sciSpacy")
# except:
#     p = ""

for dirname, _, filenames in os.walk(PATH):
    for filename in filenames:
        if filename.endswith(".json")  :
            json_file = os.path.join(dirname, filename)
            # print("found json file: " + json_file)
            with open(json_file, 'rb') as f:
                each_paper_dict = json.load(f)
                for metadata_item in each_paper_dict['metadata'].items():
                    if metadata_item[0] == "url" and metadata_item[1] > "":
                        print(str(metadata_item[1]))

