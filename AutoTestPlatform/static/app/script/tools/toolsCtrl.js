/**
 * Created by liujing1 on 2017/3/30.
 */
myApp.controller('toolsCtrl', function ($scope, $http) {

        $scope.activeList = ["active", "disactive", "disactive", "disactive", "disactive", "disactive", "disactive", "disactive", "disactive", "disactive"];
        $scope.flag_done_success = true
        $scope.flag_done_fail = true
        $scope.flag_text = ""
        $scope.request = {
            url: "",
            body: "",
            header: "",
            method: "",
            num: 0
        }

        $scope.test = function () {
            $scope.flag_done_success = true
            $scope.flag_done_fail = true
            $http.post('tools/request_repeat', $scope.request).success(function (response) {

                if (response.code == 1) {
                    $scope.flag_done_success = false
                }
                if (response.code == 0) {
                    $scope.flag_done_fail = false
                    $scope.flag_text = response.msg
                }

            })
        }

        $scope.active = function(id) {
         for (var i=0;i<$scope.activeList.length;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[id]='active';
     }

    }
)

