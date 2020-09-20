import fuzzy_pandas
import pandas
import http.client, json, os, sys
from urllib.parse import urlparse


def ask_a_question(question):
    try:
        authoring_conn = http.client.HTTPSConnection(authoring_endpoint,port=443)
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key
        }
        authoring_conn.request ("GET", get_endpoint_key_method, "", headers)
        response = authoring_conn.getresponse ()
        endpoint_key = json.loads(response.read())["primaryEndpointKey"]

        runtime_conn = http.client.HTTPSConnection(runtime_endpoint,port=443)
        headers = {
            # Note this differs from the "Ocp-Apim-Subscription-Key"/<subscription key> used by most Cognitive Services.
            'Authorization': 'EndpointKey ' + endpoint_key,
            'Content-Type': 'application/json'
        }
        runtime_conn.request ("POST", query_kb_method, question, headers)
        response = runtime_conn.getresponse ()
        answer = response.read ()
        # print(json.dumps(json.loads(answer), indent=4))
        return json.loads(answer)

    except :
        print ("Unexpected error:", sys.exc_info()[0])
        print ("Unexpected error:", sys.exc_info()[1])


key_var_name = 'QNA_MAKER_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

authoring_endpoint_var_name = 'QNA_MAKER_ENDPOINT'
if not authoring_endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(authoring_endpoint_var_name))
# Note http.client.HTTPSConnection wants only the host name, not the protocol (that is, 'https://')
authoring_endpoint = urlparse(os.environ[authoring_endpoint_var_name]).netloc

runtime_endpoint_var_name = 'QNA_MAKER_RUNTIME_ENDPOINT'
if not runtime_endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(runtime_endpoint_var_name))
runtime_endpoint = urlparse(os.environ[runtime_endpoint_var_name]).netloc

kb_var_name = 'QNA_MAKER_KB_ID'
if not kb_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(kb_var_name))
kb_id = os.environ[kb_var_name]

get_endpoint_key_method = "/qnamaker/v4.0/endpointKeys"

query_kb_method = "/qnamaker/knowledgebases/" + kb_id + "/generateAnswer"

PATH = "C:/Dev/EPIC-QA/epic_qa_consumer_2020-06-10_v2.tar/"

papers_epic_qa_df = pandas.DataFrame(columns=['dirname', 'filename', 'url'])

print ('Loading papers ...')
for dirname, _, filenames in os.walk(PATH):
    for filename in filenames:
        if filename.endswith(".json")  :
            json_file = os.path.join(dirname, filename)
            # print("found json file: " + json_file)
            with open(json_file, 'rb') as f:
                all_papers_dict = json.load(f)
                for metadata_item in all_papers_dict['metadata'].items():
                    if metadata_item[0] == "url" and metadata_item[1] > "":
                        papers_epic_qa_df.loc[len(papers_epic_qa_df)] = [ dirname, filename, str(metadata_item[1]) ]
                        # print(str(metadata_item[1]))

# print ('papers_epic_qa_df: ')
# print (papers_epic_qa_df)

PATH = "C:/Dev/EPIC-QA/"

answers_df = pandas.DataFrame(columns=['question_id', 'question', 'answer', 'score', 'url'])
answer_i = 1
        
print ('Asking questions ...')
with open(PATH + 'consumer_questions_prelim.json', 'rb') as f:
    each_paper_dict = json.load(f)
    for each_question in each_paper_dict:
        # print(str(each_question['question_id']) + ' ' + str(each_question['question']))
# JSON format for passing question to service
        question = "{'question': '" + each_question['question'] + "','top': 100}"
        answers = ask_a_question(question)
        # answers = json.loads(answers_json)
        try:
            for answer_item in answers['answers']:
                source = str(answer_item['source'])
                # print ('source: ' + source)

                # print (str(answer_item))
                
                answers_df.loc[len(answers_df)] = [ each_question['question_id'], each_question['question'], answer_item['answer'] , str(answer_item['score']), answer_item['source'] ]

                answer_i = answer_i + 1

                # print ('len(answers_df): ' + str(len(answers_df)))
        except:
            None

        # if answer_i > 100:
        #     break

papers_answers_df = answers_df.merge(papers_epic_qa_df, on='url')
# print (papers_answers_df)

print ('Matching answers back to papers / sentences ...')
papers_answers_sentences_list = []

for index, papers_answers_row in papers_answers_df.iterrows():
    # print ('index: ' + str(index))
    papers_answers_row_df = pandas.DataFrame(columns=['question_id', 'question', 'answer', 'rank', 'score', 'url', 'dirname' , 'filename'])
    papers_answers_row_df.loc[0] = papers_answers_row
    # print("papers_answers_row_df : " )
    # print (papers_answers_row_df)
    json_file = os.path.join(papers_answers_row['dirname'], papers_answers_row['filename'])
    # print("papers_answers_row['answer'] : " )
    # print ( papers_answers_row['answer'])
    sentences_df = pandas.DataFrame(columns=['text', 'sentence_ids'])

    with open(json_file, 'rb') as f:
        all_papers_dict = json.load(f)
        for contexts_item in all_papers_dict['contexts']:
            # print("contexts_item['text'] : " )
            # print( contexts_item['text'])
            # if papers_answers_row['answer'] in contexts_item['text']:
            #     print(contexts_item['text'])
            sentences_df.loc[len(sentences_df)] = [ contexts_item['text'], contexts_item['sentences'][0]['sentence_id'] + ':' + contexts_item['sentences'][len(contexts_item['sentences'])-1]['sentence_id'] ]
    # print("sentences_df : " )
    # print(sentences_df)

    # fuzzy match answers back to sentence text to get the closest match
    matched_results = fuzzy_pandas.fuzzy_merge(papers_answers_row_df,
                                            sentences_df,
                                            left_on = ['answer'],
                                            right_on = ['text'],
                                            keep = 'all', # papers_answers_row_df.columns.to_list(),
                                            # keep_left = 'all', # papers_answers_row_df.columns.to_list(),
                                            # keep_right = 'all', # sentences_df.columns.to_list(),
                                            method = 'levenshtein',
                                            # left_id_col='rank',
                                            # right_id_col='sentence_ids',
                                            ignore_case=True)


    # print("matched_results : " )
    # print(matched_results)
    # matched_results.to_csv('C:/Dev/EPIC-QA/test.csv' )
    if len(matched_results.index) > 0:
        papers_answers_sentences_list.append(matched_results)
    # print ('len(papers_answers_sentences_list): ' + str(len(papers_answers_sentences_list)))

print ('Writing output files ...')
# print ('len(papers_answers_sentences_list): ' + str(len(papers_answers_sentences_list)))
# print ('str(papers_answers_sentences_list): ' + str(papers_answers_sentences_list))
papers_answers_sentences_df = pandas.concat(papers_answers_sentences_list, ignore_index=True) #, sort=False)
papers_answers_sentences_df = papers_answers_sentences_df.sort_values(['question_id', 'score'], ascending=[True, False])
papers_answers_sentences_df['rank'] = papers_answers_sentences_df \
    .assign(score=pandas.to_numeric(papers_answers_sentences_df['score'], errors='coerce')) \
    .groupby('question_id')['score'].rank('first', ascending=False)
papers_answers_sentences_df['rank'] = papers_answers_sentences_df['rank'].astype(int)
papers_answers_sentences_df = papers_answers_sentences_df.sort_values(['question_id', 'rank'])
print (papers_answers_sentences_df)
papers_answers_sentences_df.to_csv(PATH + 'EPIC-QA consumer question QnA Maker output.tsv',sep='\t', index=False)

# write file in EPIC-QA submission format
papers_answers_sentences_df['q'] = "Q0"
papers_answers_sentences_df['run_name'] = "CORONAWHY_1"
submission_columns = ['question_id', 'q', 'sentence_ids', 'rank', 'score', 'run_name']
submission_df = papers_answers_sentences_df[submission_columns]
submission_df.to_csv(PATH + 'EPIC-QA consumer question QnA Maker submission 01.tsv',sep='\t', index=False,header=False)

input('Finished! Press Enter to close.')
