# 数据库处理工具
"""
@author:liujing
"""
import json


def convert_to_dict(obj):
    """
    把Object对象转换成Dict对象
    :param obj:
    :return:
    """
    dict_body = {}
    dict_body.update(obj.__dict__)
    return dict_body


def convert_to_dicts(obj_list):
    """
    对象列表转换为字典列表
    :param obj_list:
    :return:
    """
    obj_arr = []

    for o in obj_list:
        # 把Object对象转换成Dict对象
        dict_body = {}
        dict_body.update(o.__dict__)
        obj_arr.append(dict_body)

    return obj_arr


def class_to_dict(obj):
    """
    把对象(支持单个对象、list、set)转换成字典
    :param obj:
    :return:
    """
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


def str_to_json(str1):
    test = str1.replace("\'", "\"")
    return json.loads(test)
