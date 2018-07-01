from flask import Flask, request,jsonify
import json
import requests

app=Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return "Service is running"

@app.route('/stat',methods=['POST'])
def pull_request():
    req=request.json
    url=req['url']
    url=list(url)
    url.insert(10,'/repos')
    url="".join(url)
    print(url)
    url="https://api."+url+"/pulls"
    output=requests.get(url)
    list_pull=json.loads(output.content)
    list_pull_two=[{'id':x['id'],'status':x['state']} for x in list_pull]
    return jsonify(list_pull_two)

if __name__=='__main__':
    app.run(port=9999,debug=True)