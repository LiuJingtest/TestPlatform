import json
import re

from jsonschema import validate, ValidationError, SchemaError, FormatError

from AutoTestPlatform.apps.tools import functool
from .dapi import Interface
from .req import ReqResp
from ...models import CheckModel, Case, ResultDetail
from AutoTestPlatform.apps.tools import dbtool, Constant


class CaseEntity(ReqResp):

    result_id = 0
    result_detail = object
    is_pass = 0
    case = object
    d_api = object
    depnd_api_id = 0
    exp_status = 200
    status_result = 2
    exp_header = ""
    header_result = 2
    exp_data = ""
    check_id = 0
    body_result = 2
    schema = {}
    schema_result = 2
    schema_msg = ""
    err_msg = ""
    front_sql = ""
    rear_sql = ""

    def __init__(self, case_id, var_map, result_id):
        ReqResp.__init__(self)
        if result_id != 0:
            self.result_id = result_id
            self.result_detail = ResultDetail.objects.create(result_id=self.result_id)
        self.case = Case.objects.all().get(case_id=case_id)
        self.url = self.case.case_url
        self.param = self.case.input_data
        self.protocol = self.case.case_protocol
        self.depnd_api_id = self.case.depnd_api_id
        self.method = self.case.case_method
        self.var_map = var_map
        self.pro_id = self.case.pro_id
        # self.url = self.protocol + "://" + self.var_map["host"]+self.url
        self.url = self.protocol + "://" +self.url
        self.exp_data = self.case.exp_data
        self.resp_type = self.case.param_type
        self.schema = self.case.case_schema
        self.check_id = self.case.check_id
        self.exp_status = self.case.exp_status
        self.exp_header = self.case.exp_header
        if self.case.front_sql != None:
            self.front_sql = self.case.front_sql
        if self.case.rear_sql != None:
            self.rear_sql = self.case.rear_sql
        if "headers" in var_map.keys():
            self.req_headers = json.loads(self.var_map["headers"])
        if "encode" in var_map.keys():
            self.encode_type = self.var_map["encode"]

    def handle_depnd_param(self):
        while re.search(Constant.PATTERN_TYPE3, self.param):
            self.d_api = Interface(self.depnd_api_id, var_map=self.var_map)
            self.d_api.handle_depnd_param()
            self.d_api.run()
            self.param = re.sub(Constant.PATTERN_TYPE3,
                                str(self.d_api.get_param_value(re.search(Constant.PATTERN_TYPE3, self.param).group())),
                                self.param, 1)

    def check_status(self):
        # 0-----未通过，1-----通过，2-----未检验, 3------错误
        if self.exp_status != 0:
            try:
                self.status_result = int((lambda x, y: x == y)(self.exp_status,self.resp["status_code"]))
            except:
                self.status_result = 3
        else:
            self.status_result = 2

    def check_header(self):
        self.header_result = 2

    def check_schema(self):
        # 0-----未通过，1-----通过，2-----未检验, 3------错误
        if self.schema != "" and self.schema is not None:
            try:
                self.schema = json.loads(self.schema)
                validate(self.resp["response_data"]["body"], self.schema)
                self.schema_result = 1
                self.schema_msg = "校验通过"
            except ValidationError as e:
                msg = str(e).split("\nFailed validating")[0]
                self.schema_msg = "校验失败，失败原因："+str(msg)
                self.schema_result = 0
            except SchemaError:
                self.schema_result = 3
                self.schema_msg = "校验异常，请检查schema是否正确"
            except FormatError:
                self.schema_result = 3
                self.schema_msg = "校验异常，请检查schema是否正确"
            except Exception:
                self.schema_result = 3
                self.schema_msg = "校验异常，请检查schema是否正确"
        else:
            self.schema_result = 2
            self.schema_msg = "未进行schema校验"

    def check_result(self):
        if self.exp_data != "":
            try:
                check_name, check_code = self.set_check_code()
                result1 = functool.get_return(check_name, check_code)
                if result1.find("True") != -1:
                    self.body_result = 1
                else:
                    self.body_result = 0
            except Exception as e:
                self.body_result = 3
                self.err_msg += "\n"+str(e)
        else:
            self.body_result = 2

    def save_result(self):
        if self.resp_type != "json":
            if self.param is not None and self.param != '':
                self.param = json.loads(self.param)
        input_data = {
            "url": self.url,
            "body": self.param
        }
        self.result_detail.case_id = self.case.case_id
        self.result_detail.api_id = self.case.api_id
        self.result_detail.input_data = input_data
        self.result_detail.out_data = self.resp
        self.result_detail.is_pass = self.is_pass
        self.result_detail.schema_check = self.schema_result
        self.result_detail.body_check = self.body_result
        self.result_detail.header_check = self.header_result
        self.result_detail.status_check = self.status_result
        self.result_detail.schema_msg = self.schema_msg
        self.result_detail.err_msg = self.err_msg
        self.result_detail.save()

    def set_is_pass(self, flag):
        if flag:
            if self.schema_result==3 or self.body_result==3 or self.status_result==3 or self.header_result==3:
                self.is_pass = 2
            elif self.schema_result==0 or self.body_result==0 or self.status_result==0 or self.header_result==0:
                self.is_pass = 0
            else:
                self.is_pass = 1
        else:
            self.is_pass = 2

    def get_is_pass(self):
        return self.is_pass

    def set_check_code(self):
        if self.check_id == 0:
            check_ob = CheckModel.objects.all().get(check_id=1)
        else:
            check_ob = CheckModel.objects.all().get(check_id=self.check_id)
        check_name = check_ob.check_name
        check_code = check_ob.check_code + '\nprint('+check_name+'(\''+ self.exp_data +'\',\''+ json.dumps(self.resp["response_data"]["body"]) + '\'))'
        return check_name, check_code

    def run_front_sql(self):
        if self.front_sql != "":
            with dbtool.connDB(**json.loads(self.var_map["DB"])) as db_cursor:
                db_cursor.execute(self.front_sql)

    def run_rear_sql(self):
        if self.rear_sql != "":
            with dbtool.connDB(**json.loads(self.var_map["DB"])) as db_cursor:
                db_cursor.execute(self.rear_sql)
