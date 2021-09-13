#字符串的匹配
#1.待查找的内容
f = open("qd.txt", encoding='utf-8')
for line in f:
    #2.查找的条件
    if line.startswith("qd") and line.endswith("\n"):
        print(line)

import re

a = "ppa5465sdssadsasda"
b = re.match('\d',a)
print(b)

# %% search
import re
a = "ppa5465sdssadsasda"
b = re.search('\d',a).group()
print(b)
