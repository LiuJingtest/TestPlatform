/**
 * Created by liujing1 on 2017/3/30.
 */
myApp.controller('testCtrl', function ($scope, $http, $timeout) {

    $scope.getDeviceInfo = function (devicesUdid) {
        $scope.deviceInfo = $scope.devicesList[devicesUdid]
        $http.post('app-performance/device/packages', {deviceUdid: devicesUdid}).success(function (response) {
            $scope.devicePackages = response.data
            $scope.package = $scope.devicePackages[0]
        })
    }

    $timeout(function () {
        $http.post('app-performance/devices/list', {}).success(function (response) {
            $scope.devicesList = response.data
            $scope.devicesUdidList = Object.keys($scope.devicesList)
        })
    })

    $scope.start = function () {
        $scope.data = [[], [], []]
        $scope.labels = new Array()
        $scope.resultList = [{
            "pass_num": 9,
            "end_time": 1497421044,
            "start_time": 1497421040,
            "fail_num": 2,
            "result_id": 7,
            "suite_desc": "\u65e0",
            "suite_name": "\u7ebf\u4e0a\u5192\u70df",
            "unrun_num": 17,
            "report_name": "888888",
            "suite_id": 8,
            "pro_id": 5
        }];
        for (var i = 0; i < $scope.resultList.length; i++) {
            $scope.labels[$scope.resultList.length - i - 1] = $scope.resultList[i].report_name
            $scope.data[$scope.resultList.length - i - 1] = $scope.resultList[i].pass_num
        }
        $scope.colors = ['#46BFBD'];
        $scope.series = ['PASS_NUM'];
        $scope.datasetOverride = [{
            id: 'y-axis-pass',
            label: "PASS_NUM",
            borderWidth: 3,
            type: 'line'
        }];

    }
})

