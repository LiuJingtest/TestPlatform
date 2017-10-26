import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import env


def env_list(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.get_env_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.get_env_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_create(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.create_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_edit(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.edit_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_del(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.del_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def env_var_list(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = env.get_env_varList(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")