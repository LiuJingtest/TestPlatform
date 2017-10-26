import requests
import json


def get_anyproxy_resp(data):
    host = data["host"]
    port = data["port"]
    req_id = data["req_id"]
    url = "http://"+host+":"+str(port)+"/fetchBody?id="+str(req_id)
    re = requests.get(url)
    re_body = re.json()
    re_body["content"] = json.loads(re_body["content"])
    return re_body
