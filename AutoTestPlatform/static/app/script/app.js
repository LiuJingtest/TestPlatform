var myApp = angular.module('autoTest', ['ui.router', 'ui.bootstrap', 'ngCookies', 'monospaced.elastic', "chart.js"]);

myApp.config(function ($stateProvider, $urlRouterProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $urlRouterProvider.when("", "/index");
    $stateProvider

        .state('index', {
            url: '/index',
            views: {
                '': {
                    templateUrl: '/static/app/views/project/main.html',
                    controller: 'mainCtrl'
                }
            }
        })

        .state('project', {
            url: '/project',
            views: {
                '': {
                    templateUrl: '/static/app/views/project/navigation.html',
                    controller: 'navigationCtrl'
                },
                'project_view@project': {
                    templateUrl: '/static/app/views/project/items.html',
                    controller: 'itemsCtrl'
                }
            }
        })

        .state('project.tools', {
            url: '/tools',
            views: {
                'project_view@project': {
                    templateUrl: '/static/app/views/tools/tools.html',
                    controller: 'toolsCtrl'
                }
            }
        })

        .state('project.interface', {
            url: '/interface',
            views: {
                'project_view@project': {
                    templateUrl: '/static/app/views/interface/template.html',
                    controller: 'templateCtrl'
                },
                'interface_view@project.interface': {
                    templateUrl: '/static/app/views/interface/homepage.html',
                    controller: 'homepageCtrl'
                }
            }
        })


    .state('project.interface.homepage', {
        url: '/homepage',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/homepage.html',
                controller: 'homepageCtrl'
            }
        }
    })

    .state('project.interface.globalVar', {
        url: '/globalVar',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/globalVar.html',
                controller: 'globalVarCtrl'
            }
        }
    })

    .state('project.interface.method', {
        url: '/method',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/functions.html',
                controller: 'methodCtrl',
            }
        }
    })

    .state('project.interface.validation', {
        url: '/validation',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/checker.html',
                controller: 'checkerCtrl',
            }
        }
    })

    .state('project.interface.response', {
        url: '/response',
        views: {
           'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/response.html',
                controller: 'responseCtrl',
            }
        }
    })

    .state('project.interface.APIDependency', {
        url: '/APIDependency',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/APIDependency.html',
                controller: 'APIDependencyCtrl'
            }
        }
    })

    .state('project.interface.APICase', {
        url: '/APICase',
        views: {
            'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/APICase.html',
                controller: 'APICaseCtrl'
            }
        }
    })

    .state('project.interface.task', {
        url: '/task',
        views: {
           'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/plan.html',
                controller: 'planCtrl'
            }
        }
    })

    .state('project.interface.testReport', {
        url: '/testReport',
        views: {
           'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/report.html',
                controller: 'reportCtrl'
            }
        }
    })

    .state('project.interface.record', {
        url: '/record',
        views: {
           'interface_view@project.interface': {
                templateUrl: '/static/app/views/interface/record.html',
                controller: 'recordCtrl'
            }
        }
    })

    .state('project.app-performance', {
        url: '/app-performance',
        views: {
           'project_view@project': {
                    templateUrl: '/static/app/views/appPerformance/test.html',
                    controller: 'testCtrl'
                },
        }
    })
})
