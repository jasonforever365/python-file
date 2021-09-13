import re

b= '027-86934758'
a =re.match('\d{3}-\d{7}',b)
print(a)