myApp.controller('navigationCtrl', function ($scope, $http, $cookieStore, $timeout) {

    var pro_id = $cookieStore.get("currProID");

    $scope.activeItemList = ["disactive", "disactive", "disactive", "disactive", "disactive", "disactive"];

    $timeout(function () {
        var item_id = $cookieStore.get("currItemID");
        for (var i = 0; i < $scope.activeItemList.length; i++) {
                $scope.activeItemList[i] = "disactive";
            }
        if (item_id != 10) {
            $scope.activeItemList[item_id] = 'active';
        }
        $http.post('project/detail', {
            "pro_id": pro_id
        }).success(function (response) {
            $scope.pro = response.data;
        });
    })

    $scope.recordItemID = function (id) {
        $cookieStore.put("currItemID", id);
        for (var i = 0; i < $scope.activeItemList.length; i++) {
            $scope.activeItemList[i] = "disactive";
        }
        $scope.activeItemList[id] = 'active';
    }
})

