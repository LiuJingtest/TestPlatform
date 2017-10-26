from django.shortcuts import HttpResponse
import json

from AutoTestPlatform.apps.InterfaceTest.datahandle import record


def record_anyproxy_req(req):
    """
        获取anyproxy录制的结果
        请求方法：post
        如：
        {
             req_id:5，    需要获取的请求的id
             host:"192.168.1.102",     本机的anyproxy服务器的host
             port:8002     GUI界面的端口地址（一般默认为8002）
         }
        :return:
        """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = record.get_anyproxy_resp(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")