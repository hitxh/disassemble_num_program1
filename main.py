
import numpy as np
import math


def dec2three(test_num):
     max_wei = math.floor(math.log(test_num, 3))   # 向下  取整数
     # for m in range(max_wei):
     # print("max_wei:", max_wei)
     fanhuizhi = np.zeros(max_wei+1, np.int)
     for i in range(max_wei+1):
         fanhuizhi[max_wei-i] = test_num//math.pow(3, max_wei-i)
         test_num= test_num- fanhuizhi[max_wei-i]*math.pow(3, max_wei-i)
         # print(fanhuizhi[max_wei-i])
     return fanhuizhi


N = 10
celve_num = 1
# num = len(bin(N))-2                       # 10的二进制最大个数
wei_num = math.ceil(math.log(N, 2))

max_num = math.ceil(math.pow(3, wei_num))       # 由三进制数字组成的最大数
# print("max_num:", max_num)
# print(np.linspace(1, max_num, max_num))
for i in np.linspace(1, max_num, max_num):
    wait_test_num = dec2three(i)
    # print("i=", i, "三进制数字:  低位---->高位","位数", len(wait_test),"  ", wait_test)
    eq_two_num = 0
    for k in range(len(wait_test_num)):
        # eq_two_num = 1
        eq_two_num = eq_two_num + wait_test_num[k] * math.pow(2, k)

    # print("等效的二进制数字   eq_two_num:",  eq_two_num)
    if(eq_two_num == N):
        print("策略%d"%(celve_num))
        celve_num += 1
        for k in range(len(wait_test_num)):
            if(wait_test_num[k]!= 0):
                print("%d元的币值%d个"%(math.pow(2, k), wait_test_num[k]))
