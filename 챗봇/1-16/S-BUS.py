from flask import Flask, request
import pprint
import json
import random
import requests

pp = pprint.PrettyPrinter(width=41, compact=True)
app = Flask(__name__)


@app.route('/terminals', methods=['GET', 'POST'])
def process_webhook():
    # DialogFlow에서 query로 출발 터미널 이름을 받아와야 함
    request_json = request.json
    terminal = request_json.get('queryResult')["outputContexts"][0]["parameters"].get('terminal')
    terminal_dest = request_json.get('queryResult')["outputContexts"][0]["parameters"].get('terminal2')
    time = request_json["queryResult"]["queryText"]

    # 터미널 이름을 기준으로 terminals.json 파일을 읽음
    with open('./terminals.json')as json_file:
        json_data = json.load(json_file)
        #print(json_data[terminal])
    time_spend = random.randint(1, 6)

    fee = time_spend * 10000


    # 터미널이 가지고 있는 destination의 이름을 모두 가지고 와서 리스트 형식으로 리턴
    fulfillText = terminal + '에서 ' + terminal_dest + '로 가는 버스는 ' + time + '에 출발해서 ' + str(time_spend) +' 시간이 소요돼. 운임료는 ' + str(fee) +'원이야. 즐여'
    print(fulfillText)

    # dest_list = []
    # for item in json_data[terminal]:
    #     if item['destName'] != terminal:
    #         dest_list.append(item['destName'])
    # print(dest_list)
    return {"fulfillmentText" : fulfillText}

@app.route('/fee', methods=['GET', 'POST'])
def get_fee():
    request_json = request.json

if __name__ == '__main__':
    app.run(debug=True)
