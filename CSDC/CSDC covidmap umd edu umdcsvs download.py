
from bs4 import BeautifulSoup
import gzip
import os
from pathlib import Path
import re
import requests
import shutil
from urllib.parse import urlparse
from urllib.request import Request, urlopen, urlretrieve

# url = 'https://covidmap.umd.edu/umdcsvs/'
# ext = 'csv'

# def listFD(url, ext=''):
#     page = requests.get(url).text
#     print (page)
#     soup = BeautifulSoup(page, 'html.parser')
#     return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

# for file in listFD(url, ext):
#     print (file)

def gunzip(gzipped_file_name, work_dir):
    "gunzip the given gzipped file"

    # see warning about filename
    filename = os.path.split(gzipped_file_name)[-1]
    filename = re.sub(r"\.gz$", "", filename, flags=re.IGNORECASE)

    with gzip.open(gzipped_file_name, 'rb') as f_in:  # <<========== extraction happens here
        with open(os.path.join(work_dir, filename), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
def read_url(url, local_path):
    url = url.replace(" ","%20")
    print('url: ' + url)
    url_path = urlparse(url).path
    print ('url_path: ' + url_path)
    Path(local_path + url_path).mkdir(parents=True, exist_ok=True)
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    for i in x:
        file_name = i.extract().get_text()
        file_href = ''
        try:
            file_href = i.extract().get('href')
            # if file_href.endswith('.csv'):
                # print ('file_href: ' + url_new + file_href)
        except:
            None
        url_new = url + file_name
        url_new = url_new.replace(" ","%20")
        if(file_name[-1]=='/' and file_name[0]!='.'):
            read_url(url_new, local_path)
        # if file_name.endswith('.csv'):
        #     print('url_new csv: ' + url_new)
        if file_name.endswith('..>') or file_name.endswith('.csv') or file_name.endswith('.gz'):
            url_path_to_file = urlparse(url).path
            print ('url_path_to_file: ' + url_path_to_file)
            url_wo_file = urlparse(url).scheme + '://' + urlparse(url).netloc + urlparse(url).path
            print ('url_wo_file: ' + url_wo_file)
            file_href = i.extract().get('href')
            print('file_href: ' + file_href)
            r = requests.get(url_wo_file + file_href, stream = True) 
            with open(local_path + url_path_to_file + file_href,"wb") as each_file: 
                each_file.write(r.content)
                if file_href.endswith(".gz"):
                    gunzip(local_path + url_path_to_file + file_href, local_path + url_path_to_file)


read_url("https://covidmap.umd.edu/umdcsvs/", 'C:/Dev/CSDC/')

input("Finished! Press Enter to close.")