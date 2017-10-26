# 处理全局变量相关的请求

from AutoTestPlatform.apps.tools import jsontool
from ..models import Vars, VarValue, Env


def create_vars(data):
    """
    创建变量
    :param data:
    :return:
    """
    try:
        var = data.copy()
        del (var["value"])
        if data['var_name'] == '':
            return {
                "code": 0,
                "msg": "变量名不能为空！"
            }
        var_id = Vars.objects.create(**var).var_id
        for value in data["value"]:
            value = {
                "env_id": value['env_id'],
                "var_value": value['var_value'],
                "var_id": var_id,
                "pro_id": data['pro_id']
            }
            VarValue.objects.create(**value)
        return {
            "code": 1,
            "msg": "创建变量成功！"
        }
    except Exception as e:

        return {
            "code": 0,
            "msg": "创建失败，参数错误！"
        }


def get_var_of_env(data):
    """
    获取变量在不同环境的所有值
    :param data:
    :return:
    """
    var_id = data["var_id"]
    body_list = []
    var_value_list = VarValue.objects.all().filter(var_id=var_id)
    var_info = jsontool.class_to_dict(Vars.objects.all().get(var_id=var_id))
    del (var_info['_state'])
    for var_value in var_value_list:
        a = jsontool.class_to_dict(var_value)
        b = jsontool.class_to_dict(Env.objects.all().get(env_id=a["env_id"]))
        var = dict(a, **b)
        del (var['_state'])
        del (var['id'])
        del (var['pro_id'])
        del (var['var_id'])
        body_list.append(var)
    body = {"value": body_list}
    body = dict(body, **var_info)
    return {
        "code": 1,
        "msg": "返回成功",
        "data": body
    }


def get_var_list(data):
    """
    获取变量信息列表
    :param data:
    :return:
    """
    pro_id = data["pro_id"]
    body = []
    var_list_ob = Vars.objects.all().filter(pro_id=pro_id)
    for var_ob in var_list_ob:
        a = jsontool.class_to_dict(var_ob)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "返回成功",
        "data": body
    }


def edit_var(data):
    var_id = data["var_id"]
    var = data.copy()
    del(var["value"])
    Vars.objects.all().filter(var_id=var["var_id"]).update(**var)
    for value in data["value"]:
        value = {
            "var_value": value['var_value'],
            "env_id": value["env_id"],
            "var_id": var_id,
            "pro_id": data['pro_id']
        }
        VarValue.objects.all().filter(var_id=var_id, env_id=value["env_id"]).delete()
        VarValue.objects.create(**value)
    return {
            "code": 1,
            "msg": "编辑变量成功！"
        }


def del_var(data):
    var_id = data["var_id"]
    Vars.objects.all().get(var_id=var_id).delete()
    VarValue.objects.all().filter(var_id=var_id).delete()
    return {
        "code": 1,
        "msg": "删除成功"
    }
