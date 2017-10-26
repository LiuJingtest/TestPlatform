from AutoTestPlatform.apps.tools import jsontool
from ..models import Api, CaseSuite, Case


def get_api_list(data):
    """
    获取项目下的套件列表
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    test = Api.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_api_detail(data):
    """
    获取单个模块详情
    :param data:
    :return:
    """
    api_id = data['api_id']
    data = Api.objects.all().get(api_id=api_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_api(data):
    """
    新建接口
    :param data:
    :return: 无
    """
    Api.objects.create(**data)
    return {
        "code": 1,
        "msg": "创建接口成功",
    }


def edit_api(data):
    """
    编辑接口
    :param data:
    :return: 无
    """
    api_id = data['api_id']
    Api.objects.all().filter(api_id=api_id).update(**data)
    case_ob = {
        "case_url": data['api_url'],
        "case_method": data['api_method'],
        "param_type": data['param_type'],
        "case_protocol": data['api_protocol'],
    }
    Case.objects.filter(api_id=api_id).update(**case_ob)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_api(data):
    api_id = data["api_id"]
    Api.objects.all().get(api_id=api_id).delete()
    CaseSuite.objects.all().filter(api_id=api_id).delete()
    Case.objects.all().filter(api_id=api_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def get_api_case_list(data):
    api_id = data["api_id"]
    body = []
    test = Case.objects.all().filter(api_id=api_id)
    for a in test:
        a = jsontool.class_to_dict(a)
        suite_list = list(CaseSuite.objects.all().filter(case_id=a["case_id"]).values_list("suite_id", flat=True))
        del (a['_state'])
        a["suite_list"] = suite_list
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }
