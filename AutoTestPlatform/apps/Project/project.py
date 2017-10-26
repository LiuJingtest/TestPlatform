from AutoTestPlatform.apps.Project.models import Project
from AutoTestPlatform.apps.tools import jsontool


def get_pro_list():
    """
    获取所有的项目
    :return: 所有的项目，类型为列表
    """
    try:
        body = []
        test = Project.objects.all()
        for a in list(test):
            a = jsontool.class_to_dict(a)
            del (a['_state'])
            body.append(a)
        return {
            "code": 1,
            "msg": "获取成功",
            "data": body
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "msg": "获取失败",
        }


def get_pro_detail(data):
    """
    获取单个项目详情
    :param data:
    :return:
    """
    try:
        pro_id = data['pro_id']
        data = Project.objects.all().get(pro_id=pro_id)
        data_json = jsontool.convert_to_dict(data)
        del(data_json['_state'])
        return {
            "code": 1,
            "msg": "获取成功",
            "data": data_json
        }
    except Exception as e:
        return {
            "code": 0,
            "msg": "请求超时",
        }


def create_pro(data):
    """
    新建项目
    :param data:
    :return: 无
    """
    try:
        if data['pro_name'] == '':
            return {
                "code": 0,
                "msg": "项目名不能为空！"
            }
        Project.objects.create(**data)
        return {
                "code": 1,
                "msg": "项目创建成功"
            }
    except Exception:
        return {
                "code": 0,
                "msg": "项目创建失败"
            }


def edit_pro(data):
    """
    编辑项目
    :param data:
    :return: 无
    """
    try:
        if data['pro_name'] == '':
            return {
                "code": 0,
                "msg": "项目名不能为空！"
            }
        a = Project.objects.all().filter(pro_id=data['pro_id']).update(**data)
        if a == 0:
            return {
                "code": 0,
                "msg": "修改失败，项目id不存在！"
            }
        return {
            "code": 1,
            "msg": "修改成功"
        }
    except Exception:
        return {
            "code": 0,
            "msg": "参数错误"
        }


def del_pro(data):
    """
    删除项目
    :param data:
    :return:无
    """
    try:
        pro_id = data['pro_id']
        pro = Project.objects.all().get(pro_id=pro_id)
        pro.delete()
        return {
            "code": 1,
            "msg": "删除成功"
        }
    except Exception as e:
        return {
            "code": 0,
            "msg": "请求超时"
        }
