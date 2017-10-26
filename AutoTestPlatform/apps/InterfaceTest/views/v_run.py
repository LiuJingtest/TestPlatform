import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import caserun


def run(req):
    """
   运行用例
   请求方法：post
   如：
    {
    "pro_id":1,        case_id
    "suite_id":2,      case类型，手动为1，录制为2
    "env_id":4          环境id
    "report_name":"123123"
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = caserun.get_run_info(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")