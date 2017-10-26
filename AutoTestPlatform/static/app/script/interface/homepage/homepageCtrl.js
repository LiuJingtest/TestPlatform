myApp.controller('homepageCtrl', function ($scope, $http, $cookieStore, $timeout,$location,$rootScope) {
    var pro_id = $cookieStore.get("currProID");
    $scope.resultList = new Array()
    $scope.data = [[], [], []]
    $scope.labels = new Array()

    $scope.planList="";
    $timeout(function () {
        $http.post("interface/project/plan/list",{
            "pro_id":pro_id,
            "status":1
        }).success(function(response){
            if(response.code==1){
                $scope.planList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $http.post('interface/project/result/list', {
            "pro_id": pro_id
        }).success(function (response1) {
            if (response1.code = 1) {
                $scope.resultList = response1.data;
                for (var i = 0; i < $scope.resultList.length; i++) {
                    $scope.labels[$scope.resultList.length-i-1] = $scope.resultList[i].report_name
                    $scope.data[0][$scope.resultList.length-i-1] = $scope.resultList[i].pass_num
                    $scope.data[1][$scope.resultList.length-i-1] = $scope.resultList[i].fail_num
                    $scope.data[2][$scope.resultList.length-i-1] = $scope.resultList[i].fail_num + $scope.resultList[i].pass_num
                }
            } else {
                alert(response1.msg)
            }
        })
    })
    $scope.colors = ['#46BFBD', '#FF0000', '#DCDCDC'];
    $scope.series = ['PASS_NUM', 'FAIL_NUM', 'CASE_NUM'];
    $scope.onClick = function (points, evt) {
    };
    $scope.datasetOverride = [{
        id:'y-axis-pass',
        label: "PASS_NUM",
        borderWidth: 3,
        type: 'line'
      },{
        id:'y-axis-fail',
        label: "FAIL_NUM",
        borderWidth: 3,
        type: 'line'
      },{
        id:'y-axis-total',
        label: "CASE_NUM",
        borderWidth: 3,
        type: 'line'
      }];

    $scope.gotoPlan=function(id){
        $rootScope.planId=id;
        $rootScope.planSelect=1;
        $rootScope.active(7);
        $location.url("/interface/project/task");

    }

})

