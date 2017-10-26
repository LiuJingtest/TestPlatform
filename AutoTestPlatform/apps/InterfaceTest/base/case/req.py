import re

import requests

from AutoTestPlatform.apps.tools import functool
from ...models import Functions
from AutoTestPlatform.apps.tools import Constant


class ReqResp:

    pro_id = 0
    var_map = {}
    url = ""
    param = ""
    method = ""
    protocol = ""
    resp = {}
    req_headers = {}
    encode_type = "utf-8"
    resp_type = ""

    def __init__(self):
        pass

    def setUrl(self):
        while re.search(Constant.PATTERN_TYPE1, self.url):
            re_str = re.search(Constant.PATTERN_TYPE1, self.url).group()
            self.url = re.sub(Constant.PATTERN_TYPE1, self.var_map[re_str[2:-2]], self.url)

    def setReqParam(self):
        while re.search(Constant.PATTERN_TYPE1, self.param):
            re_str = re.search(Constant.PATTERN_TYPE1, self.param).group()
            self.param = re.sub(Constant.PATTERN_TYPE1, self.var_map[re_str[2:-2]], self.param)
        while re.search(Constant.PATTERN_TYPE2, self.param):
            re_str = re.search(Constant.PATTERN_TYPE2, self.param).group()
            func_name = re.search("\\w+",re_str).group()
            func_code = self.setFuncCode(func_name, re_str[2:-2])
            self.param = re.sub(Constant.PATTERN_TYPE2, functool.get_return(func_name, func_code), self.param)

    def sendRequest(self):
        method_type = self.getMethodType()
        if method_type == 1:
            req = requests.request(method=self.method, url=self.url, params=self.param, headers=self.req_headers,
                                   verify=False)
        elif method_type == 2:
            req = requests.request(method=self.method, url=self.url, data=self.param.encode(self.encode_type),
                                   headers=self.req_headers, verify=False)
        if req.status_code == 200 or req.status_code == 304:
            self.resp = {
                "status_code": req.status_code,
                "response_data": {
                    "body": req.json()
                }
            }
        else:
            self.resp = {
                "status_code": req.status_code,
                "response_data": {
                    "body": ""
                }
            }

    def setFuncCode(self, func_name, func_str_re):
        func = Functions.objects.all().get(pro_id=self.pro_id, func_name=func_name)
        func_code = func.func_code + '\nprint('+ func_str_re + ')'
        return func_code

    def setRespDefault(self):
        self.resp = {
            "status_code": 404,
            "response_data": {
                "header": "",
                "body": ""
            }
        }

    def getMethodType(self):
        if self.method.lower() == "get":
            return 1
        if self.method.lower() == "post":
            return 2

    def run(self):
        self.setUrl()
        self.setReqParam()
        self.sendRequest()