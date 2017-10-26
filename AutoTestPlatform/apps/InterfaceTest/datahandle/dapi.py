import json

from AutoTestPlatform.apps.tools import casetool
from ..base.case.dapi import Interface
from ..models import DepndApi, Case
from AutoTestPlatform.apps.tools import jsontool


def get_dapi_list(data):
    """
    获取项目下的套件列表
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    test = DepndApi.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_dapi_detail(data):
    """
    获取单个模块详情
    :param data:
    :return:
    """
    depnd_api_id = data['depnd_api_id']
    data = DepndApi.objects.all().get(depnd_api_id=depnd_api_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_dapi(data):
    """
    新建依赖接口
    :param data:
    :return: 无
    """
    pro_id = data['pro_id']
    depnd_api_name = data['depnd_api_name']
    depnd_api_protocol = data['depnd_api_protocol']
    depnd_api_method = data['depnd_api_method']
    depnd_api_url = data['depnd_api_url']
    depnd_api_type = data['depnd_api_type']
    depnd_api_desc = data['depnd_api_desc']
    depnd_api_param = data['depnd_api_param']
    depnd_id = data['depnd_id']
    DepndApi.objects.create(pro_id=pro_id, depnd_api_name=depnd_api_name,depnd_api_desc=depnd_api_desc,
                            depnd_api_method=depnd_api_method, depnd_api_param=depnd_api_param,
                            depnd_api_protocol=depnd_api_protocol, depnd_api_url=depnd_api_url,
                            depnd_api_type=depnd_api_type,depnd_id=depnd_id)
    return {
        "code": 1,
        "msg": "创建成功",
    }


def edit_dapi(data):
    """
    编辑依赖接口
    :param data:
    :return: 无
    """
    pro_id = data['pro_id']
    depnd_api_id = data['depnd_api_id']
    depnd_api_name = data['depnd_api_name']
    depnd_api_protocol = data['depnd_api_protocol']
    depnd_api_method = data['depnd_api_method']
    depnd_api_url = data['depnd_api_url']
    depnd_api_type = data['depnd_api_type']
    depnd_api_desc = data['depnd_api_desc']
    depnd_api_param = data['depnd_api_param']
    depnd_id = data['depnd_id']
    DepndApi.objects.all().filter(depnd_api_id=depnd_api_id).update(
        pro_id=pro_id, depnd_api_name=depnd_api_name,
        depnd_api_desc=depnd_api_desc, depnd_api_method=depnd_api_method, depnd_api_param=depnd_api_param,
        depnd_api_protocol=depnd_api_protocol, depnd_api_url=depnd_api_url, depnd_api_type=depnd_api_type,
        depnd_id=depnd_id)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_dapi(data):
    depnd_api_id = data['depnd_api_id']
    a = list(Case.objects.all().filter(depnd_api_id=depnd_api_id))
    b = list(DepndApi.objects.all().filter(depnd_id=depnd_api_id))
    if len(a) != 0 or len(b) != 0:
        return {
            "code": 0,
            "msg": "有依赖该接口的用例或是依赖接口，不能被删除"
        }
    else:
        DepndApi.objects.all().get(depnd_api_id=depnd_api_id).delete()
        return {
            "code": 1,
            "msg": "删除成功"
        }


def run_d_api(data):
    depnd_api_id = data['depnd_api_id']
    env_id = data["env_id"]
    var_map = casetool.get_env_var_map(env_id)
    c = Interface(depnd_api_id, var_map=var_map)
    c.handle_depnd_param()
    c.run()
    return {
        "code": 1,
        "msg": "运行成功",
        "data": {
            "url": c.url,
            "request_body": c.param,
            "status": c.resp["status_code"],
            "header": json.dumps(dict(c.resp["response_data"]["header"],ensure_ascii=False)),
            "response_body": json.dumps(c.resp["response_data"]["body"],ensure_ascii=False),
        }
    }
