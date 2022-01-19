### 파이썬 300제 241번
##import datetime
##
##now = datetime.datetime.now()
##print(now)

### 파이썬 300제 242
##import datetime
##
##now = datetime.datetime.now()
##print(type(now))

### 파이썬 300제 243
##import datetime
##
##now = datetime.datetime.now()
##
##for i in range(5, 0, -1):
##    delta = datetime.timedelta(days = -i) # days 대신 hours seconds 등 다른 시간도 사용 가능
##    date = now + delta
##    print(date)

### 파이썬 300제 244
##import datetime
##
##now = datetime.datetime.now()
##print(now.strftime("%H:%M:%S")) # Y 연도, D 날짜

### 파이썬 300제 245
##import datetime
##
##day = "2020-05-04"
##
##
##ret = datetime.datetime.strptime(day, "%Y-%m-%d")
##print(ret)


# 파이썬 300제 246

##import time
##import datetime
##
##while True:
##    now = datetime.datetime.now()
##    print(now)
##    time.sleep(1)

# 파이썬 300제 247

##import os                   # os.rename() 가장 많이 사용하는 방식이다.
##from os import rename       # rename()
##from os import *            # getcwd(), rename(), ...
##import os as myos           # myos.getcwd()  모듈 이름이 너무 길 때 사용


### 파이썬 300제 248
##import os
##dirt = os.getcwd()
##print(dirt)


### 파이썬 300제 249
##import os
##
##os.rename("C:\\Users\\h\\Desktop\\test.txt", "C:\\Users\\h\\Desktop\\rename.txt")



# 파이썬 300제 250

import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
































