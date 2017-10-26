import json

from AutoTestPlatform.apps.tools import casetool
from ..base.case.case import CaseEntity
from ..models import Api, CaseSuite, Case, DepndApi
from AutoTestPlatform.apps.tools import jsontool


def get_suite_case_list(data):
    suite_id = data["suite_id"]
    body = []
    test = CaseSuite.objects.all().filter(suite_id=suite_id)
    for a in list(test):
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a.case_id))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_api_case_list(data):
    api_id = data["api_id"]
    body = []
    test = list(set(CaseSuite.objects.all().filter(api_id=api_id).values_list("case_id", flat=True)))
    for a in test:
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_pro_case_list(data):
    pro_id = data["pro_id"]
    body = []
    test = list(set(CaseSuite.objects.all().filter(pro_id=pro_id).values_list("case_id", flat=True)))
    for a in test:
        a = jsontool.class_to_dict(Case.objects.all().get(case_id=a))
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_case_detail(data):
    case_id = data["case_id"]
    data_case = jsontool.convert_to_dict(Case.objects.all().get(case_id=case_id))
    data_api = jsontool.convert_to_dict(Api.objects.all().get(api_id=data_case["api_id"]))
    del (data_api['_state'])
    if data_case["depnd_api_id"] != 0:
        depnt_api = jsontool.convert_to_dict(DepndApi.objects.all().get(depnd_api_id=data_case["depnd_api_id"]))
        del (depnt_api['_state'])
        data_case["depnt_api"] = depnt_api
    data_case["api"] = data_api
    del (data_case['_state'])
    suite_list = list(CaseSuite.objects.all().filter(case_id=case_id).values_list("suite_id", flat=True))
    data_case["suite_list"] = suite_list
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_case
    }


def create_case(data):
    case = data.copy()
    del(case["suite_list"])
    case_id = Case.objects.create(**case).case_id
    suite_list_data = data['suite_list']
    case_suite = {
        "pro_id": data['pro_id'],
        "api_id": data['api_id'],
        "case_id": case_id
    }
    for suite_id in suite_list_data:
        case_suite["suite_id"] = suite_id
        CaseSuite.objects.create(**case_suite)
    return {
        "code": 1,
        "msg": "保存成功",
        "data":{
            "case_id": case_id
        }
    }


def edit_case(data):
    case_id = data['case_id']
    case = data.copy()
    del (case["suite_list"])
    Case.objects.all().filter(case_id=case_id).update(**case)
    CaseSuite.objects.all().filter(case_id=case_id).delete()
    suite_list_data = data['suite_list']
    case_suite = {
        "pro_id": data['pro_id'],
        "api_id": data['api_id'],
        "case_id": case_id
    }
    for suite_id in suite_list_data:
        case_suite["suite_id"] = suite_id
        CaseSuite.objects.create(**case_suite)
    return {
            "code": 1,
            "msg": "保存成功"
        }


def del_case(data):
    case_id = data['case_id']
    Case.objects.all().get(case_id=case_id).delete()
    CaseSuite.objects.all().filter(case_id=case_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def run_case(data):
    case_id = data['case_id']
    env_id = data["env_id"]
    var_map = casetool.get_env_var_map(env_id)
    c = CaseEntity(case_id, var_map, 0)
    c.run_front_sql()
    c.handle_depnd_param()
    c.run()
    c.check_schema()
    c.check_result()
    c.check_status()
    c.check_header()
    c.run_rear_sql()
    return {
        "code": 1,
        "msg": "运行成功",
        "data": {
            "url": c.url,
            "request_body": c.param,
            "status": c.resp["status_code"],
            "exp_status": c.exp_status,
            "status_check": c.status_result,
            # "header": json.dumps(dict(c.resp["response_data"]["header"],ensure_ascii=False)),
            "exp_header": c.exp_header,
            "header_check": c.header_result,
            "response_body": json.dumps(c.resp["response_data"]["body"],ensure_ascii=False),
            "exp_data": c.exp_data,
            "body_check": c.body_result,
            "schema": json.dumps(c.schema),
            "schema_check": c.schema_result,
            "schema_msg": c.schema_msg
        }
    }
