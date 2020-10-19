import pandas
dfs = pandas.read_html('https://www.taiwanlottery.com.tw/Info/number/frequency.aspx?GAME=SL638')
dfs = dfs[0]
dfs = dfs.fillna(0)

ordinary_num_dict = {}
for i in range(0,6,2):
    for a in range(2,15):
        ordinary_num_dict[dfs[i][a]] = dfs[i+1][a]
ordinary_num_dict.pop(0)
ordinary_num_dict = sorted(ordinary_num_dict.items(), key=lambda item:item[1])
ordinary_num_list = list(ordinary_num_dict)

special_num_dict = {}
for i in range(2,10):
    special_num_dict[dfs[6][i]] = dfs[7][i]
special_num_dict = sorted(special_num_dict.items(), key=lambda item:item[1])
special_num_list = list(special_num_dict)

import time
year, month, day = time.localtime()[0:3]

print("從 民國97年 至 今天(民國%d年%d月%d日) 的統計:"%(year-1911,month,day))
print("\n最冷門的六個普通號碼為:")
for num in ordinary_num_list[:6]:
    print(num[0],end = " ")
print("\n\n最冷門的特別號為:\n%d"%int(special_num_list[0][0]))
print("\n祝您好運~~")
    



