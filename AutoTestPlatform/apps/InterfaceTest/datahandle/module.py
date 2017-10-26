from AutoTestPlatform.apps.tools import jsontool
from ..models import Module, Api, Case


def get_module_list(data):
    """
    获取项目下的模块列表
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    test = Module.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_module_detail(data):
    """
    获取单个模块详情
    :param data:
    :return:
    """
    module_id = data['module_id']
    data = Module.objects.all().get(module_id=module_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_module(data):
    """
    新建模块
    :param data:
    :return: 无
    """
    pro_id = data["pro_id"]
    module_name = data['module_name']
    module_desc = data['module_desc']
    Module.objects.create(pro_id=pro_id, module_name=module_name, module_desc=module_desc)
    return {
        "code": 1,
        "msg": "创建模块成功",
    }


def edit_module(data):
    """
    编辑项目
    :param data:
    :return: 无
    """
    module_id = data["module_id"]
    module_name = data['module_name']
    module_desc = data['module_desc']
    a = Module.objects.all().filter(module_id=module_id).update(module_name=module_name, module_desc=module_desc)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_module(data):
    module_id = data["module_id"]
    Module.objects.all().get(module_id=module_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


def get_module_api_list(data):
    module_id = data["module_id"]
    body = []
    test = Api.objects.all().filter(module_id=module_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_module_case_list(data):
    module_id = data["module_id"]
    body = []
    test = Case.objects.all().filter(module_id=module_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }
