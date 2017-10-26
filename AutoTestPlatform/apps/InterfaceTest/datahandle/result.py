from AutoTestPlatform.apps.tools import jsontool
from ..models import Result, ResultDetail, Case, Api, Suite, CheckModel

import json


def get_result_list(data):
    pro_id = data["pro_id"]
    body = []
    test = Result.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        b = jsontool.class_to_dict(Suite.objects.all().get(suite_id=a["suite_id"]))
        var = dict(a, **b)
        del (var['_state'])
        body.append(var)
    body.reverse()
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_result_detail_list(data):
    result_id = data["result_id"]
    body_list = []
    result_detail_list = ResultDetail.objects.all().filter(result_id=result_id)
    for result_datail in result_detail_list:
        a = jsontool.class_to_dict(result_datail)
        a["input_data"] = eval(a["input_data"])
        a["out_data"] = eval(a["out_data"])
        b = jsontool.class_to_dict(Case.objects.all().get(case_id=a["case_id"]))
        del (b['input_data'])
        c = jsontool.class_to_dict(Api.objects.all().get(api_id=a["api_id"]))
        if b["check_id"] != 0:
            checker = jsontool.class_to_dict(CheckModel.objects.all().get(check_id=b["check_id"]))
        else:
            checker = {
                "check_name":"",
                "check_desc":"默认",
                "check_code":"",
            }
        b = dict(b, **checker)
        var = dict(a, **b)
        var = dict(var, **c)
        del (var['_state'])
        if result_datail.is_pass !=2:
            var["out_data"]["response_data"]["body"] = json.dumps(var["out_data"]["response_data"]["body"])
            # var["out_data"]["response_data"]["header"] = str(var["out_data"]["response_data"]["header"]).replace("\'", "\"")
        body_list.append(var)
    body_list.sort(key=lambda api: api["api_id"], reverse=False)
    return {
        "code": 1,
        "msg": "返回成功",
        "data": body_list
    }


def get_result_detail(data):
    result_detail_id = data["result_detail_id"]
    result_detail = ResultDetail.objects.all().get(result_detail_id=result_detail_id)
    a = jsontool.class_to_dict(result_detail)
    a["input_data"] = jsontool.str_to_json(a["input_data"])
    a["out_data"] = jsontool.str_to_json(a["out_data"])
    b = jsontool.class_to_dict(Case.objects.all().get(case_id=a["case_id"]))
    del (b['input_data'])
    c = jsontool.class_to_dict(Api.objects.all().get(api_id=a["api_id"]))
    if b["check_id"] != 0:
        checker = jsontool.class_to_dict(CheckModel.objects.all().get(check_id=b["check_id"]))
    else:
        checker = {
            "check_name": "",
            "check_desc": "默认",
            "check_code": "",
        }
    b = dict(b, **checker)
    var = dict(a, **b)
    var = dict(var, **c)
    del (var['_state'])
    var["input_data"]["body"] = str(var["input_data"]["body"]).replace("\'", "\"")
    var["input_data"]["url"] = str(var["input_data"]["url"]).replace("\'", "\"")
    var["out_data"]["response_data"]["body"] = str(var["out_data"]["response_data"]["body"]).replace("\'", "\"")
    var["out_data"]["response_data"]["header"] = str(var["out_data"]["response_data"]["header"]).replace("\'", "\"")
    return {
        "code": 1,
        "msg": "返回成功",
        "data": var
    }


def del_result(data):
    result_id = data["result_id"]
    Result.objects.all().get(result_id=result_id).delete()
    ResultDetail.objects.all().filter(result_id=result_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }