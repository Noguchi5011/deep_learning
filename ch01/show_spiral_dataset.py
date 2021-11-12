# coding: utf-8
import sys
sys.path.append('..')  # 親ディレクトリのファイルをインポートするための設定
from dataset import spiral
import matplotlib.pyplot as plt
#ここ追加
import numpy as np

x, t = spiral.load_data()
print('x', x.shape)  # (300, 2)
print('t', t.shape)  # (300, 3)

# 編集点
for (x,y), label in zip(x, t):
 index = np.argmax(label)
 # print(x,y,np.argmax(label), label)
 if index == 0:
   index = "red"
 elif index == 1:
   index = "green"
 else :
   index = "yellow"

 plt.scatter(x, y, c=index)

#________

# # データ点のプロット
# N = 100
# CLS_NUM = 3
# markers = ['o', 'x', '^']
# for i in range(CLS_NUM):
#     plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])
# plt.show()
