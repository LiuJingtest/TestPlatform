from django.conf.urls import url
from AutoTestPlatform.apps.InterfaceTest.views import v_project, v_env, v_vars, v_func, v_checker,\
    v_module, v_suite, v_api, v_case, v_run, v_result, v_dapi, v_record, v_plan

urlpatterns = [
    url(r'project/list$', v_project.pro_list, name="获取项目列表"),
    url(r'project/detail$', v_project.pro_detail, name="获取项目详情"),
    url(r'project/create$', v_project.pro_create, name="创建项目"),
    url(r'project/edit$', v_project.pro_edit, name="修改编辑项目"),
    url(r'project/delete$', v_project.pro_del, name="删除项目"),

    url(r'project/env/list$', v_env.env_list, name="获取环境列表"),
    url(r'project/env/detail$', v_env.env_detail, name="获取环境详情"),
    url(r'project/env/create$', v_env.env_create, name="创建环境"),
    url(r'project/env/edit$', v_env.env_edit, name="修改编辑环境"),
    url(r'project/env/delete$', v_env.env_del, name="删除环境"),
    url(r'project/env/varList$', v_env.env_var_list, name="获取特定环境下所有变量列表"),

    url(r'project/var/list$', v_vars.var_list, name="获取变量列表"),
    url(r'project/var/detail$', v_vars.var_detail, name="获取变量详情"),
    url(r'project/var/create$', v_vars.var_create, name="创建变量"),
    url(r'project/var/edit$', v_vars.var_edit, name="修改编辑变量"),
    url(r'project/var/delete$', v_vars.var_del, name="删除变量"),

    url(r'project/func/create$', v_func.func_create, name="创建方法"),
    url(r'project/func/list$', v_func.func_list, name="获取方法列表"),
    url(r'project/func/detail$', v_func.func_detail, name="获取方法详情"),
    url(r'project/func/edit$', v_func.func_edit, name="编辑方法"),
    url(r'project/func/delete$', v_func.func_delete, name="删除方法"),
    url(r'project/func/run$', v_func.func_run, name="运行方法"),

    url(r'project/check/create$', v_checker.check_create, name="创建方法"),
    url(r'project/check/list$', v_checker.check_list, name="获取方法列表"),
    url(r'project/check/detail$', v_checker.check_detail, name="获取方法详情"),
    url(r'project/check/edit$', v_checker.check_edit, name="编辑方法"),
    url(r'project/check/delete$', v_checker.check_delete, name="删除方法"),
    url(r'project/check/run$', v_checker.check_run, name="运行方法"),

    url(r'project/module/list$', v_module.module_list, name="获取模块列表"),
    url(r'project/module/detail$', v_module.module_detail, name="获取模块详情"),
    url(r'project/module/create$', v_module.module_create, name="创建模块"),
    url(r'project/module/edit$', v_module.module_edit, name="编辑修改模块"),
    url(r'project/module/delete$', v_module.module_del, name="删除模块"),
    url(r'project/module/apiList$', v_module.module_api_list, name="获取模块下的接口列表"),
    url(r'project/module/caseList$', v_module.module_case_list, name="获取模块下的用例列表"),

    url(r'project/suite/list$', v_suite.suite_list, name="获取套件列表"),
    url(r'project/suite/detail$', v_suite.suite_detail, name="获取套件详情"),
    url(r'project/suite/create$', v_suite.suite_create, name="创建套件"),
    url(r'project/suite/edit$', v_suite.suite_edit, name="编辑修改套件"),
    url(r'project/suite/delete$', v_suite.suite_del, name="删除套件"),
    url(r'project/suite/caseList$', v_suite.suite_case_list, name="获取套件下的case列表"),

    url(r'project/api/list$', v_api.api_list, name="获取项目中的接口列表"),
    url(r'project/api/detail$', v_api.api_detail, name="获取接口详情"),
    url(r'project/api/create$', v_api.api_create, name="创建接口"),
    url(r'project/api/edit$', v_api.api_edit, name="编辑修改接口"),
    url(r'project/api/delete$', v_api.api_del, name="删除接口"),
    url(r'project/api/caseList$', v_api.api_case_list, name="获取接口下的case列表"),

    url(r'project/caseList$', v_case.case_list, name="获取项目中的case列表"),
    url(r'project/case/detail$', v_case.case_detail, name="获取case详情"),
    url(r'project/case/create$', v_case.case_create, name="创建case"),
    url(r'project/case/edit$', v_case.case_edit, name="编辑case"),
    url(r'project/case/delete$', v_case.case_del, name="删除case"),
    url(r'project/case/runsingal$', v_case.case_run, name="运行单个case"),

    url(r'project/case/run$', v_run.run, name="运行用例"),

    url(r'project/result/list$', v_result.result_list, name="获取项目的结果列表"),
    url(r'project/result/detailList$', v_result.result_detail_list, name="获取结果的详细信息列表"),
    url(r'project/result/caseDetail$', v_result.result_detail, name="获取单个用例运行结果的详细信息"),
    url(r'project/result/delete$', v_result.result_delete, name="删除结果"),

    url(r'project/dapi/list$', v_dapi.dapi_list, name="获取项目下的依赖接口列表"),
    url(r'project/dapi/detail$', v_dapi.dapi_detail, name="获取项目下的依赖接口列表"),
    url(r'project/dapi/create$', v_dapi.dapi_create, name="新建依赖接口"),
    url(r'project/dapi/edit$', v_dapi.dapi_edit, name="编辑依赖接口"),
    url(r'project/dapi/delete$', v_dapi.dapi_delete, name="编辑依赖接口"),
    url(r'project/dapi/run$', v_dapi.dapi_run, name="运行依赖接口"),

    url(r'project/record/reqdetail$', v_record.record_anyproxy_req, name="从anyproxy服务器获取录制case的响应信息"),

    url(r'project/plan/create$', v_plan.plan_create, name="创建计划"),
    url(r'project/plan/delete$', v_plan.plan_delete, name="删除计划"),
    url(r'project/plan/edit$', v_plan.plan_edit, name="编辑计划"),
    url(r'project/plan/list$', v_plan.plan_list, name="获取计划列表"),
    url(r'project/plan/detail$', v_plan.plan_detail, name="获取计划详情"),

]