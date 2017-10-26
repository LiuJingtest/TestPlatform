import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import result


def result_list(req):
    """
      获取项目所有的结果列表
      请求方法：post
      如：
      {
       "pro_id":1      项目id
       }
      :return:
      如：
      成功：
      {
      "data": [
        {
          "result_id": 39,
          "suite_id": 1,
          "start_time": "1478617457",
          "pass_num": 1,
          "report_name": "test",
          "end_time": "1478617457",
          "fail_num": 1,
          "pro_id": 1
        },
        {
          "result_id": 40,
          "suite_id": 1,
          "start_time": "1478617504",
          "pass_num": 1,
          "report_name": " 2016.11.08_ 冒烟测试 ",
          "end_time": "1478617505",
          "fail_num": 1,
          "pro_id": 1
        }
      ],
      "code": 1,
      "msg": "获取成功"
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = result.get_result_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_detail_list(req):
    """
      获取项目所有的结果列表
      请求方法：post
      如：
      {
       "result_id":50      结果id
       }
      :return:
      如：
      成功：
      {
      "code": 1,
      "data": [
        {
          "exp_data": "超时11",
          "pro_id": 5,
          "case_name": "正确登录",
          "api_id": 1,
          "module_id": 1,
          "is_pass": 0,
          "case_id": 1,
          "result_id": 50,
          "result_detail_id": 90,
          "is_set": 1,
          "check_type": 0,
          "input_data": "{'pro_id': 2}",
          "out_data": "{'content': {'msg': '请求超时', 'code': 0}, 'header': {'Content-Type': 'application/json', 'Date': 'Tue, 08 Nov 2016 16:04:39 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Server': 'WSGIServer/0.2 CPython/3.5.2'}, 'status_code': 200}",
          "case_desc": "正向验证"
        },
        {
          "exp_data": "超时",
          "pro_id": 5,
          "case_name": "密码错误",
          "api_id": 1,
          "module_id": 1,
          "is_pass": 1,
          "case_id": 2,
          "result_id": 50,
          "result_detail_id": 91,
          "is_set": 1,
          "check_type": 0,
          "input_data": " {\"username\": \"liujing\",\"pwd\":\"000000\"}",
          "out_data": "{'content': {'msg': '请求超时', 'code': 0}, 'header': {'Content-Type': 'application/json', 'Date': 'Tue, 08 Nov 2016 16:04:39 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Server': 'WSGIServer/0.2 CPython/3.5.2'}, 'status_code': 200}",
          "case_desc": "反向验证"
        }
      ],
      "msg": "返回成功"
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = result.get_result_detail_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_detail(req):
    """
      获取单个用例结果详情
      请求方法：post
      如：
      {
       "result_detail_id":50      结果用例id
       }
      :return:
      如：
      成功：
      {
      "data": {
        "out_data": {
          "response_data": {
            "header": {
              "Connection": "keep-alive",
              "Content-Type": "application/json",
              "Transfer-Encoding": "chunked",
              "X-Powered-By": "PHP/5.4.16",
              "Date": "Wed, 16 Nov 2016 06:22:24 GMT",
              "Server": "nginx/1.6.3"
            },
            "body": {
              "data": {},
              "msg": "用户名或者密码错误",
              "code": 20010
            }
          },
          "status_code": 200
        },
        "depnd_api_id": null,
        "module_id": 2,
        "input_data": {
          "url": "http://oa.supernano.com/index.php?r=api/login/login",
          "body": {
            "username": "liujing3@supernano.com",
            "pwd": "000000"
          }
        },
        "is_set": 1,
        "exp_data": "错误",
        "api_url": "{{host}}/index.php?r=api/login/login",
        "pro_id": 2,
        "case_id": 2,
        "api_method": "post",
        "api_desc": "无",
        "api_name": "登录接口",
        "api_type": "json",
        "api_id": 2,
        "result_detail_id": 163,
        "case_name": "错误登录-密码未加密",
        "is_pass": 1,
        "api_protocol": "http",
        "api_param": "username,pwd",
        "result_id": 94,
        "case_desc": "无",
        "check_type": null
      },
      "msg": "返回成功",
      "code": 1
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = result.get_result_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def result_delete(req):
    """
      删除结果
      请求方法：post
      如：
      {
       "result_id":50      结果id
       }
      :return:
      如：
      成功：
      {
      "code": 1,
      "msg": "删除成功"
    }
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = result.del_result(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")