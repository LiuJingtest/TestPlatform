import json

from AutoTestPlatform.apps.tools import strtool
from .req import ReqResp
from ...models import DepndApi
from AutoTestPlatform.apps.tools import jsonpath


class Interface(ReqResp):
    case = object
    depnd_api = object

    def __init__(self, D_api_id, var_map):
        ReqResp.__init__(self)
        self.depnd_api_id = D_api_id
        self.depnd_api = DepndApi.objects.all().get(depnd_api_id=self.depnd_api_id)
        self.url = self.depnd_api.depnd_api_url
        self.param = self.depnd_api.depnd_api_param
        self.protocol = self.depnd_api.depnd_api_protocol
        self.depnd_api_id = self.depnd_api.depnd_id
        self.method = self.depnd_api.depnd_api_method
        self.var_map = var_map
        self.pro_id = self.depnd_api.pro_id
        if "host" in var_map.keys():
            self.url = self.protocol + "://" + self.var_map["host"]+self.url
        else:
            self.url = self.protocol + "://" + self.url
        if "headers" in var_map.keys():
            self.req_headers = json.loads(self.var_map["headers"])
        if "encode" in var_map.keys():
            self.encode_type = self.var_map["encode"]

    def handle_depnd_param(self):
        while "$." in self.param:
            path = strtool.str_replace(self.param, 2)
            self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
            self.d_api.run()
            self.param = self.param.replace(path, str(self.d_api.get_param_value(path)))

    def get_param_value(self, param_path):
        return jsonpath.jsonpath(self.resp["response_data"]["body"], param_path)[0]

