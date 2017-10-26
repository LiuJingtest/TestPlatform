myApp.controller('reportCtrl', function ($scope, $http, $cookieStore, $timeout,$rootScope) {
    var pro_id = $cookieStore.get("currProID");
    $scope.wid = {}
    $scope.List = ['active'];
    $scope.reportDetal = [];
    $scope.suiteList = "";
    $scope.resultList = "";
    $scope.result = {
        "result_id": 1,
        "suite_id": 1,
        "start_time": "1478617457",
        "pass_num": 1,
        "report_name": "test",
        "end_time": "1478617457",
        "fail_num": 1,
        "pro_id": 1
    }
    $scope.allResult = [];
    $scope.api = {
        "api_param": "username,pwd",
        "api_id": 1,
        "module_id": 1,
        "pro_id": pro_id,
        "api_url": "",
        "api_method": "post",
        "api_type": "34",
        "api_protocol": "http",
        "api_name": "登录接口",
        "api_desc": "登录"
    }
    $scope.check={
        "check_name": "",
        "check_id": 0,
        "pro_id": pro_id,
        "check_desc": "",
        "check_code": ""
    }

    var date;
    var m;
    var s;
    $scope.timeInval = [];
    $rootScope.caseRun;
    $timeout(function () {
        $scope.suite = "";
        $scope.startDate = "";
        $scope.endDate = "";
        $scope.title = "";
        $http.post('interface/project/suite/list', {
            "pro_id": pro_id
        }).success(function (response) {
            if (response.code == 1) {
                $scope.suiteList = response.data;
            } else {
                alert(response.msg)
            }
        })
        $scope.repDetail = false;
        $scope.repList = true;
        $http.post('interface/project/result/list', {
            "pro_id": pro_id
        }).success(function (response1) {
            if (response1.code = 1) {
                $scope.resultList = response1.data;
                $scope.totalItems=$scope.resultList.length;
                $scope.currentPage = 1;//d当前页面
                $scope.pageChanged(1);
                for (var i = 0; i < $scope.resultList.length; i++) {
                    date = new Date(($scope.resultList[i].end_time - $scope.resultList[i].start_time) * 1000);
                    m = date.getMinutes();
                    s = date.getSeconds();
                    if (m > 0) {
                        $scope.timeInval[i] = m + "m" + s + "s";
                    } else {
                        $scope.timeInval[i] = s + "s";
                    }
                }
                if($rootScope.caseRun==1){
                    $rootScope.showDetail($scope.resultList[0]);
                }
            } else {
                alert(response1.msg)
            }
        })
    })

    $scope.pageList=[];
    $scope.pageChanged=function(index){
        if(index==1){
            $http.post('interface/project/result/list', {
                "pro_id": pro_id
            }).success(function (response1) {
                if (response1.code = 1) {
                    $scope.resultList = response1.data;
                    $scope.totalItems=$scope.resultList.length;
                    $scope.pageList=[];
                    if($scope.totalItems>0){
                        if($scope.currentPage==Math.ceil($scope.resultList.length/15)){
                            for(var i=0;i<$scope.resultList.length-($scope.currentPage-1)*15;i++){
                                $scope.pageList[i]=$scope.resultList[($scope.currentPage-1)*15+i];
                            }
                        }else{
                            for(var i=0;i<15;i++){
                                $scope.pageList[i]=$scope.resultList[($scope.currentPage-1)*15+i];
                            }
                        }
                    }
                }else{
                    alert(response1.msg)
                }
            })
        }else{
            $http.post('interface/project/result/detailList', {
                "result_id": resultDetailId
            }).success(function (response) {
                if (response.code = 1) {
                    $scope.allResult = response.data;
                    $scope.totalItems2=$scope.allResult.length;
                    $scope.reaultDetailList=[];
                    if($scope.totalItems2>0){
                        if($scope.currentPage2==Math.ceil($scope.allResult.length/15)){
                            for(var i=0;i<$scope.allResult.length-($scope.currentPage2-1)*15;i++){
                                $scope.reaultDetailList[i]=$scope.allResult[($scope.currentPage2-1)*15+i];
                            }
                        }else{
                            for(var i=0;i<15;i++){
                                $scope.reaultDetailList[i]=$scope.allResult[($scope.currentPage2-1)*15+i];
                            }
                        }
                    }
                }else{
                    alert(response.msg)
                }
            })
        }
    }

    $scope.clearSelect = function () {
        $scope.suite = "";
        $scope.startDate = "";
        $scope.endDate = "";
        $scope.title = "";
    }

    var resultDetailId=0;
    $rootScope.showDetail = function (obj) {
        $scope.result = obj;
        $scope.repList = false;
        $scope.repDetail = true;
        resultDetailId=obj.result_id;
        $http.post('interface/project/result/detailList', {
            "result_id": obj.result_id
        }).success(function (response) {
            if (response.code = 1) {
                $scope.allResult = response.data;
                $scope.currentPage2=1;
                $scope.totalItems2=$scope.allResult.length;
                $scope.pageChanged(2);
                $scope.resultStr = "";
                for (var i = 0; i < $scope.allResult.length - 1; i++) {
                    $scope.reportDetal[i] = false;
                     //$scope.styleList.push($scope.tableStyle);
                }
            } else {
                alert(response.msg)
            }
        })
    }

    $scope.showReport = function (obj, index) {
        $scope.res=obj;
        $http.post("interface/project/api/detail", {
            "api_id": obj.api_id
        }).success(function (response) {
            if (response.code == 1) {
                $scope.api = response.data;
            } else {
                alert(response.msg);
            }
        })
        $scope.reportDetal[index] = !$scope.reportDetal[index];
    }

    $scope.returnList = function () {
        $rootScope.caseRun=0;
        $scope.repDetail = false;
        $scope.repList = true;
        $http.post('interface/project/result/list', {
            "pro_id": pro_id
        }).success(function (response1) {
            if (response1.code = 1) {
                $scope.resultList = response1.data;
                $scope.totalItems=$scope.resultList.length;
                $scope.pageChanged(1);
            } else {
                alert(response1.msg)
            }
        })
    }

    $scope.delReport = function (id) {
        $http.post("interface/project/result/delete", {
            "result_id": id
        }).success(function (response) {
            if (response.code == 1) {
                $http.post('project/result/list', {
                    "pro_id": pro_id
                }).success(function (response1) {
                    if (response1.code = 1) {
                        $scope.resultList = response1.data;
                        $scope.totalItems=$scope.resultList.length;
                        $scope.pageChanged(1);
                    } else {
                        alert(response1.msg)
                    }
                })
            } else {
                alert(response.msg)
            }
        })
    }

     $scope.getResult=function(obj,index){
         $scope.res=obj;
         switch (index){
             case 1:
                 $("#statusDetail").modal();
                 break;
             case 2:
                 $("#bodyDetail").modal();
                 break;
             case 3:
                 $("#schemaDetail").modal();
                 break;
             case 4:
                 $("#headerDetail").modal();
                 break;
         }
    }

    /*
    $scope.styleList=[];
    $scope.tableStyle = {
        "background-color": "white",
        //"height": "35px"
    }

    $scope.styleChange = {
        "background-color": "#eeeeff",
        //"height": "35px"
    }

    $scope.tableGray = function (index) {
        $scope.styleList[index]=$scope.styleChange;

    }

    $scope.tableWhite = function (index) {
        $scope.styleList[index]=$scope.tableStyle;
    }*/

    $('.form_date').datetimepicker({
        format: 'yyyy-mm-dd',
        startDate: '1900-01-01',
        autoclose: true,
        bootcssVer: 3,
        language: 'zh_CN',
        minView: "month"
    });
})
