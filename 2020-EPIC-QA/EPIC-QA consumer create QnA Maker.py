# EIPC-QA consumer list urls.py
# Lists the url tags found in the consumer documents

import json
import os
import pandas
import shutil

import http.client
import time
from urllib.parse import urlparse

# get list of urls to be added to QnA Maker
PATH = "C:/Dev/EPIC-QA/epic_qa_consumer_2020-06-10_v2.tar/"
# uncomment lines below to delete the target directory
# try:
#     shutil.rmtree(PATH + "coronawhy-sciSpacy")
# except:
#     p = ""

urls = []

for dirname, _, filenames in os.walk(PATH):
    for filename in filenames:
        if filename.endswith(".json")  :
            json_file = os.path.join(dirname, filename)
            # print("found json file: " + json_file)
            with open(json_file, 'rb') as f:
                each_paper_dict = json.load(f)
                for metadata_item in each_paper_dict['metadata'].items():
                    if metadata_item[0] == "url" and metadata_item[1] > "":
                        urls.append(metadata_item[1])

# print (str(urls))


key_var_name = 'QNA_MAKER_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

authoring_endpoint_var_name = 'QNA_MAKER_ENDPOINT'
if not authoring_endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(authoring_endpoint_var_name))
# Note http.client.HTTPSConnection wants only the host name, not the protocol (that is, 'https://')
authoring_endpoint = urlparse(os.environ[authoring_endpoint_var_name]).netloc


def format_content(kb_model, urls):

    # Convert the request to a string.
    content = json.dumps(kb_model)

    content = str.replace(content, '"urls": []' , '"urls": ' + str(urls))

    print(content)
    return content

def pretty_print(content):
  # Note: We convert content to and from an object so we can pretty-print it.
  return json.dumps(json.loads(content), indent=4)

def call_qna_method(qna_method, content, REST_verb):
  print('Calling ' + REST_verb + ' ' + authoring_endpoint + qna_method + '.')
  headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json',
    'Content-Length': len (content)
  }
  conn = http.client.HTTPSConnection(authoring_endpoint)
  conn.request (REST_verb, qna_method, content, headers)
  response = conn.getresponse ()

  return response.getheader('Location'), response.read ()

def check_status(check_status_method):
  print('Calling ' + authoring_endpoint + check_status_method + '.')
  headers = {'Ocp-Apim-Subscription-Key': subscription_key}
  conn = http.client.HTTPSConnection(authoring_endpoint)
  conn.request("GET", check_status_method, None, headers)
  response = conn.getresponse ()
  return response.read ()

def call_and_wait_qna_method(qna_method, content, REST_verb):
    operation, result = call_qna_method(qna_method, content, REST_verb)
    print(str(result))
    print(pretty_print(result))

    # Add operation ID to URL route
    check_status_method = '/qnamaker/v4.0' + operation

    # Set done to false
    done = False

    # Continue until done
    while False == done:

        # Gets the status of the operation.
        status = check_status(check_status_method)

        # Print status checks in JSON with presentable formatting
        print(pretty_print(status))

        # Convert the JSON response into an object and get the value of the operationState field.
        state = json.loads(status)['operationState']

        # If the operation isn't finished, wait and query again.
        if state == 'Running' or state == 'NotStarted':
            print('Waiting 30 seconds...')
            time.sleep(30)
        else:
            done = True # request has been processed, if successful, knowledge base is created
    try:
        result = json.loads(status)['resourceLocation']
    except:
        result = "no resourceLocation found"
    return result

# main ##################

kb_model = {
    "name": "EPIC-QA-Consumer",
    "qnaList": [],
    "urls": [],
    "files": []
    }
content = format_content (kb_model, urls[:10])
qna_method = '/qnamaker/v4.0/knowledgebases/create'
kb_id = call_and_wait_qna_method(qna_method, content, 'POST')

kb_model = {
    "add": {
        "qnaList": [],
        "urls": [],
        "files": []
        }
    }
qna_method = '/qnamaker/v4.0' + kb_id
for i in range(11,len(urls), 5):
    content = format_content (kb_model, urls[i:i+5])
    call_and_wait_qna_method(qna_method, content, 'PATCH')

