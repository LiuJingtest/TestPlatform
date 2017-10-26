def str_replace(str_re, str_type):
    # 替换全局变量
    if str_type == 1:
        a = str_re.find('{{')
        b = str_re.find('}}')
        str1 = str_re[a + 2:b]
        return a, b+2, str1
    # 替换依赖接口值
    if str_type == 2:
        a = str_re.find('$.')
        b_list = [str_re.find('"', a), str_re.find(',', a), str_re.find('}', a), str_re.find('\'', a)]
        b = len(str_re)
        for i in b_list:
            if 0 < i < b:
                b = i
        path = str_re[a:b]
        return path
    # 替换常用方法返回值
    if str_type == 3:
        a = str_re.find('{$')
        b = str_re.find('$}')
        str1 = str_re[a + 2:b]
        str_func_name = str1[0:str1.find('(')]
        return a, b + 2, str1, str_func_name