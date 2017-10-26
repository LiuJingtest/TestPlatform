from AutoTestPlatform.apps.tools import jsontool
from ..models import Case, Suite, CaseSuite


def get_suite_list(data):
    """
    获取项目下的套件列表
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    test = Suite.objects.all().filter(pro_id=pro_id)
    for a in list(test):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_suite_detail(data):
    """
    获取单个模块详情
    :param data:
    :return:
    """
    suite_id = data['suite_id']
    data = Suite.objects.all().get(suite_id=suite_id)
    data_json = jsontool.convert_to_dict(data)
    del(data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def create_suite(data):
    """
    新建模块
    :param data:
    :return: 无
    """
    pro_id = data["pro_id"]
    suite_name = data['suite_name']
    suite_desc = data['suite_desc']
    Suite.objects.create(pro_id=pro_id, suite_name=suite_name, suite_desc=suite_desc)
    return {
        "code": 1,
        "msg": "创建套件成功",
    }


def edit_suite(data):
    """
    编辑项目
    :param data:
    :return: 无
    """
    suite_id = data["suite_id"]
    suite_name = data['suite_name']
    suite_desc = data['suite_desc']
    Suite.objects.all().filter(suite_id=suite_id).update(suite_name=suite_name, suite_desc=suite_desc)
    return {
        "code": 1,
        "msg": "修改成功"
    }


def del_suite(data):
    suite_id = data["suite_id"]
    Suite.objects.all().get(suite_id=suite_id).delete()
    CaseSuite.objects.all().filter(suite_id=suite_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }


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

