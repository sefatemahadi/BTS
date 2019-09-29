# import operator
# x = {'we': 2, 'gerat': 4, 'a': 3, 'e': 1, '0': 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
# print(sorted_x)
# import os
# path =os.getcwd()+'/Test/Summaries/'
# counter =1
# for i in range(151,201):
#     #os.rename(path+'Document_'+str(i)+'_Summary_1.txt',path+'Document_'+str(800+i)+'_Summary_1.txt')
#     os.rename(path+'Document_'+str(i)+'_Summary_1.txt',path+'Document_'+str(counter)+'_Summary_1.txt')
#     counter+=1
#

# from sklearn.metrics import precision_score,recall_score,f1_score
# x =[1,0,1,1,1,1,1,0]
# y =[0,1,1,0,1,1,0,0]
#
# print(precision_score(y,x,average='macro'))
# print(recall_score())

from sklearn.model_selection import KFold
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([9, 10, 11, 12])
kf = KFold(n_splits=2,shuffle=True)
kf.get_n_splits(X)

for train_index,test_index in kf.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)
    print()
    print()