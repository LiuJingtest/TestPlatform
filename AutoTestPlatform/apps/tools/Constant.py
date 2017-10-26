# 变量后替换{{}}
PATTERN_TYPE1 = "{{\w+}}"

# 函数替换{$$}
PATTERN_TYPE2 = "{\$(\S.*?)\$}"

# json提取$.
PATTERN_TYPE3 = "\$\.[^(\"|'|,)]+"
