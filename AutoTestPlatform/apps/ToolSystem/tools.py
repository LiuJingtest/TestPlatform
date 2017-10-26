from json import JSONDecodeError

import requests
import json

from requests.exceptions import MissingSchema


def request_repeat(data):
    try:
        url = data["url"]
        body = data["body"]
        header = data["header"]
        if header != '':
            header = json.loads(header)
        num = int(data["num"])
        method = data["method"]
        for i in range(0, num):
            requests.request(method=method, url=url, headers=header, data=body)
        return {
            "code": 1,
            "msg": "运行完毕",
        }
    except JSONDecodeError:
        return {
            "code": 0,
            "msg": "请求头类型错误，请使用规范的json格式",
        }
    except MissingSchema:
        return {
            "code": 0,
            "msg": "url格式错误",
        }
    except Exception:
        return {
            "code": 0,
            "msg": "运行异常",
        }
