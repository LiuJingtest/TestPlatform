import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import vars


def var_list(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vars.get_var_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vars.get_var_of_env(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_create(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vars.create_vars(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_edit(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vars.edit_var(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def var_del(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = vars.del_var(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")