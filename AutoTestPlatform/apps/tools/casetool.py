from AutoTestPlatform.apps.InterfaceTest.models import VarValue, Vars


def get_env_var_map(env_id):
    var_map = {}
    var_value_ob_list = VarValue.objects.all().filter(env_id=env_id)
    for a in list(var_value_ob_list):
        var = Vars.objects.all().get(var_id=a.var_id)
        var_map[var.var_name] = a.var_value
    return var_map
